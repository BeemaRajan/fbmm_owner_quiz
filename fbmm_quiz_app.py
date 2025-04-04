import streamlit as st
import random

# ------------------------------------------------------------------------------
# 1. QUIZ QUESTIONS
# ------------------------------------------------------------------------------

QUESTIONS = [
    {
        "question": "It's a Saturday night. What are you up to?",
        "options": {
            "Watching movies": ["Duane"],
            "Date night!": ["Dan"],
            "Going out to dinner": ["David"],
            "Probably working ...": ["Erica"],
            "Dinner with friends at a good restaurant or a live show, but you'd rather be having a quiet night at home": ["Jamie"],
            "Online retail therapy": ["Jen"],
            "Sitting on the couch watching TV": ["Julie"],
        }
    },
    {
        "question": "Who was your childhood crush?",
        "options": {
            "Jaclyn Smith": ["Carmen"],
            "Brian from the Backstreet Boys": ["Erica"],
            "Lindsey Lohan": ["Dan"],
            "The Dallas Cowboys Cheerleaders": ["Duane"],
            "Brad Pitt": ["Jen"],
            "Olivia Newton-John": ["David"],
            "Rick Springfield": ["Julie"],
            "The Bionic Woman": ["Jamie"]
        }
    },
    {
        "question": "What is your drink of choice?",
        "options": {
            "Cabernet / a good red wine": ["Carmen"],
            "An old fashioned": ["Dan"],
            "Coffee": ["Duane"],
            "Pina colada": ["Erica"],
            "Hendrick's and tonic with a cucumber slice": ["Jamie"],
            "Sangria": ["Jen"],
            "Gin and tonic": ["Julie"],
            "Water or bourbon. Sometimes together": ["David"],
        }
    },
    {
        "question": "Describe yourself in three words.",
        "options": {
            "Intense. Caring. Honest. In that order.": ["Carmen"],
            "Decisive. Energetic. Loyal.": ["Dan"],
            "Stoic. Quiet. Thoughtful.": ["David"],
            "Committed. Supportive. Trustworthy.": ["Duane"],
            "Loyal. Driven. Social.": ["Erica"],
            "Universal. Flexible. Careful.": ["Jamie"],
            "Detailed. Coy. Thoughtful.": ["Jen"],
            "Detailed. Funny. Driven.": ["Julie"],
        }
    },
    {
        "question": "What's your favorite TV show?",
        "options": {
            "Seinfeld": ["Carmen"],
            "Gunsmoke": ["Dan"],
            "The Lincoln Lawyer": ["David"],
            "Below Deck": ["Erica"],
            "Ted Lasso": ["Jamie"],
            "Ozark": ["Jen"],
            "The Real Housewives of Anything": ["Julie"],
            "Your favorite political commentator": ["Duane"]
        }
    },
    {
        "question": "What's your favorite color?",
        "options": {
            "Purple": ["Erica"],
            "Red": ["Carmen", "Jen"],
            "Green": ["Jamie"],
            "Blue": ["Dan", "David", "Duane", "Julie"]
        }
    },
    {
        "question": "What's your favorite vacation spot?",
        "options": {
            "Bahamas": ["Julie"],
            "La Jolla, CA": ["David"],
            "Majorca, Spain": ["Jamie"],
            "30A": ["Duane"],
            "Any all-inclusive beach resort": ["Erica"],
            "Scotland": ["Dan"],
            "Aruba": ["Carmen"],
            "Hawaii": ["Jen"],
        }
    },
    {
        "question": "What's your favorite emoji?",
        "options": {
            "🤗 (hug / spirit hands)": ["Erica"],
            "😏 (smirk)": ["Jamie"],
            "👍 (thumbs up)": ["Duane", "Jen"],
            "🥴 (wiggle mouth)": ["Julie"],
            "❤ (red heart)": ["Carmen"],
            "🤣 (rolling on the floor laughing)": ["Dan", "David"]
        }
    }
]

# ------------------------------------------------------------------------------
# 2. IMAGES
# ------------------------------------------------------------------------------

OWNER_IMAGE_URLS = {
    "Carmen": "https://github.com/BeemaRajan/fbmm_owner_quiz/blob/cd6e7950eeb21eeb407d800a2d02b623c7505792/images/Carmen.png",
    "Dan":    "https://github.com/BeemaRajan/fbmm_owner_quiz/blob/cd6e7950eeb21eeb407d800a2d02b623c7505792/images/Dan.png",
    "David":  "https://github.com/BeemaRajan/fbmm_owner_quiz/blob/cd6e7950eeb21eeb407d800a2d02b623c7505792/images/David.png",
    "Duane":  "https://github.com/BeemaRajan/fbmm_owner_quiz/blob/cd6e7950eeb21eeb407d800a2d02b623c7505792/images/Duane.png",
    "Erica":  "https://github.com/BeemaRajan/fbmm_owner_quiz/blob/cd6e7950eeb21eeb407d800a2d02b623c7505792/images/Erica.png",
    "Jamie":  "https://github.com/BeemaRajan/fbmm_owner_quiz/blob/cd6e7950eeb21eeb407d800a2d02b623c7505792/images/Jamie.png",
    "Jen":    "https://github.com/BeemaRajan/fbmm_owner_quiz/blob/cd6e7950eeb21eeb407d800a2d02b623c7505792/images/Jen.png",
    "Julie":  "https://github.com/BeemaRajan/fbmm_owner_quiz/blob/cd6e7950eeb21eeb407d800a2d02b623c7505792/images/Julie.png",
}

# ------------------------------------------------------------------------------
# 3. RESULT-FINDING LOGIC (supports multiple owners per answer)
# ------------------------------------------------------------------------------

def get_best_match(selected_owners_lists):
    """
    Given a list of owner lists (one list per selected answer),
    return the owner with the highest total score.
    If there’s a tie, pick one randomly.
    """
    tally = {}
    for owners in selected_owners_lists:
        for owner in owners:
            tally[owner] = tally.get(owner, 0) + 1

    max_count = max(tally.values())
    top_owners = [owner for owner, count in tally.items() if count == max_count]
    return random.choice(top_owners)

# ------------------------------------------------------------------------------
# 4. STREAMLIT UI
# ------------------------------------------------------------------------------

def main():
    st.title("Which FBMM Owner Are You?")
    st.write("Answer the questions below and click **Submit** to see your match.")

    selected_owner_lists = []

    for i, item in enumerate(QUESTIONS):
        st.subheader(f"Question {i+1}")
        st.write(item["question"])
        choice = st.radio("Select an answer:", list(item["options"].keys()), key=f"q_{i}")
        selected_owner_lists.append(item["options"][choice])
        st.write("---")

    if st.button("Submit"):
        result_owner = get_best_match(selected_owner_lists)
        st.markdown(f"## You are most like **{result_owner}**!")

        if result_owner in OWNER_IMAGE_URLS:
            st.image(OWNER_IMAGE_URLS[result_owner], caption=result_owner)
        else:
            st.write("No image available.")

        st.write("Thanks for taking the quiz!")

if __name__ == "__main__":
    main()