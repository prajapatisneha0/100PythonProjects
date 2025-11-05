from bs4 import BeautifulSoup

with open("website.html") as file:
    content = file.read()

soup = BeautifulSoup(content,"html.parser")
# for title tag
#print(soup.title.name)  # print tag name
#print(soup.title.string) #print text in the title

#print(soup.prettify())

# for first anchor tag
# print(soup.a)

# all_anchor_tag = soup.find_all(name="a")
# print(all_anchor_tag)

# Extracting text from tags
# for tag in all_anchor_tag:
#     print(tag.getText())

# Extracting attribute from tags
#     print(tag.get("href"))

# Finding elements by attribute
# heading = soup.find("h1",id="name")
# print(heading)

# section_heading = soup.find(name="h3",class_="heading")
# print(section_heading)

# h3_heading = soup.find_all("h3",class_="heading")
# print(h3_heading)

# specific elements
# company_url = soup.select_one("p a")
# print(company_url)

# for id
# name_heading = soup.select_one("#name")
# print(name_heading)

# for classes
# headings = soup.select(".heading")
# print(headings)
