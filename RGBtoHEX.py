"""
RGB-HEX COnverter contains:
A method to convert RGB to Hex
A method to convert Hex to RGB
A method that starts the prompt cycle
"""
def rgb_hex():
  invalid_msg = "What you entered was invalid."
  red = int(raw_input("Enter your value for red to be converted: "))
  if red < 0 or red > 255:
    print invalid_msg
    return
  green = int(raw_input("Enter your value for green to be converted: "))
  if green < 0 or green > 255:
    print invalid_msg
    return
  blue = int(raw_input("Enter your value for blue to be converted: "))
  if blue < 0 or blue > 255:
    print invalid_msg
    return
  val = (red << 16) + (green << 8) + blue
  val = hex(val).upper()
  print "Converted RGB value is: %s" % val
  
def hex_rgb():
  hex_val = raw_input("Enter your hexadecimal value to be converted: ")
  if len(hex_val) != 6:
    print "What you entered was invalid."
    return
  else:
    hex_val = int(hex_val, 16)
    
  two_hex_digits = 2 ** 8
  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  red = hex_val % two_hex_digits
  print "Converted hexadecimal value is: %d%d%d" % (red, green, blue)

def convert():
  while True:
    print "...RGB-HEX Converter started..."
    option = raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
    if option == "1":
      "RGB to HEX..."
      rgb_hex()
    elif option == "2":
      "Hex to RGB..."
      hex_rgb()
    elif option == "X" or option == "x":
      break
    else:
      print "Input invalid. Try again."
    
convert()