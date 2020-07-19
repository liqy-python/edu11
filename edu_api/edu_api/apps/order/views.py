from django.db import transaction
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from order.models import Order
from order.serializers import OrderModelSerializers


class OrderAPIView(CreateAPIView):
    """生成订单的视图"""
    queryset = Order.objects.filter(is_delete=False,is_show=True)
    serializer_class = OrderModelSerializers

    # @transaction.atomic()  # 开始事务， 当方法执行完成后自动提交事务
    # def post(self, request, *args, **kwargs):
    #     # 开启事务
    #     with transaction.atomic():
    #         print("1111")
    #         # 记录事务的回滚点
    #         savepoint = transaction.savepoint()
    #         # 遇到异常  可以回到上一事务开启的点
    #         transaction.savepoint_rollback(savepoint)
    #         return Response({'message':'生成订单成功'})



