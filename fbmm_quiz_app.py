import streamlit as st
import random
import urllib.parse

# ------------------------------------------------------------------------------
# 1. GITHUB IMAGE SETTINGS
# ------------------------------------------------------------------------------

# Replace with your actual GitHub repo URL base
GITHUB_IMAGE_BASE_URL = "https://raw.githubusercontent.com/BeemaRajan/fbmm_owner_quiz/main/images/"

# ------------------------------------------------------------------------------
# 2. QUIZ QUESTIONS
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
            "❤ (heart)": ["Carmen"],
            "🤣 (rolling on the floor laughing)": ["Dan", "David"]
        }
    }
]

# ------------------------------------------------------------------------------
# 3. OWNER IMAGES
# ------------------------------------------------------------------------------

OWNER_IMAGE_URLS = {
    name: f"{GITHUB_IMAGE_BASE_URL}{name}.png" for name in
    ["Carmen", "Dan", "David", "Duane", "Erica", "Jamie", "Jen", "Julie"]
}

# ------------------------------------------------------------------------------
# 4. LOGIC: SCORE TALLY
# ------------------------------------------------------------------------------

def get_best_match(selected_owners_lists):
    tally = {}
    for owners in selected_owners_lists:
        for owner in owners:
            tally[owner] = tally.get(owner, 0) + 1

    max_count = max(tally.values())
    top_owners = [owner for owner, count in tally.items() if count == max_count]
    return random.choice(top_owners)

# ------------------------------------------------------------------------------
# 5. HELPERS
# ------------------------------------------------------------------------------

def get_answer_image_url(answer_text):
    """Converts an answer like 'Brad Pitt' or 'la jolla, ca' to a filename-based image URL."""
    base_name = answer_text.lower().replace(" ", "_").replace(",", "").replace("’", "").replace("'", "")
    base_name = base_name.replace("...", "").replace(":", "").replace("(", "").replace(")", "")
    for ext in ['.png', '.jpg', '.jpeg']:
        test_url = f"{GITHUB_IMAGE_BASE_URL}{base_name}{ext}"
        return test_url  # You could check if it's reachable, but we'll trust you uploaded it

# ------------------------------------------------------------------------------
# 6. STREAMLIT APP
# ------------------------------------------------------------------------------

def main():
    st.set_page_config(page_title="FBMM Owner Quiz", layout="centered")

    # Inject custom styles
    st.markdown(
        """
        <style>
            body {
                background-color: #f8f9fa;
            }
            .stButton>button {
                background-color: #b30059;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 8px 16px;
            }
            .stRadio > div {
                background-color: #fff;
                padding: 10px;
                border-radius: 10px;
            }
            img {
                border-radius: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Which FBMM Owner Are You?")
    st.write("Answer the questions below and click **Submit** to see your match.")
    st.image(f"{GITHUB_IMAGE_BASE_URL}header_pic.png", use_column_width=True)

    selected_owner_lists = []

    for i, item in enumerate(QUESTIONS):
        st.subheader(f"Question {i+1}")
        st.write(item["question"])

        # Show answer options with optional image below each
        options = list(item["options"].keys())
        choice = st.radio("Select an answer:", options, key=f"q_{i}")

        # Display a small image under the selected answer
        image_url = get_answer_image_url(choice)
        st.image(image_url, width=200)

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
