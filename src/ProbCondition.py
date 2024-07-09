from ProbGenerator import ProbGenerator
import random

# this class generates an iterator of prompts that pose the
# scenario with raw probabilities

class ProbCondition:
    def __init__(self):
        self.choice_sets = ProbGenerator().createChoiceSets()

        
    def createPrompt(self,choice, var = "alt"):
        letter_choices = ["F","J"]
        safe_ind = random.randrange(0,2)
        safe_letter = letter_choices[safe_ind]
        risk_letter = letter_choices[1-safe_ind]
        if var == "main":
            if choice[0] < 0:
                safe_choice = "-$"+str(choice[0]*-1)
            else:
                safe_choice = "$"+str(choice[0])
            if choice[2] < 0:
                risk_choice = "-$"+str(choice[2]*-1)
            else:
                risk_choice = "$"+str(choice[2])
            if safe_letter == "F":
                return {"prompt":f"Please choose between the two options below:\nGive your answer using the tags <Answer> CHOICE </Answer>, where CHOICE is either F or J.\n F: {safe_choice} with certainty \nor\nJ: {risk_choice} with probability {choice[1]}, $0 with probability {round(1-choice[1],2)}.",
                "risk": risk_letter
            }
            else:
                return {"prompt":f"Please choose between the two options below:\nGive your answer using the tags <Answer> CHOICE </Answer>, where CHOICE is either F or J.\n F: {risk_choice} with probability {choice[1]}, $0 with probability {round(1-choice[1],2)}  \nor\nJ: {safe_choice} with certainty.",
                "risk": risk_letter
            }
        elif var == "alt":
            if choice[0] < 0:
                safe_choice = f"A sure loss of ${choice[0]*-1}"
            else:
                safe_choice = f"A sure gain of ${choice[0]}"
            if choice[2] < 0:
                risk_choice = f"A {choice[1]*100}% chance of losing of ${choice[2]*-1}, otherwise $0" 
            else:
                risk_choice = f"A {choice[1]*100}% chance of gaining of ${choice[2]}, otherwise $0"

            if safe_letter == "F":
                return {"prompt":f"Please choose between the two options below:\nGive your answer using the tags <Answer> CHOICE </Answer>, where CHOICE is either F or J.\n F: {safe_choice}, \nor\nJ: {risk_choice}.",
                "risk": risk_letter
            }
            else:
                return {"prompt":f"Please choose between the two options below:\nGive your answer using the tags <Answer> CHOICE </Answer>, where CHOICE is either F or J.\n F: {risk_choice},  \nor\nJ: {safe_choice}.",
                "risk": risk_letter
            }

    def PromptList(self,):
        return list(map(self.createPrompt ,self.choice_sets))

# pc  = ProbCondition()
# li = pc.PromptList()

#print(li[0:20])
