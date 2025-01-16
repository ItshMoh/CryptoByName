import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s -%(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from graph import workflow
from state import AgentState

from dotenv import load_dotenv
load_dotenv()

# if document:
#     if "Context" not in document:
#         collection.update_one({"user_id":user_id},{"$set":{"Context":[{"question": " ","answer":" "}]}})
#         logger.info("Context field was not present in the document. Created a new one %s", user_id)
#         document = collection.find_one({"user_id": user_id}) 
#         Memory = document['Context']
#         logger.info("memory is being retrieved %s", Memory) 
#     else:
#         Memory = document['Context']  
#         logger.info("memory is being retrieved %s", Memory)  
# else:
#     print("You are not registered. Please make a account")
#     logger.info("User was not registered %s", user_id)            
def main():
    while True:
        query = input("Enter your query (or type 'exit' to stop): ")
        logger.info("Processing main function with query  %s", query)
        if query.lower() == "exit":
            print("Exiting...")
            break

        try:
            graph = workflow.compile()
            answer = graph.invoke({'query': query})
            print(answer['result'])
            # collection.update_one({"user_id":user_id},{"$push":{"Context": {"question": query, "answer": answer['result']}}})
            
        except Exception as e:
            logger.error("Error in main function: %s", e)

if __name__ == "__main__":
    main()
