from transformers import AutoModelForCausalLM, AutoTokenizer
import accelerate
import optimum
import auto_gptq
import torch
from dotenv import find_dotenv, load_dotenv
import os

class HuggingFaceModel:
  def __init__(self, name="TheBloke/Llama-2-13B-chat-GPTQ", prompt_format='f"[INST] <<SYS>>{system_prompt}<</SYS>>\n{user_prompt}[/INST]"', hf_key=None):

    self.model_name = name
    self.prompt_format = prompt_format

    self.tokenizer = AutoTokenizer.from_pretrained(name, use_fast=True)

    if hf_key == None:
      dotenv_path = find_dotenv()
      load_dotenv(dotenv_path)
      self.model = AutoModelForCausalLM.from_pretrained(name,
                      token=os.environ.get("hf_key", "key"),
                      device_map="auto",
                      trust_remote_code=True,
                      revision="main")
    else:
      self.model = AutoModelForCausalLM.from_pretrained(name,
                      token=hf_key,
                      device_map="auto",
                      trust_remote_code=True,
                      revision="main")

  def run(self, user_prompt, system_prompt="", temperature=0.0):

    prompt = eval(self.prompt_format)

    prompt_len = len(prompt)

    input_ids = self.tokenizer(prompt, return_tensors='pt').input_ids.cuda()
    output_tokens = self.model.generate(inputs=input_ids, temperature=temperature, do_sample=True, max_new_tokens=100)
    output = self.tokenizer.decode(output_tokens[0])

    output = output[prompt_len:]

    if len(output) > 0:
      return output
    else:
      return "<Answer>None</Answer>"
