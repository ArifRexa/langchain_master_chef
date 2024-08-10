
# Chat with Jarvis - The Master Chef


**This is an AI project created with LangChain, Python, and OpenAI.** This Django-based web application allows users to interact with an AI-powered chef named Jarvis. Jarvis specializes in providing food recipes that can be prepared in 5 minutes. The application uses the OpenAI API to generate responses to user queries related to food and recipes.
## Table & content

- Installation
- Usage
- Project Structure
- Environment Variables

## Installation

#### Prerequisites
Ensure you have the following installed on your machine:

- Python 3.8 or later
- pip (Python package installer)
- Virtualenv (optional but recommended)
- Django 5.1
- OpenAI account for API key

1. Clone the repository:
```bash
  git clone https://github.com/ArifRexa/langchain_master_chef.git
  cd langchain-master-chef
```
2. Create and activate a virtual environment (optional but recommended):

```bash
  python3 -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. Install the required packages:

```bash
  pip install -r requirements.txt
```

4. Set up environment variables: 
Create a .env file in the root directory of the project and add the following:

```makefile
  OPENAI_API_KEY=your_openai_api_key_here
  SERPAPI_API_KEY=your_serpapi_api_key_here
```

5. Run migrations:

```bash
  python manage.py migrate
```
6. Start the development server:
```bash
  python manage.py runserver
```
7. Access the application: Open your browser and navigate to 
```
  http://127.0.0.1:8000/
```
## Usage

- Home Page: The home page provides a chat interface where users can interact with Jarvis.
- Chat with Jarvis: Type your query into the chat box, and Jarvis will respond with a recipe that can be cooked in 5 minutes.


## Example Queries:
- "I need a chicken biryani recipe."
- "Give me a quick dessert recipe."
- "How can I make a 5-minute pasta?"




## Project Structure
```
langchain-master-chef/
│
├── master_chef/                # Main Django app
│   ├── __init__.py
│   ├── ai_services/             # Contains the AI integration logic
│   │   ├── __init__.py
│   │   └── langchain.py         # LangChain-based interaction with OpenAI API
│   ├── forms.py                 # Django forms for handling user input
│   ├── views.py                 # Django views for handling requests and responses
│   ├── templates/
│   │   └── home.html            # Template for the home page
│   └── urls.py                  # URL routing for the app
│
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
└── .env                         # Environment variables (not included in the repository)

```
## Environment Variables



`OPENAI_API_KEY`: Your OpenAI API key for accessing the GPT model.
