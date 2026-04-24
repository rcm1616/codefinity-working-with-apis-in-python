import requests

def count_cat_facts_with_cat():
    url = "https://catfact.ninja/facts?limit=10"
    response = requests.get(url)
    data = response.json()
    facts = data["data"]
    count = 0
    for fact in facts:
        ##print(fact['fact'])
        if 'cat' in fact ['fact'].lower():
            count +=1
      
    # your code here
    print(count)

count_cat_facts_with_cat()
