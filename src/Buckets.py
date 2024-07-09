import random
from ProbGenerator import ProbGenerator
class Buckets:
    def __init__(self):
        self.choice_sets = ProbGenerator().createChoiceSets()
         
    def generate_risk_ticket(self,outcome, chance, rand=True):
        if outcome < 0:
            zero = "-$0"
            option = f"-${outcome*-1}"
        else:
            zero = "$0"
            option = f"${outcome}"
        risk_bucket = [option] * int((chance)*20)     
        
        risk_bucket.extend([zero]*int((1-chance)*20))
        if rand is True:
            random.shuffle(risk_bucket)
        return ", ".join(risk_bucket)
    def generate_safe_ticket(self,outcome):
        if outcome < 0:
            option = f"-${outcome*-1}"
        else:
            option = f"${outcome}"
        return", ".join([option]*20)
    def generate_prompt(self, choice, rand=True):
        letter_choices = ["F","J"]
        safe = choice[0]
        prob = choice[1]
        risk = choice[2]
        safe_ind = random.randrange(0,2)
        safe_letter = letter_choices[safe_ind]
        risk_letter = letter_choices[1-safe_ind]
        if safe < 0:
            block_1 = "In front of you are two buckets, labeled F and J. Each associated with a specific loss of money. You hava single opportunity to choose one of two buckets. A ticket will be randomly drawn from the bucket you choose, and you will receive the outcome written on the ticket.\n Below are all all the tickets in each bucket, listed in random order:\n"
        else:
            block_1 = "In front of you are two buckets, labeled F and J. Each associated with a specific gain of money. You hava single opportunity to choose one of two buckets. A ticket will be randomly drawn from the bucket you choose, and you will receive the outcome written on the ticket.\n Below are all all the tickets in each bucket, listed in random order:\n"
        if safe_letter == "F":
            bucket_f = self.generate_safe_ticket(safe)
            bucket_j = self.generate_risk_ticket(outcome=risk, chance=prob, rand=rand)
        else:
            bucket_f = self.generate_risk_ticket(outcome=risk, chance=prob, rand=rand)
            bucket_j = self.generate_safe_ticket(safe)
        return {"prompt": f"{block_1} F: {bucket_f}\nor\n J: {bucket_j} \n Which would you choose?\n Give your answer using the tags <Answer> CHOICE </Answer>, where CHOICE is either F or J.", "risk":risk_letter}
    def PromptList(self):
        return list(map(self.generate_prompt ,self.choice_sets))
        