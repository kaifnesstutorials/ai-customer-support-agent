from app.utils.llm import get_llm_response

def critic_agent(answer):
    prompt = f"""
You are a strict quality checker.

Check if the following answer is:
- Correct
- Complete
- Based on given information

Answer:
{answer}

Reply ONLY with:
GOOD or BAD
"""

    return get_llm_response(prompt)