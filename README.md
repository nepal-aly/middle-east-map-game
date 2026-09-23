# Geospatial Map Quiz & Automated ETL Data Pipeline 🗺️

A high-performance geospatial data application developed in Python utilizing `pandas` for data manipulation and `turtle` for vector-based spatial rendering. The application ingests geographic datasets, validates user query inputs via normalized lookups, dynamically renders vector pins, and executes an automated ETL routine upon session exit to persist missed entries into a structured CSV data store.

---

## 🛠️ Tech Stack & Technical Architecture

* **Language:** Python 3.x
* **Data Processing & ETL:** Pandas (CSV ingestion, dataset normalization, relational filtering, vector indexing, automated data persistence)
* **Geospatial Engine & GUI:** Turtle Graphics (Custom coordinate systems, vector graphics rendering, dynamic canvas drawing)
* **Core Engineering Principles:** ETL Pipelines, Data Integrity, Case-Insensitive String Normalization, State Persistence, Memory-Efficient Data Processing

---

## 🏗️ Project Architecture

* **main.py** — Core engine handling spatial queries, event loop management, and coordinate lookups
* **coordinates.csv** — Primary relational dataset mapping geographic entities to 2D spatial coordinates (x, y)
* **countries_to_learn.csv** — Dynamically generated output pipeline isolating unguessed spatial entities upon process termination
* **map.gif** — High-resolution base GIS visual map asset
* **README.md** — Project documentation

---

## 🎮 System Workflow & Operations

* **Input Processing:** Ingests user input via an interactive dialog and normalizes text strings via `.title()` formatting to match primary dataset keys.
* **Spatial Rendering:** Performs rapid lookup in `coordinates.csv` and dynamically plots vector markers with text labels at calculated screen coordinates.
* **Automated Data Persistence:** Triggers an automated extraction script upon inputting `Exit`, computing set differences via list comprehensions, and exporting unvisited locations into `countries_to_learn.csv`.

---

## 🌟 Engineering Highlights

* **Automated ETL Pipeline:** Seamlessly handles the lifecycle of spatial data — from reading raw CSV files to exporting refined target data upon user exit.
* **Real-Time Vector Mapping:** Converts tabular coordinate data into live vector rendering without latency.
* **Robust Error & Case Normalization:** Eliminates user input discrepancies by standardizing incoming strings before querying the underlying DataFrame.
* **State Management & Live Metrics:** Continuously computes score metrics and dynamically updates UI state in real-time.

---

## 🚀 Installation & Execution

1. **Clone the repository:**
   `git clone https://github.com/nepal-aly/middle-east-map-quiz.git`

2. **Navigate to the directory:**
   `cd middle-east-map-quiz`

3. **Install required dependencies:**
   `pip install pandas`

4. **Launch the application:**
   `python main.py`
