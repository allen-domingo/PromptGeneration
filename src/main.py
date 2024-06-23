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
    freq_exp = [0,0]
    freq_letter = [0,0]
    freq_risk_letter = [0,0]

    gptInstance = HuggingFaceModel(name="openai-community/gpt2")

    # we generate a list where each element is a tuple containing
    # a reward for the safe option, a probability for the risky option
    # and a reward for the risky option
    c_sets = ProbGenerator().createChoiceSets()

    # we go through this list and for each element we
    # get a response from the LLM when the problem is
    # phrased experientially
    for choice_set in c_sets:
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

        print(ans)

        pattern = re.search("(?<=\<Answer>)(.*?)(?=\</Answer>)",ans)

        # if the pattern is found
        if pattern != None:
            answer = re.sub("\s","",pattern.group())
        else:
            answer = "None"

        if answer in letter_list:
            if(answer != experience["risk"]):
                        freq_exp[0] += 1
            elif(answer == experience["risk"]):
                        freq_exp[1] += 1
            if answer == "F":
                    freq_letter[0]+=1
            elif answer == "J":
                    freq_letter[1]+=1


    print("\n")
    pc_list = ProbCondition().PromptList()

    for prompt in pc_list:

        ans = gptInstance.run(prompt["prompt"])

        pattern = re.search("(?<=\<Answer>)(.*?)(?=\</Answer>)",ans)

        # if the pattern is found
        if pattern != None:
            answer = re.sub("\s","",pattern.group())
        else:
            answer = "None"

        if answer in letter_list:
            if(answer != prompt["risk"]):
                        freq_desc[0] += 1
            elif(answer == prompt["risk"]):
                        freq_desc[1] += 1
            if answer == "F":
                    freq_letter[0]+=1
            elif answer == "J":
                    freq_letter[1]+=1



    df = pd.DataFrame(answer_list)
    fig1 = px.bar(df, x=answer_list,y=freq_desc, labels={"answer_list": "Option", "freq": "Frequency"}
,                  title="Description Option Frequency")
    fig1.show()
    fig2 = px.bar(df, x=answer_list,y=freq_exp, labels={"answer_list": "Option", "freq": "Frequency"}
,                  title="Experience Option Frequency")
    fig2.show()
    results = f"""RESULTS
    Description | Safe: {freq_desc[0]} Risky: {freq_desc[1]}
    Experience | Safe: {freq_exp[0]} Risky: {freq_exp[1]}
    Letter Chosen | F: {freq_letter[0]} J: {freq_letter[1]}
    Risk Letter |cF: {freq_risk_letter[0]} J: {freq_risk_letter[1]}
    """
    f = open("results.txt", "w")
    f.write(results)

main()
