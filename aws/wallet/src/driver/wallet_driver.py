from src.interface.driver.wallet_driver import WalletDriver


class WalletDriverImpl(WalletDriver):

    async def get_wallets(self) -> dict:
        pass