import turtle,pandas
screen = turtle.Screen()
screen.bgpic("map.gif")
screen.setup(width=900, height =450)
screen.title(" middle east map")

data = pandas.read_csv("coordinates.csv")
countries = data.country.to_list()
guessed = []
score = 0
while len(guessed) < 21:
    answer = screen.textinput(title=f"Correct! Your score is {score} from 21", prompt="type a country name and hit Enter!").title()
    if answer in countries:
        guessed.append(answer)
        score += 1
   

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        country_x = data[data.country == answer]["x"].item()
        country_y = data[data.country == answer]["y"].item()
        t.goto(country_x,country_y)
        t.fillcolor("red")
        t.begin_fill()
        t.circle(15)
        t.end_fill()
        t.write(answer,font=("arial",12))
    if answer == "Exit":
        missing = [country for country in countries if country not in guessed]
        new_data = pandas.DataFrame(missing).to_csv("countries_to_learn.csv")
        break
