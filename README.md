# IPL Exploratory Data Analysis (2008-2024)

A comprehensive exploratory data analysis of Indian Premier League (IPL) cricket matches spanning from 2008 to 2024, utilizing Python-based data analysis and visualization techniques.

## 📋 Project Overview

This project provides an in-depth analysis of IPL match data, uncovering trends, patterns, and insights about team performance, player achievements, venue characteristics, and match dynamics over 17 seasons of the tournament.

**Dataset:** 1,095 matches across 20 columns of match-level data  
**Time Period:** 2008-2024  
**Technologies:** Python, Pandas, NumPy, Matplotlib, Seaborn

## 📊 Dataset Structure

The analysis is built on a comprehensive matches dataset containing the following features:

### Match Information
- **id** - Unique identifier for each match
- **season** - IPL season/year
- **date** - Match date
- **city** - Host city
- **venue** - Stadium name
- **match_type** - Stage of tournament (League, Qualifier, Final, etc.)

### Team & Player Data
- **team1 & team2** - Participating teams
- **toss_winner** - Team winning the coin toss
- **toss_decision** - Toss decision (bat/field)
- **winner** - Match winner
- **player_of_match** - Player awarded Man of the Match

### Match Outcome
- **result** - Victory method (runs/wickets)
- **result_margin** - Margin of victory (numerical)
- **target_runs** - Target score for chasing team
- **target_overs** - Overs allocated for chase
- **super_over** - Indicates if match went to Super Over tie-breaker

### Officials
- **umpire1 & umpire2** - On-field umpire names

## 🔍 Key Findings

### 1. Match Distribution Across Seasons
- **Peak Season:** IPL 2013 recorded the maximum number of matches
- The tournament has maintained consistent match schedules, with most seasons hosting 56-62 league matches plus knockout stages

### 2. Top Performing Players (Player of the Match Awards)

| Rank | Player | Awards |
|------|--------|--------|
| 1 | AB de Villiers | 25 |
| 2 | CH Gayle | 22 |
| 3 | RG Sharma | 19 |
| 4 | V Kohli | 18 |
| 5 | DA Warner | 18 |
| 6 | MS Dhoni | 17 |
| 7 | YK Pathan | 16 |
| 8 | RA Jadeja | 16 |
| 9 | SR Watson | 16 |
| 10 | AD Russell | 15 |

**Key Insight:** AB de Villiers is the most decorated player with 25 Player of the Match awards, establishing himself as the most consistent match-winner throughout his IPL career.

### 3. Popular Match Venues

The top 10 cities hosting IPL matches:

| Rank | City | Matches |
|------|------|---------|
| 1 | Mumbai | 173 |
| 2 | Kolkata | 93 |
| 3 | Delhi | 90 |
| 4 | Chennai | 85 |
| 5 | Hyderabad | 77 |
| 6 | Bangalore | 65 |
| 7 | Chandigarh | 61 |
| 8 | Jaipur | 57 |
| 9 | Pune | 51 |
| 10 | Abu Dhabi | 37 |

**Key Insight:** Mumbai has hosted the maximum number of matches (173), establishing it as the primary IPL hub. The concentration in major metro cities reflects audience demographics and infrastructure availability.

### 4. Match Dynamics & Statistics

- **Average Target Score:** 165.68 runs
- **Median Target Score:** 166 runs
- **Average Match Margin:** 17.26 (runs/wickets)
- **Median Match Margin:** 8 (indicating competitive matches)
- **Result Distribution:** Matches are decided primarily by runs or wickets

### 5. Toss Impact Analysis
- Toss winners have the strategic advantage of choosing to bat or field first
- Win/loss correlation with toss decisions provides insights into team decision-making strategies

### 6. Match Outcomes
- **Super Overs:** Rare occurrences used to determine winners in tied matches
- **Result Types:** Predominantly decided by runs (batting team couldn't chase) or wickets (fielding team successful)
- **Result Margins:** Range from 1 to 146 runs/wickets, showing variable competition levels

## 🛠️ Data Cleaning & Preprocessing

### Data Quality Observations
- **Total Records:** 1,095 matches
- **Total Features:** 20 columns

### Missing Values Handling
- **city column:** 51 null values (4.7%)
- **player_of_match column:** 5 null values
- **winner column:** 5 null values
- **result_margin column:** 19 null values
- **target_runs/target_overs:** 3 null values each
- **method column:** 1,074 null values (98% missing) - **Removed**

### Data Standardization
- Unified team names to current franchises (e.g., Delhi Daredevils → Delhi Capitals, Kings XI Punjab → Punjab Kings)
- Ensured consistency in venue and city nomenclature
- No duplicate records found in the dataset

## 📁 Project Structure

```
IPL-Exploratory-Data-Analysis/
├── notebooks/
│   └── IPL-data-analysis.ipynb     # Main analysis notebook
├── data/
│   └── matches.csv                  # Match data (1,095 records)
├── src/                             # Source code modules
├── assets/                          # Visualization outputs
├── app.py                           # Streamlit web application
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip or conda package manager

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/razesoni/IPL-Exploratory-Data-Analysis.git
cd IPL-Exploratory-Data-Analysis
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

### Usage

#### Run the Jupyter Notebook
```bash
jupyter notebook notebooks/IPL-data-analysis.ipynb
```

#### Run the Streamlit Web App
```bash
streamlit run app.py
```

The Streamlit app provides an interactive dashboard for exploring IPL statistics, team performance, player achievements, and venue analysis.

## 📦 Dependencies

Core libraries used in this analysis:
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computations
- **matplotlib** - Static visualizations
- **seaborn** - Statistical data visualization
- **streamlit** - Interactive web application framework

See `requirements.txt` for complete dependency list.

## 💡 Analysis Highlights

### Player Performance Insights
- International stars (de Villiers, Gayle) consistently outperformed with high Player of the Match awards
- Indian batsmen (Kohli, Sharma) demonstrated sustained excellence
- All-rounders (Jadeja, Watson) provided match-winning performances

### Venue Dynamics
- Metro cities (Mumbai, Kolkata, Delhi, Chennai) dominate match hosting
- Smaller venues (Abu Dhabi, Ranchi) host fewer matches but are strategically important
- Home advantage plays a significant role in team performance

### Match Patterns
- Competitive balance: Median margin of 8 indicates well-matched contests
- Target scores average 165-166 runs, reflecting modern T20 dynamics
- Success in chase depends on consistency and risk-taking strategies

## 🔬 Methodology

1. **Data Collection:** Sourced IPL match records from 2008-2024
2. **Data Cleaning:** Handled missing values and standardized team nomenclature
3. **Exploratory Analysis:** Statistical summaries and distribution analysis
4. **Visualization:** Created informative charts and graphs for pattern identification
5. **Insights Generation:** Derived actionable conclusions from data patterns

## 📈 Potential Extensions

Future analysis could include:
- Ball-by-ball data for detailed performance metrics
- Player statistics integration (runs, wickets, economy rate)
- Predictive modeling for match outcomes
- Team-specific performance trends over time
- Venue-specific pitch behavior analysis
- Seasonal trends and tournament evolution

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Report issues or bugs
- Suggest improvements or new analyses
- Submit pull requests with enhancements
- Share insights or findings from the data

## 📄 License

This project is open source and available for educational and research purposes.

## ✉️ Contact

**Author:** [Razesoni](https://github.com/razesoni)

For questions, suggestions, or collaboration opportunities, feel free to reach out through GitHub issues or direct contact.

---

**Last Updated:** September 2024  
**Data Span:** 2008-2024 (17 IPL Seasons)  
**Total Matches Analyzed:** 1,095
