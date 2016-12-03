#!/usr/bin/python
import sys
from utilities import *

def getAllData(cityList):
    gmapsDist = readGoogleAPI()
    allData = dict()
    for city1 in cityList:
        allData[city1] = dict()
        print city1
        dists = dict()
        times = dict()
        for city2 in cityList:
            d =  gmapsDist.distance_matrix(city1, city2, mode='transit', units='metric')
            if d['rows'][0]['elements'][0]['status'] == 'OK':
                dists[city2] = d['rows'][0]['elements'][0]['distance']['value']
                times[city2] = d['rows'][0]['elements'][0]['duration']['value']
        allData[city1]['distances'] = dists
        allData[city1]['durations'] = times
    return allData

def main():
    if len(sys.argv) < 3:
        print "WRONG!!!"
        exit()
    citiesFilename = sys.argv[1]
    finalDataFilename = sys.argv[2]

    cityList = readYamlData(citiesFilename)['cities']
    finalData = getAllData(cityList)
    writeYamlData(finalData, finalDataFilename)

if __name__ == "__main__":
    main()
