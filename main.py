import turtle, pandas

screen = turtle.Screen()
screen.bgpic("map.gif")
screen.setup(width=900, height=450)
screen.title("middle east map")

data = pandas.read_csv("coordinates.csv")
countries = data.country.to_list()
guessed = []

while len(guessed) < len(countries):
    answer = screen.textinput(title=f"{len(guessed)}/{len(countries)} Countries Correct", prompt="type a country name and hit Enter! (type Exit to stop)")
    if answer is None:
        answer = "Exit"
    answer = answer.strip().title()

    if answer == "Exit":
        missing = [country for country in countries if country not in guessed]
        pandas.DataFrame(missing, columns=["country"]).to_csv("countries_to_learn.csv", index=False)
        break

    if answer in countries and answer not in guessed:
        guessed.append(answer)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        country_x = data[data.country == answer]["x"].item()
        country_y = data[data.country == answer]["y"].item()
        t.goto(country_x, country_y)
        t.fillcolor("red")
        t.begin_fill()
        t.circle(15)
        t.end_fill()
        t.write(answer, font=("arial", 12))

if len(guessed) == len(countries):
    screen.title("You guessed all the countries!")

screen.exitonclick()
