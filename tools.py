from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

def save_to_txt(data:str, filename:str = 'research_output.txt'):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"Timestamp: {timestamp}\n\n{data}\n"
    with open(filename, 'a') as file:
        file.write(formatted_text)

    return f"Data saved to {filename} at {timestamp}"

save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves the research output to a text file with a timestamp"
)

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    description = "search the web for information"
)


api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

