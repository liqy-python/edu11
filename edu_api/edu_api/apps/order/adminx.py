import xadmin
from .models import Order
from .models import OrderDetail


class OrderModelAdmin(object):
    # 订单模型
    pass


xadmin.site.register(Order,OrderModelAdmin)


class OrderDetailModelAdmin(object):
    # 订单管理
    pass


xadmin.site.register(OrderDetail,OrderDetailModelAdmin)