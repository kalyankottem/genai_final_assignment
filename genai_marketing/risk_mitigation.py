# risk_mitigation.py

import ollama

# ---------------------------------
# RISK MITIGATION AGENT
# ---------------------------------

def analyze_risk(content):

    prompt = f"""
    You are a Risk Mitigation AI Agent
    for a luxury fashion brand.

    Analyze this localized campaign:

    {content}

    Check for:

    1. Cultural Hallucination
    - misuse or exaggeration of cultural identity

    2. Regional Cringe
    - awkward or forced localization
    - outdated slang
    - unnatural tone

    3. Algorithmic Bias
    - stereotyping
    - exclusion
    - lack of diversity

    4. Brand Dilution
    - campaign feels cheap instead of luxury

    For each category:
    - classify as LOW, MEDIUM, or HIGH
    - explain why

    Then suggest mitigation improvements.

    Finally give:
    SAFE or RISKY
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

    return response["message"]["content"]