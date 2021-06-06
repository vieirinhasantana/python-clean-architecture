# -*- coding: utf-8 -*-
from src.domain.wallet import Wallet, Wallets
from src.interface.driver.wallet_driver import WalletDriver
from src.interface.repository.wallet_repository import WalletRepository


class WalletRepositoryImpl(WalletRepository):
    wallet_driver: WalletDriver

    def __init__(self, wallet_driver: WalletDriver):
        self.wallet_driver = wallet_driver

    def get_list(self) -> Wallets:
        res = self.wallet_driver.get_wallets()
        return Wallets(
            values=[Wallet(id=a["id"], name=a["name"]) for a in res["wallets"]]
        )
