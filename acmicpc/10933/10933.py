import hashlib
h = hashlib.new('ripemd160')
h.update(input().encode('utf-8'))
print(h.hexdigest())
