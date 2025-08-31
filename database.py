# This file contains the classes that handle looking up Bible data

class word:
    def __init__(self, greek, english, strongs):
        self.greek = greek
        self.english = english
        self.strongs = strongs
    
# class word


class verse:
    def __init__(self):
        self.words = {}
        self.num_words = 0

# class verse


class chapter:
    def __init__(self):
        self.verses = {}
        self.num_verses = 0

# class chapter


class book:
    def __init__(self):
        self.chapters = {}
        self.num_chapters = 0

# class book


class database:
    def __init__(self):
        self.books = {}

# class database

# Either constructs the database from csvs or unpickles it
def initialize():
    return "Not done"