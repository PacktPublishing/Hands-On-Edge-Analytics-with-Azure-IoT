import sensor

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QVGA)
sensor.set_vflip(1)

while True:
    img = sensor.snapshot()
    res = img.find_qrcodes()

    if len(res) > 0:
        img.draw_string(2,2, res[0].payload(), color=(255,255,255), scale=1.5)
