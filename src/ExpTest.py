from OpenAIModel import OpenAIModel
from HuggingFaceModel import HuggingFaceModel
from ProbGenerator import ProbGenerator
from ExpSim import ExpSim
import pandas as pd
import plotly.express as px
import re
def main():
    answer_list = ["safe","risk"]
    letter_list = ["F","J"]
    freq_exp = [0,0]
    freq_letter = [0,0]
    freq_risk_letter = [0,0]\
     # we generate a list where each element is a tuple containing
    # a reward for the safe option, a probability for the risky option
    # and a reward for the risky option
    c_sets = ProbGenerator().createChoiceSets()
    choice_string = [str(c) for c in c_sets]
    c_sets_len = len(c_sets)
    data_exp = {
            "safe":[0]*c_sets_len,
            "risky":[0]*c_sets_len
    }
    
    exp_frame = pd.DataFrame.from_dict(data_exp)
    exp_frame.index = choice_string
    for i in range(5):
        index = 0
        # we go through this list and for each element we
        # get a response from the LLM when the problem is
        # phrased experientially
        for choice_set in c_sets:
            #gptInstance = HuggingFaceModel(name="openai-community/gpt2")
            gptInstance = OpenAIModel()
            # generate an experiential prompt
            experience = ExpSim(choice_set).iterate(10)
            ans = gptInstance.run(experience["prompt"])

            # keep track of how often the risk letter was
            # a particular letter (the ExpSim class selects randomly,
            # so the frequency should be equal)
            if experience["risk"] == "F":
                    freq_risk_letter[0] +=1
            else:
                    freq_risk_letter[1] +=1

            pattern = re.search("(?<=\<Answer>)(.*?)(?=\</Answer>)",ans)

            # if the pattern is found
            if pattern != None:
                answer = re.sub("\s","",pattern.group())
            else:
                answer = "None"

            if answer in letter_list:
                if(answer != experience["risk"]):
                                freq_exp[0] += 1
                                data_exp["safe"][index] += 1
                elif(answer == experience["risk"]):
                                data_exp["risky"][index] += 1
                                freq_exp[1] += 1
                if answer == "F":
                        freq_letter[0]+=1
                elif answer == "J":
                        freq_letter[1]+=1
            index +=1
    #write results to file called results.txt
    results = f"""RESULTS
    Experience | Safe: {freq_exp[0]} Risky: {freq_exp[1]}
    Letter Chosen | F: {freq_letter[0]} J: {freq_letter[1]}
    Risk Letter | F: {freq_risk_letter[0]} J: {freq_risk_letter[1]}
    """
    f = open("results.txt", "w")
    f.write(results)
    exp_frame = pd.DataFrame.from_dict(data_exp)
    exp_frame.index = choice_string
    f1 = open("experience.txt","w")
    f1.write(exp_frame.to_string())



main()