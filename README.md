# Indexer: Un outil d'Indexation Web en Python

# Jules Dumouchel


## À propos

Ce programme est un outil d'indexation de documents écrit en Python. Il prend en charge l'indexation de fichiers au format JSON en utilisant des techniques de lemmatisation et de stemming, puis génère des index non positionnels ou positionnels selon les besoins de l'utilisateur.

## Utilisation

Pour installer les dépendances du programme, entrez la commande suivante :

```bash
python -m pip install -r requirements.txt
```

Voici un exemple d'utilisation de l'indexer :

```python
 # Use french stemmer
stem_indexer = Indexer(stem_lang = "french")

# Non positionnal indexing of 'title' field
stem_indexer.create_index("data/crawled_urls.json", "title", pos=False)

# Saving result in JSON file
stem_indexer.save_index("data/title.non_pos_stem_index.json")
```

Sinon, vous pouvez lancer la démo en utilisant: : 

```bash
python main.py
```