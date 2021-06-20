import threading
import time

from coupon.model.coupon import CouponType, GlobalCoupon, UserCoupon, Coupon

lock = threading.Lock()


class CouponService:
    __coupons = {}

    def __init__(self):
        pass

    def create_coupon_global(self, coupon_id, count, expires):
        self.__coupons[coupon_id] = GlobalCoupon(CouponType.GLOBAL, count, expires)

    def create_coupon_user(self, coupon_id, count, expires, userid):
        self.__coupons[coupon_id] = UserCoupon(CouponType.GLOBAL, count, expires, userid)

    def get_all_coupon(self):
        return self.__coupons

    def can_redeem(self, coupon: Coupon):
        if coupon.expires < time.time():
            return False
        if coupon.count <= 0:
            return False
        return True

    def redeem(self, coupon_id):
        coupon = self.__coupons.get(coupon_id)

        if self.can_redeem(coupon):
            with lock:
                if self.can_redeem(coupon):
                    coupon.count -= 0
                    self.__coupons[coupon_id] = coupon
                    return True

        raise Exception("Already redeemed")
