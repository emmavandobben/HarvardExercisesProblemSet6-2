import nltk
from nltk.tokenize import TweetTokenizer

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        #postives is the directory to a file containing positive words, negative to file with negative word. 
        #make posList and fill it with the content from positive-words.txt
        self.positives = []
        for line in open(positives):
           if not line.startswith(";"):   #remove comments
             line = line.strip()          #strip from whitespace
             self.positives.append(line)
             
        self.negatives = []
        for line in open(negatives):
           if not line.startswith(";"):   #remove comments
             line = line.strip()          #strip from whitespace
             self.negatives.append(line)
             #print(line)

             

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        #seperate words in the string with tokenize text. TweetTokenizer is a token for tweets. http://www.nltk.org/api/nltk.tokenize.html
        self.tokenizer = TweetTokenizer()
        tokens = self.tokenizer.tokenize(text)
        score = 0
        #positive= 0
        # negative= 0
        # neutral= 0
        #iteration
        for token in tokens: 
                 token.lower
                 if token in self.positives:
                      score += 1
                      #positive += 1
                 elif token in self.negatives:
                      score -= 1
                      #negative += 1
                 #else: neutral += 1
        #print (score)
        return (score)
        #, positive, negative, neutral 
