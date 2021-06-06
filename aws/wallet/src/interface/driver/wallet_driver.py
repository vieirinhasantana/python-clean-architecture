# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class WalletDriver(metaclass=ABCMeta):
    @abstractmethod
    def get_wallets(self) -> dict:
        raise NotImplementedError
