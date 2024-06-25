from Prompt import Prompt
# from OpenAIModel import OpenAIModel
from HuggingFaceModel import HuggingFaceModel
from ExpSim import ExpSim
from ProbCondition import ProbCondition
from ProbGenerator import ProbGenerator
import pandas as pd
import plotly.express as px
import re


def main():
    answer_list = ["safe","risk"]
    letter_list = ["F","J"]
    freq_desc = [0,0]
    freq_letter = [0,0]
    freq_risk_letter = [0,0]

    gptInstance = HuggingFaceModel(name="openai-community/gpt2")

    # we generate a list where each element is a tuple containing
    # a reward for the safe option, a probability for the risky option
    # and a reward for the risky option
    c_sets = ProbGenerator().createChoiceSets()

    pc_list = ProbCondition().PromptList()
    choice_string = [str(c) for c in c_sets]
    c_sets_len = len(c_sets)
    data_des = {
            "safe":[0]*c_sets_len,
            "risky":[0]*c_sets_len
    }
    for i in range(50):
        index = 0
        for prompt in pc_list:
                if prompt["risk"] == "F":
                        freq_risk_letter[0] +=1
                else:
                        freq_risk_letter[1] +=1
                ans = gptInstance.run(prompt["prompt"])

                pattern = re.search("(?<=\<Answer>)(.*?)(?=\</Answer>)",ans)

                # if the pattern is found
                if pattern != None:
                        answer = re.sub("\s","",pattern.group())
                else:
                        answer = "None"

                if answer in letter_list:
                        if(answer != prompt["risk"]):
                                        data_des["safe"][index] += 1
                                        freq_desc[0] += 1
                        elif(answer == prompt["risk"]):
                                        data_des["risky"][index] += 1
                                        freq_desc[1] += 1
                        if answer == "F":
                                freq_letter[0]+=1
                        elif answer == "J":
                                freq_letter[1]+=1
                index+=1



    df = pd.DataFrame(answer_list)
    fig1 = px.bar(df, x=answer_list,y=freq_desc, labels={"answer_list": "Option", "freq": "Frequency"}
,                  title="Description Option Frequency")
    fig1.show()
 
    results = f"""RESULTS
    Description | Safe: {freq_desc[0]} Risky: {freq_desc[1]}
    Letter Chosen | F: {freq_letter[0]} J: {freq_letter[1]}
    Risk Letter |cF: {freq_risk_letter[0]} J: {freq_risk_letter[1]}
    """
    f = open("results.txt", "w")
    f.write(results)
    prob_frame = pd.DataFrame.from_dict(data_des)
    prob_frame.index = choice_string
    f1 = open("prob.txt","w")
    f1.write(prob_frame.to_string())

main()
