# Aqui importamos os módulos necessários para os testes
from pytest import fixture


@fixture(scope="module")
def listen_address():
    return '[::]:50051'


# Aqui criamos uma instância do servidor gRPC 
@fixture(scope="module")
def grpc_server(listen_address):
    from calculator_pb2_grpc import add_CalculatorServicer_to_server
    from calculator_server import Calculator

    from concurrent import futures

    from grpc import server

    grpc_server = server(futures.ThreadPoolExecutor(max_workers=10))

    add_CalculatorServicer_to_server(Calculator(), grpc_server)

    grpc_server.add_insecure_port(listen_address)
    grpc_server.start()

    yield

    grpc_server.stop(True)


@fixture(scope="module")
def channel(grpc_server, listen_address):
    from grpc import insecure_channel
    return insecure_channel(listen_address)


@fixture(scope="module")
def calculator_client(channel):
    from calculator_pb2_grpc import CalculatorStub
    return CalculatorStub(channel)


def test_sum(calculator_client):
    from calculator_pb2 import SumRequest

    # given
    a = 256.5
    b = 128.8

    expected = a + b

    # when
    result = calculator_client.Sum(SumRequest(a=a, b=b))

    # then
    assert result.s == expected

def test_mult(calculator_client):
    from calculator_pb2 import MultiplyRequest

    #given
    a = 5
    b = 4

    expected = a*b
    #when
    result = calculator_client.Multiply(MultiplyRequest(a=a, b=b))
    
    #then
    assert result.s == expected


def test_biggest(calculator_client):
    from calculator_pb2 import BiggestRequest
    #given
    a = 5
    b = 4
    c = 8

    expected = max([a,b,c])
    #when
    result = calculator_client.Biggest(BiggestRequest(a=a,b=b,c=c))
    
    #then
    assert result.s == expected

def test_div(calculator_client):
    from calculator_pb2 import DivRequest
    #given
    a = 5
    b = 4
    quo = int(a/b)
    div_rest = a % b

    expected = (quo,div_rest)
    #when
    result = calculator_client.Div(DivRequest(dividendo = a, divisor = b))
    #then
    assert (result.quo,result.div_rest) == expected    