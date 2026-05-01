import qrcode
img = qrcode.make('some data here')
img.save("some_file.png")
