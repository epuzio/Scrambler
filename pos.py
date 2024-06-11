#part of speech tagger
#mostly from this tutorial: https://www.geeksforgeeks.org/nlp-part-of-speech-default-tagging/
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import markovify #much easier method
from random import choice
from collections import defaultdict
import random
import string
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download('averaged_perceptron_tagger')
TXT_PATH = "margret"

words = []

with open(f"{TXT_PATH}.txt", 'r') as f:
    lines = f.readlines()
    words = [word.translate(str.maketrans('', '', string.punctuation)) for line in lines for word in line.split()]
pos_tags = pos_tag(words)
# print(pos_tags)
tags = defaultdict(lambda: defaultdict(int))
for word, tag in pos_tags:
    tags[tag][word] += 1

# print(tags)

# Convert defaultdict to grammar format
grammar = "\n".join([f"{key} -> {' | '.join(value.keys())}" for key, value in tags.items()])
print(grammar)

# Convert the tags to a CFG
start_symbol = nltk.Nonterminal('S')  # You can choose any non-terminal as the start symbol
productions = [nltk.Production(nltk.Nonterminal(tag), [word]) for tag, words in tags.items() for word in words.keys()]
cfg = nltk.CFG(start_symbol, productions)















# productions = defaultdict(lambda: defaultdict(int)) #tag, productions, max_depth
# nonterminals = []
# with open(f"rules.txt", 'r') as rules_txt:
#     lines = rules_txt.readlines()
#     for l in lines:
#         nonterminals.add(l.split(" -> "))

# for lhs, rhs in nonterminals:
#     productions[lhs][rhs] += 1


# terminals = {'CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNS', 
#              'NNPS', 'PDT', 'POS', 'PRP', 'PRP$', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB', 'VBD',
#               'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB'}

# def get_productions(POS):
#     rhs = random.choice([w for w in productions[POS] for x in range(productions[POS][w])])
#     return [rhs.split(" ")]

# def get_rand_word(POS): #return random word tagged that way (probabilistically weighted)
#     return random.choice([w for w in tags[POS] for x in range(tags[POS][w])])

# def gen_sentence():
#     sentence = ['S']
#     terminals = set()
#     for i, c in sentence:
#         while c not in terminals:
#             offspring = get_productions[c]
#             new_sentence = sentence[0:i]
#             for o in offspring:
#                 new_sentence.append(offspring)
#             new_sentence.append(sentence[i:])
#             sentence = new_sentence

#     for i in range(sentence): #convert POS tags to random words
#         word = get_rand_word(sentence[i])
#         sentence[i] = word
        
        
            




# # #Use stanford NLP parser for parsing sentences:
# # nlp = stanfordnlp.Pipeline()
# # with open(f"{TXT_PATH}.txt", 'r') as f:
# #     lines = f.readlines()
# #     for line in lines:
# #         doc = nlp(lines)
# #         doc.sentences[0].print_dependencies()




