def extrac1():
    import re
    import linecache
    pattern="[0-9]\."
    lookup='REFERENCES'
    fhand4=open("references.txt","w")
    with open("pdf_text.txt") as myFile:
            for rnum, line in enumerate(myFile, 1):
                if lookup in line.upper():
                     temp=rnum;


    #print(rnum)
    #print(temp)
    for i in range (temp,rnum):
        s=linecache.getline("pdf_text.txt", i)
        #s=s+linecache.getline("pdf_text.txt",(i+1))
        #print(s)
    #print(temp)
    #for i in range()
    #file1=open("pdf_text.txt")
    #for line in file1:
        if re.search("[0-9]\.",s):
            if s[0].isdigit():
                    fhand4.write(s)