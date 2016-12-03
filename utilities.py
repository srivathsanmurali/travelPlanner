import yaml
import googlemaps

def readGoogleAPI(geoCode=False):
    keys = readYamlData('key.yaml')
    if not geoCode:
        gmaps = googlemaps.Client(key=keys['distances'])
    else:
        gmaps = googlemaps.Client(key=keys['geoCode'])
    return gmaps

def readYamlData(filename):
    with open(filename,'r') as f:
        t = yaml.load(f)
    if t == None:
        print  "cant read file"
        exit()
    return t

def writeYamlData(data, filename):
    with open(filename, 'w') as f:
       t = yaml.dump(data, f)

