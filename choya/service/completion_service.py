# 1. Import our agent class
from autogen import ConversableAgent, LLMConfig

# 2. Define our LLM configuration for OpenAI's GPT-4o mini
#    uses the OPENAI_API_KEY environment variable
llm_config = LLMConfig(api_type="openai", model="gpt-4o-mini")

import logging
logger = logging.getLogger("completion_service")
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class LlmService():

    def __init__(self):
        pass

    def agent_chat(self, clients_message):
        # 3. Create our LLM agent
        with llm_config:
            my_agent = ConversableAgent(
                name="Bill_agent",
                system_message="You are a very helpfull AI assistant and who is ready to answer clients questions.",
            )

        # 4. Run the agent with a prompt
        response = my_agent.run(
            message=str(clients_message),
            max_turns=1,
            user_input=False
        )

        # 5. Iterate through the chat automatically with console output
        response.process()

        # 6. Print the chat
        string_response = response.messages[1]['content']
        logger.info(f"Agent response:  {string_response}")
        return string_response