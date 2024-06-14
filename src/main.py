from Prompt import Prompt
from APITest import AI
from ExpSim import ExpSim
from ProbCondition import ProbCondition
from ProbGenerator import ProbGenerator
import pandas as pd
import plotly.express as px
import sys

def main():
    answer_list = ["safe","risk"]
    letter_list = ["F","J"]
    letter_list2 = ["<Answer> F </Answer>","<Answer> J </Answer>"]
    freq_desc = [0,0]
    freq_exp = [0,0]
    # if sys.argv[1] != None:
    #     tries = int(sys.argv[1])
    c_sets = ProbGenerator().createChoiceSets()
    for choice_set in c_sets:
      #  pr = Prompt()
        experience = ExpSim(choice_set).iterate(10)
        gptInstance = AI()
        stream = gptInstance.run(experience["prompt"])
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                answer = chunk.choices[0].delta.content
                if answer in letter_list:
                    if(answer != experience["risk"]):
                        freq_exp[0] += 1
                    elif (answer == experience["risk"]):
                        freq_exp[1] += 1
                    print(chunk.choices[0].delta.content, end="" )
    print("\n")
    pc_list = ProbCondition().PromptList()
    for prompt in pc_list:
        gptInstance = AI()

        stream = gptInstance.run(prompt["prompt"],strm=False)
        for chunk in stream:
            if chunk is not None:
                answer = stream.choices[0].message.content
                
                if answer in letter_list2:
                    if(answer != prompt["risk"]):
                        freq_desc[0] += 1
                    elif(answer == prompt["risk"]):
                        freq_desc[1] += 1
                    print(answer != prompt["risk"])
               
   
    df = pd.DataFrame(answer_list)
    fig1 = px.bar(df, x=answer_list,y=freq_desc, labels={"answer_list": "Option", "freq": "Frequency"}
,                  title="Description Option Frequency")
    fig1.show()
    fig2 = px.bar(df, x=answer_list,y=freq_exp, labels={"answer_list": "Option", "freq": "Frequency"}
,                  title="Experience Option Frequency")
    fig2.show()
 
main()