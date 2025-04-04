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
    """
    Combine all owners from each question into a big tally, 
    then pick the most frequent owner. 
    If there's a tie, choose randomly among those top owners.
    """
    tally = {}
    for owners_for_question in selected_owners_lists:
        for owner in owners_for_question:
            tally[owner] = tally.get(owner, 0) + 1

    max_count = max(tally.values())
    top_owners = [owner for owner, count in tally.items() if count == max_count]
    return random.choice(top_owners)

# ----------------------------------------------------------------------------
# 3. HELPER FUNCTION TO RENDER EACH QUESTION
# ----------------------------------------------------------------------------
def render_question(question_title, answers, key_prefix, image_base_url=GITHUB_IMAGE_BASE_URL):
    """
    Renders a question with a single radio group (BuzzFeed-style).
    :param question_title: str - the text for the question
    :param answers: list of dicts, each with:
        {
           'label': 'Answer text',
           'image': 'some_filename.jpg' (can be "" if no image),
           'owners': ['Dan', 'David']  # or a single item
        }
    :param key_prefix: unique key for st.radio
    :param image_base_url: prefix for image URLs
    :return: list of owners for the user’s selected answer
    """
    st.subheader(question_title)
    
    # The radio button labels (one per possible answer)
    labels = [a["label"] for a in answers]
    selected_label = st.radio("Select an answer:", labels, key=key_prefix)

    # Display image for whichever answer is selected
    for a in answers:
        if a["label"] == selected_label:
            if a["image"]:
                st.image(image_base_url + a["image"], width=200)
            return a["owners"]

    return []

# ----------------------------------------------------------------------------
# 4. STREAMLIT MAIN UI
# ----------------------------------------------------------------------------
def main():
    st.set_page_config(page_title="FBMM Owner Quiz", layout="centered")

    st.title("Which FBMM Owner Are You?")
    st.write("You know which team you're on. But which owner are you most like? Find out!")
    st.image(f"{GITHUB_IMAGE_BASE_URL}header_pic.png", use_container_width=True)

    # We'll collect all answers in this list.
    all_selected_owners = []

    # --------------------------
    # Question 1
    # --------------------------
    q1_answers = [
        {"label": "Watching movies", 
         "image": "", 
         "owners": ["Duane"]},
        {"label": "Date night!", 
         "image": "", 
         "owners": ["Dan"]},
        {"label": "Going out to dinner", 
         "image": "", 
         "owners": ["David"]},
        {"label": "Probably working ...", 
         "image": "", 
         "owners": ["Erica"]},
        {"label": "Dinner with friends at a good restaurant or a live show, but you'd rather be having a quiet night at home",
         "image": "", 
         "owners": ["Jamie"]},
        {"label": "Online retail therapy", 
         "image": "", 
         "owners": ["Jen"]},
        {"label": "Sitting on the couch watching TV", 
         "image": "", 
         "owners": ["Julie"]},
    ]
    owners_q1 = render_question(
        "Question 1: It's a Saturday night. What are you up to?",
        q1_answers,
        key_prefix="q1"
    )
    all_selected_owners.append(owners_q1)

    # --------------------------
    # Question 2
    # --------------------------
    q2_answers = [
        {"label": "Jaclyn Smith", 
         "image": "Jaclyn_Smith.png", 
         "owners": ["Carmen"]},
        {"label": "Brian from the Backstreet Boys", 
         "image": "Brian_from_the_Backstreet_Boys.png", 
         "owners": ["Erica"]},
        {"label": "Lindsey Lohan", 
         "image": "Lindsay_Lohan.jpg", 
         "owners": ["Dan"]},
        {"label": "The Dallas Cowboys Cheerleaders", 
         "image": "Dallas_Cowboys_Cheerleaders.jpg", 
         "owners": ["Duane"]},
        {"label": "Brad Pitt", 
         "image": "Brad_Pitt.png", 
         "owners": ["Jen"]},
        {"label": "Olivia Newton-John", 
         "image": "Olivia_Newton_John.png", 
         "owners": ["David"]},
        {"label": "Rick Springfield", 
         "image": "Rick_Springfield.jpg", 
         "owners": ["Julie"]},
        {"label": "The Bionic Woman", 
         "image": "The_Bionic_Woman.jpg", 
         "owners": ["Jamie"]},
    ]
    owners_q2 = render_question(
        "Question 2: Who was your childhood crush?",
        q2_answers,
        key_prefix="q2"
    )
    all_selected_owners.append(owners_q2)

    # --------------------------
    # Question 3
    # --------------------------
    q3_answers = [
        {"label": "Cabernet / a good red wine", 
         "image": "cabernet.jpg", 
         "owners": ["Carmen"]},
        {"label": "An old fashioned", 
         "image": "old_fashioned.jpg", 
         "owners": ["Dan"]},
        {"label": "Coffee", 
         "image": "coffee.jpg", 
         "owners": ["Duane"]},
        {"label": "Pina colada", 
         "image": "pina_colada.jpg", 
         "owners": ["Erica"]},
        {"label": "Hendrick's and tonic with a cucumber slice", 
         "image": "hendricks.png", 
         "owners": ["Jamie"]},
        {"label": "Sangria", 
         "image": "sangria.jpg", 
         "owners": ["Jen"]},
        {"label": "Gin and tonic", 
         "image": "gin_and_tonic.jpg", 
         "owners": ["Julie"]},
        {"label": "Water or bourbon. Sometimes together", 
         "image": "bourbon.jpg", 
         "owners": ["David"]},
    ]
    owners_q3 = render_question(
        "Question 3: What is your drink of choice?",
        q3_answers,
        key_prefix="q3"
    )
    all_selected_owners.append(owners_q3)

    # --------------------------
    # Question 4
    # --------------------------
    # No images were provided for these answers, so we use an empty string for "image"
    q4_answers = [
        {"label": "Intense. Caring. Honest. In that order.", 
         "image": "", 
         "owners": ["Carmen"]},
        {"label": "Decisive. Energetic. Loyal.", 
         "image": "", 
         "owners": ["Dan"]},
        {"label": "Stoic. Quiet. Thoughtful.", 
         "image": "", 
         "owners": ["David"]},
        {"label": "Committed. Supportive. Trustworthy.", 
         "image": "", 
         "owners": ["Duane"]},
        {"label": "Loyal. Driven. Social.", 
         "image": "", 
         "owners": ["Erica"]},
        {"label": "Universal. Flexible. Careful.", 
         "image": "", 
         "owners": ["Jamie"]},
        {"label": "Detailed. Coy. Thoughtful.", 
         "image": "", 
         "owners": ["Jen"]},
        {"label": "Detailed. Funny. Driven.", 
         "image": "", 
         "owners": ["Julie"]},
    ]
    owners_q4 = render_question(
        "Question 4: Describe yourself in three words.",
        q4_answers,
        key_prefix="q4"
    )
    all_selected_owners.append(owners_q4)

    # --------------------------
    # Question 5
    # --------------------------
    q5_answers = [
        {"label": "Seinfeld", 
         "image": "seinfeld.png", 
         "owners": ["Carmen"]},
        {"label": "Gunsmoke", 
         "image": "gunsmoke.jpg", 
         "owners": ["Dan"]},
        {"label": "The Lincoln Lawyer", 
         "image": "lincoln_lawyer.jpg", 
         "owners": ["David"]},
        {"label": "Below Deck", 
         "image": "below_deck.jpg", 
         "owners": ["Erica"]},
        {"label": "Ted Lasso", 
         "image": "ted_lasso.png", 
         "owners": ["Jamie"]},
        {"label": "Ozark", 
         "image": "ozark.jpg", 
         "owners": ["Jen"]},
        {"label": "The Real Housewives of Anything", 
         "image": "the_real_housewives.jpg", 
         "owners": ["Julie"]},
        {"label": "Your favorite political commentator", 
         "image": "favorite_political_commentator.png", 
         "owners": ["Duane"]},
    ]
    owners_q5 = render_question(
        "Question 5: What's your favorite TV show?",
        q5_answers,
        key_prefix="q5"
    )
    all_selected_owners.append(owners_q5)

    # --------------------------
    # Question 6
    # --------------------------
    q6_answers = [
        {"label": "Purple", 
         "image": "purple.jpg", 
         "owners": ["Erica"]},
        {"label": "Red", 
         "image": "red.jpg", 
         "owners": ["Carmen", "Jen"]},
        {"label": "Green", 
         "image": "green.png", 
         "owners": ["Jamie"]},
        {"label": "Blue", 
         "image": "blue.jpg", 
         "owners": ["Dan", "David", "Duane", "Julie"]},
    ]
    owners_q6 = render_question(
        "Question 6: What's your favorite color?",
        q6_answers,
        key_prefix="q6"
    )
    all_selected_owners.append(owners_q6)

    # --------------------------
    # Question 7
    # --------------------------
    q7_answers = [
        {"label": "Bahamas", 
         "image": "bahamas.png", 
         "owners": ["Julie"]},
        {"label": "La Jolla, CA", 
         "image": "la_jolla_ca.jpg", 
         "owners": ["David"]},
        {"label": "Majorca, Spain", 
         "image": "majorca_spain.jpg", 
         "owners": ["Jamie"]},
        {"label": "30A", 
         "image": "30a.jpg", 
         "owners": ["Duane"]},
        {"label": "Any all-inclusive beach resort", 
         "image": "beach_resort.png", 
         "owners": ["Erica"]},
        {"label": "Scotland", 
         "image": "scotland.jpg", 
         "owners": ["Dan"]},
        {"label": "Aruba", 
         "image": "aruba.jpg", 
         "owners": ["Carmen"]},
        {"label": "Hawaii", 
         "image": "hawaii.jpg", 
         "owners": ["Jen"]},
    ]
    owners_q7 = render_question(
        "Question 7: What's your favorite vacation spot?",
        q7_answers,
        key_prefix="q7"
    )
    all_selected_owners.append(owners_q7)

    # --------------------------
    # Question 8
    # --------------------------
    # No images provided here, so each image is ""
    q8_answers = [
        {"label": "🤗 (hug / spirit hands)", 
         "image": "", 
         "owners": ["Erica"]},
        {"label": "😏 (smirk)", 
         "image": "", 
         "owners": ["Jamie"]},
        {"label": "👍 (thumbs up)", 
         "image": "", 
         "owners": ["Duane", "Jen"]},
        {"label": "🥴 (wiggle mouth)", 
         "image": "", 
         "owners": ["Julie"]},
        {"label": "❤ (heart)", 
         "image": "", 
         "owners": ["Carmen"]},
        {"label": "🤣 (rolling on the floor laughing)", 
         "image": "", 
         "owners": ["Dan", "David"]},
    ]
    owners_q8 = render_question(
        "Question 8: What's your favorite emoji?",
        q8_answers,
        key_prefix="q8"
    )
    all_selected_owners.append(owners_q8)

    # --------------------------
    # SUBMIT BUTTON & RESULTS
    # --------------------------
    # SUBMIT button & results
    if "result_owner" not in st.session_state:
        st.session_state.result_owner = None

    if st.button("Submit"):
        if st.session_state.result_owner is None:
            result_owner = get_best_match(all_selected_owners)
            st.session_state.result_owner = result_owner

    if st.session_state.result_owner:
        st.markdown(f"## You are most like **{st.session_state.result_owner}**!")
        st.image(OWNER_IMAGE_URLS[st.session_state.result_owner])
        st.write("Thanks for taking the quiz!")

        # Optional: let user retake quiz
        if st.button("Retake Quiz"):
            st.session_state.result_owner = None
            st.rerun()


if __name__ == '__main__':
    main()

