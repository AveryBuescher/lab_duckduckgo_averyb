import requests
import pytest

url_ddg = "https://api.duckduckgo.com"

def test_ddg0():

    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")

    rsp_data = resp.json()

    assert "DuckDuckGo" in rsp_data["Heading"]

president_list = ["Washington","Adams","Jefferson","Madison","Monroe","Adams","Jackson","Buren","Harrison","Tyler","Polk","Taylor","Fillmore","Pierce","Buchanan","Lincoln","Johnson","Grant","Hayes","Garfield","Arthur","Cleveland","Harrison","Cleveland","McKinley","Roosevelt","Taft","Wilson","Harding","Coolidge","Hoover","Roosevelt","Truman","Eisenhower","Kennedy","Johnson","Nixon","Ford","Carter","Reagan","Bush","Clinton","Bush","Obama","Trump"]
resp = requests.get(url_ddg + "/?q=presidents+of+the+united+states&format=json")
rsp_data = resp.json()

rsp_relatedtopics = rsp_data["RelatedTopics"]
check_string = ""
for x in rsp_data["RelatedTopics"]:
        check_string += ' ' + x['Text']

@pytest.mark.parametrize("p",president_list)
def test_presidents(p):
    assert p in check_string
