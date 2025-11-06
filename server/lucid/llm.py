#!/usr/bin/env python

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", max_tokens=None, timeout=None, max_retries=2
)
