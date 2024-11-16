from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper, DuckDuckGoSearchAPIWrapper
from langchain.agents import AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate

class BlogGenerator:
    def __init__(self, google_api_key: str):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro",
            temperature=0.7,
            google_api_key=google_api_key
        )

        self.tools = [
            WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper()),
            DuckDuckGoSearchRun(api_wrapper=DuckDuckGoSearchAPIWrapper())
        ]

         # Create the prompt template for the agent
        template = """You are an expert blog writer and researcher. Your task is to research a topic and write a comprehensive blog post about it.

        Given a topic, you should:
        1. Research the topic thoroughly using Wikipedia and DuckDuckGo search
        2. Write a well-structured blog post using the researched information

        The blog must include:
        - Heading: A captivating headline
        - Introduction: An engaging introduction that hooks the reader
        - Content: Well-researched and organized main content with relevant subheadings
        - Summary: A strong conclusion that summarizes key points

        Format the blog in markdown and ensure all information is accurate and well-supported.

        TOOLS:
        ------
        You have access to the following tools:
        {tools}
        
        You gotta make sure "Action:" comes after "Thought:"
        Example:

        Question:{input}
        Thought:{agent_scratchpad}
        Action: the action to take, should be one of [{tool_names}]
        Action Input: the input to the action
        Observation: the result of the action
        (this Thought/Action/Action Input/Observation can repeat multiple times)
        Final Answer: the final answer to the original input question.
        
        When you have gathered enough information to write the blog, proceed to write it.
        Format your final answer as a complete blog post in markdown.

        Begin! Remember to start with understanding the topic through research before writing the blog.

        {agent_scratchpad}"""

        self.prompt = PromptTemplate(
            template=template,
            input_variables=["input", "agent_scratchpad"],
            partial_variables={
                "tools": ", ".join([tool.name for tool in self.tools]),
                "tool_names": ", ".join([tool.name for tool in self.tools])
            }
        )

        self.agent = create_react_agent(
            llm=self.llm,
            tools=self.tools,
            prompt=self.prompt
        )

        self.agent_executor = AgentExecutor(
            agent=self.agent,
            tools=self.tools,
            verbose=True,
            handle_parsing_errors=True
        )

    def generate_blog(self, topic: str) -> str:
        """Generate a blog post on the given topic."""
        try:
            prompt = f"""Research and write a comprehensive blog post about "{topic}".
            Make sure to gather accurate information and present it in a well-structured format."""

            result = self.agent_executor.invoke({"input": prompt})

            return result["output"]
        except Exception as e:
            print(f"Error generating blog: {e}")
            return f"Error generating blog: {str(e)}"