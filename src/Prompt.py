import random, math
class Prompt:
    def __init__(self):
        self.base = random.randrange(10, 20)
        definite_phrases = ["for sure", "for certain", "definitely"]
        self.def_phrase_picked = random.choice(definite_phrases)

        # Define risk phrases
        risk_phrases = ["chance for", "opportunity to win", "possibility of getting"]
        self.risk_phrase_picked = random.choice(risk_phrases)

        risk_phrases_loss = ["chance to lose", "opportunity to lose", "possibility to lose"]
        self.risk_phrase_loss_picked = random.choice(risk_phrases_loss)

        

        # Define fail phrases
        fail_phrases = ["chance for $0", "risk of getting nothing", "possibility of $0"]
        self.fail_phrase_picked = random.choice(fail_phrases)

        fail_phrases_loss = ["chance to lose $0", "risk of losing nothing", "possibility of losing $0"]
        self.fail_phrase_loss_picked = random.choice(fail_phrases_loss)

        self.lower_multiples = [1.1111, 1.25, 1.42857, 1.66667]
        self.higher_multiples= [2,2.5,3.3333,4,5,10]

    def highRiskGainPrompt(self,pos_ev=True, rand=False):
        multiplier_low = random.choice(self.higher_multiples)
        if pos_ev is True:
            risk_probability_low = round((1 / multiplier_low),1)*100 
            risk_option_low = round(self.base * multiplier_low, 0)# + math.ceil(self.base*(random.randrange(1, 3)/10))
        else:
            risk_probability_low = round((1 / multiplier_low),1)*100 
            risk_option_low = round(self.base * multiplier_low, 0)# - math.ceil(self.base*(random.randrange(1, 3)/10))
        if rand is True:
            prompts = [
        f"You have two options, option A: get ${self.base} {self.def_phrase_picked} or option B a {risk_probability_low}% {self.risk_phrase_picked} ${risk_option_low} with a {100 - risk_probability_low}% {self.fail_phrase_picked}.",
        f"Choose between option A: getting ${self.base} {self.def_phrase_picked} or option B: {risk_probability_low}% {self.risk_phrase_picked} ${risk_option_low}, but be aware there's a {100 - risk_probability_low}% {self.fail_phrase_picked}.",
        f"Option A: ${self.base} {self.def_phrase_picked}. Option B: {risk_probability_low}% {self.risk_phrase_picked} ${risk_option_low}, with a {100 - risk_probability_low}% {self.fail_phrase_picked}.",
        f"Would you prefer to receive option A: ${self.base} {self.def_phrase_picked}, or option B: take a {risk_probability_low}% {self.risk_phrase_picked} ${risk_option_low}? Remember, there's a {100 - risk_probability_low}% {self.fail_phrase_picked}.",
        f"Option A: get ${self.base} {self.def_phrase_picked} immediately or option B, gamble with a {risk_probability_low}% {self.risk_phrase_picked} ${risk_option_low}, knowing there's a {100 - risk_probability_low}% {self.fail_phrase_picked}."
    ]
            return random.choice(prompts)
        else:
            return f"Imagine you are in a game where you trying to win as much money as possible. Which option do you prefer? Option A: ${self.base} {self.def_phrase_picked}. Option B: {risk_probability_low}% {self.risk_phrase_picked} ${risk_option_low}, with a {100 - risk_probability_low}%  {self.fail_phrase_picked}."
    
    def lowRiskGainPrompt(self, pos_ev=True, rand=False):
        multiplier = random.choice(self.lower_multiples)
        if pos_ev is True:
            risk_probability = round((1 / multiplier),1)*100 
            risk_option = round(self.base * multiplier, 0)# + math.ceil(self.base*(random.randrange(1, 3)/10))
        else:
            risk_probability = round((1 / multiplier),1)*100 
            risk_option = round(self.base * multiplier, 0)# - math.ceil(self.base*(random.randrange(1, 3)/10))
        if rand is True:
            prompts = [
        f"You have two options, option A: get ${self.base} {self.def_phrase_picked} or option B a {risk_probability}% {self.risk_phrase_picked} ${risk_option} with a {100 - risk_probability}% {self.fail_phrase_picked}.",
        f"Choose between option A: getting ${self.base} {self.def_phrase_picked} or option B: {risk_probability}% {self.risk_phrase_picked} ${risk_option}, but be aware there's a {100 - risk_probability}% {self.fail_phrase_picked}.",
        f"Option 1self.base {self.def_phrase_picked}. Option 2: {risk_probability}% {self.risk_phrase_picked} ${risk_option}, with a {100 - risk_probability}% {self.fail_phrase_picked}.",
        f"Would you prefer to receive option A: ${self.base} {self.def_phrase_picked}, or option B: take a {risk_probability}% {self.risk_phrase_picked} ${risk_option}? Remember, there's a {100 - risk_probability}% {self.fail_phrase_picked}.",
        f"Option A: get ${self.base} {self.def_phrase_picked} immediately or option B, gamble with a {risk_probability}% {self.risk_phrase_picked} ${risk_option}, knowing there's a {100 - risk_probability}% {self.fail_phrase_picked}."
    ]
            return random.choice(prompts)
        else:
            return f"Imagine you are in a game where you trying to win as much money as possible. Which option do you prefer? Option A: ${self.base} {self.def_phrase_picked}. Option B: {risk_probability}% {self.risk_phrase_picked} ${risk_option}, with a {100 - risk_probability}%  {self.fail_phrase_picked}."
    def highRiskLossPrompt(self,pos_ev=True, rand=False):
        multiplier_low = random.choice(self.higher_multiples)
        if pos_ev is True:
            risk_probability_low = round((1 / multiplier_low),1)*100 
            risk_option_low = round(self.base * multiplier_low, 0)# + math.ceil(self.base*(random.randrange(1, 3)/10))
        else:
            risk_probability_low = round((1 / multiplier_low),1)*100 
            risk_option_low = round(self.base * multiplier_low, 0)# - math.ceil(self.base*(random.randrange(1, 3)/10))
        if rand is True:   
            prompts = [
        f"You have two options, option A: lose ${self.base} {self.def_phrase_picked} or option B a {risk_probability_low}% {self.risk_phrase_loss_picked} ${risk_option_low} with a {100 - risk_probability_low}% {self.fail_phrase_loss_picked}.",
        f"Choose between option A: losing ${self.base} {self.def_phrase_picked} or option B: {risk_probability_low}% {self.risk_phrase_loss_picked} ${risk_option_low}, but be aware there's a {100 - risk_probability_low}% {self.fail_phrase_loss_picked}.",
        f"Option A: a loss of ${self.base} {self.def_phrase_picked}. Option B: {risk_probability_low}% {self.risk_phrase_loss_picked} ${risk_option_low}, with a {100 - risk_probability_low}% {self.fail_phrase_loss_picked}.",
        f"Would you prefer to receive option A: lose ${self.base} {self.def_phrase_picked}, or option B: take a {risk_probability_low}% {self.risk_phrase_loss_picked} ${risk_option_low}? Remember, there's a {100 - risk_probability_low}% {self.fail_phrase_loss_picked}.",
        f"Option A: lose ${self.base} {self.def_phrase_picked} immediately or option B, gamble with a {risk_probability_low}% {self.risk_phrase_loss_picked} ${risk_option_low}, knowing there's a {100 - risk_probability_low}% {self.fail_phrase_loss_picked}."
    ]
            return random.choice(prompts)
        else:
              return f"Imagine you are in a game where you trying to lose as little money as possible. Which option do you prefer? Option A: a loss of ${self.base} {self.def_phrase_picked}. Option B: {risk_probability_low}% {self.risk_phrase_loss_picked} ${risk_option_low}, with a {100 - risk_probability_low}% {self.fail_phrase_loss_picked}."
    
    def lowRiskLossPrompt(self, pos_ev=True, rand=False):
        multiplier = random.choice(self.lower_multiples)
        if pos_ev is True:
            risk_probability = round((1 / multiplier),1)*100  
            risk_option = round(self.base * multiplier, 0)# + math.ceil(self.base*(random.randrange(1, 3)/10))
        else:
            risk_probability = round((1 / multiplier),1)*100 
            risk_option = round(self.base * multiplier, 0)# - math.ceil(self.base*(random.randrange(1, 3)/10))
        if rand is True:
            prompts = [
        f"You have two options, option A: lose ${self.base} {self.def_phrase_picked} or option B a {risk_probability}% {self.risk_phrase_loss_picked} ${risk_option} with a {100 - risk_probability}% {self.fail_phrase_loss_picked}.",
        f"Choose between option A: losing ${self.base} {self.def_phrase_picked} or option B: {risk_probability}% {self.risk_phrase_loss_picked} ${risk_option}, but be aware there's a {100 - risk_probability}% {self.fail_phrase_loss_picked}.",
        f"Option 1: a loss of ${self.base} {self.def_phrase_picked}. Option 2: {risk_probability}% {self.risk_phrase_loss_picked} ${risk_option}, with a {100 - risk_probability}% {self.fail_phrase_loss_picked}.",
        f"Would you prefer to receive option A: lose ${self.base} {self.def_phrase_picked}, or option B: take a {risk_probability}% {self.risk_phrase_loss_picked} ${risk_option}? Remember, there's a {100 - risk_probability}% {self.fail_phrase_loss_picked}.",
        f"Option A: lose ${self.base} {self.def_phrase_picked} immediately or option B, gamble with a {risk_probability}% {self.risk_phrase_loss_picked} ${risk_option}, knowing there's a {100 - risk_probability}% {self.fail_phrase_loss_picked}."
    ]
            return random.choice(prompts)
        else:
              return f"Imagine you are in a game where you trying to lose as little money as possible. Which option do you prefer? Option A: a loss of ${self.base} {self.def_phrase_picked}. Option B: {risk_probability}% {self.risk_phrase_loss_picked} ${risk_option}, with a {100 - risk_probability}% {self.fail_phrase_loss_picked}."