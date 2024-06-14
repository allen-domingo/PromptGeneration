import random, numpy as np
class ProbGenerator:
    def __init__(self) -> None:
        self.base = random.randrange(10, 20)
        self.lower_multiples = [1.1111, 1.25, 1.42857, 1.66667]
        self.higher_multiples= [2,2.5,3.3333,4,5,10]
    def createChoiceSets(self):
        neg_ints = np.linspace(-10,-1,10, dtype=int)
        pos_ints = np.linspace(1,10,10, dtype=int)
        x = np.concatenate((neg_ints,pos_ints))
        probs = np.linspace(.05,.95,19)
        grid = np.meshgrid(x, probs)
        sure_thing = np.around(grid[0].ravel(),2)
        risk_prob = np.around(grid[1].ravel(),2)
        risky_outcome = np.around(sure_thing/risk_prob,2)
        return  list(zip(sure_thing,risk_prob, risky_outcome))   
    def lowRisk(self):
        multiple = random.choice(self.lower_multiples)
        return (self.base, 
                round(self.base*multiple),
                1/multiple)
    def highRisk(self):
        multiple = random.choice(self.higher_multiples)
        return (self.base, 
                round(self.base*multiple),
                1/multiple)