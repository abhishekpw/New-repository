import xml.etree.ElementTree as ET
from fastapi import FastAPI

app = FastAPI()

def search_xml(query):
    tree = ET.parse("data.xml")
    root = tree.getroot()

    results = []

    for patent in root.findall(".//patent"):
        title = patent.findtext("title")
        company = patent.findtext("company")
        year = patent.findtext("year")

        if query.lower() in title.lower() or query.lower() in company.lower():
            results.append({
                "title": title,
                "company": company,
                "year": year
            })

    return results


@app.get("/search")
def search(q: str):
    return search_xml(q)
