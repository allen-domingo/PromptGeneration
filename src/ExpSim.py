from ProbGenerator import ProbGenerator
import random
class ExpSim:
    def __init__(self, probabilities=None):
        if probabilities is None:
            generator = ProbGenerator()
            self.probs =  generator.lowRisk()
        else:
            self.probs = probabilities

        
        self.letter_choices = ["F","J"]
        self.risk_letter = random.choice(self.letter_choices)
        self.prompt = "Imagine you are playing a a game where you are tying to win as much money as possible. You have two options, F and J.\n"
        
    def iterate(self, trials=10):
        #print(self.probs)
        for i in range(trials):
          pick = random.randrange(0,2)
          
          gain = 0
          if self.letter_choices[pick] ==self. risk_letter:
              result = random.uniform(0,1)
              if result < self.probs[1]:
                  gain = self.probs[2]
          else:
              gain = self.probs[0]
          self.prompt = self.prompt + f"You choose option {self.letter_choices[pick]}, and get ${gain}.\n"
        
        print(self.prompt)
        return {"prompt": self.prompt + "Which would you now choose? \nGive your answer using the tags <Answer> CHOICE </Answer>, where CHOICE is either F or J.", "risk":self.risk_letter}
              
exp = ExpSim()
exp.iterate()