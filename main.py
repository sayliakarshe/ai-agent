from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()


async def main():
    agent = Agent(
        task = 
         """ You are housing agent. 
         You are job is to help user to find a house.
         User might be looking for house to buy or rent.
         Ask for user preferences and find a house for them.
         Ask to buy or rent.
         Ask for location.
         Ask for Budget.
         Based on the user preferences, find a house for them.
         Give top 3 options for the choises made by user.
         """,

        llm=ChatOpenAI(model="gpt-4o"),
    )
    await agent.run()

asyncio.run(main())