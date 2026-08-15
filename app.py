import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from src.utils import (
    load_and_preprocess_ipl_data,
    filter_ipl_dataset,
    get_team_win_statistics,
    get_top_pom_players,
    get_final_winners_summary
)

# --- Page Configuration ---
st.set_page_config(
    page_title="IPL Analytics Hub (2008–2024)",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- High-Contrast Dark & Cricket-Themed Styling ---
def apply_custom_styles():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(
                rgba(11, 15, 23, 0.92), 
                rgba(11, 15, 23, 0.97)
            ),
            url("https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?q=80&w=2000&auto=format&fit=crop");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: #F3F4F6 !important;
        }

        h1, h2, h3, h4, h5, h6, p, span, label {
            color: #F9FAFB !important;
        }

        [data-testid="stSidebar"] {
            background-color: rgba(17, 24, 39, 0.92) !important;
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border-right: 1px solid rgba(255, 255, 255, 0.12);
        }

        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] .stMarkdown {
            color: #E5E7EB !important;
            font-weight: 500 !important;
        }

        div[data-baseweb="select"] > div {
            background-color: rgba(31, 41, 55, 0.9) !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
            color: #FFFFFF !important;
            border-radius: 8px;
        }

        span[data-baseweb="tag"] {
            background-color: #FF6B00 !important;
            color: #FFFFFF !important;
            border-radius: 6px;
            font-weight: 500;
        }

        div[data-testid="stMetric"] {
            background: rgba(31, 41, 55, 0.65) !important;
            border: 1px solid rgba(255, 255, 255, 0.15) !important;
            padding: 18px 24px;
            border-radius: 12px;
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            box-shadow: 0 8px 24px 0 rgba(0, 0, 0, 0.4);
            transition: transform 0.2s ease, border-color 0.2s ease;
        }

        div[data-testid="stMetric"]:hover {
            transform: translateY(-3px);
            border-color: #FF6B00 !important;
        }

        div[data-testid="stMetricLabel"] p {
            font-size: 0.95rem !important;
            font-weight: 500 !important;
            color: #D1D5DB !important;
        }

        div[data-testid="stMetricValue"] {
            font-size: 1.9rem !important;
            font-weight: 700 !important;
            color: #FFFFFF !important;
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
            background-color: rgba(31, 41, 55, 0.6);
            padding: 8px 12px;
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .stTabs [data-baseweb="tab"] {
            border-radius: 6px;
            color: #D1D5DB !important;
            font-weight: 600;
            padding: 8px 18px;
        }

        .stTabs [aria-selected="true"] {
            background-color: #FF6B00 !important;
            color: #FFFFFF !important;
        }

        .js-plotly-plot {
            background: rgba(31, 41, 55, 0.5) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 12px;
            padding: 8px;
            backdrop-filter: blur(10px);
        }

        .badge {
            background: linear-gradient(135deg, #FF6B00 0%, #FFA726 100%);
            color: #FFFFFF !important;
            padding: 5px 14px;
            border-radius: 16px;
            font-size: 0.8rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            display: inline-block;
            margin-bottom: 8px;
        }

        [data-testid="stDataFrame"] {
            background: rgba(31, 41, 55, 0.6) !important;
            border: 1px solid rgba(255, 255, 255, 0.15) !important;
            border-radius: 8px;
            padding: 6px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

apply_custom_styles()

# --- Plotly Dark Theme Helper ---
def style_plotly_chart(fig):
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#F3F4F6", family="sans-serif", size=12),
        margin=dict(l=25, r=25, t=45, b=25),
        legend=dict(
            font=dict(color="#F3F4F6"),
            bgcolor="rgba(17, 24, 39, 0.6)",
            bordercolor="rgba(255, 255, 255, 0.15)",
            borderwidth=1
        )
    )
    fig.update_xaxes(
        tickfont=dict(color="#D1D5DB"),
        title_font=dict(color="#F9FAFB"),
        showgrid=True,
        gridcolor="rgba(255, 255, 255, 0.08)",
        zeroline=False
    )
    fig.update_yaxes(
        tickfont=dict(color="#D1D5DB"),
        title_font=dict(color="#F9FAFB"),
        showgrid=True,
        gridcolor="rgba(255, 255, 255, 0.08)",
        zeroline=False
    )
    return fig

# --- Data Loading with Caching ---
@st.cache_data
def get_data() -> pd.DataFrame:
    return load_and_preprocess_ipl_data("data/raw/matches.csv")

try:
    df = get_data()
except Exception as e:
    st.error(f"Error loading dataset: {e}. Ensure `matches.csv` is placed inside `data/raw/`.")
    st.stop()

# --- Sidebar Filters ---
st.sidebar.markdown("### 🔍 Filter IPL Matches")

all_seasons = sorted(df["season"].astype(str).unique())
selected_seasons = st.sidebar.multiselect(
    "Select Season(s):",
    options=all_seasons,
    default=all_seasons
)

all_match_types = sorted(df["match_type"].dropna().unique())
selected_match_types = st.sidebar.multiselect(
    "Select Match Type:",
    options=all_match_types,
    default=all_match_types
)

all_teams = sorted(set(df["team1"].dropna().unique()).union(set(df["team2"].dropna().unique())))
selected_teams = st.sidebar.multiselect(
    "Select Team(s):",
    options=all_teams,
    default=all_teams[:5]
)

all_cities = sorted(df["city"].dropna().unique())
selected_cities = st.sidebar.multiselect(
    "Select Host City:",
    options=all_cities,
    default=[]
)

# Apply filter
filtered_df = filter_ipl_dataset(
    df=df,
    seasons=selected_seasons,
    match_types=selected_match_types,
    teams=selected_teams if selected_teams else all_teams,
    cities=selected_cities
)

# --- Header & KPIs ---
st.markdown('<span class="badge">Indian Premier League Analytics</span>', unsafe_allow_html=True)
st.title("🏏 IPL Match Analysis & Team Performance Dashboard")
st.markdown("Comprehensive insights on IPL seasons, match outcomes, toss impacts, player awards, and venue statistics.")
st.write("")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

total_matches = len(filtered_df)
total_seasons = filtered_df["season"].nunique() if total_matches > 0 else 0
super_overs = (filtered_df["super_over"] == "Y").sum() if total_matches > 0 else 0
toss_win_match_win_pct = (
    f"{round((filtered_df['toss_match_winner']).mean() * 100, 1)}%"
    if total_matches > 0 else "0%"
)

kpi1.metric("Total Matches", f"{total_matches:,}")
kpi2.metric("Seasons Covered", f"{total_seasons}")
kpi3.metric("Super Over Matches", f"{super_overs}")
kpi4.metric("Toss Win ➔ Match Win", toss_win_match_win_pct)

st.divider()

# --- Main Dashboard Tabs ---
tab1, tab2, tab3, tab4 = st.tabs([
    "🏆 Team & Tournament Dominance",
    "🪙 Toss & Match Dynamics",
    "⭐ Player & Venue Analytics",
    "📋 Raw Data Explorer"
])

# ==========================================
# TAB 1: Team & Tournament Dominance
# ==========================================
with tab1:
    col_t1, col_t2 = st.columns(2)

    with col_t1:
        st.subheader("Total Match Wins by Franchise")
        if not filtered_df.empty:
            wins_df = filtered_df["winner"].value_counts().reset_index()
            wins_df.columns = ["Team", "Wins"]
            fig_wins = px.bar(
                wins_df,
                x="Wins",
                y="Team",
                orientation="h",
                color="Wins",
                color_continuous_scale="Inferno"
            )
            fig_wins.update_layout(yaxis=dict(autorange="reversed"))
            st.plotly_chart(style_plotly_chart(fig_wins), use_container_width=True)
        else:
            st.warning("No match data available for the active filters.")

    with col_t2:
        st.subheader("IPL Championship Title Distribution (Finals)")
        titles_df = get_final_winners_summary(df)
        if not titles_df.empty:
            fig_titles = px.pie(
                titles_df,
                values="Titles",
                names="Team",
                hole=0.45,
                color_discrete_sequence=px.colors.sequential.Plasma_r
            )
            fig_titles.update_traces(textposition="inside", textinfo="percent+label")
            st.plotly_chart(style_plotly_chart(fig_titles), use_container_width=True)

    st.subheader("Team Win Rate Efficiency (Matches Won vs Played)")
    win_stats = get_team_win_statistics(filtered_df)
    if not win_stats.empty:
        fig_win_rate = px.bar(
            win_stats,
            x="Team",
            y="Win %",
            color="Win %",
            hover_data=["Played", "Won"],
            color_continuous_scale="Viridis"
        )
        fig_win_rate.update_layout(xaxis_tickangle=-35)
        st.plotly_chart(style_plotly_chart(fig_win_rate), use_container_width=True)

# ==========================================
# TAB 2: Toss & Match Dynamics
# ==========================================
with tab2:
    col_ts1, col_ts2 = st.columns(2)

    with col_ts1:
        st.subheader("Toss Decision Breakdown")
        if not filtered_df.empty:
            toss_counts = filtered_df["toss_decision"].value_counts().reset_index()
            toss_counts.columns = ["Decision", "Count"]
            fig_toss = px.pie(
                toss_counts,
                values="Count",
                names="Decision",
                color="Decision",
                color_discrete_map={"field": "#00A86B", "bat": "#FF6B00"},
                hole=0.4
            )
            fig_toss.update_traces(textposition="inside", textinfo="percent+label")
            st.plotly_chart(style_plotly_chart(fig_toss), use_container_width=True)

    with col_ts2:
        st.subheader("Impact of Winning Toss on Match Victory")
        if not filtered_df.empty:
            toss_conv = filtered_df["toss_match_winner"].map(
                {True: "Toss Winner Won", False: "Toss Winner Lost"}
            ).value_counts().reset_index()
            toss_conv.columns = ["Result", "Count"]

            fig_conv = px.pie(
                toss_conv,
                values="Count",
                names="Result",
                color="Result",
                color_discrete_map={"Toss Winner Won": "#3B82F6", "Toss Winner Lost": "#EF4444"},
                hole=0.4
            )
            fig_conv.update_traces(textposition="inside", textinfo="percent+label")
            st.plotly_chart(style_plotly_chart(fig_conv), use_container_width=True)

    st.subheader("Victory Method: Runs vs Wickets Margin Distribution")
    if not filtered_df.empty:
        fig_margin = px.box(
            filtered_df[filtered_df["result"].isin(["runs", "wickets"])],
            x="result",
            y="result_margin",
            color="result",
            color_discrete_map={"runs": "#FFA726", "wickets": "#26C6DA"},
            points="outliers"
        )
        st.plotly_chart(style_plotly_chart(fig_margin), use_container_width=True)

# ==========================================
# TAB 3: Player & Venue Analytics
# ==========================================
with tab3:
    col_pv1, col_pv2 = st.columns(2)

    with col_pv1:
        st.subheader("Top 10 Player of the Match Awardees")
        pom_df = get_top_pom_players(filtered_df, top_n=10)
        if not pom_df.empty:
            fig_pom = px.bar(
                pom_df,
                x="Awards",
                y="Player",
                orientation="h",
                color="Awards",
                color_continuous_scale="YlOrRd"
            )
            fig_pom.update_layout(yaxis=dict(autorange="reversed"))
            st.plotly_chart(style_plotly_chart(fig_pom), use_container_width=True)

    with col_pv2:
        st.subheader("Top Host Cities by Match Volume")
        if not filtered_df.empty:
            city_df = filtered_df["city"].value_counts().head(10).reset_index()
            city_df.columns = ["City", "Matches"]
            fig_city = px.bar(
                city_df,
                x="City",
                y="Matches",
                color="Matches",
                color_continuous_scale="Teal"
            )
            fig_city.update_layout(xaxis_tickangle=-35)
            st.plotly_chart(style_plotly_chart(fig_city), use_container_width=True)

    st.subheader("Matches Played Per Season Trend")
    if not filtered_df.empty:
        season_df = filtered_df["season"].astype(str).value_counts().reset_index()
        season_df.columns = ["Season", "Matches"]
        season_df = season_df.sort_values(by="Season")

        fig_season = px.line(
            season_df,
            x="Season",
            y="Matches",
            markers=True,
            line_shape="linear"
        )
        fig_season.update_traces(line_color="#FF6B00", marker=dict(size=8, color="#FFA726"))
        st.plotly_chart(style_plotly_chart(fig_season), use_container_width=True)

# ==========================================
# TAB 4: Raw Data Explorer
# ==========================================
with tab4:
    st.subheader("Interactive IPL Match Records")

    available_cols = list(filtered_df.columns)
    default_cols = [
        col for col in [
            "season", "date", "match_type", "team1", "team2", 
            "toss_winner", "toss_decision", "winner", "result", "result_margin", "player_of_match", "venue", "city"
        ] if col in available_cols
    ]

    show_cols = st.multiselect(
        "Select visible columns:",
        options=available_cols,
        default=default_cols
    )

    st.dataframe(filtered_df[show_cols], use_container_width=True, height=450)

    csv_bytes = filtered_df[show_cols].to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Filtered IPL Data as CSV",
        data=csv_bytes,
        file_name="ipl_filtered_matches.csv",
        mime="text/csv"
    )