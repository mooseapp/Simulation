class Listener:
    """Represents one Listener"""
    def __init__(self, xpos, ypos, num):
        self.x = xpos
        self.y = ypos
        self.loc=(xpos, ypos)
        self.num = num
        self.songs=[]

class Band:
    """Represents one Band"""
    def __init__(self, xpos, ypos, num):
        self.x = xpos
        self.y = ypos
        self.loc = (xpos, ypos)
        self.num = num
        self.songs=[]

class Song:
    """Represents one Song"""
    def __init__(self, rating, my_band):
        self.rating = rating
        self.my_band = my_band
        self.num_plays=0
        my_band.songs.append(self)
    def __eq__(self, other):
        return self.my_band.loc == other.my_band.loc
    def play(self):
        self.num_plays=self.num_plays+1

    def distance(self,listener):
        return (((self.my_band.x - listener.x)**2 + (self.my_band.y - listener.y)**2)**0.5)/self.rating
        
    def __hash__(self): return hash(id(self))
    def __eq__(self, x): return x is self
    def __ne__(self, x): return x is not self

class Cluster:
    """Represents a cluster of an equal number of Songs of similar location"""
    def __init__(self,cluster_songs):
        self.cluster_songs = cluster_songs
