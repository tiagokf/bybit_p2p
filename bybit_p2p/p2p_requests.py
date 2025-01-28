from ._p2p_manager import P2PManager
from ._p2p_helper import P2PMethods


class P2PRequests(P2PManager):
    def get_current_balance(self, **kwargs):
        """
        Obtain wallet balance, query asset information of each currency. By default, currency information with assets or liabilities of 0 is not returned.

        :key accountType: Account type, UNIFIED
        :returns: Response dictionary
        """

        return self.http_req_handler(
            method=P2PMethods.GET_CURRENT_BALANCE,
            params=kwargs
        )

    def get_account_information(self, **kwargs):
        """
        Get Account Information

        :return: Response dictionary
        """

        return self.http_req_handler(
            method=P2PMethods.GET_ACCOUNT_INFORMATION,
            params=kwargs
        )

    def get_ads_list(self, **kwargs):
        """
        Get Ads List

        :key itemId: Advertisement ID
        :key status: 1 - Sold out, 2 - Available
        :key side: 0 - Buy, 1 - Sell
        :key tokenId: Token ID, e.g.: USDT,BTC,ETH
        :key page: Page number, default is 1
        :key size: Page size, default is 10
        :key currency_id: Currency ID, e.g.: HKD,USD,EUR
        :return: Response dictionary
        """

        return self.http_req_handler(
            method=P2PMethods.GET_ADS_LIST,
            params=kwargs
        )

    def get_ad_detail(self, **kwargs):
        """
        Get Ad Detail

        :key itemId: Advertisement ID
        :return: Response dictionary
        """

        return self.http_req_handler(
            method=P2PMethods.GET_AD_DETAIL,
            params=kwargs
        )
