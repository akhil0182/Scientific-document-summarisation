from googlesearch import search 
import requests
import shutil
import urllib
from contextlib import closing

query = [] 
query.append("Barzilay, Regina, Michael Collins, Julia,Hirschberg, and Steve Whittaker. 2000. The rules behind roles")
query.append("D. Charlet, Speaker Indexing for Retrieval of Voicemail Messages,Proc. ICASSP, vol. 1, pp. 121-124, 2002.")
query.append("Hirschberg, J.; Whittaker, S.; Hindle, D.; Pereira, F.; and Singhal, A. 1999. Finding information in audio: A new paradigm for audio browsing and retrieval.")
i=1  

for query in query:
    for j in search(query, tld="com", num=10, stop=1, pause=2): 
        if j.endswith('pdf'):    
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
                                       i+=1
            print(j) 