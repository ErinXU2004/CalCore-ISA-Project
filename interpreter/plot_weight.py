import json
import matplotlib.pyplot as plt
from datetime import datetime

with open("user_profiles/erin_weight_log.json", "r") as f:
    data = json.load(f)

dates = [datetime.strptime(entry["date"], "%Y-%m-%d") for entry in data["weight_history"]]
weights = [entry["weight"] for entry in data["weight_history"]]

plt.figure(figsize=(8, 4))
plt.plot(dates, weights, marker='o', linestyle='-', linewidth=2)
plt.title(f"{data['name']}'s Weight Trend")
plt.xlabel("Date")
plt.ylabel("Weight (kg)")
plt.grid(True)
plt.tight_layout()
plt.savefig("output/weight_curve.png")
plt.show()
