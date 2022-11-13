class Bill:
    """
    Object that contains data about a bill, such as
    total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class RoomMate:
    """
    Creates a RoomMate person who lives in the house
    and pays a share of the bill.
    """

    def __init__(self, name, days):
        self.name = name
        self.days = days

    def pay(self, bill, roommate):
        weight = self.days / (self.days + roommate.days)
        to_pay = bill.amount * weight
        return to_pay 