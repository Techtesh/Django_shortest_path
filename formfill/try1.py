# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 09:29:39 2020

@author: Hitesh
"""
from geopy import distance
import json
from geopy.geocoders import Nominatim
from sys import maxsize 
from itertools import permutations
app = Nominatim(user_agent="tutorial")

def get_location_by_address(address):
        #time.sleep(1)
        try:
            return app.geocode(address).raw
        except:
            return get_location_by_address(address)

def location_finder(l1):
    #print("working on",l1)   
    location = get_location_by_address(l1)
    latitude = location["lat"]
    longitude = location["lon"]
    return(longitude,latitude)

newdata=[]
newdata2=[]

def pathfinder(data):
     print(data)   
     #print(len(data))
     for i in range (0,len(data)):
         currdata=[]
         for j in range(0,len(data)):
             temp1=list(data[i][2])
             temp2=list(data[j][2])
             temp1[0]=eval(temp1[0])
             temp1[1]=eval(temp1[1])
             temp2[0]=eval(temp2[0])
             temp2[1]=eval(temp2[1])
             d=distance.distance(temp1,temp2).km
             #print(temp1,temp2,d)
             temp3=data[i][0]
             temp4=data[j][0]
             #print(temp3,temp4,d)
             currdata.append(d)
             newdata.append((temp3,temp4,d))
         newdata2.append(currdata)
     #print(newdata)
     #print("#"*25)
     #print(newdata2)
     return newdata2
 
def travellingSalesmanProblem(graph, s=0): 
    c=0
    # store all vertex apart from source vertex 
    vertex = [] 
    for i in range(V): 
        if i != s: 
            vertex.append(i) 
    
    # store minimum weight Hamiltonian Cycle 
    min_path = maxsize 
    next_permutation=permutations(vertex)
    for i in next_permutation:
        #print(i)
        # store current Path weight(cost) 
        current_pathweight = 0
 
        # compute current path weight 
        k = s 
        for j in i: 
            current_pathweight += graph[k][j] 
            k = j 
        current_pathweight += graph[k][s] 
 
        # update minimum 
        if min_path<current_pathweight:
            c=i
        min_path = min(min_path, current_pathweight) 
    #print(type(c))
    
    
    return c 





def codegen(cities):
    global V
    V=len(cities)
    vals=[]
    data=[]
    for index,city in enumerate(cities):
        val=location_finder(city)
        #print(vals)
        vals.append([eval(val[0]),eval(val[1])])
        print(index,city,val)
        data.append([index,city,val])
    #print(data)
    print(vals)   
    
    newdata2=pathfinder(data)
    #print(newdata2)
    V=len(newdata2)
    ranks=travellingSalesmanProblem(newdata2)
    ranks=travellingSalesmanProblem(newdata2)
    #ranks[-1],ranks[-2]=ranks[-2],ranks[-1]
    #print(ranks)
    output=[]
    print(cities[0]+"->")
    
    output.append(vals[0])
    try:
        for r in ranks:
            print(cities[r]+"->")
            output.append(vals[r])
        #for india one
        """
        t=output[-1]
        output[-1]=output[-2]
        output[-2]=t"""
        #for europe1
        """
        t=output[0]
        output=output[1:]
        output.append(t)"""
    except:
        pass
    vals=sorted(vals,key =lambda x:x[0])
    #vals.append(vals[0])
    
    
    featuresop=[]
    
    geometry={
              "type":"LineString"
              ,"coordinates":[]
              }
    geometry["coordinates"]=output
    
    features1={
                    "type":"Feature",
                    "properties":{},
                    "geometry":geometry
                }
    for val in vals:
        geometry2={
                "type": "Point",
                "coordinates":[] 
                }
        geometry2["coordinates"]=val
        features2={
                        "type": "Feature",
                        "properties": {},
                        "geometry":  geometry2     }
        featuresop.append(features2)
        
    opdata={
            "type":"FeatureCollection",
            "features":[
            
                   
                ]
     
     }
    for feature in featuresop:
        opdata["features"].append(feature)
    opdata["features"].append(features1)
    geofile='J:\data2\pytrip\static\css\map_project\data.geojson'
    with open(geofile, 'w') as outfile:
        json.dump(opdata, outfile)




if __name__=="__main__":
    n=int(input("enter no of stops"))
    print("enter steps")
    cities=[]
    for _ in range(0,n):
        #cities.append(input())
        pass
    cities=["istanbul","rome","paris","london","madrid"]
    print(cities)
    codegen(cities)
    #
    V=len(cities)