import numpy as np
import classes
import random

def cluster_points(all_songs, mu):
    clusters  = {}
    for s in all_songs:
        bestmukey = min([(i[0], np.linalg.norm(s.my_band.loc-mu[i[0]])) \
                    for i in enumerate(mu)], key=lambda t:t[1])[0]
        try:
            clusters[bestmukey].append(s)
        except KeyError:
            clusters[bestmukey] = [s]
    return clusters

def reevaluate_centers(mu, clusters):
    newmu = []
    keys = sorted(clusters.keys())
    for k in keys:
        newmu.append(np.mean(list(np.array(s.my_band.loc) for s in clusters[k]), axis = 0))
    return newmu

def has_converged(mu, oldmu):
    return (set([tuple(a) for a in mu]) == set([tuple(a) for a in oldmu]))

def find_centers(all_songs, mu):
    """TODO: Take a list of Song objects instead of coordinates"""
    # Initialize to K random centers
    K=len(mu)
    oldmu = random.sample(list(np.array(s.my_band.loc) for s in all_songs),K)
    while not has_converged(mu, oldmu):
        oldmu = mu
        # Assign all points in X to clusters
        clusters = cluster_points(all_songs, mu)
        # Reevaluate centers
        mu = reevaluate_centers(oldmu, clusters)
    return(mu, clusters)
