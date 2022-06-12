load_cars(id) - function
========================

Used to call information from JSON file. Originally configured to give an id (int argument) to call a specific record
from data store. It can be easily configured to behave in different ways. Instead of searching by id, we can search
by any argument: name, model, year and price. Or we can leave it without arguments and without conditional statement
to gather all the records from JSON file.


delete_cars(id) - function
==========================

Used to delete records from JSON file. Originally configured to give an id (int argument) to delete a specific record
from data store. It can be easily configured to behave in different ways. Instead of delete by id, we can delete
by any argument: name, model, year and price.


add_car(id, name, model, year, Price) - function
================================================

Used to add records in JSON file. We have to pass all the arguments in order to add a new record in a proper way.
It can be used in different ways. When you call it, you can add just one record, or create another method to add a
lot of records from other sources such as lists etc.


update_car(id, name, model, year, Price) - function
===================================================

Used to update records in JSON file. Originally, we have to pass all the arguments in order to update an existing
record in a proper way. But you can choose on your needs to pass only the arguments that you want, in case you need to
update specific data on a specific record. When you call it, you can update one record, by firstly searching by ID
and then update all the desired data.


json_to_xml.py
==============

In case you don't need to work with a JSON file, you use the instructions that are inside this code, to convert all
the data, from JSON format to an XML one.
