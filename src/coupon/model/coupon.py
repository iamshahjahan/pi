from abc import ABC
from enum import Enum


class CouponType(Enum):
    GLOBAL, INDIVIDUAL = 1, 2


class Coupon(ABC):
    def __init__(self, coupon_type: CouponType, count, expires):
        self.coupon_type = coupon_type
        self.count = count
        self.expires = expires

    def __repr__(self):
        return f"{self.coupon_type, self.count, self.expires}"


class GlobalCoupon(Coupon):
    def __init__(self, coupon_type: CouponType, count, expires):
        super(GlobalCoupon, self).__init__(coupon_type, count, expires)


class UserCoupon(Coupon):
    def __init__(self, coupon_type: CouponType, userid, count, expires):
        super(UserCoupon, self).__init__(coupon_type, count, expires)
        self.userid = userid


class GroupCoupon(Coupon):
    def __init__(self, coupon_type: CouponType, groupid, count, expires):
        super(GroupCoupon, self).__init__(coupon_type, count, expires)
        self.groupid = groupid
