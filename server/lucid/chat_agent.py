#!/usr/bin/env python

import os
from typing import cast

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


class ChatAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash", temperature=0, max_tokens=None,
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )

    def chat(self, message: str) -> str:
        """Send a message to the LLM"""
        prompt_template = ChatPromptTemplate.from_template(
            """You are a helpful assistant.
            Always respond concisely — use one or two clear sentences maximum.

            Question: {question}

            Answer:
        """
        )

        prompt = prompt_template.invoke({"question": message})
        response = self.llm.invoke(prompt)

        return cast(str, response.content)
