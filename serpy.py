import serpapi
import requests
import json
import random
from rapidfuzz import fuzz
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
client = serpapi.Client(api_key=API_KEY)

def findCiting(link: str, count: int):

    citing_articles_dict = { }

    KEY_lnk = str(link) + "&api_key=" + API_KEY
    cited_list = requests.get(KEY_lnk).json()
    looping_list = cited_list
    for i in range(count):
        if ( i % 10 ) == 0 and i != 0:
            looping_link = looping_list["serpapi_pagination"]["next"]
            KEY_ll = looping_link + "&api_key=" + API_KEY
            looping_list = requests.get(KEY_ll).json()
        citing_title = looping_list["organic_results"][i % 10].get("title", "Empty")
        citing_authors = looping_list["organic_results"][i % 10]["publication_info"]["authors"]
        citing_link = looping_list["organic_results"][i % 10].get("link", "Empty")
        citing_articles_dict[i] = {
            "title": citing_title,
            "link": citing_link,
            "authors": citing_authors
        }
    if citing_articles_dict:
        return citing_articles_dict
    else:
        return None

def search(query_term):

    results = client.search({
        "engine": "google_scholar",
        "q": query_term
    })

    print("Searched!")

    title = results["organic_results"][0].get("title", "Empty")
    citation_count = int(results["organic_results"][0]["inline_links"]["cited_by"].get("total", "0"))
    article_link = results["organic_results"][0].get("link", "Empty")
    authors = results["organic_results"][0]["publication_info"].get("Authors", "Empty")
    cited_serplink = results["organic_results"][0]["inline_links"]["cited_by"].get("serpapi_scholar_link", "Empty")

    details = [title, article_link, authors, citation_count]

    #print(citation_count, article_link, title, authors, cited_serplink)


    if title:
        if (score := fuzz.ratio(query_term, title)) > 85:
            print("Found: score " + str(score))
            return findCiting(cited_serplink, citation_count), details
        else:
            print("Failed: score " + str(score))
            return None, details
    else:
        print("Failed: No results!")
        return None, None

def readwrite(input_file: str):
    case_number = str(random.randint(0, 999))
    case_dict = {}
    print(case_number)
    with open(input_file, "r") as file:
        lines = file.readlines()
        case_dict = {"Random Case Number": case_number, "Total Analyzed": len(lines), "Content": {}}
        for line in lines:
            stripped_line = line.strip()
            line_citing, line_details = search(stripped_line)
            case_dict["Content"].update({
                lines.index(line): {
                    "Query": stripped_line,
                    "Title": (line_details or [None])[0],
                    "Link": (line_details or [None, None])[1],
                    "Authors": (line_details or [None, None, None])[2],
                    "Citation Count": (line_details or [None, None, None, None])[3],
                    "Citing Articles": line_citing
                },
            })
    with open("report" + case_number + ".txt", "w") as file:
        json.dump(case_dict, file, indent=4)

readwrite("titles.txt")

#citation_count = 22
#cited_serplink = "https://serpapi.com/search.json?as_sdt=400005&cites=18308769696422031659&engine=google_scholar&hl=en"



