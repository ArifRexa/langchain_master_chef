import os
from dotenv import load_dotenv
from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain_openai import ChatOpenAI

# Load environment variables from a .env file
load_dotenv()

def ask_recipe(recipe_message: str) -> str:
    """
    This function interacts with the OpenAI API to generate a food recipe
    based on the user's input. The chatbot is designed to behave as "Jarvis,
    The Master Chef," providing recipes that can be cooked in 5 minutes.

    :param recipe_message: The recipe request message from the user.
    :return: The response from the AI, containing the recipe or a message
             indicating the inability to provide one.
    """
    # Retrieve the OpenAI API key from environment variables
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY not found in environment variables.")
    
    # Initialize the chat model
    chat = ChatOpenAI(api_key=api_key)

    # Define the system message for the AI's role
    system_message = SystemMessagePromptTemplate.from_template(
        """
        Your name is Jarvis. You are a master chef, so first introduce yourself as 
        'Jarvis, The Master Chef'. You can write any type of food recipe that can be 
        cooked in 5 minutes. You are only allowed to answer food-related queries. 
        If you don't know the answer, respond with 'I don't know the answer'.
        """
    )

    # Define the human message template
    human_message = HumanMessagePromptTemplate.from_template(
        "{asked_recipe}"
    )

    # Combine the system and human messages into a chat prompt template
    chat_prompt_template = ChatPromptTemplate.from_messages(
        [system_message, human_message]
    )

    # Format the prompt with the user's input
    formatted_message = chat_prompt_template.format(asked_recipe=recipe_message)

    # Invoke the chat model and return the AI's response
    response = chat.invoke(formatted_message)
    return response.content






















# import os
# from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv

# load_dotenv()

# def askRecipe(recipe_message):
#     secret_key = os.environ.get('OPENAI_API_KEY')
#     print(secret_key)
#     chat = ChatOpenAI(api_key=secret_key)
#     system_message = SystemMessagePromptTemplate.from_template(
#         """Your name is Jarvis. You are a master chef so First Introduce yourself as Jarivs The Master Chef. You can 
#         write any type of food recipe which can be cooked in 5 minutes. You are only allowed to answer food related 
#         queries. If You don't know the answer then tell I don't know the answer."""

#     )
#     human_message = HumanMessagePromptTemplate.from_template(
#         "{asked_recipe}"
#     )

#     chatPromptTemplate = ChatPromptTemplate.from_messages(
#         [system_message, human_message]
#     )
#     formatted_message = chatPromptTemplate.format(asked_recipe=recipe_message)
#     response = chat.invoke(formatted_message)
#     return response.content
