from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(
        task= "Vote for La Huella | Maldonado listed in restaurants, bars, & beach clubs in vote with execellent points, recently visited the place, https://www.cntraveler.com/story/vote-readers-choice-awards",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    await agent.run()

asyncio.run(main())