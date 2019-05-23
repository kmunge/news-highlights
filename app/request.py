import urllib.request,json
from .model import Source,Article


# Getting api key
api_key = '0af32b93a8c54362886057dd4a2f1089'

#Getting the news base url
base_url = None
articles_url = None
search_url = None

def configure_request(app):
    global api_key,base_url, articles_url, search_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config["NEWS_API_BASE_URL"]
    articles_url = app.config["ARTICLES_BASE_URL"]
    search_url = app.config["SEARCH_URL"]


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results



def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects
    Args:
        source_list: A list of dictionaries that contain the source details
    Returns :
        source_results: A list of source objects
    '''
    source_results = []

    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        category = source_item.get('category')
        country = source_item.get('country')
        url = source_item.get('url')

        if url:
            source_object = Source(id, name, description, category, country, url)
            source_results.append(source_object)

    return source_results


def get_articles(id):
    '''
    Function that gets the articles data for each id
    '''
    get_article_url = articles_url.format(id,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results


def process_articles(articles_list):
    '''
    Function  that processes the articles results and transform them to a list of Objects
    Args:
        articles_list: A list of dictionaries that contain the articles details
    Returns :
        articles_results: A list of articles objects
    '''
    articles_results= []
    
    for article_item in articles_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        url = article_item.get('url')

        author, title, description, urlToImage, publishedAt,url

        if urlToImage:
            articles_object = Article(author, title, description, urlToImage, publishedAt,url)
            articles_results.append(articles_object)   
    return articles_results

def search_source(source_name):
    '''
    Function that looks for articles based on their sources
    '''
    search_source_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(api_key,source_name)  
    with urllib.request.urlopen(search_source_url) as url:
        search_source_data = url.read()
        search_source_response = json.loads(search_source_data)

        search_source_results=[]

        if search_source_response['sources']:
            search_source_list = search_source_response['sources']
            search_source_results = process_results(search_source_list)


    return search_source_results