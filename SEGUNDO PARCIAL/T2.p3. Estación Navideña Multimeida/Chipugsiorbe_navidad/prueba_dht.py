import adafruit_dht, board
sensor=adafruit_dht.DHT11(board.D4)

print(sensor.temperature)
print(sensor.humidity)
