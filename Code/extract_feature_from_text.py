import spacy

from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
from gensim.summarization import summarize



# document1 ="""Machine learning (ML) is the scientific study of algorithms and statistical models that computer systems use to progressively improve their performance on a specific task. Machine learning algorithms build a mathematical model of sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to perform the task. Machine learning algorithms are used in the applications of email filtering, detection of network intruders, and computer vision, where it is infeasible to develop an algorithm of specific instructions for performing the task. Machine learning is closely related to computational statistics, which focuses on making predictions using computers. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. Data mining is a field of study within machine learning, and focuses on exploratory data analysis through unsupervised learning.In its application across business problems, machine learning is also referred to as predictive analytics."""


stopwords = list(STOP_WORDS)
nlp = spacy.load('en')



def word_frequencies(docx):
	# Build Word Frequency
	# word.text is tokenization in spacy
	word_frequencies = {}
	for word in docx:
		if word.text in stopwords: continue
		if word.text not in word_frequencies.keys():
			word_frequencies[word.text] = 1
		else:
			word_frequencies[word.text] += 1

	# Maximum Word Frequency
	maximum_frequency = max(word_frequencies.values())

	for word in word_frequencies.keys():  
		word_frequencies[word] = (word_frequencies[word]/maximum_frequency)


	return(word_frequencies)


def sentence_scores(docx,word_frequencies):
	# Sentence Tokens
	sentence_list = [ sentence for sentence in docx.sents ]

	# Sentence Score via comparrng each word with sentence
	sentence_scores = {}  
	for sent in sentence_list:
		for word in sent:
			if word.text.lower() in word_frequencies.keys():
				if len(sent.text.split(' ')) < 30:
					if sent not in sentence_scores.keys():
						sentence_scores[sent] = word_frequencies[word.text.lower()]
					else:
						sentence_scores[sent] += word_frequencies[word.text.lower()]


	return(sentence_scores)

def summarize_sentence_heapq(sentence_scores):
	summarized_sentences = nlargest(7, sentence_scores, key=sentence_scores.get)

	# List Comprehension of Sentences Converted From Spacy.span to strings
	final_sentences = [ w.text for w in summarized_sentences ]

	summary = ' '.join(final_sentences)

	return(summary)


def spacy_summarize(document):

	docx = nlp(document)
	# Tokenization of Text
	mytokens = [token.text for token in docx]
	word_frequency= word_frequencies(docx)


	sent_scores= sentence_scores(docx,word_frequency)
	return(summarize_sentence_heapq(sent_scores))



def genism_summarize(doc):
	sum_gen = summarize(doc)
	return(sum_gen)

