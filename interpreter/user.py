# interpreter/user.py

class CalCoreUser:
    def __init__(self, name, age, gender, height_cm, weight_kg, body_fat_pct):
        self.name = name
        self.age = age
        self.gender = gender
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.body_fat_pct = body_fat_pct

    def bmr(self):
        """Calculate BMR"""
        lean_mass = self.weight_kg * (1 - self.body_fat_pct / 100)
        return round(370 + 21.6 * lean_mass, 2)

    def calories_burned(self, activity, duration_min):
        """Calculate Calories burn depend on different activities"""
        MET_table = {
            "WALK": 3.5,
            "DANCE": 5.5,
            "RUN": 8.0,
            "CYCLE": 6.0,
            "SWIM": 7.0
        }
        met = MET_table.get(activity.upper(), 4.0)  # default
        kcal = met * self.weight_kg * (duration_min / 60)
        return round(kcal, 2)

    def summary(self):
        return {
            "Name": self.name,
            "Height(cm)": self.height_cm,
            "Weight(kg)": self.weight_kg,
            "Body Fat %": self.body_fat_pct,
            "BMR(kcal/day)": self.bmr()
        }

