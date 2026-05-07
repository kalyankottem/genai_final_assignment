# cultural_scraper.py

import ollama

# ---------------------------------
# SAMPLE CULTURAL DATASET
# ---------------------------------

trend_database = {

    "Mumbai": {
        "trend_data": """
        Bollywood-inspired streetwear,
        nightlife aesthetics,
        luxury sneakers,
        oversized silhouettes,
        premium urban fashion.
        """,

        "fashion_styles": [
            "Streetwear",
            "Nightlife Luxury",
            "Bold Urban"
        ],

        "tone_styles": [
            "Confident",
            "Energetic",
            "Premium Gen-Z"
        ]
    },

    "Delhi": {
        "trend_data": """
        monochrome luxury fashion,
        influencer-driven styling,
        luxury handbags,
        elite aesthetics,
        premium ethnic fusion.
        """,

        "fashion_styles": [
            "Elite Luxury",
            "Monochrome",
            "Ethnic Fusion"
        ],

        "tone_styles": [
            "Sophisticated",
            "Luxury Premium",
            "Influencer Style"
        ]
    },

    "Bengaluru": {
        "trend_data": """
        minimal fashion,
        techwear aesthetics,
        startup culture styling,
        sneaker culture,
        smart casual luxury.
        """,

        "fashion_styles": [
            "Minimal",
            "Techwear",
            "Smart Casual"
        ],

        "tone_styles": [
            "Modern",
            "Clean",
            "Conversational"
        ]
    },

    "Hyderabad": {
        "trend_data": """
        Indo-western luxury,
        heritage-inspired fashion,
        premium festive styling,
        cinematic aesthetics,
        elegant streetwear.
        """,

        "fashion_styles": [
            "Elegant Streetwear",
            "Heritage Luxury",
            "Festive Premium"
        ],

        "tone_styles": [
            "Elegant",
            "Cinematic",
            "Modern Traditional"
        ]
    },

    "Kolkata": {
        "trend_data": """
        artistic fashion,
        vintage aesthetics,
        handcrafted styling,
        indie luxury culture,
        intellectual fashion identity.
        """,

        "fashion_styles": [
            "Vintage Luxury",
            "Artistic Indie",
            "Handcrafted Fashion"
        ],

        "tone_styles": [
            "Intellectual",
            "Creative",
            "Minimal Elegant"
        ]
    }
}

# ---------------------------------
# CULTURAL SCRAPER FUNCTION
# ---------------------------------

def generate_cultural_insights(city):

    city_data = trend_database[city]

    trend_data = city_data["trend_data"]

    prompt = f"""
    You are a Cultural Scraper AI Agent
    for a luxury fashion brand.

    Analyze these cultural trend signals for {city}:

    {trend_data}

    Generate insights about:
    - Gen-Z behavior
    - fashion aesthetics
    - luxury expectations
    - streetwear preferences
    - slang/tone patterns
    - visual styles

    Keep response concise and structured.
    """

    response = ollama.chat(
        model='llama3',
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return {
        "insights": response["message"]["content"],
        "fashion_styles": city_data["fashion_styles"],
        "tone_styles": city_data["tone_styles"]
    }