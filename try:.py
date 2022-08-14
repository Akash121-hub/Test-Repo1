# try:
#  if '1' != 1:
#   raise "firstError"
#  else:
#   print("firstError has not occured")
# except "TypeError":
#  print("firstError has occured")



def test1(param):
    return str(param)

def test2(param):
    return str(2 * param)

result = test1(1) + test2(2)
print(result)