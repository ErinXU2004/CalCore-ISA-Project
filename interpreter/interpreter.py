from user import load_user_from_json
import os
from datetime import datetime
import json
import sys


class CalCoreState:
    def __init__(self, user):
        self.user = user
        self.calories_in = 0
        self.calories_out = 0
        self.log = []

    def eat(self, amount, category):
        self.calories_in += amount
        self.log.append(f"EAT: +{amount} kcal ({category})")

    def move(self, activity, duration_min):
        # 简化估算：热量消耗 = BMR * MET系数 * 时间 / 1440
        MET = {"WALK": 3.5, "RUN": 7.0, "DANCE": 5.5}.get(activity.upper(), 3.5)
        kcal = round(self.user.bmr * MET * duration_min / 1440, 2)
        self.calories_out += kcal
        self.log.append(f"MOVE: -{kcal} kcal ({activity} {duration_min} min)")

    def query_deficit(self):
        deficit = self.calories_in - self.calories_out
        self.log.append(f"QUERY: Current deficit = {deficit:+.2f} kcal")

    def query_bmr(self):
        explanation = self.user.explain_bmr_calculation()
        self.log.append("QUERY: BMR Calculation Requested")
        self.log.append(explanation)

    def print_log(self):
        os.makedirs("output", exist_ok=True)
        with open("output/sample_output.txt", "w") as f:
            f.write("User Profile: " + str(self.user.to_dict()) + "\n\n")
            for entry in self.log:
                f.write(entry + "\n")

    def log_weight(self, weight, date_str):
        log_path = f"user_profiles/{self.user.name.lower()}_weight_log.json"

        # 加载旧数据
        if os.path.exists(log_path):
            with open(log_path, "r") as f:
                data = json.load(f)
        else:
            data = {"name": self.user.name, "weight_history": []}

        # 加入新的记录
        data["weight_history"].append({"date": date_str, "weight": weight})

        # 清洗重复日期，保留最新写入的记录
        seen = {}
        for entry in data["weight_history"]:
            seen[entry["date"]] = entry  # 后写的会覆盖前面的

        # 转为列表并排序
        clean_history = list(seen.values())
        clean_history.sort(key=lambda x: x["date"])

        data["weight_history"] = clean_history

        # 保存
        with open(log_path, "w") as f:
            json.dump(data, f, indent=2)

        self.log.append(f"[WEIGHT] {date_str} — {weight} kg")




if len(sys.argv) < 2:
    print("Usage: python interpreter.py <path_to_cal_file>")
    sys.exit(1)

cal_file_path = sys.argv[1]

if __name__ == "__main__":
    user = load_user_from_json("user_profiles/erin.json")
    state = CalCoreState(user)

    with open(cal_file_path, "r") as f:
        lines = f.readlines()

    for line in lines:
        tokens = line.strip().split()
        if not tokens:
            continue
        cmd = tokens[0].upper()

        if cmd == "EAT":
            amount = int(tokens[1])
            category = tokens[2]
            state.eat(amount, category)
        elif cmd == "MOVE":
            activity = tokens[1]
            duration = int(tokens[2])
            state.move(activity, duration)
        elif cmd == "QUERY":
            if tokens[1].upper() == "DEFICIT":
                state.query_deficit()
            elif tokens[1].upper() == "BMR":
                state.query_bmr()
        elif cmd == "LOG_WEIGHT":
            if len(tokens) == 3:
                date_str = tokens[1]
                weight = float(tokens[2])
            else:
                # 默认使用今天
                from datetime import datetime
                date_str = datetime.now().strftime("%Y-%m-%d")
                weight = float(tokens[1])
            state.log_weight(weight, date_str)



    state.print_log()
