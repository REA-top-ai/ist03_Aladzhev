import requests, json, os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")




def get_first_50():
    adress = "https://newsapi.org/v2/everything"
    pars_mine = {
        "q": "latest",
        "apiKey": API_KEY,
        "pageSize": 100,
        "sortBy": "relevancy",
        "language": "en"
    }
    response = requests.get(adress, params=pars_mine)
    parsed_data = response.json()



    ans = []
    for article in parsed_data.get("articles", []):
        name = article.get("title", "")
        link = article.get("url")
        descript = article.get("description", "")
        if (name != None) and (link != None) and (descript != None) and (len(descript) >= 50):
            ans.append({"headline": name, "news_source": article.get("source", {}).get("name", "Unknown"),
                "release_date": article.get("publishedAt", ""),
                "writer": article.get("author", "Unknown")})
            if len(ans) >= 50:
                break
    return ans




ans = get_first_50()
print(json.dumps(ans, indent=4))   
