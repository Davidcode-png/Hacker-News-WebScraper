from bs4 import BeautifulSoup
import requests
import lxml

website_url = 'https://news.ycombinator.com/'
response = requests.get(website_url)
content = response.text
soup = BeautifulSoup(content,"lxml")
first_new = soup.find('a',class_='titlelink')

table = soup.find_all('table')[2]
table_values_link = table.find_all('a',href=True,class_='titlelink')
table_values_score = table.find_all('span',class_='score')
table_values_author = table.find_all('a',href=True,class_='hnuser')


with open('output.txt','w') as file:
	for i in range(len(table_values_link) - 1):
		text = str(i),'.',' ',table_values_link[i].text,' by', table_values_author[i].text, ' has', table_values_score[i].text,' Link ->',table_values_link[i]['href']
		text = ' '.join(text)
		file.write(text)
		file.write('\n')

#link = table_values[0]["href"]
# print(link)
# website_url = link
# response = requests.get(link)
# content = response.text
# soup_first = BeautifulSoup(content,"lxml")
# #print(soup_first.prettify())
# title = soup_first.title.text
# print(title)
# content = soup_first.find('div',class_='prose-lg')
# all_texts = content.find_all('p')
# for txt in all_texts:
# 	print(txt.text)
# #text_list.append(title)



# for i,tab in enumerate(table_values):
#  	print(i,'---',tab["href"])
#print(table.prettify())