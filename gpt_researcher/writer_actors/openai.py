from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI, ChatAnthropic
from langchain.schema.output_parser import StrOutputParser


class OpenAIWriterActor:
    def __init__(self):
        self.model = ChatOpenAI(model="gpt-3.5-turbo-16k")
        self.prompt = ChatPromptTemplate.from_messages([
            ("system",
             "You are an AI critical thinker research assistant. Your sole purpose is to write well written, critically acclaimed, objective and structured reports on given text."
             ),
            ("user",
             '"""{results}""" Using the above information, answer the following'
                       ' question or topic: "{query}" in a detailed report --'
                       " The report should focus on the answer to the question, should be well structured, informative,"
                       " in depth, with facts and numbers if available, a minimum of 1,200 words and with markdown syntax and apa format. "
                       "You MUST determine your own concrete and valid opinion based on the given information. Do NOT deter to general and meaningless conclusions."
                       "Write all used source urls at the end of the report in apa format"
             )
        ])

    @property
    def runnable(self):
        return {
            "answer": {
                "query": lambda x: x["query"],
                "results": lambda x: "\n\n".join(x["results"])
                      }
                      |self.prompt | self.model | StrOutputParser()
        }
