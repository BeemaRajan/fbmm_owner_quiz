# FBMM Owner Quiz

A short, fun, BuzzFeed-style quiz built with **Python** and **Streamlit**, created as a lightweight interactive web app and deployed using **Streamlit Community Cloud**.

Live App: https://fbmmownerquiz.streamlit.app/  
GitHub Repository: https://github.com/BeemaRajan/fbmm_owner_quiz

---

## Project Overview

The FBMM Owner Quiz is a simple interactive quiz application designed for entertainment and internal engagement. Users answer a series of multiple-choice questions and receive immediate feedback within the browser.

The goal of this project was to explore Streamlit as a rapid application development tool and to demonstrate how basic Python logic can be turned into a shareable web experience with minimal setup.

---

## Features

- Interactive multiple-choice quiz
- Real-time user input handling
- Simple scoring and result display
- Web-based interface (no installation required for users)
- Deployed and publicly accessible via Streamlit Cloud

---

## Technology Stack

- **Python** – core programming language
- **Streamlit** – framework for building interactive web apps in Python
- **Streamlit Community Cloud** – hosting and deployment platform

---

## Project Structure

```
fbmm_owner_quiz/
├── images/                  # Image assets used in the app
├── fbmm_quiz_app.py         # Main Streamlit application script
├── requirements.txt         # Python dependencies
└── LICENSE                  # MIT License
```

---

## Running the App Locally

### Prerequisites

- Python 3.x installed
- pip package manager

### Installation

Clone the repository:

```
git clone https://github.com/BeemaRajan/fbmm_owner_quiz.git
cd fbmm_owner_quiz
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the Streamlit app:

```
streamlit run fbmm_quiz_app.py
```

The app will be available at:

```
http://localhost:8501
```

---

## How the App Works

The application logic is contained in `fbmm_quiz_app.py`. Streamlit widgets are used to display questions, capture user responses, and update the interface dynamically. Each user interaction triggers a re-run of the script, allowing the app to maintain state and update results seamlessly.

Streamlit handles all front-end rendering, allowing the app to remain entirely Python-based.

---

## Deployment

This project is deployed using **Streamlit Community Cloud**, which connects directly to the GitHub repository and automatically builds the app.

Live deployment:
https://fbmmownerquiz.streamlit.app/

To deploy your own version:
1. Fork the repository on GitHub
2. Log in to https://streamlit.io/cloud
3. Connect your forked repository
4. Select `fbmm_quiz_app.py` as the entry point and deploy

---

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
