# -*- coding: utf-8 -*-
from src.driver.mongodb import MongoDatabaseDriver

with MongoDatabaseDriver(
    host="localhost:27017",
    database="application_database",
    username="application_user",
    password="application_pass",
) as mgo:
    print("dada", mgo.test_ping())
