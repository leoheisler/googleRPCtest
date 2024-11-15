from calculator_pb2_grpc import CalculatorServicer

from calculator_pb2 import SumRequest
from calculator_pb2 import SumReply
from calculator_pb2 import MultiplyRequest
from calculator_pb2 import MultiplyReply
from calculator_pb2 import BiggestRequest
from calculator_pb2 import BiggestReply
from calculator_pb2 import DivRequest
from calculator_pb2 import DivReply
from grpc import ServicerContext


class Calculator(CalculatorServicer):

    def Sum(self, request: SumRequest, context: ServicerContext) -> SumReply:
        return SumReply(s=request.a + request.b)
    
    def Multiply(self, request: MultiplyRequest, context: ServicerContext):
        return MultiplyReply(s= request.a * request.b)
    
    def Biggest(self, request: BiggestRequest, context:ServicerContext):
        return BiggestReply(s = max([request.a,request.b,request.c]))
    
    def Div(self, request:DivRequest, context: ServicerContext):
        return DivReply(quo = int(request.dividendo / request.divisor), div_rest = request.dividendo % request.divisor)

