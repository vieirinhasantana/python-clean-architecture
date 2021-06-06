# -*- coding: utf-8 -*-

from flask import Flask
from src.driver.wallet_driver import WalletDriverImpl
from src.interactor.wallet_interactor import WalletInteractor
from src.repository.wallet_repository import WalletRepositoryImpl
from src.rest.wallet_resource import WalletResource

app = Flask(__name__)

wallet_resource = WalletResource(
    wallet_usecase=WalletInteractor(
        wallet_repository=WalletRepositoryImpl(wallet_driver=WalletDriverImpl())
    )
)

app.add_url_rule("/", view_func=wallet_resource.index)

app.run()

# with MongoDatabaseDriver(
#     host="localhost:27017",
#     database="application_database",
#     username="application_user",
#     password="application_pass",
# ) as mgo:
#     print(hex(id(mgo)))
