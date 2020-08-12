# Public Security Corpora

This is a project dedicated to the construction of an open corpora, a set of texts bodies in Brazilian Portuguese dedicated to Public Security subjects. 

As an academic research output, in this phase it is intended to be composed by two parts:

1. News Corpus, containing news texts about Public Security themes extracted from Newspapers websites;
2. Tweets Corpus, contining tweets;

Each script used to generate the corpora and each json file that contains them is inside the folder named referring to the text sources.

## News Corpus

The News Corpus is composed by texts extracted only for the "Diário de Pernambuco" Newspaper website. The content was found using the site search mechanism with the query containing the portuguese terms: _"segurança pública" + crim* + pernambuco_. 

In its current structure, this corpus contain the following information from the news: title, publication date, author, text, url and content type (if the origin is a news article or the articles from a subpart of the Diario de Pernambuco Newspaper environment called "Blog do Diário" where can be found several texts exclusively dedicated to Public Security themes).


### News Corpus scraping

The news corpus scraping was based in two main technologies: Selenium Web Driver and Scrapy, bot used with Python Language.

Selenium Web Driver script (_diario_scraping_search_results.py_) scraped the initial results page and got the html code of the target elements. To start this script, is just call in a terminal:

```
python diario_scraping_search_results.py
```

Or open it in a Python IDE and run the script using one Python interpreter (iPython, for example). Check if Selenium Web Driver and if the Google Chrome driver are available in Python environment. If not, is necessary to install it. See [Selenium Web Driver documentation page for Python](https://selenium-python.readthedocs.io/installation.html).

Two spiders were created using the Scrapy framework for scraping the news articles from the links in the previously scraped html code, and the posts on the newspaper blog. To run them, is just use their names as was attributed in the scripts: "news" for the spider dedicated for the news articles and "posts" for the one dedicated to posts articles, using _-o json_file_name.json_ to save the information they scraped in a specific json file.

```
scrapy crawl "news" -o diario_seguranca_news.json
```

and

```
scrapy crawl "posts" -o blog-diario_seguranca_posts.json
```

These calls will start the spider scripts named _spider_diario_news.py_ and _spider_diario-blog-seg_posts.py_.

Remember to check if Scrapy framework is available in Python environment. If not, is necessary to install it too. It is necessary to create a project and put both spiders scripts into the spiders subfolder. See [Scrapy documentation page](https://docs.scrapy.org/en/latest/intro/install.html).

After running these two spiders scripts according to the commands passed in the terminal, two json files will be created. They will need some data cleaning, according to the last script to be executed: data_cleaning.py.
Is just call it in a terminal:

```
python data_cleaning.py
```

Or open it in a Python IDE and execute it with the interpreter. Data cleaning script will create three new json files:

* _news_full-corpus.json_, containing all the news scraped and cleaned.
* _news-diario_corpus_, containing only the subset of texts from newspaper articles.
* _blog-diario_corpus_, containing only the subset of texts from "Blog do Diário" articles.


### News Corpus json files

The News Corpus, in its current stage, is stored in a json file called _news_full-corpus.json_.


## Tweets Corpus

This corpus is composed by tweets retrieved using a spacific geographic location, the city of Recife, capital of the state of Pernambuco (Brazil), and a set of keywords related to public security.

In its current structure, the corpus contains the following information: the tweet id, the text, and three kinds of georeferencing information, geo, coordinates and place. Note that not all tweets have this georeferencing information, but these fields have been left because they are considered to be important information for future refinements on this corpus.


### Tweets Corpus Scraping

To perform this scraping, Python's Tweepy library was used. Here the scraping script called _twitter_scraper.py_ was obtained from the work by:

Reinoso, G., Farooq, B., & Forum, C. T. R. (2015). Urban Pulse Analysis Using Big Data. In Canadian Transportation Research Forum 50th Annual Conference (p. 16p.). Montreal: Transportation Association of Canada (TAC). Retrieved from [https://trid.trb.org/view/1417784](https://trid.trb.org/view/1417784).

This script has been changed to include the search elements mentioned above (location and keywords related to public security). To run it, simply have the Tweepy library installed and run the following command at a terminal:

```
python twitter_scraper.py
```

Or open it in a Python IDE and run the script using one Python interpreter. Check the [Tweepy documentation](http://docs.tweepy.org/en/latest/) to understand how to install it in your Python environment.

After executing this script, an initial version of the corpus called _initial_tweets_base.json_ will be obtained, containing all fields of information for each tweet. To extract fields of interest and eliminate duplicates in textual records, the _tweets_initial_cleaning.py_ script must be executed in a terminal:

```
python tweets_initial_cleaning.py
```

Once this is done, the desired corpus version will be obtained.


### Tweets Corpus json file

The json file containing the tweets corpus with initial cleaning is called _tweets_corpus.json_.


## More information

This is currently a project in progress. In the future there will be a greater amount of news and tweets incorporated into the relevant corporations, as well as the intention to build a corpus dedicated to Facebook posts on the topic of Public Security. If you have some idea to colaborate and imporve the project, please contact the author on the emails provided bellow.


## Author

* **Victor Diogho Heuer de Carvalho**, Msc.

[victor.carvalho@delmiro.ufal.br](victor.carvalho@delmiro.ufal.br)

[victor.hcarvalho@ufpe.br](victor.hcarvalho@ufpe.br)

*Assistant Professor*

Campus do Sertão, Delmiro Gouveia - Alagoas

Universidade Federal de Alagoas (Brasil)

*Dsc. Candidate*

Graduate Program in Management Engineering, Recife - Pernambuco

Universidade Federal de Pernambuco (Brazil)


## Colaborators

* **Ana Paula Cabral Seixas Costa**, Dsc.

*Associate Professor*

Departamento de Engenharia de Produção, Recife - Pernambuco

Universidade Federal de Pernambuco (Brazil)


* **Thyago Celso Cavalcante Nepomuceno**, Dsc.

*Adjunct professor*

Centro Acadêmico do Agreste, Caruaru - Pernambuco

Universidade Federal de Pernambuco (Brazil)