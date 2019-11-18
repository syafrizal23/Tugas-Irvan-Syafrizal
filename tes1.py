with open('Book1.jpeg', 'rb') as fd:
    file_head = fd.read(3)
Anumbers = {'jpeg': bytes([0xFF,0xD8,0xFF])}
max_read_size = max(len(m) for m in Anumbers.values()) 
  
with open('Book1.jpeg', 'rb') as fd:
    file_head = fd.read(max_read_size)
  
if file_head.startswith(Anumbers['jpeg']):
    print("Ini Benar,File Jpeg ")
else:
    print("Ini Bukan File Jpeg")
