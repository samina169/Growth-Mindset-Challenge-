import streamlit as st

# Title of the app
st.title("Growth Mindset Challenge")

# Introduction
st.write("Welcome to the Growth Mindset Challenge! Here, you can reflect on your mindset and take on challenges to foster a growth mindset.")

# Challenge prompt
st.header("Today's Challenge")
challenge = st.text_area("What challenge will you take on today?", "Write your challenge here...")
if st.button("Submit"):
    st.success(f"Great! You've decided to take on the challenge: {challenge}")

# Reflection section
st.header("Reflection")
reflection = st.text_area("How did you feel about this challenge?", "Write your reflections here...")
if st.button("Reflect"):
    st.success("Thank you for sharing your reflections!")

# Additional resources
st.header("Resources")
st.write("Here are some resources to help you develop a growth mindset:")
st.write("- [Mindset: The New Psychology of Success by Carol S. Dweck](https://www.amazon.com/Mindset-Psychology-Carol-S-Dweck/dp/0345472322)")
st.write("- [Growth Mindset Videos](https://www.youtube.com/results?search_query=growth+mindset)")
