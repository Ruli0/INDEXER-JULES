import spacy
import json
from nltk.stem.snowball import SnowballStemmer

class Indexer:
   def __init__(self, stem_lang=None):
      model = "fr_core_news_md"
      self.nlp = spacy.load(model)
      self.stemmer = SnowballStemmer(stem_lang) if stem_lang else None
   
   def create_index(self, input_file, field, pos=False, skip_lem=False):
      """Indexes a JSON file."""
      if not skip_lem:
         # Loading the file
         with open(input_file, 'r', encoding="utf-8") as file:
            file_content = json.load(file)

         # Lemmatizing
         docs = [doc[field] for doc in file_content]
         self.lem_docs = self.lemmatize(docs)
      
         # Stemming
         if self.stemmer:
            for i, doc in enumerate(self.lem_docs):
               self.lem_docs[i] = [self.stemmer.stem(token) for token in doc]

      # Indexing
      if pos:
         self.index = self.pos_index(self.lem_docs)
      else:
         self.index = self.non_pos_index(self.lem_docs)
         
      
   def save_index(self, output_file):
      """Saves the index to a JSON file."""
      with open(output_file, 'w', encoding="utf-8") as file:
         file.write(json.dumps(self.index, ensure_ascii=False))
      
   def save_statistics(self, output_file):
      """Computes and saves statistics about the index."""
      n_docs = len(self.lem_docs)
      n_total_tokens = len(self.index)
      avg_tokens_per_doc = sum([len(doc) for doc in self.lem_docs]) / n_docs

      statistics = {
         "n_docs": n_docs,
         "n_total_tokens": n_total_tokens,
         "avg_tokens_per_doc": avg_tokens_per_doc
      }

      with open(output_file, 'w', encoding="utf-8") as file:
         file.write(json.dumps(statistics, ensure_ascii=False))

   def lemmatize(self, docs):
      """Lemmatizes a list of documents."""
      docs = list(self.nlp.pipe(docs, disable=["parser", "ner"]))
      new_docs = []
      for i, doc in enumerate(docs):
         new_docs.append([])
         for token in doc:
            if token.is_alpha and not token.is_stop:
               new_docs[i].append(token.lemma_.lower())
      return new_docs

   @staticmethod
   def non_pos_index(docs):
      """Lists docs that contain the lemma"""
      result = {}
      for i, doc in enumerate(docs):
         for lemma in doc:
            if not lemma in result:
               result[lemma] = []
            result[lemma].append(i)
      return result

   @staticmethod
   def pos_index(docs):
      """Lists the position of a lemma in a document"""
      result = {}
      for i, doc in enumerate(docs):
         for j, lemma in enumerate(doc):
            if not lemma in result:
               result[lemma] = {}
            if not i in result[lemma]:
               result[lemma][i] = []
            result[lemma][i].append(j)
      return result