# main
import subprocess
from gpt_researcher.researcher import Researcher


if __name__ == '__main__':

    def md2pdf(md_file, pdf_file):
        subprocess.run(["pandoc", md_file, "-o", pdf_file])

    stocks = ["AMZN", "AAPL", "GOOG", "MSFT"]

    for stock in stocks:
        researcher = Researcher(stock)
        research = researcher.run()
        with open(f"output/{stock}.md", "w") as f:
            f.write(research)
        md2pdf(f"output/{stock}.md", f"output/{stock}.pdf")


