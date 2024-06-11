from Prompt import Prompt
from APITest import AI
from ExpSim import ExpSim
import pandas as pd
import plotly.express as px
import sys

def main():
    answer_list = ["A","B"]
    freq_desc = [0,0]
    freq_exp = [0,0]
    tries = int(sys.argv[1])
    for i in range(tries):
      #  pr = Prompt()
        experience = ExpSim()
        gptInstance = AI()
        stream = gptInstance.run(experience.iterate(10))
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                answer = chunk.choices[0].delta.content
                if len(answer) == 1:
                    if(answer == "A"):
                        freq_exp[0] += 1
                    elif (answer == "B"):
                        freq_exp[1] += 1
                    print(chunk.choices[0].delta.content, end="" )
    print("\n")
    for i in range(tries):
        pr = Prompt().highRiskGainPrompt(rand=True)
        print(pr)
        gptInstance = AI()
        stream = gptInstance.run(pr)
        print
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                answer = chunk.choices[0].delta.content
                print(answer)
                if len(answer) == 1:
                    if(answer == "A"):
                        freq_desc[0] += 1
                    elif (answer == "B"):
                        freq_desc[1] += 1
                    #print(chunk.choices[0].delta.content, end="" )
    print("\n")
    df = pd.DataFrame(answer_list)
    fig1 = px.bar(df, x=answer_list,y=freq_desc, labels={"answer_list": "Option", "freq": "Frequency"}
,                  title="Description Option Frequency")
    fig1.show()
    fig2 = px.bar(df, x=answer_list,y=freq_exp, labels={"answer_list": "Option", "freq": "Frequency"}
,                  title="Experience Option Frequency")
    fig2.show()
 
main()