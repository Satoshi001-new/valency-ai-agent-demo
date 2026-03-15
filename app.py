import os
from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent
from langchain.prompts import StringPromptTemplate
from langchain_openai import OpenAI
from langchain.chains import LLMChain

# 1. Your Custom Data (The "Secret Sauce")
CHEMICAL_DB = {
    "Acetone": "Highly flammable. Flash point: -20°C. Causes serious eye irritation.",
    "Benzene": "Carcinogenic. Flammable liquid and vapor. Store in a cool place.",
    "Ethanol": "Flammable. Flash point: 13°C. Keep away from heat and sparks.",
}

# 2. Define a Tool for the Agent to use
def search_chemical_safety(query: str):
    """Searches for safety information about a chemical."""
    # Look for the chemical in our "database"
    for chemical, info in CHEMICAL_DB.items():
        if chemical.lower() in query.lower():
            return f"Safety Info for {chemical}: {info}"
    return "Chemical not found in safety database."

# 3. Setup the Agent Tools
tools = [
    Tool(
        name="ChemicalSafetySearch",
        func=search_chemical_safety,
        description="Useful for finding safety data and flash points of chemicals."
    )
]

# Note for Rajmi: This script is a 'Proof of Concept'. 
# When you write your article, you will explain how this logic 
# can be scaled to thousands of chemicals using a real database.

if __name__ == "__main__":
    print("--- Valency AI Agent Demo Started ---")
    query = "Is Acetone dangerous?"
    result = search_chemical_safety(query)
    print(f"User Query: {query}")
    print(f"Agent Output: {result}")
