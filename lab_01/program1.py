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





