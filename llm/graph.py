from typing import TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph import END, StateGraph, START
# from agents import CFA_Agent
from state import AgentState
from agents import   Pay_Agent,Master_Agent
from langchain_core.messages import HumanMessage
import logging
logging.basicConfig(level=logging.INFO,format= '%(asctime)s -%(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
import subprocess
from transfer import transfer_eth
import pymongo
from pymongo import MongoClient
import os
import urllib.parse
from dotenv import load_dotenv
load_dotenv()
user_name = os.getenv("USER_NAME")
password = os.getenv("PASSWORD")
encoded_username = urllib.parse.quote_plus(user_name)
encoded_password = urllib.parse.quote_plus(password)
mongo_uri = f"mongodb+srv://{encoded_username}:{encoded_password}@mlproject.yu0js.mongodb.net/?retryWrites=true&w=majority&appName=MlProject"
client = MongoClient(mongo_uri)
db = client['walletcontact']
collection = db['walletcontact']
workflow= StateGraph(AgentState)
state = AgentState()

def Master_Node(state):
    query = state["query"]
    result = Master_Agent(query)
    return {"result":result['answer']}

def Pay_Node(state):
    query = state["query"]
    result = Pay_Agent(query)
    print("Transferring",result['amount'],"to",result['name'])
    print("now transferring.")
    doc = collection.find_one({"name": result['name']})
    walletAddress = doc['walletAddress']
    transfer_eth(walletAddress,result['amount'])
    print("after transfer")
    return {"result": "Transfer completed"} 

# def Search_Node(state):
#     query = state["query"]
#     result = Search_Agent(query)
#     return {"result":result['answer']}

#adding nodes to the workflow
workflow.add_node("Master-Agent",Master_Node)
workflow.add_node("Pay-Agent",Pay_Node)
#adding edges to the workflow
workflow.add_edge(START, "Master-Agent")
# workflow.add_edge("Master-Agent", "Search-Agent")
workflow.add_edge("Master-Agent", "Pay-Agent")
workflow.add_edge("Pay-Agent", END)








