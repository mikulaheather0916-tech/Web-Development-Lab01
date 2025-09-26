import streamlit as st
import time


# Page Config and Title
st.set_page_config(page_title="Which Hogwarts House Are You?")
st.title("Which Hogwarts House Are You?")
st.image("WebDevLab01/Images/hogwarts_crest.jpg")

st.write(
    """
    A BuzzFeed‑style quiz for Phase 2. Answer five questions, and we'll sort you into **Gryffindor**, **Ravenclaw**,
    **Hufflepuff**, or **Slytherin**  with a short blurb and study tip for your house.
    """
)


# House data
HOUSES = {
    "Gryffindor": {
        "desc": "Brave, daring, and chivalrous. You leap before you look (but it works out).",
    },
    "Ravenclaw": {
        "desc": "Wit beyond measure. You value knowledge, cleverness, and originality.",
    },
    "Hufflepuff": {
        "desc": "Loyal, patient, and kind. You believe steady effort wins the day.",
    },
    "Slytherin": {
        "desc": "Ambitious and resourceful. You love strategy and getting results.",
    },
}


# Helper
def add_points(scores: dict, house: str, pts: int = 1):
    scores[house] = scores.get(house, 0) + pts


# Questions — 5 minimum, 3+ types
q1 = st.radio(  
    "1) Pick a magical companion:",
    ["Snowy owl", "Ginger cat", "Toad", "Serpent"],
    index=None,
)
st.image("images/snowowl.jpeg")

q2 = st.multiselect(  
    "2) Choose the traits you admire most (pick any):",
    ["Bravery", "Intelligence", "Loyalty", "Ambition"],
)

q3 = st.slider(  
    "3) Ideal group size for adventures:",
    min_value=1,
    max_value=10,
    value=3,
)

q4 = st.number_input(  
    "4) How many hours per week would you spend mastering a new spell?",
    min_value=0,
    max_value=50,
    value=5,
    step=1,
)

q5 = st.selectbox(  
    "5) Your favorite Hogwarts class:",
    [
        "Defense Against the Dark Arts",
        "Transfiguration",
        "Herbology",
        "Potions",
        "Charms",
        "History of Magic",
    ],
)

st.image("WebDevLab01/Images/sortinghat.png")
# Evaluate
if st.button("Sort me!"):
    if q1 is None or not q2:
        st.warning("Please answer at least Question 1 and pick one or more traits in Question 2.")
        st.stop()

    scores = {}

    # Q1 mapping
    if q1 == "Snowy owl":
        add_points(scores, "Ravenclaw", 2)
    elif q1 == "Ginger cat":
        add_points(scores, "Gryffindor", 2)
    elif q1 == "Toad":
        add_points(scores, "Hufflepuff", 2)
    elif q1 == "Serpent":
        add_points(scores, "Slytherin", 2)

    # Q2 mapping (multi)
    for trait in q2:
        if trait == "Bravery":
            add_points(scores, "Gryffindor")
        if trait == "Intelligence":
            add_points(scores, "Ravenclaw")
        if trait == "Loyalty":
            add_points(scores, "Hufflepuff")
        if trait == "Ambition":
            add_points(scores, "Slytherin")

    # Q3 mapping
    if q3 <= 2:
        add_points(scores, "Ravenclaw")
    elif 3 <= q3 <= 5:
        add_points(scores, "Gryffindor")
        add_points(scores, "Hufflepuff")
    else:
        add_points(scores, "Slytherin")

    # Q4 mapping
    if q4 < 5:
        add_points(scores, "Hufflepuff")
    elif 5 <= q4 <= 15:
        add_points(scores, "Ravenclaw")
    elif 16 <= q4 <= 30:
        add_points(scores, "Gryffindor")
    else:
        add_points(scores, "Slytherin")

    # Q5 mapping
    if q5 == "Defense Against the Dark Arts":
        add_points(scores, "Gryffindor", 2)
    elif q5 == "Transfiguration":
        add_points(scores, "Ravenclaw", 2)
    elif q5 == "Herbology":
        add_points(scores, "Hufflepuff", 2)
    elif q5 == "Potions":
        add_points(scores, "Slytherin", 2)
    elif q5 == "Charms":
        add_points(scores, "Ravenclaw")
    elif q5 == "History of Magic":
        add_points(scores, "Hufflepuff")

    # Progress animation while we "sort" you
    prog = st.progress(0)  
    for i in range(100):
        time.sleep(0.01)
        prog.progress(i + 1)

    # Final result
    result = max(scores, key=scores.get)
    st.metric("Your House", result, delta=f"score {scores[result]}")  

    with st.container(border=True):
        st.header(f"Welcome to {result}!")
        st.write(HOUSES[result]["desc"])
        

    if scores[result] >= 4:
        st.balloons() 

    st.subheader("A quick tip for your house")
    tips = {
        "Gryffindor": "Channel energy into bold goals, like Harry!!!",
        "Ravenclaw": "Summarize your learning after each session! Stay studious!.",
        "Hufflepuff": "Stay steady!!! Your reliability is your superpower :)",
        "Slytherin": "You are very strategic, use that to ur advantage!",
    }
    st.write(tips[result])
