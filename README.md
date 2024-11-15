# googleRPCtest
trying out gRPC for python
<h1>How to use it</h1>
First download the grpc and test libs

<code>python3 -m pip install grpcio</code> 
<code>python3 -m pip install grpcio-tools</code>
<code>python3 -m pip install pytest</code>

<ul>
  <li>
    Define the RR messages in calculator.proto - the nums represent the parameters' order in the function
  </li>
  <li>
    Compile the calculator.proto using -> <code>python3 -m grpc_tools.protoc \ -I. --python_out=. --grpc_python_out=. calculator.proto</code>
  </li>
  <li>
     Define the servers' functions in calculator_server.py 
  </li>
</ul>

With this you should be able send requests to a python server, in calculator_integration_test you can find an easy example of sending requests<br>
and use its reply

