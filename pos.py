import nltk
import spacy
from nltk.tokenize import sent_tokenize, word_tokenize
import pandas as p

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Load the spaCy model for lemmatization and POS tagging
nlp = spacy.load('en_core_web_sm')

# Step 1: Read Data from a Text File
def read_file(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    return text

# Step 2: Tokenize the text into sentences
def tokenize_sentences(text):
    sentences = sent_tokenize(text)
    return sentences

# Step 3: Tokenize and lemmatize the words in each sentence
def tokenize_and_lemmatize(sentence):
    doc = nlp(sentence)
    lemmatized_sentence = ' '.join([token.lemma_ for token in doc])
    return lemmatized_sentence

# Step 4: Extract subject, verb, and predicate
def extract_subject_verb_predicate(sentence):
    doc = nlp(sentence)
    subject = ""
    verb = ""
    predicate = ""
    
    for token in doc:
        if "subj" in token.dep_:
            subject = token.text
        if "VERB" in token.pos_:
            verb = token.lemma_
        if "obj" in token.dep_:
            predicate = token.text
    
    return subject, verb, predicate

# Main function to process the text
def main(filepath):
    text = read_file(filepath)
    sentences = tokenize_sentences(text)
    
    refined_sentences = []
    for sentence in sentences:
        lemmatized_sentence = tokenize_and_lemmatize(sentence)
        subject, verb, predicate = extract_subject_verb_predicate(lemmatized_sentence)
        if subject and verb and predicate:
            refined_sentence = {"Subject":subject,"Verb":verb,"Predicate":predicate}
            refined_sentences.append(refined_sentence)
    
    return refined_sentences

# Example usage
if __name__ == "__main__":
    filepath = r"C:\Users\user\Downloads\sample-pdf-text.txt"  # Replace with the path to your text file
    refined_sentences = main(filepath)
    print("\n***Without dataframe***")
    for sentence in refined_sentences:
        print(sentence)
    print("\n***With Dataframe***")
    df=p.DataFrame(refined_sentences)
    print(df)


    
