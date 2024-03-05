from PIL import Image
import os
from pyzbar.pyzbar import decode

# 特定のフォルダパス（ここを適宜変更してください）
folder_path = '.\QRtest'

# 出力ファイル
output_file = 'qrcode.txt'

# フォルダ内の画像ファイルを探索
for filename in os.listdir(folder_path):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(folder_path, filename)
        
        # 画像を開く
        with Image.open(image_path) as img:
            # 画像のサイズを取得
            width, height = img.size
            # 右上の部分を切り取る（例: 画像の幅の50%、高さの上から20%の範囲）
#            qr_area = img.crop((width - width, 0, width, height))
            qr_area = img.crop((0, 0, width, height))
            
            # QRコードを読み取る
            qr_codes = decode(qr_area)
            
            if qr_codes:
                # QRコードの内容をファイルに書き込む
                with open(output_file, 'a') as file:
                    for qr in qr_codes:
                        print(f'File {filename}:', qr.data.decode('utf-8'))
                        file.write(qr.data.decode('utf-8') + '\n')
            else:
                print(image_path + ':QRコードなしのファイル')
