import requests
from bs4 import BeautifulSoup

# Making a Get Request
url = 'https://www.patrickwanis.com/50-points-of-advice-from-an-80-year-old-man/'
page = requests.get(url)
#Parsing the HTML
soup = BeautifulSoup(page.content, 'html.parser')

#Find content
s = soup.find('div', class_ = 'elementor-widget-container')
content = soup.find_all('p')

count = 0 # to use as a counter on the list
list_numb = []
list_string = []

# create a list of numbers from 1-50 with a '.' at the end to match values on content
while count <= 50:
    count = count + 1
    count_string = f'{count}.'
    list_numb.append(count_string)

# search for same values with list to search for exact information in content
for i in content:
    for line in i:
        for num in list_numb:
            if num in line:
                if '-' in line: # i used this line of code because there was a line containing 'COVID-19' so this excludes
                    pass
                else:
                    list_string.append(line) # appended each line in to a list

unique_set = list(set(list_string)) # I used sorted because I was having some repeated lines in list

my_dic = {} # created this dict because all the lines were scrambled and I needed to sort it

for i in unique_set:
    line = i.split() # Since the line was a string I split the line to exclude the first number
    line_string = ' '.join(line[1:]) # Creation of a line without the number
    line1 = line[0].replace('.', '') # Dropped the '.' to isolate only as a number
    line_n = int(line1) # converstion from a string to a int
    my_dic[line_n] = line_string # appended the number to the correct line

sorted_dict = dict(sorted(my_dic.items())) # sorted the dictionary because keys where scrambled

print(f"Henry Cavill's 50 Points Of Advice From An 80 - Year - Old Man")
for key, value in sorted_dict.items():
    print(f'{key}. {value}') # gives you the dict iterated







