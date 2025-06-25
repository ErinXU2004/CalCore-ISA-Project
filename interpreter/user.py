# interpreter/user.py
import json

class CalCoreUser:
    def __init__(self, name, age, gender, height_cm, weight_kg, body_fat):
        self.name = name
        self.age = age
        self.gender = gender
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.body_fat = body_fat
        self.bmr = self.calculate_bmr()

    def calculate_bmr(self):
        # Harris-Benedict Equation
        if self.gender.upper() == "F":
            return round(447.593 + 9.247 * self.weight_kg + 3.098 * self.height_cm - 4.330 * self.age, 2)
        else:
            return round(88.362 + 13.397 * self.weight_kg + 4.799 * self.height_cm - 5.677 * self.age, 2)

    def explain_bmr_calculation(self):
        if self.gender.upper() == "F":
            formula = "BMR = 447.593 + 9.247 × weight + 3.098 × height − 4.330 × age"
            calc_steps = (
                f"BMR = 447.593 + 9.247×{self.weight_kg} + 3.098×{self.height_cm} − 4.330×{self.age}\n"
                f"    = {447.593} + {round(9.247 * self.weight_kg, 2)} + {round(3.098 * self.height_cm, 2)} - {round(4.330 * self.age, 2)}"
            )
        else:
            formula = "BMR = 88.362 + 13.397 × weight + 4.799 × height − 5.677 × age"
            calc_steps = (
                f"BMR = 88.362 + 13.397×{self.weight_kg} + 4.799×{self.height_cm} − 5.677×{self.age}\n"
                f"    = {88.362} + {round(13.397 * self.weight_kg, 2)} + {round(4.799 * self.height_cm, 2)} - {round(5.677 * self.age, 2)}"
            )

        explanation = (
            "=== BMR Calculation Summary ===\n"
            "Model Used: Harris-Benedict Equation (1919, revised)\n"
            "Context: Scientific estimate of Basal Metabolic Rate (BMR)\n\n"
            f"Input:\n"
            f"  Gender: {'Female' if self.gender.upper() == 'F' else 'Male'}\n"
            f"  Age: {self.age} years\n"
            f"  Height: {self.height_cm} cm\n"
            f"  Weight: {self.weight_kg} kg\n\n"
            f"Formula:\n  {formula}\n\n"
            f"Calculation:\n  {calc_steps}\n"
            f"  ≈ {self.bmr} kcal/day\n\n"
            "Note: This BMR reflects the energy required for survival at complete rest,\n"
            "and does not include minor daily activity (e.g., walking, dressing).\n"
            "For that, consider RMR ≈ BMR × 1.1\n"
        )
        return explanation

    def to_dict(self):
        return {
            "Name": self.name,
            "Age": self.age,
            "Gender": self.gender,
            "Height(cm)": self.height_cm,
            "Weight(kg)": self.weight_kg,
            "Body Fat %": self.body_fat,
            "BMR(kcal/day)": self.bmr
        }

def load_user_from_json(path):
    with open(path, 'r') as f:
        data = json.load(f)
    return CalCoreUser(**data)


