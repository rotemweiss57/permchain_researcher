# main
from gpt_researcher.researcher import Researcher
if __name__ == '__main__':
    researcher = Researcher("Should I invest in Apple stock?")
    research = researcher.run()
    print(research)
