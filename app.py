import streamlit as st
import requests

st.title("SocialGrowth.ai 🚀")

followers = st.number_input("Followers")
niche = st.text_input("Niche")
engagement = st.number_input("Engagement (%)")
problem = st.text_area("Describe your problem")

if st.button("Analyze"):
    response = requests.post(
        "http://127.0.0.1:8000/analyze",
        json={
            "followers": followers,
            "niche": niche,
            "engagement": engagement,
            "problem": problem
        }
    )

    result = response.json()

    st.write("### Keywords:", result["keywords"])
    st.write("### Strategy:")
    for s in result["strategy"]:
        st.write("- ", s)