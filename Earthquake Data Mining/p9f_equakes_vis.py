'''                       p9f_equakes_vis.py
CIS 210: Winter 2019
Project 9: World-Wide Earthquake Watch

Author: Jarett Nishijo
Credits: Miller and Ranum Text

Plots earthquakes on a world map using K-means algorithm
'''
import random
from math import *
from turtle import *

def readFile(fname):
    '''(string) -> dictionary
    {Key: [latitude, longitude, magnitude]}

    returns a dictionary of earthquakes that are recorded in a file

    >>> readFile('equakes50f.txt')
    {1: [-125.815, 43.756, 5.2], 2: [-122.0086667, 42.2915, 5.1],
    3: [-122.0583333, 42.3575, 6.0], 4: [-122.0266667, 42.3161667, 5.9],
    5: [-122.6065, 45.0351667, 5.6], 6: [-122.188, 46.2073333, 5.7],
    7: [-122.182, 46.2026667, 5.0], 8: [-122.1825, 46.208, 5.0],
    9: [-122.1973333, 46.2035, 5.2], 10: [-122.1958333, 46.2098333, 5.1],
    11: [-125.603, 42.752, 5.4], 12: [-126.103, 43.687, 5.2],
    13: [-125.774, 44.98, 5.6]}

    >>> readFile('notafile')
    #Returns error for nonfiles.
    '''
    datafile = open(fname,'r')
    datadict = {}
    key = 0
    next(datafile)              #skips file header

    for line in datafile:
        item = line.split(',')  
        key += 1
        lat = float(item[1])
        lon = float(item[2])
        mag = float(item[4])
        datadict[key] = [lon,lat,mag]

    return datadict

def euclidD(point1,point2):
    '''(list,list) -> num

    Returns distance between 2 point on a cartesian graph
    using euclidean method

    >>> euclidD([0,0],[1,1])
    1.4142135623730951

    >>> euclidD([0,0],[-1,-1])    #Accepts negative points
    1.4142135623730951
    '''
    total = 0
    for index in range(len(point1)):
        diff = (point1[index] - point2[index]) ** 2
        total += diff

    euclidDistance = sqrt(total)
    
    return euclidDistance

def createCentroids(k,datadict):
    '''(int,dict) -> list

    returns k amount of centroids used for k-means algorithm

    >>> createCentroids(3,{1:1,2:2,3:3,4:4})
    [4, 2, 3]

    >>> createCentroids(1,{1:1,2:2,3:3,4:4})
    [1]
    '''
    centroids = []
    centroidct = 0
    centroidkeys = []

    while centroidct < k:
        rkey = random.randint(1,len(datadict))
        if rkey not in centroidkeys:
            centroids.append(datadict[rkey])
            centroidkeys.append(rkey)
            centroidct += 1

    return centroids

def createClusters(k,centroids,datadict,repeats):
    '''(int,list,dict,int) -> list

    returns clusters of numbers in dict based on k centroids
    ***For earthquake data only***

    #Example: Data for equakes50f.txt
    
    >>> createClusters(4,[[-122.0266667, 42.3161667, 5.9],
    [-122.1958333, 46.2098333, 5.1], [-126.103, 43.687, 5.2],
    [-122.0583333, 42.3575, 6.0]],{1: [-125.815, 43.756, 5.2],
    2: [-122.0086667, 42.2915, 5.1], 3: [-122.0583333, 42.3575, 6.0],
    4: [-122.0266667, 42.3161667, 5.9], 5: [-122.6065, 45.0351667, 5.6],
    6: [-122.188, 46.2073333, 5.7], 7: [-122.182, 46.2026667, 5.0],
    8: [-122.1825, 46.208, 5.0], 9: [-122.1973333, 46.2035, 5.2],
    10: [-122.1958333, 46.2098333, 5.1], 11: [-125.603, 42.752, 5.4],
    12: [-126.103, 43.687, 5.2], 13: [-125.774, 44.98, 5.6]},10)
    
    [[2], [5, 6, 7, 8, 9, 10], [1, 11, 12, 13], [3, 4]]
    '''
    for apass in range(repeats):
        #print("****PASS",apass,"****")
        clusters = []
        for i in range(k):
            clusters.append([])

        for akey in datadict:   #distances of points from centroid
            distances = []
            for clusterIndex in range(k):
                dist = euclidD(datadict[akey],centroids[clusterIndex])
                distances.append(dist)

            mindist = min(distances)
            index = distances.index(mindist)

            clusters[index].append(akey)

        dimensions = len(datadict[1])
        for clusterIndex in range(k):   #creates clusters for every centroid
            sums = [0] * dimensions
            for akey in clusters[clusterIndex]:
                datapoints = datadict[akey]
                for ind in range(len(datapoints)):
                    sums[ind] = sums[ind] + datapoints[ind]
            for ind in range(len(sums)):
                clusterlen = len(clusters[clusterIndex])
                if clusterlen != 0:
                    sums[ind] = sums[ind] / clusterlen

            centroids[clusterIndex] = sums
        '''
        for c in clusters:
            print("Cluster")
            for key in c:
                print(datadict[key],end=" ")
            print()
        '''
    return clusters

def eqDraw(k,eqDict,eqClusters):
    '''(int,dict,list) -> None

    plots earthquakes on world map.
    Dot size on map is based on magnitude of earthquake

    #Example: Data from equakes50f.txt
    
    >>> eqDraw(4,{1: [-125.815, 43.756, 5.2],
    2: [-122.0086667, 42.2915, 5.1], 3: [-122.0583333, 42.3575, 6.0],
    4: [-122.0266667, 42.3161667, 5.9], 5: [-122.6065, 45.0351667, 5.6],
    6: [-122.188, 46.2073333, 5.7], 7: [-122.182, 46.2026667, 5.0],
    8: [-122.1825, 46.208, 5.0], 9: [-122.1973333, 46.2035, 5.2],
    10: [-122.1958333, 46.2098333, 5.1], 11: [-125.603, 42.752, 5.4],
    12: [-126.103, 43.687, 5.2], 13:
    [-125.774, 44.98, 5.6]},[[2], [5, 6, 7, 8, 9, 10],
    [1, 11, 12, 13], [3, 4]])

    *Turtle graphics*
    '''
    speed(0)
    screensize(canvwidth=1800, canvheight=900)
    bgpic('worldmap1800_900.gif')
    colorlist = ["red","green","blue","orange","cyan","yellow"]
    hideturtle()
    quakewin = Screen()
    wFactor = (quakewin.screensize()[0]/2)/180  #Scales points to the 1800x900 screensize
    hFactor = (quakewin.screensize()[1]/2)/90
    
    for clusterIndex in range(k):
        color(colorlist[clusterIndex])
        for akey in eqClusters[clusterIndex]:
            penup()
            lon = eqDict[akey][0]
            lat = eqDict[akey][1]
            mag = eqDict[akey][2]
            setpos(lon*wFactor,lat*hFactor)
            dot(1.5**mag)
    
    return None

def visualizeQuakes(k,r,dataFile):
    '''(int,int,string) -> None

    Plots earthquakes on world map.
    ***Similar to eqDraw but shorter parameters***

    >>> visualizeQuakes(4,10,'equakes50f.txt')
    *Turtle Graphics*
    '''
    
    datadict = readFile(dataFile)
    centroids = createCentroids(k,datadict)
    clusters = createClusters(k,centroids,datadict,r)
    eqDraw(k,datadict,clusters)

    return None

def main():
    '''() -> None

    Main function that tests visualizeQuakes

    >>> main()
    *Turtle Graphics*
    '''
    k = 4
    r = 10
    datafile = 'earthquakes.csv'

    visualizeQuakes(k,r,datafile)

    return None
main()
