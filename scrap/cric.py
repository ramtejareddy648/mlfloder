from pycricbuzz import Cricbuzz
from tkinter import Tk,Label

root=Tk()
root.title("live cricket score")
root.geometry("1000x850")


c=Cricbuzz()
try:
    match=c.matches()
    score=c.livescore(match[0]["id"])
    commentry=c.commentary(match[0]["id"])
    score_board=c.scorecard(match[0]["id"])
    formatted=''
    for key,value in score.items():
        formatted+=f"{key}:\n"
        for sub_key,sub_value in value.items():
            formatted+=f"{sub_key}:{sub_value}\n"
        formatted+="\n"
    print(formatted)






    score1=Label(root,font=("time",15,"blod"),bg="white",text=formatted,justify="left")
    score1.grid(row=2,column=2,pady=25,padx=100)
except Exception as e:
    print(f'error is {e}')
root.mainloop()
