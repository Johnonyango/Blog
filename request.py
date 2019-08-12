from app import app
import urllib.request, json
from .models import movie
Movie = movie.Movie

# Getting api key
api_key = app.config['QUOTE_API_BASE_URL']

base_url = app.config["QUOTE_API_BASE_URL"]

def get_quotes(category):
    """
    function that gets the json response to our url request
    """
    get_quotes_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quote_results = None

        if get_quotes_response['results']:
            quote_results_list = get_quotes_response['results']

            quotes_results = process_results(quote_results_list)

    return quote_results

def process_results(quote_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    quote_results = []
    for quote_item in quote_list:
        id = quote_item.get('id')
        title = quote_item.get('original_title')
        
        if poster:
            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
            movie_results.append(movie_object)

    return movie_results


def get_movie(id):
    get_movie_details_url = base_url.format(id,api_key)
    with urllib.request.urlopen(get_movie_details_url) as url:

        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)
        
        movie_object = None
        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')

            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)

    return movie_object

def search_movie(movie_name):
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)
    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)

        search_movie_results = None
        if search_movie_response['results']:
            search_movie_results = process_results(search_movie_list)
    
    return search_movie_results


