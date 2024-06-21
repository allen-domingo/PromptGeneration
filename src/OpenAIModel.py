from openai import OpenAI
from dotenv import find_dotenv, load_dotenv
import os
class OpenAIModel:
  def __init__(self, name="gpt-3.5-turbo", api_key=None):

    self.model_name = name

    if api_key == None:
      dotenv_path = find_dotenv()
      load_dotenv(dotenv_path)
      self.openai = OpenAI(
        organization=os.environ.get("ORGANIZATION", "org"),
        api_key=os.environ.get("api_key", "key")
      )
    else:
      self.openai = OpenAI(api_key=api_key)

  def run(self, prompt, temperature=0.0, strm=False):
    response = self.openai.chat.completions.create(
      model=self.model_name,
      messages=[{"role": "user", "content": prompt}],
      temperature=temperature,
      stream=strm)
    return response.choices[0].message.content
