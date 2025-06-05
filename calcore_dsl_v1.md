📘 CalCore DSL v1.0 Specification
A domain-specific language for compiling structured lifestyle behavior into programmable daily routines, with a focus on weight loss and mood-conscious health management.

1. 🎯 Design Goal
CalCore DSL transforms user lifestyle behaviors—such as eating, moving, planning, and reflecting—into structured, programmable instructions. The goal is to:

Provide a lightweight alternative to logging-based fitness apps

Enable behavior simulation, feedback, and planning through interpretable code

Support goal-driven, emotionally aware, low-friction health management

2. 📐 Instruction Format
Each instruction line follows a simple, comma-separated format:

css
复制
编辑
INSTRUCTION ARG1, ARG2 [, ARG3...]
All arguments are positional. Optional arguments may depend on the instruction type.

3. 🧩 Instruction Set
Instruction	Purpose	Example	Notes
EAT	Log food intake	EAT 320, PROTEIN	Adds calories to CaloriesIn
MOVE	Log physical activity	MOVE WALK, 30	Subtracts estimated calories from CaloriesOut
QUERY	Request internal state	QUERY DEFICIT	Outputs status (e.g., current deficit)
SETGOAL	Set behavioral targets	SETGOAL DEFICIT, 500	Sets GoalDeficit
REWARD	Log emotional intake/reward	REWARD MILKTEA, 150	Treated like EAT, marked as reward
MOOD	Log mood status	MOOD STRESS, HIGH	Updates MoodState
SLEEP	Log sleep time	SLEEP 7.5	May affect recommendations (future versions)

4. 📦 System State Registers
The interpreter maintains internal variables simulating the lifestyle context:

Register	Description
CaloriesIn	Total calories consumed today
CaloriesOut	Estimated calories burned today
DeficitBalance	CaloriesOut - CaloriesIn
GoalDeficit	Target deficit for the day
MoodState	User’s reported mood (e.g., STRESS=HIGH)
MealHistory[]	List of EAT entries
MoveHistory[]	List of MOVE entries

5. 📄 Sample CalCore Script (.cal file)
graphql
复制
编辑
# sample_day.cal

SETGOAL DEFICIT, 400
EAT 300, CARB
MOVE DANCE, 45
QUERY DEFICIT
EAT 500, BALANCED
MOVE WALK, 20
REWARD CHOCOLATE, 150
QUERY DEFICIT
MOOD STRESS, LOW
6. 🖥️ Sample Output (from interpreter)
csharp
复制
编辑
[08:00] EAT: +300 kcal (CARB)
[09:00] MOVE: -200 kcal (DANCE 45min)
[10:00] QUERY: Current deficit = -100 kcal
[12:30] EAT: +500 kcal (BALANCED)
[14:00] MOVE: -70 kcal (WALK 20min)
[17:00] REWARD: +150 kcal (CHOCOLATE)
[20:00] QUERY: Current deficit = -420 kcal
[21:00] MOOD: STRESS level set to LOW
7. 🧠 Future Extensions (v1.1+)
Planned features for future versions:

Feature	Description
PLAN <template>	Load a predefined plan (e.g., "shoot day", "lazy Sunday")
SUGGEST	Ask system to recommend next action
IF / ELSE	Conditional execution (e.g., IF DEFICIT < 0 THEN MOVE YOGA, 15)
ALERT	Custom warnings based on current state

8. 📌 Usage Tips
CalCore scripts are not time-based but sequence-based.

You can define your own templates to describe various life patterns.

The goal is not micromanagement, but behavioral structure.

✍️ Author
Erin Xu
EECS @ University of Michigan
GitHub: @erinhua
Email: erinhua@umich.edu
