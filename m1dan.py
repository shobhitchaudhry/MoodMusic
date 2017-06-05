import os
import re
from tinytag import TinyTag
import pyglet
from pyglet.gl import *
from pyglet.window import key
import sys
from mus_library import *

window = pyglet.window.Window()
player = pyglet.media.Player()

def blues():
    print "Playing Blues.\n"

def rock():
    print "Playing Rock.\n"

options = {0 : blues,
                1 : blues,
                2 : blues,
                3 : rock,
}


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print 'Exiting'
        sys.exit()
    elif symbol == key.LEFT:
        print 'Previous track'
        player.pause()
    elif symbol == key.RIGHT:
        print 'Next track'
        player.next_source()
    elif symbol == key.SPACE:
        if player.playing:
            player.pause()
            print 'Paused'
        else:
            player.play()
            print 'Playing'


@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0)
    glVertex2f(window.width, 0)
    glVertex2f(window.width, window.height)
    glEnd()

def main():
    mus_files = []
    music_folder = os.path.join("d:", "Downloads", "Music")
    library = AVLTree()
    library = build_library(music_folder, library)
    library.display()

    genres = library.inorder_traverse()

    #print sys.argv[1] (to pass args without prompt)
    print "0-Nervous, 1-Calm, 2-Anxious"
    moodnumber = raw_input('Enter a Mood NUMBER: ')
    print "Hello ", moodnumber
    options[int(moodnumber)]()
    bluesobject = library.find_genre("rock")
    bluesobject.a_tree.display()
    songs = bluesobject.a_tree.inorder_traverse()
    for song in songs:
        play = pyglet.media.load(song.path)
        player.queue(play)
    player.play()
    pyglet.app.run()

    #blues- nervous, anxious, calm
    #rock-other numbers ...



if __name__ == "__main__":
    main()
