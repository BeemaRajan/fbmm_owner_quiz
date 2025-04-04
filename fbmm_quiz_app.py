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

    def render_question(question_title, answer_image_map, key_prefix, owner_map):
        st.subheader(question_title)
        selected_answer = None
        for label, img_file in answer_image_map.items():
            if st.radio("", [label], key=f"{key_prefix}_{label}"):
                selected_answer = label
            if img_file:  # Only show image if it's not None or empty
                st.image(GITHUB_IMAGE_BASE_URL + img_file, width=200)
        if selected_answer:
            selected.append(owner_map[selected_answer])


    # Question 1
    render_question(
        "Question 1: It's a Saturday night. What are you up to?",
        {
            "Watching movies": "",
            "Date night!": "",
            "Going out to dinner": "",
            "Probably working ...": "",
            "Dinner with friends at a good restaurant or a live show, but you'd rather be having a quiet night at home": "",
            "Online retail therapy": "",
            "Sitting on the couch watching TV": ""
        },
        "q1",
        {
            "Watching movies": ["Duane"],
            "Date night!": ["Dan"],
            "Going out to dinner": ["David"],
            "Probably working ...": ["Erica"],
            "Dinner with friends at a good restaurant or a live show, but you'd rather be having a quiet night at home": ["Jamie"],
            "Online retail therapy": ["Jen"],
            "Sitting on the couch watching TV": ["Julie"]
        }
    )

    # Question 2
    render_question(
        "Question 2: Who was your childhood crush?",
        {
            "Jaclyn Smith": "Jaclyn_Smith.png",
            "Brian from the Backstreet Boys": "Brian_from_the_Backstreet_Boys.png",
            "Lindsey Lohan": "Lindsay_Lohan.png",
            "The Dallas Cowboys Cheerleaders": "Dallas_Cowboys_Cheerleaders.jpg",
            "Brad Pitt": "Brad_Pitt.png",
            "Olivia Newton-John": "Olivia_Newton_John.png",
            "Rick Springfield": "Rick_Springfield.png",
            "The Bionic Woman": "The_Bionic_Woman.png"
        },
        "q2",
        {
            "Jaclyn Smith": ["Carmen"],
            "Brian from the Backstreet Boys": ["Erica"],
            "Lindsey Lohan": ["Dan"],
            "The Dallas Cowboys Cheerleaders": ["Duane"],
            "Brad Pitt": ["Jen"],
            "Olivia Newton-John": ["David"],
            "Rick Springfield": ["Julie"],
            "The Bionic Woman": ["Jamie"]
        }
    )

    # Question 3
    render_question(
        "Question 3: What is your drink of choice?",
        {
            "Cabernet / a good red wine": "cabernet.png",
            "An old fashioned": "old_fashioned.jpg",
            "Coffee": "coffee.png",
            "Pina colada": "pina_colada.jpg",
            "Hendrick's and tonic with a cucumber slice": "hendricks.png",
            "Sangria": "sangria.jpg",
            "Gin and tonic": "gin_and_tonic.jpg",
            "Water or bourbon. Sometimes together": "bourbon.jpg"
        },
        "q3",
        {
            "Cabernet / a good red wine": ["Carmen"],
            "An old fashioned": ["Dan"],
            "Coffee": ["Duane"],
            "Pina colada": ["Erica"],
            "Hendrick's and tonic with a cucumber slice": ["Jamie"],
            "Sangria": ["Jen"],
            "Gin and tonic": ["Julie"],
            "Water or bourbon. Sometimes together": ["David"]
        }
    )

    # Question 4
    render_question(
        "Question 4: Describe yourself in three words.",
        {
            "Intense. Caring. Honest. In that order.": "",
            "Decisive. Energetic. Loyal.": "",
            "Stoic. Quiet. Thoughtful.": "",
            "Committed. Supportive. Trustworthy.": "",
            "Loyal. Driven. Social.": "",
            "Universal. Flexible. Careful.": "",
            "Detailed. Coy. Thoughtful.": "",
            "Detailed. Funny. Driven.": ""
        },
        "q4",
        {
            "Intense. Caring. Honest. In that order.": ["Carmen"],
            "Decisive. Energetic. Loyal.": ["Dan"],
            "Stoic. Quiet. Thoughtful.": ["David"],
            "Committed. Supportive. Trustworthy.": ["Duane"],
            "Loyal. Driven. Social.": ["Erica"],
            "Universal. Flexible. Careful.": ["Jamie"],
            "Detailed. Coy. Thoughtful.": ["Jen"],
            "Detailed. Funny. Driven.": ["Julie"]
        }
    )

    # Question 5
    render_question(
        "Question 5: What's your favorite TV show?",
        {
            "Seinfeld": "seinfeld.jpg",
            "Gunsmoke": "gunsmoke.jpg",
            "The Lincoln Lawyer": "lincoln_lawyer.jpg",
            "Below Deck": "below_deck.jpg",
            "Ted Lasso": "ted_lasso.png",
            "Ozark": "ozark.jpg",
            "The Real Housewives of Anything": "The_real_housewives.jpg",
            "Your favorite political commentator": "favorite_political_commentator.png"
        },
        "q5",
        {
            "Seinfeld": ["Carmen"],
            "Gunsmoke": ["Dan"],
            "The Lincoln Lawyer": ["David"],
            "Below Deck": ["Erica"],
            "Ted Lasso": ["Jamie"],
            "Ozark": ["Jen"],
            "The Real Housewives of Anything": ["Julie"],
            "Your favorite political commentator": ["Duane"]
        }
    )

    # Question 6
    render_question(
        "Question 6: What's your favorite color?",
        {
            "Purple": "purple.png",
            "Red": "red.png",
            "Green": "green.png",
            "Blue": "blue.jpg"
        },
        "q6",
        {
            "Purple": ["Erica"],
            "Red": ["Carmen", "Jen"],
            "Green": ["Jamie"],
            "Blue": ["Dan", "David", "Duane", "Julie"]
        }
    )

    # Question 7
    render_question(
        "Question 7: What's your favorite vacation spot?",
        {
            "Bahamas": "bahamas.png",
            "La Jolla, CA": "la_jolla_ca.jpg",
            "Majorca, Spain": "majorca_spain.jpg",
            "30A": "30a.jpg",
            "Any all-inclusive beach resort": "beach_resort.png",
            "Scotland": "scotland.jpg",
            "Aruba": "aruba.jpg",
            "Hawaii": "hawaii.jpg"
        },
        "q7",
        {
            "Bahamas": ["Julie"],
            "La Jolla, CA": ["David"],
            "Majorca, Spain": ["Jamie"],
            "30A": ["Duane"],
            "Any all-inclusive beach resort": ["Erica"],
            "Scotland": ["Dan"],
            "Aruba": ["Carmen"],
            "Hawaii": ["Jen"]
        }
    )

    # Question 8
    render_question(
        "Question 8: What's your favorite emoji?",
        {
            "🤗 (hug / spirit hands)": "hug.png",
            "😏 (smirk)": "smirk.png",
            "👍 (thumbs up)": "thumbs_up.png",
            "🥴 (wiggle mouth)": "wiggle_mouth.png",
            "❤ (heart)": "red_heart.png",
            "🤣 (rolling on the floor laughing)": "laughing.png",
        },
        "q8",
        {
            "🤗 (hug / spirit hands)": ["Erica"],
            "😏 (smirk)": ["Jamie"],
            "👍 (thumbs up)": ["Duane", "Jen"],
            "🥴 (wiggle mouth)": ["Julie"],
            "❤ (heart)": ["Carmen"],
            "🤣 (rolling on the floor laughing)": ["Dan", "David"]
        }
    )

    if st.button("Submit"):
        result = get_best_match(selected)
        st.markdown(f"## You are most like **{result}**!")
        st.image(OWNER_IMAGE_URLS[result], caption=result)
        st.write("Thanks for taking the quiz!")

if __name__ == '__main__':
    main()


