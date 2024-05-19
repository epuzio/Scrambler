#part of speech tagger
#mostly from this tutorial: https://www.geeksforgeeks.org/nlp-part-of-speech-default-tagging/
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import markovify
from random import choice
from collections import defaultdict
import random

def tag(input):
    words = []
    with open(input, 'r') as f:
        words = f.readlines()
        words = [word.strip() for word in words]

    pos_tags = pos_tag(words)
    tags = defaultdict(lambda: defaultdict(int))
    for word, tag in pos_tags:
        tags[tag][word] += 1
    return tags
    

def rewrite_at(index, replacements, the_list):
    del the_list[index]
    the_list[index:index] = replacements

def generate_sentence(grammar, start_symbol):
    sentence_list = []
    all_terminals = False
    while not all_terminals:
        all_terminals = True
        for position, symbol in enumerate(grammar):
            if symbol in grammar._lhs_index:
                all_terminals = False
                    derivations = grammar._lhs_index[symbol]
                    derivation = random.choice(derivations) # or weighted_choice(derivations) if you have a function for that
                    rewrite_at(position, derivation.rhs(), sentence_list)
        return sentence_list
    
def main():
  print(tag())

if __name__ == "__main__":
  main()