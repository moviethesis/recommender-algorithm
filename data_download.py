from zipfile import ZipFile
import json
import os.path
import pandas as pd

def fetch_data():
    # fetch data if not exists
    if os.path.isfile('./data/ml-25m.zip'):
        print("MovieLens 25M Dataset is downloaded!")
    else:
        print("MovieLens 25M Dataset not found. Starting download...")
        os.system("wget http://files.grouplens.org/datasets/movielens/ml-25m.zip")
        os.system("mv ml-25m.zip data/")
        print("MovieLens 25M Dataset downloaded!")

    if os.path.isfile('./data/ml-latest-small.zip'):
        print("MovieLens Latest Small Dataset is downloaded!")
    else:
        print("MovieLens Latest Small Dataset not found. Starting download...")
        os.system("wget http://files.grouplens.org/datasets/movielens/ml-latest-small.zip")
        os.system("mv ml-latest-small.zip data/")
        print("MovieLens Latest Small Dataset downloaded!")
        
def extract_data():
    if os.path.isfile('./data/ml-25m/movies.csv'):
        print("MovieLens 25M Dataset is already extracted!")
    elif os.path.isfile('data/ml-25m.zip'):
        print("Zip file found. Starting extract...")
        with ZipFile('data/ml-25m.zip', 'r') as zipObj:
            zipObj.extractall("./data/")
        print("Files extracted!")
        
    if os.path.isfile('./data/ml-latest-small/movies.csv'):
        print("MovieLens Latest Small Dataset is already extracted!")
    elif os.path.isfile('data/ml-latest-small.zip'):
        print("Zip file found. Starting extract...")
        with ZipFile('data/ml-latest-small.zip', 'r') as zipObj:
            zipObj.extractall("./data/")
        print("Files extracted!")
    
def internal_prepare_for_load():
    fetch_data()
    extract_data()
    
def load_unprocessed_df(use_large):
    internal_prepare_for_load()
    if use_large:
        movies = pd.read_csv('./data/ml-25m/movies.csv')
        links = pd.read_csv('./data/ml-25m/links.csv')
        ratings = pd.read_csv('./data/ml-25m/ratings.csv')
        tags = pd.read_csv('./data/ml-25m/tags.csv')
        genome_tags = pd.read_csv('./data/ml-25m/genome-tags.csv')
        genome_scores = pd.read_csv('./data/ml-25m/genome-scores.csv')
        return movies, links, ratings, tags, genome_tags, genome_scores
    else:
        movies = pd.read_csv('./data/ml-latest-small/movies.csv')
        links = pd.read_csv('./data/ml-latest-small/links.csv')
        ratings = pd.read_csv('./data/ml-latest-small/ratings.csv')
        tags = pd.read_csv('./data/ml-latest-small/tags.csv')
        return movies, links, ratings, tags, [], []
