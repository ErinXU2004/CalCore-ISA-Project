from user import load_user_from_json
import os

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


if __name__ == "__main__":
    user = load_user_from_json("user_profiles/erin.json")
    state = CalCoreState(user)

    with open("examples/sample_day.cal", "r") as f:
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

    state.print_log()
