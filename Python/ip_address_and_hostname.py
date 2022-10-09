# Display hostname andIP address
import socket
def host_IP():
   try:
      hname = socket.gethostname()
      hip = socket.gethostbyname(hname)
      print("Hostname:  ",hname)
      print("IP Address: ",hip)
   except:
      print("Unable to get Hostname and IP")
# Driver code
host_IP() #Function call