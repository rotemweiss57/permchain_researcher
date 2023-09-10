# main
import subprocess
from gpt_researcher.researcher import Researcher
from gpt_researcher.search_actors.tavily import TavilySearchActor
from gpt_researcher.search_actors.gpt_researcher import GPTResearcherActor
from gpt_researcher.writer_actors.openai import OpenAIWriterActor



if __name__ == '__main__':

    def md2pdf(md_file, pdf_file):
        subprocess.run(["pandoc", md_file, "-o", pdf_file])

    stocks = ["AMZN", "AAPL", "GOOG", "MSFT"]

    for stock in stocks[:1]:
        researcher = Researcher(GPTResearcherActor(), OpenAIWriterActor())
        research = researcher.run(stock)
        with open(f"output/{stock}.md", "w") as f:
            f.write(research)
        md2pdf(f"output/{stock}.md", f"output/{stock}.pdf")


