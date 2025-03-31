from flask import Flask,request,jsonify



app=Flask("__name__")

items=[
    
    {
    "id":1,
    "name":"item-1",
    "descrption":"this item-1 descrption"
    },
    {
    "id":2,
    "name":"item-2",
    "descrption":"this item-2 descrption"
    }


    ]

@app.route("/")
def home():
    return "this is home page"


@app.route("/items",methods=["GET"])
def itemsprint():
    return jsonify(items)


@app.route("/items/<int:item_id>",methods=["GET"])
def retrive_one(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"there is no that id in this items"})
    return jsonify(item)
    
    
### CREATE A NEW TASK

@app.route("/items",methods=['POST'])
def new():
    if not request.json or not "name" in request.json:
        return jsonify({"error":"this not valid "})
    new_item={
        "id":items[-1]['id']+1,
        "name":request.json['name'],
        "descrption":request.json["descrption"]
        
    }
    items.append(new_item)
    return jsonify(new_item)



### update particular item
@app.route("/items/<int:item_id>",methods=["PUT"])
def update(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"item is not found to update"})
    item["name"]=request.json.get("name",item["name"])
    item['descrption']=request.json.get("descrption",item["descrption"])
    return(item)

##delete item

@app.route('/items/<int:item_id>',methods=["DELETE"])
def delete(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result": "Item deleted"})
        
    



if __name__=="__main__":
    app.run(debug=True)