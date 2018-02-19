from __future__ import print_function
# Required Python Machine learning Packages

# For preprocessing the data

import os
from textblob.classifiers import NaiveBayesClassifier

class SpamDetection:

      THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
      my_file = os.path.join(THIS_FOLDER, 'train.json')

      def isSpam(self,text):
        with open(SpamDetection.my_file, 'r') as fp:
          cl = NaiveBayesClassifier(fp, format="json")
          result = cl.classify(text);
          return result;

myobjectx = SpamDetection()
#
print(myobjectx.isSpam("This is do not amazing library"))

