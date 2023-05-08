def hello():
    print("Hi User")

def pack(a,b,c):
 return pack[a,b,c]

def eat_lunch(my_1st):
 if len(my_1st)==0:
    print("lunchbox empty!")
 else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_1st[0]}")
      else:
        print(f"Next I eat {my_1st[i]}")

hello()
print(pack("a","b","c"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["random"])
eat_lunch(["food","eat","sand","beach"])