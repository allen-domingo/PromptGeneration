from ProbGenerator import ProbGenerator
import random
class ProbCondition:
    def __init__(self):
        self.choice_sets = ProbGenerator().createChoiceSets()
        
    def createPrompt(self,choice):
        letter_choices = ["F","J"]
        safe_ind = random.randrange(0,2)
        safe_letter = letter_choices[safe_ind]
        risk_letter = letter_choices[1-safe_ind]
        return {"prompt":f"Please choose between the two options below:\nGive your answer using the tags <Answer> CHOICE </Answer>, where CHOICE is either F or J.\n{safe_letter}: ${choice[0]} with certainty \nor\n{risk_letter}: ${choice[2]} with probability {choice[1]}, $0 with probability {round(1-choice[1],2)}.",
        "risk": f"<Answer> {risk_letter} </Answer>"
    }
    def PromptList(self):
        return map(self.createPrompt, self.choice_sets)
pc  = ProbCondition()
li = pc.PromptList()

print(li)