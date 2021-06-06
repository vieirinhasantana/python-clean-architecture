# -*- coding: utf-8 -*-
from flask import jsonify
from src.domain.wallet import Wallets
from src.interface.usecase.wallet_usecase import WalletUsecase


class WalletResource:
    wallet_usecase: WalletUsecase

    def __init__(self, wallet_usecase: WalletUsecase):
        self.wallet_usecase = wallet_usecase

    def index(self):
        main_group: Wallets = self.wallet_usecase.get_list()
        return jsonify(wallet_response(main_group))


def wallet_response(wallets: Wallets) -> dict:
    return {
        "items": [{"id": wallet.id, "name": wallet.name} for wallet in wallets.values]
    }
