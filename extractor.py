def extrac():
    import re
    var=0
    fhand1=open("pdf_text.txt","r")
    fhand2=open("references.txt","w")
    for line in fhand1:
            if var==1: 
                fhand2.write(line)
            line=line.rstrip()

            if re.search(".*REFERENCES",line):
                var=1

if __name__ == "__main__":
    main()