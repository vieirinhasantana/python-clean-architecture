# -*- coding: utf-8 -*-
from src.domain.wallet import Wallets
from src.interface.repository.wallet_repository import WalletRepository
from src.interface.usecase.wallet_usecase import WalletUsecase


class WalletInteractor(WalletUsecase):
    wallet_repository: WalletRepository

    def __init__(self, wallet_repository: WalletRepository):
        self.wallet_repository = wallet_repository

    def get_list(self) -> Wallets:
        return self.wallet_repository.get_list()
