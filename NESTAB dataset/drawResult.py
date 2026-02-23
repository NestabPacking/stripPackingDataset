from drawUtils import *
import os ,copy ,json

MaxStableSets = [9,20,41]
MaxStableSets = [1,35,51]
datasetname = 'three'
cut = 0


dir_path = os.path.dirname(os.path.realpath(__file__))
datasetpath = dir_path+'\\'+datasetname+'\\cut_'+str(cut)+'\\'
infpfile = datasetpath+'nfp-infp.json'
pointcoordfile = datasetpath+'pointCoordinate.txt'
layermapfile = datasetpath+'LayerPoly.txt'


with open(infpfile) as file:
    polygons = json.load(file)


pos = {}
posfullOriginal = {}


# Read line by line
print("reading point coordinate..")
with open(pointcoordfile, 'r') as file:
    for line in file:
        if line[0] =='#':
            continue
        else:
            line = line.strip()
            s = line.split(' ')
            pos[int(s[3])]={"x":float(s[1]),"y":float(s[2]),"Layer":int(s[0])}

layermap = {}
with open(layermapfile, 'r') as file:
    lines = file.readlines()
print("reading layer map...")
for line in lines:
    if line[0] =='#':
            continue
    else:
        line = line.strip()
        s = line.split('\t')
        layermap[int(s[0])] = s[1]

polygonsdraws = []
for p in MaxStableSets:
    polyPos = pos[p]
    poly_id= layermap[polyPos["Layer"]]
    
    polygon = polygons[poly_id]['VERTICES']
    refpoint = polygon[0]
    print("layer: ",layermap[polyPos["Layer"]],"polygon: ",polygon)
    thispolyList = []
    for v in polygon:
        vx = v['x'] - refpoint['x'] + polyPos['x']
        vy = v['y'] - refpoint['y'] + polyPos['y']
        thispolyList.append((vx,vy))
    print(thispolyList)
    polygonsdraws.append(thispolyList)

bins = copy.deepcopy(polygons['rect'])
del polygons['rect']

binpieces = []
binlayer = []
for v in bins:
    binlayer.append((v['x'],v['y']))
binpieces.append(binlayer)

print("drawing graph..")
drawPolygons(polygonsdraws,'polygons',1,'purple')
drawPolygons(binpieces,'board',2,'green')


ax = plt.gca()
ax.xaxis.set_minor_locator(plt.MultipleLocator(1))  # Minor ticks every 0.1
plt.grid(True, linestyle='--', alpha=0.7)
plt.grid(True, which='minor', linestyle=':', alpha=0.4)
plt.legend()
plt.axis('equal')
plt.show()
#import code
#code.interact(local=locals())

