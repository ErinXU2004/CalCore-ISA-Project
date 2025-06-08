# interpreter/interpreter.py

class CalCoreState:
    def __init__(self):
        self.CaloriesIn = 0
        self.CaloriesOut = 0
        self.log = []

    def eat(self, calories, meal_type):
        self.CaloriesIn += calories
        self.log.append(f"EAT: +{calories} kcal ({meal_type})")

    def move(self, activity, duration):
        calories_burned = duration * 5
        self.CaloriesOut += calories_burned
        self.log.append(f"MOVE: -{calories_burned} kcal ({activity} {duration} min)")

    def query_deficit(self):
        deficit = self.CaloriesOut - self.CaloriesIn
        self.log.append(f"QUERY: Current deficit = {deficit} kcal")
        return deficit

    def print_log(self):
        for line in self.log:
            print(line)

def parse_instruction(line, state):
    parts = line.strip().split()
    if not parts or parts[0].startswith('#'):
        return  

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

def run_calcore_script(file_path):
    state = CalCoreState()
    with open(file_path, 'r') as f:
        for line in f:
            parse_instruction(line, state)
    state.print_log()

if __name__ == "__main__":
    run_calcore_script("examples/sample_day.cal")
