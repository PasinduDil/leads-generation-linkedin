from pydantic_ai import Agent, RunContext
from Leadgen.entity.config_entity import QuestiongeneratorConfig
from pydantic_ai import Agent
from pydantic_ai.models.groq import GroqModel
from pydantic_ai.providers.groq import GroqProvider
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Access the variable
api_key = os.getenv("GROQ_API_KEY")

class QuestionGenAgent:
    def __init__(self, config: QuestiongeneratorConfig):
        self.config = config

    def question_gen_agent():
        model = GroqModel('llama-3.3-70b-versatile',provider=GroqProvider(api_key=api_key))
        question_Gen_Agent= Agent(model=model,
            deps_type=dict,
            output_type=list[str],
            system_prompt=(
                'You are an expert business analyst specializing in creating Ideal Customer Profiles (ICP). '
                'Based on the user\'s business information provided, generate exactly 10 targeted questions '
                'that will help refine and create a comprehensive ICP. These questions should dig deeper '
                'into customer demographics, psychographics, pain points, buying behavior, and market segmentation. '
                'Format each question clearly and make them specific to the user\'s business context. '
                'Return the questions as a list of strings.'
            ),
    )
