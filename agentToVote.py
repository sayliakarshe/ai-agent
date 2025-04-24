from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(
        task= "Vote for La Susana Vik listed in restaurants, bars, & beach clubs in vote with execellent points, vote as recently visited this place,https://condenast-interactive.typeform.com/to/yJBJ9mfX?typeform-source=www.cntraveler.com",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    await agent.run()

asyncio.run(main())