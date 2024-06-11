import random
class ProbGenerator:
    def __init__(self) -> None:
        self.base = random.randrange(10, 20)
        self.lower_multiples = [1.1111, 1.25, 1.42857, 1.66667]
        self.higher_multiples= [2,2.5,3.3333,4,5,10]
    def lowRisk(self):
        multiple = random.choice(self.lower_multiples)
        return {"base": self.base, 
                "risky": round(self.base*multiple),
                "risk_prob":1/multiple}
    def highRisk(self):
        multiple = random.choice(self.higher_multiples)
        return {"base": self.base, 
                "risky": round(self.base*multiple),
                "risk_prob":1/multiple}