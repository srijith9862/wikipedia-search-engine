# wikipedia-search-engine
Simple search engine on the entire wikiedia corpus.


My code is dividec into 3 parts indexer.py, merger.py, searcher.py.

The function of indexer is to parse the given data into text and then extract different components of the text and then store it in the files.

Then these files are passes onto the merger for merging the sorted files to give a final index.

the final index files can be used for search.
The search function takes input of the qury then it searches the query from the files then gives top 10 answers as the output.

index size in  mb(591 mb )
number of files in which the inverted index is split (59)
number of tokens in the inverted index (2939081)
