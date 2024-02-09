from indexer import Indexer

indexer = Indexer()
stem_indexer = Indexer(stem_lang = "french")

# Non positionnal index
indexer.create_index("data/crawled_urls.json", "title", pos=False)
indexer.save_index("data/title.non_pos_index.json")

# Positionnal index
indexer.create_index("data/crawled_urls.json", "title", pos=True, skip_lem = True)
indexer.save_index("data/title.pos_index.json")

# Non positionnal index with stemming
stem_indexer.create_index("data/crawled_urls.json", "title", pos=False)
stem_indexer.save_index("data/title.non_pos_stem_index.json")

# Statistics
stem_indexer.save_statistics("data/metadata.json")