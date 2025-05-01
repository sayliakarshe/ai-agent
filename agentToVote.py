from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()


async def main():
    propertyName = "10 Barrel"
    linkToOpen = "https://condenast-interactive.typeform.com/to/yJBJ9mfX?typeform-source=www.cntraveler.com"
    numberOfTimesToVote = 2
    agent = Agent(
        task = 
            f"Vote for {propertyName} in the 2024 Readers' Choice Awards. "
            f"Click on the link: {linkToOpen}. "
            f"Vote for {propertyName} {numberOfTimesToVote} times."
            f"In the given link, step 1 please search for the property listed in restaurants, bars, & beach clubs. The name of property name is {propertyName}. "
            f"In step 2 please rate 'Excellent' in all the given categories. "
            f"In step 3 please select anyone option and click 'OK' button. "
            f"In step 4 please select yes. "
            f"In step 5 do not leave any note for next travellers, keep it empty and click on 'OK' button. "
            f"In step 6 click on 'No,submit my votes!' and then immideatly click on 'SUBMIT' button to finish the voting process."
            f"Please click on VOTE AGAIN button to vote again for the same property for {numberOfTimesToVote} times. "
            f"Please write and update a json file with the time one vote is finished. "
            f"Save the json file in Output for once process is closed and completed.",   
        llm=ChatOpenAI(model="gpt-4o"),
    )
    await agent.run()

asyncio.run(main())