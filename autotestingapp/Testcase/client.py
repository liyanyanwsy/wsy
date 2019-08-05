import socket

target_host = '192.168.88.1'
target_port = 12345

#建立一个socket对象,AF_INET说明将使用标准的IPv4地址或主机名，SOCK_STREAM说明是一个TCP客户端
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#连接到服务器
client.connect((target_host, target_port))

#发送数据
# client.send("i am TCP client")
d='A5B900104228792ED30830010327F7840D01FD1E0000CF83D25901006EDE000053453145533333304835333032332020000000000000000000000000000000006E0900000000801300000000000000000000000000000000000000000000000000000000FFFF2E13E8FF1400F2FF0D001000000000005200520030040000FE000000FF0300009C060000000080000000A600B500FDFF6E095F000000070000000C001E000000140009001000FAFFF7FF0000000000000000000000000000170300000000DA15'
a=bytes().fromhex('A5B900104228792ED30830010327F7840D01FD1E0000CF83D25901006EDE000053453145533333304835333032332020000000000000000000000000000000006E0900000000801300000000000000000000000000000000000000000000000000000000FFFF2E13E8FF1400F2FF0D001000000000005200520030040000FE000000FF0300009C060000000080000000A600B500FDFF6E095F000000070000000C001E000000140009001000FAFFF7FF0000000000000000000000000000170300000000DA15')


#client.send(str.encode(d))
print(a)
client.send(a)

#接收数据
response = client.recv(4096)

print(response)
