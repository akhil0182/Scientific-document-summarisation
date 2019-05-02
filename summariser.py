
import sys
import variables
sys.stdout=open("output.txt","w")
try:
    for x in range(variables.download_count):
        import sumy
        import tika
        from sumy.parsers.plaintext import PlaintextParser
        from sumy.nlp.tokenizers import Tokenizer
        from sumy.summarizers.lex_rank import LexRankSummarizer
        from tika import parser
        filename = 'python' + str(x) + '.pdf'
        raw = parser.from_file(filename)
        parser = PlaintextParser.from_string(raw['content'],Tokenizer("english"))

        summarizer = LexRankSummarizer()

        summary = summarizer(parser.document, 10)

        for sentence in summary:
            print(sentence)
        print('')
        print('')

    sys.stdout.close() 

except:
        print("Error in summariser program")
        return 1
    