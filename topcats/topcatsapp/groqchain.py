import os
from django.conf import settings
from langchain.chains import LLMChain
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq


class GroqChain():
    def __init__(self):
        groq_api_key = settings.GROQ_SECRET
        model = 'llama3-8b-8192'
    # Initialize Groq Langchain chat object and conversation
        self.groq_chat = ChatGroq(
            groq_api_key=groq_api_key,
            model_name=model
        )
        conversational_memory_length = 2
        self.memory = ConversationBufferWindowMemory(k=conversational_memory_length, memory_key="chat_history", return_messages=True)
    def generateQuestions(self,  content,num_questions):
        prompt = ChatPromptTemplate.from_messages(
                [
                    SystemMessage(
                        content='You are a friendly tutor assisting a student with their learning.'
                    ),  # This is the persistent system prompt that is always included at the start of the chat.

                    MessagesPlaceholder(
                        variable_name="chat_history"
                    ),  # This placeholder will be replaced by the actual chat history during the conversation. It helps in maintaining context.

                    HumanMessagePromptTemplate.from_template(
                        "{human_input}"
                    ),  # This template is where the user's current input will be injected into the prompt.
                ]
            )
            # Create a conversation chain using the LangChain LLM (Language Learning Model)
        conversation = LLMChain(
                llm=self.groq_chat,  # The Groq LangChain chat object initialized earlier.
                prompt=prompt,  # The constructed prompt template.
                verbose=False,   # TRUE Enables verbose output, which can be useful for debugging.
                memory=self.memory,  # The conversational memory object that stores and manages the conversation history.
            )
            # The chatbot's answer is generated by sending the full prompt to the Groq API.
        response = conversation.predict(human_input=f"Create {num_questions} short-answer practice questions (without answers, only a list of the questions in JSON format) based on the following text content: {content}",
        )
        return response
