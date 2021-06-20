from datetime import timedelta, date

from coupon.model.user import User
from service.coupon_service import CouponService


class CouponController:
    def __init__(self, coupon_service: CouponService):
        self.__coupon_service: CouponService = coupon_service

    def run(self):
        shahjahan = User(1, "Shahjahan")
        himanshu = User(1, "Himanshu")

        shahjahan_coupon_1 = self.__coupon_service.create_coupon_user(1, 2, date.today() + timedelta(days=10),
                                                                      shahjahan.userid)
        shahjahan_coupon_2 = self.__coupon_service.create_coupon_user(2, 5, date.today() + timedelta(days=10),
                                                                      shahjahan.userid)

        himanshu_coupon_1 = self.__coupon_service.create_coupon_user(3, 5, date.today() + timedelta(days=10),
                                                                     himanshu.userid)
        himanshu_coupon_2 = self.__coupon_service.create_coupon_user(4, 5, date.today() + timedelta(days=10),
                                                                     himanshu.userid)

        print(self.__coupon_service.get_all_coupon())

        self.__coupon_service.redeem(1)
        self.__coupon_service.redeem(1)


if __name__ == "__main__":
    coupon_service = CouponService()
    coupon_controller = CouponController(coupon_service)

    coupon_controller.run()
