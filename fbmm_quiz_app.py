import streamlit as st
import random

# ----------------------------------------------------------------------------
# 1. IMAGE SETTINGS
# ----------------------------------------------------------------------------
GITHUB_IMAGE_BASE_URL = "https://raw.githubusercontent.com/BeemaRajan/fbmm_owner_quiz/main/images/"

OWNER_IMAGE_URLS = {
    "Carmen": GITHUB_IMAGE_BASE_URL + "Carmen.png",
    "Dan": GITHUB_IMAGE_BASE_URL + "Dan.png",
    "David": GITHUB_IMAGE_BASE_URL + "David.png",
    "Duane": GITHUB_IMAGE_BASE_URL + "Duane.png",
    "Erica": GITHUB_IMAGE_BASE_URL + "Erica.png",
    "Jamie": GITHUB_IMAGE_BASE_URL + "Jamie.png",
    "Jen": GITHUB_IMAGE_BASE_URL + "Jen.png",
    "Julie": GITHUB_IMAGE_BASE_URL + "Julie.png",
}

# ----------------------------------------------------------------------------
# 2. MATCHING LOGIC
# ----------------------------------------------------------------------------
def get_best_match(selected_owners_lists):
    tally = {}
    for owners in selected_owners_lists:
        for owner in owners:
            tally[owner] = tally.get(owner, 0) + 1
    max_count = max(tally.values())
    top_owners = [owner for owner, count in tally.items() if count == max_count]
    return random.choice(top_owners)

# ----------------------------------------------------------------------------
# 3. STREAMLIT UI
# ----------------------------------------------------------------------------
def main():
    st.set_page_config(page_title="FBMM Owner Quiz", layout="centered")

    st.title("Which FBMM Owner Are You?")
    st.write("You know which team you're on. But which owner are you most like? Find out!")
    st.image(f"{GITHUB_IMAGE_BASE_URL}header_pic.png", use_container_width=True)

    selected = []

    # Question 1
    st.subheader("Question 1")
    q1 = st.radio("It's a Saturday night. What are you up to?", [
        "Watching movies",
        "Date night!",
        "Going out to dinner",
        "Probably working ...",
        "Dinner with friends at a good restaurant or a live show, but you'd rather be having a quiet night at home",
        "Online retail therapy",
        "Sitting on the couch watching TV"
    ])
    st.image(GITHUB_IMAGE_BASE_URL + "watching_movies.jpg", width=200)
    q1_map = {
        "Watching movies": ["Duane"],
        "Date night!": ["Dan"],
        "Going out to dinner": ["David"],
        "Probably working ...": ["Erica"],
        "Dinner with friends at a good restaurant or a live show, but you'd rather be having a quiet night at home": ["Jamie"],
        "Online retail therapy": ["Jen"],
        "Sitting on the couch watching TV": ["Julie"]
    }
    selected.append(q1_map[q1])

    # Question 2
    st.subheader("Question 2")
    q2 = st.radio("Who was your childhood crush?", [
        "Jaclyn Smith",
        "Brian from the Backstreet Boys",
        "Lindsey Lohan",
        "The Dallas Cowboys Cheerleaders",
        "Brad Pitt",
        "Olivia Newton-John",
        "Rick Springfield",
        "The Bionic Woman"
    ])
    st.image(GITHUB_IMAGE_BASE_URL + "Brad_Pitt.png", width=200)
    q2_map = {
        "Jaclyn Smith": ["Carmen"],
        "Brian from the Backstreet Boys": ["Erica"],
        "Lindsey Lohan": ["Dan"],
        "The Dallas Cowboys Cheerleaders": ["Duane"],
        "Brad Pitt": ["Jen"],
        "Olivia Newton-John": ["David"],
        "Rick Springfield": ["Julie"],
        "The Bionic Woman": ["Jamie"]
    }
    selected.append(q2_map[q2])

    # Question 3
    st.subheader("Question 3")
    q3 = st.radio("What is your drink of choice?", [
        "Cabernet / a good red wine",
        "An old fashioned",
        "Coffee",
        "Pina colada",
        "Hendrick's and tonic with a cucumber slice",
        "Sangria",
        "Gin and tonic",
        "Water or bourbon. Sometimes together"
    ])
    st.image(GITHUB_IMAGE_BASE_URL + "cabernet.png", width=200)
    q3_map = {
        "Cabernet / a good red wine": ["Carmen"],
        "An old fashioned": ["Dan"],
        "Coffee": ["Duane"],
        "Pina colada": ["Erica"],
        "Hendrick's and tonic with a cucumber slice": ["Jamie"],
        "Sangria": ["Jen"],
        "Gin and tonic": ["Julie"],
        "Water or bourbon. Sometimes together": ["David"]
    }
    selected.append(q3_map[q3])

    # Question 4
    st.subheader("Question 4")
    q4 = st.radio("Describe yourself in three words.", [
        "Intense. Caring. Honest. In that order.",
        "Decisive. Energetic. Loyal.",
        "Stoic. Quiet. Thoughtful.",
        "Committed. Supportive. Trustworthy.",
        "Loyal. Driven. Social.",
        "Universal. Flexible. Careful.",
        "Detailed. Coy. Thoughtful.",
        "Detailed. Funny. Driven."
    ])
    selected.append({
        "Intense. Caring. Honest. In that order.": ["Carmen"],
        "Decisive. Energetic. Loyal.": ["Dan"],
        "Stoic. Quiet. Thoughtful.": ["David"],
        "Committed. Supportive. Trustworthy.": ["Duane"],
        "Loyal. Driven. Social.": ["Erica"],
        "Universal. Flexible. Careful.": ["Jamie"],
        "Detailed. Coy. Thoughtful.": ["Jen"],
        "Detailed. Funny. Driven.": ["Julie"]
    }[q4])

    # Question 5
    st.subheader("Question 5")
    q5 = st.radio("What's your favorite TV show?", [
        "Seinfeld",
        "Gunsmoke",
        "The Lincoln Lawyer",
        "Below Deck",
        "Ted Lasso",
        "Ozark",
        "The Real Housewives of Anything",
        "Your favorite political commentator"
    ])
    st.image(GITHUB_IMAGE_BASE_URL + "below_deck.jpg", width=200)
    selected.append({
        "Seinfeld": ["Carmen"],
        "Gunsmoke": ["Dan"],
        "The Lincoln Lawyer": ["David"],
        "Below Deck": ["Erica"],
        "Ted Lasso": ["Jamie"],
        "Ozark": ["Jen"],
        "The Real Housewives of Anything": ["Julie"],
        "Your favorite political commentator": ["Duane"]
    }[q5])

    # Question 6
    st.subheader("Question 6")
    q6 = st.radio("What's your favorite color?", [
        "Purple",
        "Red",
        "Green",
        "Blue"
    ])
    st.image(GITHUB_IMAGE_BASE_URL + "blue.jpg", width=200)
    selected.append({
        "Purple": ["Erica"],
        "Red": ["Carmen", "Jen"],
        "Green": ["Jamie"],
        "Blue": ["Dan", "David", "Duane", "Julie"]
    }[q6])

    # Question 7
    st.subheader("Question 7")
    q7 = st.radio("What's your favorite vacation spot?", [
        "Bahamas",
        "La Jolla, CA",
        "Majorca, Spain",
        "30A",
        "Any all-inclusive beach resort",
        "Scotland",
        "Aruba",
        "Hawaii"
    ])
    st.image(GITHUB_IMAGE_BASE_URL + "hawaii.jpg", width=200)
    selected.append({
        "Bahamas": ["Julie"],
        "La Jolla, CA": ["David"],
        "Majorca, Spain": ["Jamie"],
        "30A": ["Duane"],
        "Any all-inclusive beach resort": ["Erica"],
        "Scotland": ["Dan"],
        "Aruba": ["Carmen"],
        "Hawaii": ["Jen"]
    }[q7])

    # Question 8
    st.subheader("Question 8")
    q8 = st.radio("What's your favorite emoji?", [
        "🤗 (hug / spirit hands)",
        "😏 (smirk)",
        "👍 (thumbs up)",
        "🥴 (wiggle mouth)",
        "❤ (red heart)",
        "🤣 (rolling on the floor laughing)"
    ])
    selected.append({
        "🤗 (hug / spirit hands)": ["Erica"],
        "😏 (smirk)": ["Jamie"],
        "👍 (thumbs up)": ["Duane", "Jen"],
        "🥴 (wiggle mouth)": ["Julie"],
        "❤ (red heart)": ["Carmen"],
        "🤣 (rolling on the floor laughing)": ["Dan", "David"]
    }[q8])

    # Final submission
    if st.button("Submit"):
        result = get_best_match(selected)
        st.markdown(f"## You are most like **{result}**!")
        st.image(OWNER_IMAGE_URLS[result], caption=result)
        st.write("Thanks for taking the quiz!")

if __name__ == '__main__':
    main()

