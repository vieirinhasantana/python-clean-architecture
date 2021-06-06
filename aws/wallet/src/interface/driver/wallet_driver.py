# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class WalletDriver(metaclass=ABCMeta):
    @abstractmethod
    async def get_wallets(self) -> dict:
        raise NotImplementedError
