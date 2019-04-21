##### CLASSIC TEXT - NLP PROJECT

from collections import Counter

##### function that pulls chunks out of chunked sentence and finds the most common chunks
def np_chunk_counter(chunked_sentences):

    ##### create a list to hold chunks
    chunks = list()

    ##### for-loop through each chunked sentence to extract noun phrase chunks
    for chunked_sentence in chunked_sentences:
        for subtree in chunked_sentence.subtrees(filter=lambda t: t.label() == 'NP'):
            chunks.append(tuple(subtree))

    ##### create a Counter object
    chunk_counter = Counter()

    ##### for-loop through the list of chunks
    for chunk in chunks:
        ##### increase counter of specific chunk by 1
        chunk_counter[chunk] += 1

    ##### return 30 most frequent chunks
    return chunk_counter.most_common(30)


##### function that pulls chunks out of chunked sentence and finds the most common chunks
def vp_chunk_counter(chunked_sentences):

    ##### create a list to hold chunks
    chunks = list()

    ##### for-loop through each chunked sentence to extract verb phrase chunks
    for chunked_sentence in chunked_sentences:
        for subtree in chunked_sentence.subtrees(filter=lambda t: t.label() == 'VP'):
            chunks.append(tuple(subtree))

    ##### create a Counter object
    chunk_counter = Counter()

    ##### for-loop through the list of chunks
    for chunk in chunks:
        ##### increase counter of specific chunk by 1
        chunk_counter[chunk] += 1

    ##### return 30 most frequent chunks
    return chunk_counter.most_common(30)


from nltk import pos_tag, RegexpParser
from nltk.tokenize import word_tokenize, sent_tokenize
# from tokenize_words import word_sentence_tokenize
# from chunk_counters import np_chunk_counter, vp_chunk_counter

##### import text of choice here
text = open('/Users/maosa/Desktop/programming/codecademy/python/nlp/the_iliad_of_homer.txt',encoding='utf-8').read().lower()

##### sentence and word tokenize text here
sentence_tokenized_text = sent_tokenize(text)

word_tokenized_text = []
for sentence in sentence_tokenized_text:
    word_tokenized_text.append(word_tokenize(sentence))

##### store and print any word tokenized sentence here
single_word_tokenized_sentence = word_tokenized_text[1000]
print(single_word_tokenized_sentence)
print('\n\n')

##### create a list to hold part-of-speech tagged sentences here
pos_tagged_text = []

##### create a for loop through each word tokenized sentence here
##### part-of-speech tag each sentence and append to list of pos-tagged sentences here
for sentence in word_tokenized_text:
    pos_tagged_text.append(pos_tag(sentence))

##### store and print any part-of-speech tagged sentence here
single_pos_sentence = pos_tagged_text[1000]
print(single_pos_sentence)
print('\n\n')

##### Begin by defining a piece of chunk grammar np_chunk_grammar that will chunk a noun phrase. Remember, a noun phrase consists of an optional determiner DT, followed by any number of adjectives JJ, followed by a noun NN
np_chunk_grammar = 'NP: {<DT>?<JJ>*<NN>}'

##### create noun phrase RegexpParser object here
np_chunk_parser = RegexpParser(np_chunk_grammar)

##### Define a piece of chunk grammar named vp_chunk_grammar that will chunk a verb phrase of the following form: noun phrase, followed by a verb VB, followed by an optional adverb RB
vp_chunk_grammar = 'VP: {<DT>?<JJ>*<NN><VB.*><RB.?>?}'

##### create verb phrase RegexpParser object here
vp_chunk_parser = RegexpParser(vp_chunk_grammar)

##### create a list to hold noun phrase chunked sentences and a list to hold verb phrase chunked sentences here
np_chunked_text = []
vp_chunked_text = []

##### create a for loop through each pos-tagged sentence here
##### chunk each sentence and append to lists here
for sentence in pos_tagged_text:
    np_chunked_text.append(np_chunk_parser.parse(sentence))
    vp_chunked_text.append(vp_chunk_parser.parse(sentence))

##### store and print the most common NP-chunks here
most_common_np_chunks = np_chunk_counter(np_chunked_text)
print(most_common_np_chunks)
print('\n\n')

##### store and print the most common VP-chunks here
most_common_vp_chunks = vp_chunk_counter(vp_chunked_text)
print(most_common_vp_chunks)
print('\n\n')
