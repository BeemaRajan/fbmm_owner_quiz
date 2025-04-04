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
    If there's a tie, choose randomly among the top owners.
    """
    tally = {}
    for owners_for_question in selected_owners_lists:
        for owner in owners_for_question:
            tally[owner] = tally.get(owner, 0) + 1

    max_count = max(tally.values())
    top_owners = [owner for owner, count in tally.items() if count == max_count]
    return random.choice(top_owners)

# ----------------------------------------------------------------------------
# HELPER FUNCTION TO RENDER EACH QUESTION
# ----------------------------------------------------------------------------
def render_question(question_title, answers, key_prefix, image_base_url=GITHUB_IMAGE_BASE_URL):
    """
    Renders a question with a single radio group.
    :param question_title: str
    :param answers: list of dicts, each dict:
        {
          'label': 'Answer text',
          'image': 'filename.jpg' (can be "" if no image),
          'owners': ['Dan', 'David']  # or single item
        }
    :param key_prefix: a unique string for st.radio
    :return: the owners (list) associated with the chosen answer
    """
    st.subheader(question_title)
    
    # We'll display the radio for text answers
    labels = [a['label'] for a in answers]
    selected_label = st.radio("Select an answer:", labels, key=key_prefix)
    
    # Now display the image for whichever answer is selected
    # (assuming exactly one dictionary matches the label)
    for a in answers:
        if a['label'] == selected_label:
            if a['image']:
                st.image(image_base_url + a['image'], width=200)
            return a['owners']  # Return the owners for the chosen answer

    # Fallback if nothing matched for some reason
    return []

# ----------------------------------------------------------------------------
# 3. STREAMLIT UI
# ----------------------------------------------------------------------------
def main():
    st.set_page_config(page_title="FBMM Owner Quiz", layout="centered")

    st.title("Which FBMM Owner Are You?")
    st.write("You know which team you're on. But which owner are you most like? Find out!")
    st.image(f"{GITHUB_IMAGE_BASE_URL}header_pic.png", use_container_width=True)

    # Collect all selected owners from each question in a big list
    all_selected_owners = []

    # Question 1
    q1_answers = [
        {"label": "Watching movies",
         "image": "",  # or 'watching_movies.jpg' if you have an image
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
         "owners": ["Julie"]}
    ]
    owners_for_q1 = render_question(
        "Question 1: It's a Saturday night. What are you up to?",
        q1_answers,
        key_prefix="q1"
    )
    all_selected_owners.append(owners_for_q1)

    # Question 2
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
    owners_for_q2 = render_question("Question 2: Who was your childhood crush?",
                                    q2_answers, "q2")
    all_selected_owners.append(owners_for_q2)

    # Question 3
    q3_answers = [
        {"label": "Cabernet / a good red wine", "image": "cabernet.jpg", "owners": ["Carmen"]},
        {"label": "An old fashioned", "image": "old_fashioned.jpg", "owners": ["Dan"]},
        {"label": "Coffee", "image": "coffee.jpg", "owners": ["Duane"]},
        {"label": "Pina colada", "image": "pina_colada.jpg", "owners": ["Erica"]},
        {"label": "Hendrick's and tonic with a cucumber slice", "image": "hendricks.png", "owners": ["Jamie"]},
        {"label": "Sangria", "image": "sangria.jpg", "owners": ["Jen"]},
        {"label": "Gin and tonic", "image": "gin_and_tonic.jpg", "owners": ["Julie"]},
        {"label": "Water or bourbon. Sometimes together", "image": "bourbon.jpg", "owners": ["David"]}
    ]
    owners_for_q3 = render_question("Question 3: What is your drink of choice?",
                                    q3_answers, "q3")
    all_selected_owners.append(owners_for_q3)

    # ... continue for the rest of the questions the same way ...
    
    # For brevity, I won't copy all – but you'd do each question in the same style

    # SUBMIT button
    if st.button("Submit"):
        result_owner = get_best_match(all_selected_owners)
        st.markdown(f"## You are most like **{result_owner}**!")
        st.image(OWNER_IMAGE_URLS[result_owner])
        st.write("Thanks for taking the quiz!")

if __name__ == '__main__':
    main()
