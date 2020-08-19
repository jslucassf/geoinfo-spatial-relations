import json


query = "INSERT INTO 'drawings' VALUES"

#drawings = open("drawings_2.json", "r")
with open('drawings_2.json') as json_file:
    data = json.load(json_file)
    for line in data:
        geometry = '{{ "type": "{}",  "coordinates":['.format(line["geometry"]["type"])
        if(line["geometry"]["type"]=="MultiPolygon"):
            geometry+="["
        for poly in line["geometry"]["coordinates"]:
            geometry += "["
            for coord in poly:
                geometry += ("[{}, {}],".format(coord["lng"], coord["lat"]))
            geometry = geometry[:-1] + "],"
        geometry = geometry[:-1] + "]" 
        if(line["geometry"]["type"]=="MultiPolygon"):
            geometry+="]}"
        else:
            geometry+="}"
         
        query += ("\n('{}','{}','{}','{}','{}','{}'),".format(line["_id"]["$oid"], line["userID"], line["relation"], line["landmark"], line["geometry"]["type"], geometry.replace('"', "''")))

    query = query[:-1]
    query += ";"
    
    query_file = open("json_query.json", "a")

    query_file.write(query)
    query_file.close()
