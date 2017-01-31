import classes
import matplotlib.pyplot as plt
import random

def show_bands(small_centers,small_clusters,large_centers,large_clusters):
    for c in small_clusters:
        r1=random.random()
        r2=random.random()
        plt.plot(large_centers[c][0],large_centers[c][1],color=(r1,r2,0),marker='*',ms=15)
        for i in small_clusters[c]:
            r3=random.random()
            plt.plot(small_centers[c][i][0],small_centers[c][i][1],color=(r1,r2,r3),marker='*',ms=10)
            for j in small_clusters[c][i]:
                plt.plot(j.my_band.x,j.my_band.y,color=(r1,r2,r3),marker='o',ms=j.rating/4)
