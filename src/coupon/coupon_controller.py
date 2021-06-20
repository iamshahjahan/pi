from service.coupon_service import CouponService


class CouponController:
    def __init__(self, coupon_service: CouponService):
        self.__coupon_service: CouponService = coupon_service

    def run(self):
        shahjahan = User(1, "Shahjahan")
        himanshu = User(1, "Himanshu")

        shahjahan_coupon_1 = self.__coupon_service.create_coupon_user()
