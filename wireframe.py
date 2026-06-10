import streamlit as st
import pandas as pd

from streamlit_extras.metric_cards import (
    style_metric_cards
)

from data import (
    get_topic_data,
    get_entity_data,
    get_narrative_data
)

from charts import (
    add_gap_columns,
    get_opportunities,
    sector_coverage_chart,
    topic_coverage_chart,
    growth_gap_chart,
    entity_chart,
    narrative_chart
)

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Editorial Intelligence Dashboard",
    layout="wide"
)

# =====================================================
# LOAD DATA
# =====================================================

topics_df = get_topic_data()
entity_df = get_entity_data()
narrative_df = get_narrative_data()

# =====================================================
# HEADER
# =====================================================

st.title("Editorial Intelligence Dashboard")

st.caption(
    "Monitor competitor coverage, narrative momentum, "
    "entity dominance, and editorial opportunities."
)

# =====================================================
# GLOBAL FILTERS
# =====================================================

st.markdown("### Global Filters")

g1, g2 = st.columns([1, 2])

with g1:

    selected_competitor = st.selectbox(
        "Compare Against",
        [
            "Competitors",
            "NYT",
            "WSJ",
            "Bloomberg",
            "Reuters"
        ]
    )

with g2:

    selected_sectors = st.multiselect(
        "Sectors",
        sorted(
            topics_df["Sector"].unique()
        ),
        default=sorted(
            topics_df["Sector"].unique()
        )
    )

# =====================================================
# FILTER DATA
# =====================================================

filtered_topics = topics_df[
    topics_df["Sector"].isin(
        selected_sectors
    )
].copy()

filtered_topics = add_gap_columns(
    filtered_topics,
    selected_competitor
)

# =====================================================
# KPI ROW
# =====================================================

topics_leading = (
    filtered_topics["Coverage Gap"] < 0
).sum()

topics_trailing = (
    filtered_topics["Coverage Gap"] > 0
).sum()

avg_gap = round(
    filtered_topics["Coverage Gap"].mean(),
    1
)

avg_growth_gap = round(
    filtered_topics["Growth Gap"].mean(),
    1
)

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "Topics Leading",
        topics_leading
    )

with k2:
    st.metric(
        "Topics Trailing",
        topics_trailing
    )

with k3:
    st.metric(
        "Avg Coverage Gap",
        avg_gap
    )

with k4:
    st.metric(
        "Avg Growth Gap",
        f"{avg_growth_gap}%"
    )

style_metric_cards()

st.divider()

# =====================================================
# COVERAGE LANDSCAPE
# =====================================================

st.header("Coverage Landscape")

# -----------------------------------------------------
# Sector Coverage
# -----------------------------------------------------

c1, c2 = st.columns([4, 1])

with c1:
    st.subheader(
        "Coverage by Sector"
    )

with c2:

    sector_sort = st.selectbox(
        "Sort",
        [
            "Coverage",
            "Growth",
            "Coverage Gap",
            "Alphabetical"
        ],
        key="sector_sort"
    )

sector_fig = sector_coverage_chart(
    filtered_topics,
    selected_competitor,
    sector_sort
)

st.plotly_chart(
    sector_fig,
    use_container_width=True
)

# -----------------------------------------------------
# Topic Coverage
# -----------------------------------------------------

c1, c2 = st.columns([3, 1])

with c1:
    st.subheader(
        "Coverage by Topic"
    )

with c2:

    topic_sort = st.selectbox(
        "Sort Topics",
        [
            "Coverage Gap",
            "Growth Gap",
            "Coverage",
            "Growth",
            "Alphabetical"
        ],
        key="topic_sort"
    )

topic_fig = topic_coverage_chart(
    filtered_topics,
    selected_competitor,
    topic_sort
)

st.plotly_chart(
    topic_fig,
    use_container_width=True
)

# =====================================================
# MOMENTUM
# =====================================================

st.header("Momentum")

m1, m2 = st.columns([3, 1])

with m1:
    st.subheader(
        "Topics Growing Faster Than Us"
    )

with m2:

    growth_sort = st.selectbox(
        "Sort Growth",
        [
            "Growth Gap",
            "Coverage Gap",
            "Coverage"
        ],
        key="growth_sort"
    )

growth_fig = growth_gap_chart(
    filtered_topics,
    selected_competitor,
    growth_sort
)

st.plotly_chart(
    growth_fig,
    use_container_width=True
)

# =====================================================
# ENTITY + NARRATIVE
# =====================================================

left, right = st.columns(2)

# -----------------------------------------------------
# ENTITY
# -----------------------------------------------------

with left:

    st.header(
        "Entity Intelligence"
    )

    e1, e2 = st.columns(2)

    with e1:

        entity_types = st.multiselect(
            "Entity Types",
            [
                "Company",
                "Person",
                "Organization",
                "Location"
            ],
            default=[
                "Company",
                "Person"
            ]
        )

    with e2:

        entity_sort = st.selectbox(
            "Sort",
            [
                "Competitor Advantage",
                "Alphabetical"
            ]
        )

    entity_fig = entity_chart(
        entity_df,
        entity_types,
        entity_sort
    )

    st.plotly_chart(
        entity_fig,
        use_container_width=True
    )

# -----------------------------------------------------
# NARRATIVES
# -----------------------------------------------------

with right:

    st.header(
        "Narrative Intelligence"
    )

    n1, n2 = st.columns(2)

    with n1:

        narrative_scope = st.radio(
            "Scope",
            [
                "Selected Sectors",
                "All Sectors"
            ],
            horizontal=False
        )

    with n2:

        narrative_sort = st.selectbox(
            "Sort",
            [
                "Momentum",
                "Alphabetical"
            ]
        )

    if narrative_scope == "Selected Sectors":

        narrative_sectors = selected_sectors

    else:

        narrative_sectors = None

    narrative_fig = narrative_chart(
        narrative_df,
        narrative_sectors,
        narrative_sort
    )

    st.plotly_chart(
        narrative_fig,
        use_container_width=True
    )

# =====================================================
# OPPORTUNITIES
# =====================================================

st.divider()

st.header(
    "Editorial Opportunities"
)

opps = get_opportunities(
    filtered_topics,
    selected_competitor,
    top_n=15
)

opps_display = opps[
    [
        "Topic",
        "Sector",
        "Coverage Gap",
        "Growth Gap",
        "Priority Score"
    ]
].copy()

opps_display = opps_display.sort_values(
    "Priority Score",
    ascending=False
)

st.dataframe(
    opps_display,
    use_container_width=True,
    hide_index=True
)

# =====================================================
# DATA EXPANDER
# =====================================================

with st.expander(
    "View Underlying Data"
):

    st.dataframe(
        filtered_topics,
        use_container_width=True,
        hide_index=True
    )