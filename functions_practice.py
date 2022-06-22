def hello():
  print("hello, Mae!")

def pack(cat, dog, mouse):
  return [cat, dog, mouse]
print(pack("cat", "dog", "mouse"))

def pack(a=1,b=2,c=3):
  return [1,2,3]
print(pack("1","2","3"))


def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")


eat_lunch(["meat","tacos","sushi","soup"])
eat_lunch([])