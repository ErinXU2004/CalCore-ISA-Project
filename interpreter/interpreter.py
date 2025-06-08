# interpreter/interpreter.py

from user import CalCoreUser

class CalCoreState:
    def __init__(self, user: CalCoreUser):
        self.user = user
        self.CaloriesIn = 0
        self.CaloriesOut = 0
        self.log = []
        self.log.append(f"User Profile: {user.summary()}")

    def eat(self, calories, meal_type):
        self.CaloriesIn += calories
        self.log.append(f"EAT: +{calories} kcal ({meal_type})")

    def move(self, activity, duration_min):
        calories_burned = self.user.calories_burned(activity, duration_min)
        self.CaloriesOut += calories_burned
        self.log.append(f"MOVE: -{calories_burned} kcal ({activity} {duration_min} min)")

    def query_deficit(self):
        deficit = self.CaloriesOut - self.CaloriesIn
        self.log.append(f"QUERY: Current deficit = {deficit} kcal")
        return deficit

    def query_bmr(self):
        bmr = self.user.bmr()
        self.log.append(f"QUERY: BMR = {bmr} kcal/day")
        return bmr

    def print_log(self):
        for line in self.log:
            print(line)

def parse_instruction(line, state):
    parts = line.strip().split()
    if not parts or parts[0].startswith('#'):
        return  # 注释或空行

    instr = parts[0].upper()
    args = ' '.join(parts[1:]).split(',')

    if instr == "EAT":
        calories = int(args[0])
        meal_type = args[1].strip()
        state.eat(calories, meal_type)

    elif instr == "MOVE":
        activity = args[0].strip()
        duration = int(args[1])
        state.move(activity, duration)

    elif instr == "QUERY":
        what = args[0].strip().upper()
        if what == "DEFICIT":
            state.query_deficit()
        elif what == "BMR":
            state.query_bmr()

def run_calcore_script(file_path):
    user = CalCoreUser(
        name="Erin", age=21, gender="F",
        height_cm=165, weight_kg=53, body_fat_pct=22
    )
    state = CalCoreState(user)
    with open(file_path, 'r') as f:
        for line in f:
            parse_instruction(line, state)
    state.print_log()

if __name__ == "__main__":
    run_calcore_script("examples/sample_day.cal")

def print_log(self, to_file=None):
    if to_file:
        with open(to_file, 'w') as f:
            for line in self.log:
                f.write(line + '\n')
    else:
        for line in self.log:
            print(line)


