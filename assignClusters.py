import kmeans as km
import numpy as np
import classes
import random
import matplotlib.pyplot as plt

def assign_clusters(all_songs,mu):
    """Run K-means clustering"""
    K=mu
    # X = np.array([(s.my_band.x, s.my_band.y) for s in all_songs])
    mu=random.sample(list(np.array(s.my_band.loc) for s in all_songs),K)
    # try:
    #     mu = int(mu)
    #     K=mu
    #
    #     print str(mu)
    # except:
    #     pass
    (centers, clusters)=km.find_centers(all_songs,mu)
    return(centers, clusters)


def get_song(listener,small_centers,small_clusters, large_centers,large_clusters,all_songs):
    """Return a randomly selected song for the specific listener"""
    """Sort clusters with respect to listener"""
    cluster_large_sorted_keys = sorted([(i[0], np.linalg.norm(listener.loc-large_centers[i[0]])) \
                for i in enumerate(large_centers)], key=lambda t:t[1])
    closest_large_cluster_key=cluster_large_sorted_keys[0]
    clc=closest_large_cluster_key[0]
    cluster_small_sorted_keys = sorted([(i[0], np.linalg.norm(listener.loc-small_centers[clc][i[0]])) \
                for i in enumerate(small_centers[clc])], key=lambda t:t[1])

    """Choose songs randomly for listener"""
    """Current Algorithm:
    Out of the 10 Clusters:
     20% of songs will be from the 3 closest small clusters
     15% from the next 6 closest clusters with a rating over 20
     15% from the other clusters within the large cluster with a rating over 40
     20% from the closest 3 large clusters with a rating over 60
     20% from the closest 6 large clusters with rating over 80
     10% from all songs with a rating over 90"""
    r=random.randint(1,100)
    eligible_songs=set()
    if r<=20 :
        for j in range(3):
            eligible_songs.update(small_clusters[clc][cluster_small_sorted_keys[j][0]])
    elif r<=35 :
        for j in range(6):
            eligible_songs.update([elem for elem in small_clusters[clc][cluster_small_sorted_keys[j][0]] if elem.rating>20])
    elif r<=50 :
        eligible_songs.update([elem for elem in large_clusters[cluster_large_sorted_keys[0][0]] if elem.rating>40])
    elif r<= 70:
        for j in range(3):
            eligible_songs.update([elem for elem in large_clusters[cluster_large_sorted_keys[j][0]] if elem.rating>60])
    elif r<=90:
        for j in range(6):
            eligible_songs.update([elem for elem in large_clusters[cluster_large_sorted_keys[j][0]] if elem.rating>80])
    else :
     eligible_songs.update([elem for elem in all_songs if elem.rating>90])
    return(random.sample(eligible_songs,1))
