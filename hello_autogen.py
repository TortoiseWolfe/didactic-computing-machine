from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load LLM inference endpoints from an env variable or a file
config_list = config_list_from_json(env_or_file=os.getenv("OAI_CONFIG_LIST"))

# Add the API key from the environment variable to the config list
api_key = os.getenv("AUTOGEN_API_KEY")
for config in config_list:
    config['api_key'] = api_key

def main():
    # Create an AssistantAgent
    assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})

    # Create a UserProxyAgent
    user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})

    # Initiate a chat between the two agents to solve a task
    user_proxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.")

if __name__ == "__main__":
    main()
