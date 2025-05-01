from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    propertyName = "10 Barrel"
    linkToOpen = "https://condenast-interactive.typeform.com/to/yJBJ9mfX?typeform-source=www.cntraveler.com"
    agent = Agent(
        task= "Open the given link"+ linkToOpen +"In the given link, step 1 please search for the property listed in restaurants, bars, & beach clubs. The name of property name is " + propertyName + "In step 2 please rate 'Excellent' in all the given categories. In step 3 please select anyone option and click 'OK' button. In step 4 please select yes. In step 5 do not leave any note for next travellers, keep it empty and click on 'OK' button. In step 6 click on 'No,submit my votes!' and then click on 'SUBMIT' button.",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    await agent.run()

asyncio.run(main())