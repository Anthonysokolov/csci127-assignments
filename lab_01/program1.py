def hello_name(name):
  return 'Hello ' + name + '!'


def make_abba(a, b):
  return a + b + b + a


def combo_string(a, b):
  if len(a) >= len(b):
    return b + a + b
  else:
    return a + b + a


def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  elif a_smile == False and b_smile == False:
    return True
  else:
    return False


def pos_neg(a, b, negative):
  if negative:
    if a < 0 and b < 0:
      return True
    else:
      return False
  elif a < 0 and b > 0 or a > 0 and b < 0:
    return True
  else:
    return False


def non_start(a, b):
  return a[1:] + b[1:]


def first_two(str):
  return str[:2]


def missing_char(str, n):
  return str[:n] + str[n+1:]


def string_splosion(str):
  out = ''
  for num in range(1,len(str)+1):
    out += str[:num]
    
  return out


def array_front9(nums):
  try:
    for num in range(4):
      if nums[num] == 9:
        return True
    return False
  except IndexError:
    return False



