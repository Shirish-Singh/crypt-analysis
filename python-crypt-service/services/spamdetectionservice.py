from __future__ import print_function
# Required Python Machine learning Packages

# For preprocessing the data
from textblob.classifiers import NaiveBayesClassifier


class SpamDetection:

    def isSpam(self,text):
      with open('train.json', 'r') as fp:
        cl = NaiveBayesClassifier(fp, format="json")
        result = cl.classify(text);
        return result;

myobjectx = SpamDetection()

print(myobjectx.isSpam("This is do not amazing library"))

