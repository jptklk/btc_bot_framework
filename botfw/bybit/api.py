import ccxt
from ..base.api import ApiBase


class BybitApi(ApiBase, ccxt.bybit):
    _ccxt_class = ccxt.bybit

    def __init__(self, ccxt_config={}):
        ApiBase.__init__(self)
        ccxt.bybit.__init__(self, ccxt_config)
        self.load_markets()
