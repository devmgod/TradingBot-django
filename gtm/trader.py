from .binance_api_manager import Binance_API_Manager
from .strategies.v1_strategies import V1Strategies
from .test_trader import TestTrader
from .strategies.helper import writeFile
from .logger import Logger
from .notifications import NotificationHandler

from pandas.core.common import SettingWithCopyWarning
import time
import warnings


logger = Logger("trader")
nh = NotificationHandler()


class Trader:
    def __init__(self, binance_manager: Binance_API_Manager):
        self.manager = binance_manager

    def startTrade(self):

        v1strategies = V1Strategies(self.manager, "BTTUSDT")

        warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

        try:

            trader = TestTrader("BTTUSDT")

            while True:

                ch3_df = v1strategies.ch3mGetSignal()

                trader.trade(ch3_df)

                trader.calculate_profit()

                writeFile("\n= = = = = = = = = = = = = = = = = = = =\n")
                
                time.sleep(10)

        except Exception as e:
            logger.error(e)