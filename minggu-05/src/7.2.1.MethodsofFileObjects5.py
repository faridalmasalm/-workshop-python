f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')
# 16 (output)
f.seek(5)      # Go to the 6th byte in the file
# 5 (output)
f.read(1)
# b'5' (output)
f.seek(-3, 2)  # Go to the 3rd byte before the end
# 13 (output)
f.read(1)
# b'd' (output)