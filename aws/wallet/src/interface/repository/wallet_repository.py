from abc import ABCMeta, abstractmethod

from src.domain.wallet import Wallets


class WalletRepository(metaclass=ABCMeta):
    @abstractmethod
    async def get_list(self) -> Wallets:
        raise NotImplementedError