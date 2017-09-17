import requests
import sys
from bs4 import BeautifulSoup
from mako.template import Template

def fetchPage(pep):
  r = requests.get(f'https://www.python.org/dev/peps/pep-{pep}')
  if r.status_code == 404:
   print(f'Sorry, there is no such thing as PEP {pep}')
   sys.exit()
  else:
   return r.text

def extractArticle(pep):
  page = fetchPage(pep)
  soup = BeautifulSoup(page, 'html.parser')
  content = soup.find('section')

  template = open('template.html', 'r').read()
  renderedHTML = Template(template).render(title=pep, content=content)

  with open(f'output/pep-{pep}.html', 'w') as html:
    html.write(renderedHTML)

if len(sys.argv) > 1 and len(sys.argv[1]) == 4:
  extractArticle(sys.argv[1])
else:
  print('Please enter the four digit code for a PEP eg; 0008')