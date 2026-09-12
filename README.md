# IPL Match Analytics (2008–2024)

Exploratory analysis and a Streamlit dashboard for historical IPL match outcomes, toss decisions, team performance and venues.

## Run

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Run from the repository root. The dashboard uses `data/raw/matches.csv`. The original analysis is `notebooks/IPL-data-analysis.ipynb`; check its input path before running cells.

## Repository

- `app.py`: interactive dashboard
- `src/utils.py`: data loading and filtering
- `data/raw/matches.csv`: included match dataset
- `notebooks/`: original EDA
- `assets/`: saved visualizations

## Analytical questions

Compare team win rates alongside match counts; inspect toss decisions and outcomes; explore how venue and season relate to chasing success.

## Limitations

Historical associations do not establish that choosing to chase causes a win. Account for abandoned matches, team renaming, season changes and small venue samples. Dataset source and redistribution terms should be documented before republishing. No validated predictive model or live deployment is claimed.
