from openai import OpenAI
from dotenv import find_dotenv, load_dotenv
import os
class AI:
  def __init__(self):
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)
    self.openai = OpenAI(
      organization=os.environ.get("ORGANIZATION", "org"),
      api_key=os.environ.get("api_key", "key")
    )
  def run(self, prompt):
    return self.openai.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "user", "content": prompt + "Say only the letter and nothing else"}],
      stream=True,
  )