# writer_actor.py
from langchain.adapters.openai import convert_openai_messages
from langchain.chat_models import ChatOpenAI


class WriterActor:
    def __init__(self):
        self.model = "gpt-3.5-turbo-16k"

    def generate_report_prompt(self, query, data):
        """ Generates the report prompt for the given question and research summary.
        Args: question (str): The question to generate the report prompt for
                research_summary (str): The research summary to generate the report prompt for
        Returns: str: The report prompt for the given question and research summary
        """
        prompt = [{
            "role": "system",
            "content": "You are an AI critical thinker research assistant. Your sole purpose is to write well written, critically acclaimed, objective and structured reports on given text."
        }, {
            "role": "user",
            "content": f'"""{data}""" Using the above information, answer the following'
                       f' question or topic: "{query}" in a detailed report --'
                       " The report should focus on the answer to the question, should be well structured, informative,"
                       " in depth, with facts and numbers if available, a minimum of 1,200 words and with markdown syntax and apa format. "
                       "You MUST determine your own concrete and valid opinion based on the given information. Do NOT deter to general and meaningless conclusions."
                       "Write all used source urls at the end of the report in apa format"
        }]

        return prompt

    def write(self, data):
        """ Writes a report for the given query.
        Args: query (str): The query to write a report for
        Returns: str: The report for the given query
        """
        lc_messages = convert_openai_messages(self.generate_report_prompt(data["query"], data))
        response = ChatOpenAI(model=self.model).invoke(lc_messages)
        print(response.content)
        return response.content
