from abc import ABC
from enum import Enum


class CouponLog(ABC):
    def __init__(self, coupon, redeemed_time, redeemed_by):
        self.coupon = coupon
        self.redeemed_time = redeemed_time
        self.redeemed_by = redeemed_by
