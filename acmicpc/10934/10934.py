import hashlib
h = hashlib.new('sha')
h.update(input().encode('utf-8'))
print(h.hexdigest())
