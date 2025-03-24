# IMDB_MovieInsight Objective 
Build a RAG based application where user can ask questions about about movie. This repo contains Movies metadata and imdb ratings.

#ipynb - Jupyter Source File, it is useful for learning purpose.
01_IMDB_Scraper.ipynb : Selenium based scrapper which extract movies metadata from a website https://www.imdb.com/search/title/?groups=top_1000 and download in a data/imdb_top_1000.csv, for the convenience you don't need to run this scrapper because I have already downloaded and kept this file under /data folder. I kept it here just to sake of learning purpose.

02_Movie_Insights.ipynb : This is the main file which contains the core logic of NLP. Below is the step by step understanding -
1- Uses Closed models like EMBEDDING_MODEL_NAME = "text-embedding-3-small", LLM_MODEL_NAME = "gpt-4o-mini-2024-07-18" .  For that, you have to create an account in https://platform.openai.com/ and generate the api_key. It is paid via credit card. You can start with $5 for your learning purpose. This project would need just 0.01$. 

#src folder and data folder
This is python project which ideally used a production ready project. But everytime you run this project it cost you 0.01$ each time. 


