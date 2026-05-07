# app.py

import streamlit as st
import ollama

from cultural_scraper import generate_cultural_insights
from risk_mitigation import analyze_risk

# =================================
# PAGE CONFIG
# =================================

st.set_page_config(
    page_title="AI Multi-Agent Marketing System",
    layout="wide"
)

st.title("🧠 AI Multi-Agent Marketing System")

st.write("""
Cultural Scraper → Campaign Generator →
Linguistic Localizer → Risk Mitigation
""")

# =================================
# CULTURAL SCRAPER AGENT
# =================================

st.header("🌍 Cultural Scraper Agent")

city = st.selectbox(
    "Select City",
    [
        "Mumbai",
        "Delhi",
        "Bengaluru",
        "Hyderabad",
        "Kolkata"
    ]
)

if st.button("Generate Cultural Insights"):

    with st.spinner("Generating cultural insights..."):

        result = generate_cultural_insights(city)

        # SAVE OUTPUTS

        st.session_state["cultural_insights"] = (
            result["insights"]
        )

        st.session_state["fashion_styles"] = (
            result["fashion_styles"]
        )

        st.session_state["tone_styles"] = (
            result["tone_styles"]
        )

        st.session_state["selected_city"] = city

    st.success("Cultural insights generated.")

# =================================
# DISPLAY CULTURAL INSIGHTS
# =================================

if "cultural_insights" in st.session_state:

    st.subheader("🧠 Cultural Insights")

    st.write(
        st.session_state["cultural_insights"]
    )

# =================================
# DISPLAY CULTURAL ATTRIBUTES
# =================================

if "fashion_styles" in st.session_state:

    st.subheader(
        "🎯 Suggested Localization Attributes"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.write("### Fashion Styles")

        st.write(
            st.session_state["fashion_styles"]
        )

    with col2:

        st.write("### Tone Styles")

        st.write(
            st.session_state["tone_styles"]
        )

# =================================
# CAMPAIGN GENERATOR AGENT
# =================================

if "cultural_insights" in st.session_state:

    st.header("🎨 Campaign Generator Agent")

    campaign_mode = st.radio(
        "Choose Campaign Input Mode",
        [
            "AI Generated Campaign",
            "Manual Base Campaign"
        ]
    )

    # -----------------------------
    # AI GENERATED CAMPAIGN
    # -----------------------------

    if campaign_mode == "AI Generated Campaign":

        if st.button("Generate Base Campaign"):

            cultural_context = st.session_state[
                "cultural_insights"
            ]

            city = st.session_state[
                "selected_city"
            ]

            with st.spinner(
                "Generating campaign..."
            ):

                campaign_prompt = f"""
                You are a Campaign Generator AI Agent
                for a luxury fashion brand.

                CITY:
                {city}

                CULTURAL INSIGHTS:
                {cultural_context}

                Generate:
                1. Luxury Campaign Idea
                2. Base Tagline
                3. Campaign Description

                Requirements:
                - Match local Gen-Z culture
                - Reflect city aesthetics
                - Keep luxury positioning
                - Avoid cringe slang
                - Keep language modern and stylish
                """

                response = ollama.chat(
                    model='llama3',
                    messages=[
                        {
                            "role": "user",
                            "content": campaign_prompt
                        }
                    ]
                )

                generated_campaign = response[
                    "message"
                ]["content"]

                st.session_state[
                    "generated_campaign"
                ] = generated_campaign

            st.success(
                "Base campaign generated."
            )

    # -----------------------------
    # MANUAL BASE CAMPAIGN
    # -----------------------------

    elif campaign_mode == "Manual Base Campaign":

        manual_campaign = st.text_area(
            "Enter Base Campaign",
            placeholder="Example: Own Your Style",
            height=150
        )

        if st.button("Use Manual Campaign"):

            if manual_campaign.strip() == "":

                st.warning(
                    "Please enter a campaign."
                )

            else:

                st.session_state[
                    "generated_campaign"
                ] = manual_campaign

                st.success(
                    "Manual campaign saved."
                )

# =================================
# DISPLAY GENERATED CAMPAIGN
# =================================

if "generated_campaign" in st.session_state:

    st.subheader("✨ Base Campaign")

    st.write(
        st.session_state["generated_campaign"]
    )

# =================================
# LINGUISTIC LOCALIZER
# =================================

if "generated_campaign" in st.session_state:

    st.header("🗣️ Linguistic Localizer")

    fashion_style = st.selectbox(
        "Select Fashion Style",
        st.session_state["fashion_styles"]
    )

    tone_style = st.selectbox(
        "Select Tone Style",
        st.session_state["tone_styles"]
    )

    if st.button("Generate Localized Campaign"):

        cultural_context = st.session_state[
            "cultural_insights"
        ]

        city = st.session_state[
            "selected_city"
        ]

        base_campaign = st.session_state[
            "generated_campaign"
        ]

        with st.spinner(
            "Generating localized campaign..."
        ):

            localization_prompt = f"""
            You are a Linguistic Localizer AI Agent
            for a luxury fashion brand.

            CITY:
            {city}

            CULTURAL INSIGHTS:
            {cultural_context}

            BASE CAMPAIGN:
            {base_campaign}

            SELECTED FASHION STYLE:
            {fashion_style}

            SELECTED TONE STYLE:
            {tone_style}

            Instructions:
            - Adapt language for the city
            - Match local Gen-Z culture
            - Add subtle regional language flavor
            - Use premium bilingual phrasing
            - Avoid forced slang
            - Keep luxury positioning
            - Align with selected styles
            - Make the campaign emotionally engaging

            Generate:
            1. Localized Tagline
            2. Localized Campaign Copy
            3. Tone Explanation
            """

            response = ollama.chat(
                model='llama3',
                messages=[
                    {
                        "role": "user",
                        "content": localization_prompt
                    }
                ]
            )

            localized_output = response[
                "message"
            ]["content"]

            # SAVE OUTPUT

            st.session_state[
                "localized_output"
            ] = localized_output

        st.success(
            "Localized campaign generated."
        )

# =================================
# DISPLAY LOCALIZED CAMPAIGN
# =================================

if "localized_output" in st.session_state:

    st.subheader("✨ Localized Campaign")

    st.write(
        st.session_state["localized_output"]
    )

# =================================
# RISK MITIGATION AGENT
# =================================

if "localized_output" in st.session_state:

    st.header("🛡️ Risk Mitigation Agent")

    if st.button("Run Risk Mitigation"):

        with st.spinner(
            "Analyzing campaign risks..."
        ):

            risk_result = analyze_risk(
                st.session_state[
                    "localized_output"
                ]
            )

            st.session_state[
                "risk_result"
            ] = risk_result

# =================================
# DISPLAY RISK RESULTS
# =================================

if "risk_result" in st.session_state:

    st.subheader("🚨 Risk Analysis")

    st.write(
        st.session_state["risk_result"]
    )