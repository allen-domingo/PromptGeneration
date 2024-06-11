from ProbGenerator import ProbGenerator
import random
class ExpSim:
    def __init__(self):
        generator = ProbGenerator()
        self.probs =  generator.lowRisk()
        self.prompt = "Imagine you are playing a a game where you are tying to win as much money as possible. You have two options, A and B.\n"
        
    def iterate(self, trials=5):
       
        options = ["A", "B"]
        #print(self.probs)
        for i in range(trials):
          pick = random.randrange(0,2)
          
          gain = 0
          if options[pick] == "B":
              result = random.uniform(0,1)
              if result < self.probs["risk_prob"]:
                  gain = self.probs["risky"]
          else:
              gain = self.probs["base"]
          self.prompt = self.prompt + f"You choose option {options[pick]}, and get ${gain}.\n"
        
       # print(self.prompt)
        return self.prompt + "Which would you now choose? "
              
exp = ExpSim()
exp.iterate()