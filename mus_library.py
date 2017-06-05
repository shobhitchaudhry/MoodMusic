"""
Handles everything related to music library
"""
from avl_tree import AVLTree
import os
import re
from tinytag import TinyTag
import sys

def build_library(music_folder, library):
    try:
        contents = os.listdir(music_folder)
    except Exception as e:
        print "EXCEPTION: {0}".format(e)
        print "Skipping directory: {0}".format(os.path.abspath(music_folder))
        return library

    for f in contents:
        content_path = os.path.join(music_folder, f)
        if re.search('.m4a', f) or re.search('.mp3', f):
            tag = None
            try:
                tag = TinyTag.get(os.path.join(music_folder, f))
                if tag.genre:
                    song = Song(tag.title.encode('utf-8'), tag.album.encode('utf-8'), tag.genre.lower().encode('utf-8'), content_path)
                    lib_genre = library.find_genre(song.genre)
                    if not lib_genre:
                        genre_obj = Genres(song.genre)
                        library.insert(genre_obj)
                        genre_obj.a_tree.insert(song)
                    else:
                        lib_genre.a_tree.insert(song)
                else:
                    pass
                # don't add songs that don't have a genre tag
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                print "EXCEPTION: {0}".format(e)
                print "Failed during file: {0}".format(content_path)
                print "Line no: ", exc_tb.tb_lineno

        elif os.path.isdir(content_path):
            build_library(content_path, library)

    return library

class Song():

    def __init__(self, name, album, genre, path):
        self.name = name
        self.album = album
        self.genre = genre
        self.path = path

class Genres():

    def __init__(self, genre):
        self.a_tree = AVLTree()
        self.name = genre

if __name__ == "__main__":
    music_folder = os.path.join("d:", "Music")
    library = AVLTree()
    library = build_library(music_folder, library)
    library.display()
