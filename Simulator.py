import assignClusters as ac
import numpy as np
import matplotlib.pyplot as plt
import classes as cl
import random
import showData as show

"""Simulation"""


num_listeners=100
num_bands=1000
xlimit=999
ylimit=999
songs_per_cluster=10
num_clusters=100



"""Generate random Bands with 1  song each"""
bands = []
for num in range(num_bands):
    bands.append(cl.Band(random.randint(1,xlimit),random.randint(1,ylimit),num))
    cl.Song(random.randint(1,100), bands[num])


all_songs = []
for b in bands:
    all_songs.append(b.songs[0])

"""Assign Clusters"""
small_centers={}
small_clusters={}
(large_centers, large_clusters)=ac.assign_clusters(all_songs,10)
for c in range(10):
    (small_centers[c],small_clusters[c])=ac.assign_clusters(large_clusters[c],10)

show.show_bands(small_centers,small_clusters,large_centers,large_clusters)



"""Generate Random Listeners"""
for j in range(100):
    l=cl.Listener(random.randint(0,xlimit),random.randint(0,ylimit),1)

    #print "Listener Location: " + str(l.x) + " " + str(l.y)
    plt.plot(l.x,l.y,"k+")
    for i in range(1000):
        current_song=ac.get_song(l,small_centers,small_clusters,large_centers,large_clusters,all_songs)
        current_song[0].play()
        #print "Song Choice is located at : " + str(current_song.my_band.x) + " " + str(current_song.my_band.y)
        #plt.plot(current_song.my_band.x,current_song.my_band.y,"ro",ms=5)
        #plt.show(block=False)
        #raw_input("Press Enter to continue...")
for s in enumerate(all_songs):
    plt.figure(2)
    #print str(s[0]) + ' ' + str(s[1])
    plt.plot(s[1].rating,s[1].num_plays,'o')
plt.figure(3)
for c in small_clusters:
    r1=random.random()
    r2=random.random()
    for i in small_clusters[c]:
        r3=random.random()
        num=len(small_clusters[c])*c + i
        for j in small_clusters[c][i]:
            plt.plot(num,j.num_plays,color=(r1,r2,r3),marker='o',ms=j.rating/4)
plt.show()
