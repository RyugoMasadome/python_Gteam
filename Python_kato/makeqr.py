import os
import qrcode

#QRコードの作成
img = qrcode.make("http://kujirahand.com/")

#パスの生成
path = os.path.join("files", "qrcode-kato.png")

#ファイルに保存
img.save(path)