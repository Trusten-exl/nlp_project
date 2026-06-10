import pandas as pd


# =====================================================
# TOPIC DATA
# =====================================================

def get_topic_data():

    data = [

        # =================================================
        # TECHNOLOGY
        # =================================================

        {
            "Sector": "Technology",
            "Topic": "Generative AI",

            "Us": 320,
            "NYT": 410,
            "WSJ": 360,
            "Bloomberg": 450,
            "Reuters": 340,

            "Us Growth": 12,
            "NYT Growth": 18,
            "WSJ Growth": 14,
            "Bloomberg Growth": 20,
            "Reuters Growth": 10
        },

        {
            "Sector": "Technology",
            "Topic": "AI Infrastructure",

            "Us": 180,
            "NYT": 280,
            "WSJ": 250,
            "Bloomberg": 340,
            "Reuters": 220,

            "Us Growth": 9,
            "NYT Growth": 21,
            "WSJ Growth": 18,
            "Bloomberg Growth": 24,
            "Reuters Growth": 15
        },

        {
            "Sector": "Technology",
            "Topic": "Semiconductors",

            "Us": 210,
            "NYT": 170,
            "WSJ": 240,
            "Bloomberg": 310,
            "Reuters": 260,

            "Us Growth": 6,
            "NYT Growth": 3,
            "WSJ Growth": 8,
            "Bloomberg Growth": 15,
            "Reuters Growth": 11
        },

        {
            "Sector": "Technology",
            "Topic": "Cybersecurity",

            "Us": 240,
            "NYT": 200,
            "WSJ": 220,
            "Bloomberg": 180,
            "Reuters": 210,

            "Us Growth": 8,
            "NYT Growth": 4,
            "WSJ Growth": 6,
            "Bloomberg Growth": 2,
            "Reuters Growth": 5
        },

        # =================================================
        # POLITICS
        # =================================================

        {
            "Sector": "Politics",
            "Topic": "Election Integrity",

            "Us": 260,
            "NYT": 390,
            "WSJ": 280,
            "Bloomberg": 210,
            "Reuters": 320,

            "Us Growth": 7,
            "NYT Growth": 16,
            "WSJ Growth": 10,
            "Bloomberg Growth": 4,
            "Reuters Growth": 13
        },

        {
            "Sector": "Politics",
            "Topic": "Congress",

            "Us": 300,
            "NYT": 350,
            "WSJ": 310,
            "Bloomberg": 260,
            "Reuters": 340,

            "Us Growth": 5,
            "NYT Growth": 8,
            "WSJ Growth": 6,
            "Bloomberg Growth": 4,
            "Reuters Growth": 9
        },

        {
            "Sector": "Politics",
            "Topic": "Foreign Policy",

            "Us": 170,
            "NYT": 260,
            "WSJ": 230,
            "Bloomberg": 180,
            "Reuters": 290,

            "Us Growth": 4,
            "NYT Growth": 12,
            "WSJ Growth": 10,
            "Bloomberg Growth": 5,
            "Reuters Growth": 14
        },

        # =================================================
        # BUSINESS
        # =================================================

        {
            "Sector": "Business",
            "Topic": "Private Equity",

            "Us": 120,
            "NYT": 140,
            "WSJ": 260,
            "Bloomberg": 320,
            "Reuters": 170,

            "Us Growth": 3,
            "NYT Growth": 5,
            "WSJ Growth": 13,
            "Bloomberg Growth": 18,
            "Reuters Growth": 8
        },

        {
            "Sector": "Business",
            "Topic": "M&A",

            "Us": 210,
            "NYT": 220,
            "WSJ": 300,
            "Bloomberg": 340,
            "Reuters": 260,

            "Us Growth": 6,
            "NYT Growth": 7,
            "WSJ Growth": 12,
            "Bloomberg Growth": 15,
            "Reuters Growth": 9
        },

        {
            "Sector": "Business",
            "Topic": "Inflation",

            "Us": 340,
            "NYT": 380,
            "WSJ": 310,
            "Bloomberg": 280,
            "Reuters": 360,

            "Us Growth": 4,
            "NYT Growth": 5,
            "WSJ Growth": 2,
            "Bloomberg Growth": 1,
            "Reuters Growth": 6
        },

        # =================================================
        # SPORTS
        # =================================================

        {
            "Sector": "Sports",
            "Topic": "NFL",

            "Us": 430,
            "NYT": 220,
            "WSJ": 170,
            "Bloomberg": 90,
            "Reuters": 180,

            "Us Growth": 14,
            "NYT Growth": 4,
            "WSJ Growth": 2,
            "Bloomberg Growth": 1,
            "Reuters Growth": 3
        },

        {
            "Sector": "Sports",
            "Topic": "NBA",

            "Us": 370,
            "NYT": 190,
            "WSJ": 130,
            "Bloomberg": 80,
            "Reuters": 150,

            "Us Growth": 11,
            "NYT Growth": 3,
            "WSJ Growth": 2,
            "Bloomberg Growth": 1,
            "Reuters Growth": 2
        },

        {
            "Sector": "Sports",
            "Topic": "Media Rights",

            "Us": 110,
            "NYT": 140,
            "WSJ": 190,
            "Bloomberg": 240,
            "Reuters": 130,

            "Us Growth": 4,
            "NYT Growth": 7,
            "WSJ Growth": 11,
            "Bloomberg Growth": 15,
            "Reuters Growth": 6
        }
    ]

    topics = pd.DataFrame(data)

    # =====================================================
    # COMPETITOR AGGREGATE
    # =====================================================

    competitor_cols = [
        "NYT",
        "WSJ",
        "Bloomberg",
        "Reuters"
    ]

    growth_cols = [
        "NYT Growth",
        "WSJ Growth",
        "Bloomberg Growth",
        "Reuters Growth"
    ]

    topics["Competitors"] = (
        topics[competitor_cols]
        .mean(axis=1)
        .round(1)
    )

    topics["Competitors Growth"] = (
        topics[growth_cols]
        .mean(axis=1)
        .round(1)
    )

    return topics


# =====================================================
# ENTITY DATA
# =====================================================

def get_entity_data():

    data = [

        ("Nvidia", "Company", 94),
        ("Microsoft", "Company", 87),
        ("Google", "Company", 82),
        ("Amazon", "Company", 79),
        ("TSMC", "Company", 73),

        ("Sam Altman", "Person", 92),
        ("Jensen Huang", "Person", 88),
        ("Elon Musk", "Person", 85),
        ("Jerome Powell", "Person", 76),
        ("Tim Cook", "Person", 72),

        ("OpenAI", "Organization", 95),
        ("Federal Reserve", "Organization", 81),
        ("Congress", "Organization", 74),
        ("NATO", "Organization", 69),

        ("Washington DC", "Location", 88),
        ("Silicon Valley", "Location", 83),
        ("Taiwan", "Location", 79),
        ("Brussels", "Location", 64)
    ]

    return pd.DataFrame(
        data,
        columns=[
            "Entity",
            "Type",
            "Competitor Advantage"
        ]
    )


# =====================================================
# NARRATIVE DATA
# =====================================================

def get_narrative_data():

    data = [

        (
            "AI Infrastructure Boom",
            "Technology",
            96
        ),

        (
            "Nuclear Power For AI",
            "Technology",
            88
        ),

        (
            "Election Integrity",
            "Politics",
            83
        ),

        (
            "Foreign Policy Shift",
            "Politics",
            76
        ),

        (
            "Private Equity Expansion",
            "Business",
            91
        ),

        (
            "M&A Acceleration",
            "Business",
            80
        ),

        (
            "NFL Media Rights Arms Race",
            "Sports",
            86
        ),

        (
            "Streaming Sports Fragmentation",
            "Sports",
            79
        )
    ]

    return pd.DataFrame(
        data,
        columns=[
            "Narrative",
            "Sector",
            "Momentum"
        ]
    )