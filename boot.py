'''
import network
import usocket as _socket
import ussl as ssl
import camera

camera.init()

network.WLAN(network.AP_IF).active(False)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Trojan", "my_Trojan")

img=camera.capture()

s = _socket.socket()
ai = _socket.getaddrinfo("micropython.org", 443)
addr = ai[0][-1]
print("Connect address:", addr)
s.connect(addr)
s = ssl.wrap_socket(s)
s.write(b"GET / HTTP/1.0\r\n\r\n")
print(s.read(1024))

print(len(img))
'''
