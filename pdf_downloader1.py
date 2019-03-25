from googlesearch import search 
import requests
import shutil
import urllib
from contextlib import closing
query = [] 
fhand3=open("references.txt","r")
for line in fhand3:
    query.append(line)

i=0  

for query in query:
    for j in search(query, tld="com", num=10, stop=1, pause=25): 
        if j.endswith('pdf'):    
            i+=1
            if j.startswith('ftp://'):
                with closing(urllib.urlopen(j)) as r:
                    with open("python" + str(i) +".pdf", 'wb') as f:
                        shutil.copyfileobj(r, f)
                        print(j)
            else: 
                      r = requests.get(j, stream = True)  
                      with open("python" + str(i) +".pdf","wb") as pdf: 
                            for chunk in r.iter_content(chunk_size=1024): 
  
                                  if chunk: 
                                       pdf.write(chunk) 
                                       
            print(j) 

            
            
            
