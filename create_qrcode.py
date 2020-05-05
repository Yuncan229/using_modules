import MyQR.myqr


# run函数里面的参数：def run(words, version=1, level='H', picture=None, colorized=False, contrast=1.0, brightness=1.0,
# save_name=None, save_dir=os.getcwd())
version, level, qr_name = MyQR.myqr.run(
	'https://github.com/Yuncan229',
    version=1,
    level='H',
    picture='/Users/mac/Desktop/Python 学习/haha.png',
    colorized=False,
    contrast=1.0,
    brightness=1.0,
    save_name='first_qrcode.png',
    save_dir=os.getcwd()
	)


