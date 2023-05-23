import streamlit as st
import openai as ai
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO)

# Set OpenAI API key
ai.api_key = os.environ["API_KEY"]

# Define user messages
messages = [
    "Briefly explain what your online course is",
    "Who is your ideal student for your course?",
    "What do they currently believe about the problem, solution or transformation?",
    "To be ready to buy, what do they need to believe about the problem, solution or transformation?",
]

user_responses = []

# Collect user responses
for item in messages:
    user_data = st.text_area(label=item)
    user_responses.append(user_data)

# Handle button click event
if st.button("Submit"):
    try:
        # Prepare messages for conversation with OpenAI model
        conversation = [
            {"role": "system", "content": "Generate a lead magnet using the following context"},
            {"role": "user", "content": messages[0]},
            {"role": "assistant", "content": user_responses[0]},
            {"role": "user", "content": messages[1]},
            {"role": "assistant", "content": user_responses[1]},
            {"role": "user", "content": messages[2]},
            {"role": "assistant", "content": user_responses[2]},
            {"role": "user", "content": messages[3]},
            {"role": "assistant", "content": user_responses[3]},
        ]

        # Make API call to OpenAI
        response = ai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )

        logging.info(response)
        content = response["choices"][0]["message"]["content"]

        # Display the generated content
        st.write(content)

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        st.error("An error occurred while processing. Please try again later.")
