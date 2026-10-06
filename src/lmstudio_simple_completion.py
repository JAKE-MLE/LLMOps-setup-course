import os
import openai
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(
    base_url=os.getenv("LMSTUDIO_BASE_URL"),  # ← seule vraie différence
    api_key="lm-studio",                       # clé bidon, ignorée
)

def generate(prompt):
    response = client.chat.completions.create(
        model=os.getenv("LMSTUDIO_MODEL"),     # ← au lieu de "gpt-4o"
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=500,
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print(generate("Explique moi ce qu'est un oxyure"))