import variables
#import afterbase
def download1():
    from googlesearch import search 
    import requests
    import shutil
    import urllib
    from contextlib import closing
    query = []
    fhand4=open("pdf_text.txt","r+")
    fhand3=open("references.txt","r+")
    ref_count=1
    for line in fhand3:
        if line.startswith('['):
            query.append(line)
            ref_count+=1
        if ref_count >= 7:
            break

    i=0  
    print(query)
    variables.prev_download_count = variables.download_count
    for query in query:
        for j in search(query, tld="com", num=5, stop=1, pause=25): 
            if j.endswith('pdf'):    
                i+=1
                if j.startswith('ftp://'):
                    with closing(urllib.urlopen(j)) as r:
                        with open("pythons" + str(i) +".pdf", 'wb') as f:
                            shutil.copyfileobj(r, f)
                            print(j)
                else: 
                        r = requests.get(j, stream = True)  
                        with open("python" + str(variables.download_count) +".pdf","wb") as pdf: 
                            for chunk in r.iter_content(chunk_size=1024): 
  
                                  if chunk: 
                                       pdf.write(chunk)
                        variables.download_count+=1
                                       
                print(j)
                break
    
    #fhand3.truncate(0)
    #fhand4.truncate(0)
  
    fhand3.close()
    fhand4.close()
 
          