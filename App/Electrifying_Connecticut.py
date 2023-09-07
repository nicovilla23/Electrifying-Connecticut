import streamlit as st
from streamlit_lottie import st_lottie
import json
st.set_page_config(
    page_title="Electrifying Connecticut",
    page_icon="⚡",
    layout="centered",
)


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
city = load_lottiefile("Lotties/city.json")

st.title("Welcome to Electrifying Connecticut")
st.header("Incentivizing Electric Car Adoption")
st.divider()

script= '''
At Electrifying Connecticut, we're passionate about clean and sustainable transportation. 
Our mission is to encourage the adoption of electric vehicles (EVs) in Connecticut, 
for a greener and healthier future.
\n
Are you considering buying an electric car? Wondering about the benefits, incentives, and infrastructure 
support available in Connecticut? You are in the right place!"
\n


Our app provides information, resources, and tools to help you make an informed decision about 
switching to an electric vehicle. Explore various EV models, learn about charging options, 
and discover incentives specific to Connecticut.
\n

Let's drive towards a sustainable future together! '''
st.info(script)

st_lottie(
city,
speed=1,
reverse=False,
loop=True,
)