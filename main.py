import json

jsonfile = "./data.json"


class DataStoreLibrary:

    def load_cars(id):
        with open(jsonfile, "r") as f:
            temp = json.load(f)
            for record in temp:
                if record['id'] == id:
                    name = record["name"]
                    model = record["model"]
                    year = record["year"]
                    Price = record["Price"]
                    print(name, model, year, Price)

    def add_car(id, name, model, year, Price):
        car_data = {}
        with open(jsonfile, "r") as f:
            temp = json.load(f)

        car_data["id"] = id
        car_data["name"] = name
        car_data["model"] = model
        car_data["year"] = year
        car_data["Price"] = Price

        temp.append(car_data)
        with open(jsonfile, "w") as f:
            json.dump(temp, f, indent=5)

    def delete_car(id):
        with open(jsonfile, "r") as f:
            temp = json.load(f)

        for record in temp:
            if record['id'] == id:
                temp.pop(id - 1)

        with open(jsonfile, "w") as f:
            json.dump(temp, f, indent=5)

    def update_car(id, name, model, year, Price):

        with open(jsonfile, "r") as f:
            temp = json.load(f)

        for record in temp:
            if record['id'] == id:
                record["name"] = name
                record["model"] = model
                record["year"] = year
                record["Price"] = Price

        with open(jsonfile, "w") as f:
            json.dump(temp, f, indent=5)


