from openai import OpenAI
import json

# Initialize OpenAI client
client = OpenAI()

def plan_goal(goal: str) -> dict:
    """
    Break a high-level goal into executable tasks.
    """
    prompt = f"""
You are an autonomous AI planner.

Break the following goal into clear, logical, executable tasks.
Return ONLY valid JSON in this format:

{{
  "tasks": [
    "task 1",
    "task 2",
    "task 3"
  ]
}}

Goal: {goal}
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    return json.loads(response.choices[0].message.content)
  
