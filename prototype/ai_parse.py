import openai

openai.api_key = "your_api_key_here"  # 替换成你的 API key

def convert_nl_to_dsl(user_input):
    prompt = f"""Convert the following natural language health log into CalCore DSL format:
---
{user_input}
---
Output:
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that converts user input into CalCore DSL."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message['content'].strip()
