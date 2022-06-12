import json
import xml.etree.cElementTree as ET

root = ET.Element("root")

jsonfile = "./data.json"

with open(jsonfile, "r") as f:
    temp = json.load(f)

for i in temp:
    ET.SubElement(root, "name").text = i["name"]
    ET.SubElement(root, "model").text = i["model"]
    ET.SubElement(root, "year").text = i["year"]
    ET.SubElement(root, "price").text = str(i["Price"])


tree = ET.ElementTree(root)
tree.write("cars.xml")