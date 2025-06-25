# CalCore-ISA: AI-Powered Custom Instruction Set for Fat Loss

Welcome to **CalCore-ISA**, an experimental platform that reimagines how we interact with fat-loss tracking systems by combining custom ISA (Instruction Set Architecture) design with AI-driven input interpretation.

This is not just a calculator—it's the foundation of an intelligent, extensible, user-friendly metabolic tracking engine designed for daily use.

---

## 💡 Project Vision

Most fat-loss apps require painful manual logging of food and exercise. CalCore's vision is to **eliminate manual input entirely** by enabling users to simply say:

> “I weigh 51kg today. I had 3 buns for breakfast, a bowl of noodles for dinner, and danced for 3 hours.”
1. 🔍 **Automatically interpret the input** using an AI language model
2. ⚙️ **Translate it into CalCore DSL commands**
3. 🧮 **Execute the commands via interpreter**
4. 📊 **Generate a personalized metabolic report**, including:
   - Daily calorie intake
   - Calorie consumption from activities
   - Net deficit or surplus
   - Visual summary (charts, logs, trends)

Eventually, every user will have access to:
- 📆 A per-day auto-generated metabolic summary
- 📈 Long-term weight tracking and curve plotting
- 🧠 AI-driven natural language interaction — no manual tracking needed

---

## 🔧 Features (In Progress)

- [x] DSL-based calorie and movement command parser
- [x] Support for per-user profile (height, weight, age, body fat %)
- [x] BMR/RMR calculation using Harris-Benedict equation
- [x] Calorie tracking (intake + consumption)
- [x] Weight history logging with duplicate filtering
- [x] Weight trend visualization with `matplotlib`
- [ ] Natural language to DSL parser using LLM
- [ ] Auto-generated daily metabolic report
- [ ] Web or mobile front-end

---

## 🚀 Sample Usage

Example CalCore DSL (`.cal`) input file:

```cal
LOG_WEIGHT 2025-06-25 51.7
EAT 300 carb
EAT 500 protein
MOVE DANCE 120
QUERY BMR
QUERY DEFICIT


Run the interpreter:
python interpreter/interpreter.py examples/sample_day.cal

📈 Plotting Weight Trends
Generate weight curve graph from JSON log:
python plot/plot_weight.py
Saves to output/weight_curve.png

🧠 Future: Natural Language Interface
The next step is to allow:

“I weigh 52kg today. Ate a chicken salad. Biked 1 hour.”
to be automatically transformed into:

LOG_WEIGHT 2025-06-25 52.0
EAT 350 protein
MOVE BIKE 60
This will be achieved through LLM-powered input parsing and DSL code generation.

👩‍💻 Author
Erin Xu
University of Michigan – ECE Major
🌱 A project for Ross Impact Studio and Berkeley M.Eng Application
🔗 GitHub: ErinXU2004





