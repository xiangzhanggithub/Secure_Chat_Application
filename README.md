# Secure Chat Application

By: Xiang Zhang, Yunfan Tian



This is a simple secure chat application for CS 6740 final project (server and clien t mode in localhost). You can execute the application by running **server.py** and **client.py**. Besides,  **sign_up.txt** stores username and password for server.

------

### Packages in Python:

Please Prepare following packages before running, you can install by **pip**:

```shell
pip install pyzmq
pip install protobuf
pip install bcrypt
pip install cryptography
```



### Running:

please compile **protobuf.proto** firstly:

```shell
$protoc --python_out=. protobuf.proto
```

Then, running **server.py**

```shell
$python server.py
```

And, **client.py**

```shell
$python client.py
```

