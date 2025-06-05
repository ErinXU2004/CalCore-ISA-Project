# 📘 CalCore DSL v1.0 Specification

*A domain-specific language for compiling structured lifestyle behavior into programmable daily routines, with a focus on weight loss and mood-conscious health management.*

---

## 1. 🎯 Design Goal

CalCore DSL transforms user lifestyle behaviors—such as eating, moving, planning, and reflecting—into structured, programmable instructions. The goal is to:

- Provide a lightweight alternative to logging-based fitness apps  
- Enable behavior simulation, feedback, and planning through interpretable code  
- Support goal-driven, emotionally aware, low-friction health management

---

## 2. 📐 Instruction Format

Each instruction line follows a simple, comma-separated format: `INSTRUCTION ARG1, ARG2 [, ARG3...]` 


All arguments are positional. Optional arguments may depend on the instruction type.

---

## 3. 🧩 Instruction Set

| Instruction | Purpose                    | Example                   | Notes                            |
|-------------|----------------------------|---------------------------|----------------------------------|
| `EAT`       | Log food intake            | `EAT 320, PROTEIN`        | Adds calories to `CaloriesIn`   |
| `MOVE`      | Log physical activity      | `MOVE WALK, 30`           | Subtracts calories from `CaloriesOut` |
| `QUERY`     | Request internal state     | `QUERY DEFICIT`           | Outputs status                   |
| `SETGOAL`   | Set behavioral targets     | `SETGOAL DEFICIT, 500`    | Sets `GoalDeficit`              |
| `REWARD`    | Log reward/emotional input | `REWARD MILKTEA, 150`     | Treated like EAT (tagged)       |
| `MOOD`      | Log mood level             | `MOOD STRESS, HIGH`       | Updates `MoodState`             |
| `SLEEP`     | Log sleep duration         | `SLEEP 7.5`               | Affects recovery (planned)      |

---

## 4. 📦 System Registers

| Register         | Description                             |
|------------------|-----------------------------------------|
| `CaloriesIn`     | Total calories consumed today           |
| `CaloriesOut`    | Estimated calories burned today         |
| `DeficitBalance` | `CaloriesOut - CaloriesIn`              |
| `GoalDeficit`    | Target calorie deficit for the day      |
| `MoodState`      | User’s reported stress/mood level       |
| `MealHistory[]`  | History of `EAT` actions                |
| `MoveHistory[]`  | History of `MOVE` actions               |

---

## 5. 📄 Sample CalCore Script (`.cal` file)

<pre>sample_day.cal
SETGOAL DEFICIT, 400
EAT 300, CARB
MOVE DANCE, 45
QUERY DEFICIT
EAT 500, BALANCED
MOVE WALK, 20
REWARD CHOCOLATE, 150
QUERY DEFICIT
MOOD STRESS, LOW</pre>


---

## 6. 🖥️ Sample Output (from interpreter)
```[08:00] EAT: +300 kcal (CARB)
[09:00] MOVE: -200 kcal (DANCE 45min)
[10:00] QUERY: Current deficit = -100 kcal
[12:30] EAT: +500 kcal (BALANCED)
[14:00] MOVE: -70 kcal (WALK 20min)
[17:00] REWARD: +150 kcal (CHOCOLATE)
[20:00] QUERY: Current deficit = -420 kcal
[21:00] MOOD: STRESS level set to LOW```


---

## 7. 🧠 Future Extensions (v1.1+)

Planned for future versions:

- `PLAN <template>` – Load a predefined plan (`PLAN SHOOT_DAY`)
- `SUGGEST` – Get recommendations from the system
- `IF / ELSE` – Conditional behaviors (e.g., `IF DEFICIT > 0 THEN MOVE YOGA, 20`)
- `ALERT` – Trigger warnings or reminders

---

## 8. 📌 Usage Notes

- CalCore is **sequence-based**, not time-based.
- Scripts represent **intent**, not tracking.
- Designed for structured, non-anxious lifestyle planning.

---

## ✍️ Author

**Erin Xu**  
EECS @ University of Michigan  
GitHub: [@erinhua](https://github.com/erinhua)  
Email: erinhua@umich.edu



