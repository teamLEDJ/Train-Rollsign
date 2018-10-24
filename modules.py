# -*- coding: utf-8 -*-
import time
import re
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from PIL import Image, ImageDraw, ImageSequence


class Edit(object):     # 編集用
    # 座標・型変換
    @staticmethod
    def fixdata(data):
        data["type_pos"] = (data["type_pos"] - 64) / 2
        data["dest_pos"] = (data["dest_pos"] - 64) / 2
        data["overall_pos"] = (data["overall_pos"] - 64) / 2
        dest_leftpos = re.search(r'\d+', data["dest_leftpos"])
        data["dest_leftpos"] = int(dest_leftpos.group(0)) / 2
        return data


class LED(object):      # LED表示器用

    # Setup LEDs
    def __init__(self, chain=4, bright=50):  # デフォルト設定（引数なしの場合）
        # Options
        self.options = RGBMatrixOptions()
        self.options.rows = 32
        self.options.chain_length = chain
        self.options.parallel = 1
        self.options.hardware_mapping = 'adafruit-hat-pwm'
        self.options.brightness = bright
        self.options.show_refresh_rate = 0
        self.matrix = RGBMatrix(options=self.options)
        self.canvas = self.matrix.CreateFrameCanvas()

        # テキスト用フォント
        self.gothic = graphics.Font()
        self.gothic.LoadFont("Resources/Gothic-16.bdf")

        # color
        self.white = graphics.Color(255, 255, 255)

        # LED長さ
        self._width = self.canvas.width
        self._height = self.canvas.height

    # 車種から画像を選択、開く
    def select(self, data):
        # path
        path = {
            "common": "static/images/",
            "type": "_type.png",
            "dest": "_dest.png",
            "overall": "_overall.png"
        }

        # open imgs
        type_path = path["common"] + data["train_id"] + path["type"]
        dest_path = path["common"] + data["train_id"] + path["dest"]
        overall_path = path["common"] + data["train_id"] + path["overall"]

        self.type_img = Image.open(type_path).convert('RGB')
        self.dest_img = Image.open(dest_path).convert('RGB')
        self.overall_img = Image.open(overall_path).convert('RGB')

    # 表示
    def display(self, data):
        self.canvas.Clear()

        self.canvas.SetImage(self.type_img, 0, data["type_pos"])
        self.canvas.SetImage(
            self.dest_img, data["dest_leftpos"], data["dest_pos"])

        # 全面表示する場合
        if data["overall_flg"]:
            self.canvas.SetImage(self.overall_img, 0, data["overall_pos"])

        self.canvas = self.matrix.SwapOnVSync(self.canvas)

    # 表示初期化
    def clear(self):
        self.canvas.Clear()
        self.canvas = self.matrix.SwapOnVSync(self.canvas)
