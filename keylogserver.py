import re, socket

HOST = ''
PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

f = open('backup.txt', 'w+')
keymap = open('keymap.txt', 'r+')

d = {}

#read keymappings
for line in keymap.readlines():
  l = line.split()
  try:
    d[l[1]] = l[3]
  except IndexError:
    d[l[1]] = hex(int(l[1]))
    
while 1:
  data = conn.recv(1024)
  if not data: break

  f.write(data) # save to backup file

  try:
    q = data.split()

    for v,i in enumerate(q):
      if i in d.keys():
        try:
          if q[v-1] != 'press':
            pass
          else:
            print d[i]
        except:
          print d[i]
  except:
    pass
    
conn.close()
