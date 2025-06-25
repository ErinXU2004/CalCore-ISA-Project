import re
from datetime import date

def parse_input(text):
    dsl_lines = []
    today = str(date.today())

    # Extract weight like "I weigh 52.3 kg"
    weight_match = re.search(r"weigh\s+([0-9.]+)", text, re.IGNORECASE)
    if weight_match:
        weight = weight_match.group(1)
        dsl_lines.append(f"LOG_WEIGHT {today} {weight}")

    # Extract food like "I ate a beef salad"
    eat_match = re.search(r"ate\s+([a-zA-Z0-9.,\s]+?)(?:\s+and|\s+then|$)", text, re.IGNORECASE)
    if eat_match:
        food = eat_match.group(1).strip()
        dsl_lines.append(f"EAT {food}")

    # Extract exercise like "ran for 30 minutes"
    move_match = re.search(r"(ran|danced|swam|biked|walked|exercised)\s+for\s+([0-9]+)\s+minutes", text, re.IGNORECASE)
    if move_match:
        move_type = move_match.group(1)
        duration = move_match.group(2)
        dsl_lines.append(f"MOVE {move_type} {duration}")

    return