# IPL Matches(2008-2024) Data Analysis

## Project Overview

This project is an **Exploratory Data Analysis (EDA)** of Indian Premier League (IPL) matches from 2008 to 2024. The goal is to uncover trends in match outcomes, toss decisions, and venue advantages using historical data.

This analysis is valuable for cricket enthusiasts and sports analysts to understand the statistical factors that influence winning.

---

## Dataset

The dataset used is `matches.csv`, containing details of every IPL match played, including:
- Season & Date
- Venue & City
- Teams & Toss Decisions
- Match Results (Runs/Wickets)
- Player of the Match

---

## Key Questions Addressed

This analysis aims to answer the following questions:

1.  IPL matches played across each season.
2.  Which player's won the most player of the match award?
3.  In which cities most matches were played?
4.  Does teams that have won more matches also have higher win percentage?
5.  Which teams have won the most IPL matches?
6.  Does teams choose to field first than to bat?
7.  Does toss-decision impacts match result?
8.  Which venue's are favourable for chasing?

---

## Analysis Workflow

The analysis was conducted in a Jupyter Notebook (`IPL-data-analysis.ipynb`) and followed these steps:

1.  **Data Loading:** Imported the dataset using Pandas.
2.  **Data Cleaning:**
    * Checked for and handled missing values (found in the `method` column).
    * Checked for and removed any duplicate rows.
3.  **Exploratory Data Analysis (EDA):**
    * Generated descriptive statistics for numerical columns (`result_margin`, `target_runs`).
    * Examined the value counts for categorical columns (`season`, `city`, `match_type`, `player_of_the_match`, `venue`, `toss_decision`, `winner`, `result`).
4.  **Data Visualization:**
    * Used **Seaborn** and **Matplotlib** to create plots to answer the key questions.
    * **Countplot:** To show the number of matches played, toss-decision across each season.
    * **Bar Charts:** To compare top venues favourable for chasing.
    * **Pie Charts:** To show win percentage, toss-decision, impact of toss-decision on match result.

---

## Key Findings

- **Win Percentage Analysis:** Calculated the most successful teams in IPL history based on win rates, not just total wins.
- **Toss Impact:** Analyzed whether winning the toss statistically improves the chances of winning the match.
- **Batting vs. Chasing:** Determined the optimal strategy (Batting First vs. Chasing) for different scenarios.
- **Venue Analysis:** Identified which stadiums favor chasing teams vs. defending teams.

---

## Tools and Libraries Used

* **Python 3:** The core programming language.
* **Pandas:** For data manipulation and analysis.
* **NumPy:** For numerical operations.
* **Matplotlib:** For basic data visualization.
* **Seaborn:** For advanced statistical visualization.
* **Jupyter Notebook:** As the interactive development environment.

---

## How to Use This Repository

1.  Clone the repository to your local machine:
    ```bash
    git clone [https://github.com/razesoni/IPL-Exploratory-Data-Analysis.git](https://github.com/razesoni/IPL-Exploratory-Data-Analysis.git)
    ```
2.  Install the required libraries:
    ```bash
    pip install pandas numpy matplotlib seaborn
    ```
3.  Open the Jupyter Notebook to view the analysis:
    ```bash
    jupyter notebook IPL-data-analysis.ipynb
    ```
