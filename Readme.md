# Public Security Corpora

This is a project dedicated to the construction of a open corpora, a set of texts bodies, in Brazilian Portuguese dedicated to Public Security subjects. 

As an academic research output, in this phase it is intended to be composed by three parts:

1st - News Corpus, containing news texts about Public Security themes extracted from Newspapers websites;
2nd - Tweets Corpus, contining tweets;
3rd - Facebook Corpus, containing posts;

2nd and 3rd corpora also are intended to be composed by Public Security related content.

## News Corpus

In this phase, the News Corpus is composed by texts extracted only for the "Diário de Pernambuco" Newspaper website. The content was found using the site search mechanism with the query containing the portuguese terms: "segurança pública" + crim* + pernambuco. 

In its current structure, this corpus contain the following information from the news: title, publication date, author, text, url and content type (if the origin is a news article or the articles from a subpart of the Diario de Pernambuco Newspaper environment called "Blog do Diário" where can be found several texts exclusively dedicated to Public Security themes).

### News Corpus scraping

The news corpus scraping was based in two main technologies: Selenium Web Driver and Scrapy, bot used with Python Language.

Selenium Web Driver script (diario_scraping_search_results.py) scraped the initial results page and got the html code of the target elements. To start this script, is just call in a terminal:

'''
python diario_scraping_search_results.py
'''

Or open it in a Python IDE and run the script using one pytohn interpreter (iPython, for example). Check if Selenium Web Driver and if the Google Chrome driver are available in Python environment. If not, is necessary to install it. See [Selenium Web Driver documentation page for Python](https://selenium-python.readthedocs.io/installation.html).

Two spiders were created using the Scrapy framework for scraping the news articles from the links in the previously scraped html code, and the posts on the newspaper blog. To run them, is just use their names as was attributed in the scripts: "news" for the spider dedicated for the news articles and "posts" for the one dedicated to posts articles, using "-o json_file_name.json" to save the information they scraped in a specific json file.

'''
scrapy crawl "news" -o diario_seguranca_news.json
'''

and

'''
scrapy crawl "posts" -o blog-diario_seguranca_posts.json
'''

These calls will start the spider scripts named "spider_diario_news.py" and "spider_diario-blog-seg_posts.py".

Remember to check if Scrapy framework is available in Python environment. If not, is necessary to install it too. It is necessary to create a project and put both spiders scripts into the spiders subfolder. See [Scrapy documentation page](https://docs.scrapy.org/en/latest/intro/install.html).

After running these two spiders scripts according to the commands passed in the terminal, two json files will be created. They will need some data cleaning, according to the last script to be executed: data_cleaning.py.
Is just call it in a terminal:

'''
python data_cleaning.py
'''

Or open it in a Python IDE and execute it with the interpreter. Data cleaning script will create three new json files:

* news_full-corpus.json, containing all the news scraped and cleaned.
* news-diario_corpus, containing only the subset of texts from newspaper articles.
* blog-diario_corpus, containing only the subset of texts from "Blog do Diário" articles.

### News Corpus json files

The News Corpus, in its current stage, is stored in a json file called news_full-corpus.json.

## Tweets Corpus

Incoming.

## Facebook Corpus

Incoming.

## More information

This is currently a project in progress. If you have some idea to colaborate and imporve the project, please contact the author on the emails provided bellow.

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
