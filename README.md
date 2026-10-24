# Middle East Map Quiz

An interactive map quiz built in Python with `turtle` for drawing and `pandas` for working with CSV data. The player types country names, and every correct answer is marked on the map. When the player types `Exit`, the countries they missed are saved to a CSV file so they can study them later.

---

## Tech Stack

* **Language:** Python 3.x
* **Data Handling:** Pandas (reading CSV, filtering rows, saving a new CSV)
* **Graphics:** Turtle Graphics (map background, red markers, country labels)

---

## Project Architecture

* **main.py** — Game loop: reads the answer, checks it, draws the marker, and saves missed countries on exit
* **coordinates.csv** — 21 countries with their (x, y) position on the map
* **countries_to_learn.csv** — Created when the player types `Exit`; lists the countries that were not guessed
* **map.gif** — Background map image
* **README.md** — Project documentation

---

## How It Works

* **Input:** The player types a country name; the text is cleaned with `.strip().title()` so `egypt` and `Egypt` both work.
* **Checking:** If the country is in `coordinates.csv` and wasn't guessed before, it is added to the guessed list.
* **Drawing:** The country's x and y are looked up with Pandas filtering, then a red circle and the name are drawn on the map.
* **Score:** The window title shows the progress, e.g. `5/21 Countries Correct`.
* **Saving:** Typing `Exit` (or pressing Cancel) builds the missing list with a list comprehension and saves it with `DataFrame.to_csv()`.

---

## Key Features

* **CSV → Map:** Turns a table of coordinates into markers on a map.
* **No Duplicate Points:** Guessing the same country twice doesn't add to the score.
* **Study List:** Missed countries are exported to `countries_to_learn.csv`.

---

## Installation & Execution

1. **Clone the repository:**
   `git clone https://github.com/nepal-aly/middle-east-map-game.git`

2. **Navigate to the directory:**
   `cd middle-east-map-game`

3. **Install required dependencies:**
   `pip install pandas`

4. **Launch the application:**
   `python main.py`
