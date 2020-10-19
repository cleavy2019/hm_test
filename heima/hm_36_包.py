from heima.hm_message import send_message
from heima.hm_message import receive_message

send_message.send("hello")
txt = receive_message.receive()
print(txt)