
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


paragraph = """NLP is a subfield of computer science and artificial intelligence concerned with
interactions between computers and human (natural) languages. It is used to apply machine learningalgorithms to text and speech.
For example, we can use NLP to create systems like speech recognition, document summarization,
machine translation, spam detection, named entity recognition, question answering, autocomplete,predictive typing and so on.
Nowadays, most of us have smartphones that have speech recognition.
These smartphones use NLP to understand what is said. Also, many people use laptops
 which operating system has a built-in speech recognition."""
               
               
sentences = nltk.sent_tokenize(paragraph)
stemmer = PorterStemmer()

# Stemming
for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ' '.join(words)

    

    
    
    
    