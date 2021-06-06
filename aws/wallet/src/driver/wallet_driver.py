# -*- coding: utf-8 -*-
from src.interface.driver.wallet_driver import WalletDriver


class WalletDriverImpl(WalletDriver):
    def get_wallets(self) -> dict:
        wallets = {
            "wallets": [{"id": 0, "name": "teste1"}, {"id": 1, "name": "teste2"}]
        }

        return wallets
