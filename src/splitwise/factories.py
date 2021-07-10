from split_strategies import SplitType, EqualSplitStrategy, SplitStrategy


class Factory:
    @staticmethod
    def get_strategy(users, split_type, split_info) -> SplitStrategy:
        if split_type == SplitType.EQUAL:
            return EqualSplitStrategy(users, split_info.get("split_amount"))
