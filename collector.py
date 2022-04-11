'''
  COMPENG 2DX3 Final Project
  Boran Seckin - seckinb - 400305852

  This code collects data sent by the microcontroller over UART.
  It calculates Y and Z components of the vector and saves the data
  into data.txt file in X Y Z format.
'''

import math
import serial

SETS = 8
RESOLUTION = 32
ANGLE = 2 * math.pi / RESOLUTION

def main():
  ser = serial.Serial('/dev/tty.usbmodemME4010231', 115200)

  while (True):
    try:
      line = ser.readline().decode("utf-8").rstrip()
      print(line)

      if (line == "start"):
        for i in range(SETS):
          file = open("data.txt", "a")
          print(f'set-{i + 1}')
          for j in range(RESOLUTION):
            line = ser.readline().decode("utf-8").rstrip()
            print(line)
            y = (int(line) / SETS) * math.sin(ANGLE * j);
            z = (int(line) / SETS) * math.cos(ANGLE * j);
            file.write(f"{i * 50} {y} {z}\n")
          file.close()
        break
    except KeyboardInterrupt:
      exit()

if __name__ == "__main__":
  main()
