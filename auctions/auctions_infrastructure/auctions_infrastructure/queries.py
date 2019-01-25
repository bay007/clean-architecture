from abc import abstractmethod

from dataclasses import dataclass
from typing import List

from auctions.domain.types import AuctionId
from auctions_infrastructure.models import (
    Auction,
    Bid,
)


class GetAuctionDetails:

    @dataclass
    class Dto:
        auction: Auction
        bids: List[Bid]

    @abstractmethod
    def query(self, auction_id: AuctionId) -> 'Dto':
        pass


class GetAuctionDetailsDjangoOrm(GetAuctionDetails):

    def query(self, auction_id: AuctionId) -> GetAuctionDetails.Dto:
        auction = Auction.objects.get(pk=auction_id)
        bids = Bid.objects.filter(
            auction_id=auction_id
        ).select_related('bidder').order_by('-amount')[:3]
        return self.Dto(auction, bids)