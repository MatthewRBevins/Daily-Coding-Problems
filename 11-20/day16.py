class order:
    def __init__(self):
        orders = []
    def record(self, order_id):
        orders.append(order_id)
    def get_last(self, i):
        return orders[i]
