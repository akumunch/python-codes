import turtle 
import pandas

ALIGN= "left"
FONT= ("Courier", 10, "bold")


def answer_in_data(answer,data):
    states=data["state"].to_list()
    if (answer in states):
        return True
    return False

def getcords(answer,dict):
    for value in dict.values():
        for key,val in value.items():
            if (val==answer):
                index=key
    print(index)
    x=dict['x'][index]
    y=dict['y'][index]
    return (x,y)

def exitsequence(states_left,data):
    states= data["state"].to_list()
    states_left=[state for state in states if state not in correct_guesses]
    dataframe_left= pandas.DataFrame(states_left)
    csv_left=dataframe_left.to_csv('us-state-game/states_to_learn.csv')


game_is_on=True
ctr=0
tim=turtle.Turtle()
tim.hideturtle()
screen= turtle.Screen()
screen.title("U.S. State Game")
image="us-state-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data= pandas.read_csv('us-state-game/50_states.csv')
data_dict=data.to_dict()
correct_guesses=[]



while(game_is_on):
    screen.tracer(0)  
    answer= (screen.textinput(title=f"{ctr}/50 States Correct", prompt="What's another state's name?")).title()

    if ((answer=="Exit") or (ctr==50)):
        states_left=[]
        exitsequence(states_left,data)
        game_is_on=False
    
    if (answer_in_data(answer,data)):
        ctr+=1
        correct_guesses.append(answer)
        cords=getcords(answer,data_dict) #returns tuple
        # state_data= data[data['state']==answer]
        # tim.setpos(state_data.x.item(),state_data.y.item()) easiest way, no need of the getcords function
        tim.setpos(cords)
        tim.write(answer, align=ALIGN, font=FONT)
    screen.update()

