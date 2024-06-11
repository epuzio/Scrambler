#part of speech tagger
#mostly from this tutorial: https://www.geeksforgeeks.org/nlp-part-of-speech-default-tagging/
import stanza

import ssl
stanza.download("en")
nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,constituency')
doc = nlp('This is a test')
for sentence in doc.sentences:
    print(sentence.constituency)