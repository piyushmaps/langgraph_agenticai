import streamlit as st
import os
from datetime import date
from langchain_core.messages import AIMessage, HumanMessage
from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config= Config() #configuration are present inside the fields like in select llm(groq,openai), select Model(mixtral-8x-b, O3-3.5b etc)
        self.user_controls= {}
        