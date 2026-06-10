import pandas as pd
import plotly.express as px


# =====================================================
# HELPERS
# =====================================================

def add_gap_columns(
    df,
    competitor
):

    df = df.copy()

    df["Coverage Gap"] = (
        df[competitor]
        - df["Us"]
    )

    df["Growth Gap"] = (
        df[f"{competitor} Growth"]
        - df["Us Growth"]
    )

    return df


# =====================================================
# OPPORTUNITIES
# =====================================================

def get_opportunities(
    df,
    competitor,
    top_n=10
):

    temp = add_gap_columns(
        df,
        competitor
    )

    temp["Priority Score"] = (
        temp["Coverage Gap"] * 0.6
        +
        temp["Growth Gap"] * 0.4
    )

    return (
        temp
        .sort_values(
            "Priority Score",
            ascending=False
        )
        .head(top_n)
    )

def sector_coverage_chart(
    topics_df,
    competitor,
    sort_by="Coverage"
):

    sector_df = (
        topics_df
        .groupby("Sector")
        .agg({
            "Us": "sum",
            competitor: "sum",
            "Us Growth": "mean",
            f"{competitor} Growth": "mean"
        })
        .reset_index()
    )

    sector_df["Coverage Gap"] = (
        sector_df[competitor]
        - sector_df["Us"]
    )

    sector_df["Growth Gap"] = (
        sector_df[f"{competitor} Growth"]
        - sector_df["Us Growth"]
    )

    # ============================
    # SORTING
    # ============================

    if sort_by == "Coverage":

        sector_df = sector_df.sort_values(
            competitor,
            ascending=False
        )

    elif sort_by == "Growth":

        sector_df = sector_df.sort_values(
            f"{competitor} Growth",
            ascending=False
        )

    elif sort_by == "Coverage Gap":

        sector_df = sector_df.sort_values(
            "Coverage Gap",
            ascending=False
        )

    elif sort_by == "Alphabetical":

        sector_df = sector_df.sort_values(
            "Sector"
        )

    rows = []

    for _, row in sector_df.iterrows():

        rows.append({

            "Sector": row["Sector"],
            "Source": "Us",

            "Coverage": row["Us"],
            "Growth": row["Us Growth"],

            "Coverage Gap": 0,
            "Growth Gap": 0

        })

        rows.append({

            "Sector": row["Sector"],
            "Source": competitor,

            "Coverage": row[competitor],
            "Growth": row[f"{competitor} Growth"],

            "Coverage Gap": row["Coverage Gap"],
            "Growth Gap": row["Growth Gap"]

        })

    chart_df = pd.DataFrame(rows)

    fig = px.bar(
        chart_df,
        x="Sector",
        y="Coverage",
        color="Source",
        barmode="group",
        text="Coverage"
    )

    fig.update_traces(
        texttemplate="%{y:.0f}",
        textposition="outside"
    )

    fig.update_traces(
        customdata=chart_df[
            [
                "Growth",
                "Coverage Gap",
                "Growth Gap"
            ]
        ],
        hovertemplate=
        "<b>%{x}</b><br>"
        + "Source: %{fullData.name}<br>"
        + "Coverage: %{y:,.0f}<br>"
        + "Weekly Growth: %{customdata[0]:.1f}%<br>"
        + "Coverage Gap: %{customdata[1]:,.0f}<br>"
        + "Growth Gap: %{customdata[2]:.1f}%"
        + "<extra></extra>"
    )

    fig.update_layout(
        height=500,
        title=f"Coverage by Sector — Us vs {competitor}",
        xaxis_title="",
        yaxis_title="Coverage Volume"
    )

    return fig

def sector_coverage_chart(
    topics_df,
    competitor,
    sort_by="Coverage"
):

    sector_df = (
        topics_df
        .groupby("Sector")
        .agg({
            "Us": "sum",
            competitor: "sum",
            "Us Growth": "mean",
            f"{competitor} Growth": "mean"
        })
        .reset_index()
    )

    sector_df["Coverage Gap"] = (
        sector_df[competitor]
        - sector_df["Us"]
    )

    sector_df["Growth Gap"] = (
        sector_df[f"{competitor} Growth"]
        - sector_df["Us Growth"]
    )

    # ============================
    # SORTING
    # ============================

    if sort_by == "Coverage":

        sector_df = sector_df.sort_values(
            competitor,
            ascending=False
        )

    elif sort_by == "Growth":

        sector_df = sector_df.sort_values(
            f"{competitor} Growth",
            ascending=False
        )

    elif sort_by == "Coverage Gap":

        sector_df = sector_df.sort_values(
            "Coverage Gap",
            ascending=False
        )

    elif sort_by == "Alphabetical":

        sector_df = sector_df.sort_values(
            "Sector"
        )

    rows = []

    for _, row in sector_df.iterrows():

        rows.append({

            "Sector": row["Sector"],
            "Source": "Us",

            "Coverage": row["Us"],
            "Growth": row["Us Growth"],

            "Coverage Gap": 0,
            "Growth Gap": 0

        })

        rows.append({

            "Sector": row["Sector"],
            "Source": competitor,

            "Coverage": row[competitor],
            "Growth": row[f"{competitor} Growth"],

            "Coverage Gap": row["Coverage Gap"],
            "Growth Gap": row["Growth Gap"]

        })

    chart_df = pd.DataFrame(rows)

    fig = px.bar(
        chart_df,
        x="Sector",
        y="Coverage",
        color="Source",
        barmode="group",
        text="Coverage"
    )

    fig.update_traces(
        texttemplate="%{y:.0f}",
        textposition="outside"
    )

    fig.update_traces(
        customdata=chart_df[
            [
                "Growth",
                "Coverage Gap",
                "Growth Gap"
            ]
        ],
        hovertemplate=
        "<b>%{x}</b><br>"
        + "Source: %{fullData.name}<br>"
        + "Coverage: %{y:,.0f}<br>"
        + "Weekly Growth: %{customdata[0]:.1f}%<br>"
        + "Coverage Gap: %{customdata[1]:,.0f}<br>"
        + "Growth Gap: %{customdata[2]:.1f}%"
        + "<extra></extra>"
    )

    fig.update_layout(
        height=500,
        title=f"Coverage by Sector — Us vs {competitor}",
        xaxis_title="",
        yaxis_title="Coverage Volume"
    )

    return fig

def topic_coverage_chart(
    topics_df,
    competitor,
    sort_by="Coverage Gap"
):

    df = add_gap_columns(
        topics_df,
        competitor
    )

    if sort_by == "Coverage":

        df = df.sort_values(
            competitor,
            ascending=False
        )

    elif sort_by == "Growth":

        df = df.sort_values(
            f"{competitor} Growth",
            ascending=False
        )

    elif sort_by == "Growth Gap":

        df = df.sort_values(
            "Growth Gap",
            ascending=False
        )

    elif sort_by == "Coverage Gap":

        df = df.sort_values(
            "Coverage Gap",
            ascending=False
        )

    elif sort_by == "Alphabetical":

        df = df.sort_values(
            "Topic"
        )

    rows = []

    for _, row in df.iterrows():

        rows.append({

            "Topic": row["Topic"],
            "Sector": row["Sector"],

            "Source": "Us",

            "Coverage": row["Us"],
            "Growth": row["Us Growth"],

            "Coverage Gap": 0,
            "Growth Gap": 0

        })

        rows.append({

            "Topic": row["Topic"],
            "Sector": row["Sector"],

            "Source": competitor,

            "Coverage": row[competitor],
            "Growth": row[f"{competitor} Growth"],

            "Coverage Gap": row["Coverage Gap"],
            "Growth Gap": row["Growth Gap"]

        })

    chart_df = pd.DataFrame(rows)

    fig = px.bar(
        chart_df,
        x="Topic",
        y="Coverage",
        color="Source",
        barmode="group",
        text="Coverage"
    )

    fig.update_traces(
        texttemplate="%{y:.0f}",
        textposition="outside"
    )

    fig.update_traces(
        customdata=chart_df[
            [
                "Sector",
                "Growth",
                "Coverage Gap",
                "Growth Gap"
            ]
        ],
        hovertemplate=
        "<b>%{x}</b><br>"
        + "Sector: %{customdata[0]}<br>"
        + "Source: %{fullData.name}<br>"
        + "Coverage: %{y:,.0f}<br>"
        + "Weekly Growth: %{customdata[1]:.1f}%<br>"
        + "Coverage Gap: %{customdata[2]:,.0f}<br>"
        + "Growth Gap: %{customdata[3]:.1f}%"
        + "<extra></extra>"
    )

    fig.update_layout(
        height=650,
        title=f"Coverage by Topic — Us vs {competitor}",
        xaxis_title="",
        yaxis_title="Coverage Volume"
    )

    return fig

def growth_gap_chart(
    topics_df,
    competitor,
    sort_by="Growth Gap"
):

    df = add_gap_columns(
        topics_df,
        competitor
    )

    if sort_by == "Coverage Gap":

        df = df.sort_values(
            "Coverage Gap",
            ascending=False
        )

    elif sort_by == "Coverage":

        df = df.sort_values(
            competitor,
            ascending=False
        )

    else:

        df = df.sort_values(
            "Growth Gap",
            ascending=False
        )

    fig = px.bar(
        df,
        x="Topic",
        y="Growth Gap",
        color="Sector",
        text="Growth Gap"
    )

    fig.update_traces(
        texttemplate="%{y:.1f}",
        textposition="outside"
    )

    fig.update_layout(
        title=f"Growth Gap vs {competitor}",
        height=500,
        xaxis_title="",
        yaxis_title="Growth Gap (%)"
    )

    return fig

def entity_chart(
    entity_df,
    entity_types,
    sort_by="Competitor Advantage"
):

    df = entity_df.copy()

    df = df[
        df["Type"].isin(
            entity_types
        )
    ]

    if sort_by == "Alphabetical":

        df = df.sort_values(
            "Entity"
        )

    else:

        df = df.sort_values(
            "Competitor Advantage",
            ascending=False
        )

    fig = px.bar(
        df,
        x="Entity",
        y="Competitor Advantage",
        color="Type",
        text="Competitor Advantage"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        title="Entity Intelligence",
        height=500,
        xaxis_title="",
        yaxis_title="Competitor Advantage Score"
    )

    return fig

def narrative_chart(
    narrative_df,
    selected_sectors=None,
    sort_by="Momentum"
):

    df = narrative_df.copy()

    if selected_sectors:

        df = df[
            df["Sector"].isin(
                selected_sectors
            )
        ]

    if sort_by == "Alphabetical":

        df = df.sort_values(
            "Narrative"
        )

    else:

        df = df.sort_values(
            "Momentum",
            ascending=False
        )

    fig = px.bar(
        df,
        x="Narrative",
        y="Momentum",
        color="Sector",
        text="Momentum"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        title="Narrative Momentum",
        height=500,
        xaxis_title="",
        yaxis_title="Momentum Score"
    )

    return fig

