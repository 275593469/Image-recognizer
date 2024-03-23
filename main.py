import os
from translate import Translator

import get_Inception_model
from tensorflow_predictor import TensorflowPredictor

if not os.path.exists('./inception_model/classify_image_graph_def.pb'):  # 如果没下载model，则下载model
    get_Inception_model.download_inception_model()  # 下载model

translator = Translator(to_lang="zh")  # 新建Translator对象


def translator_prediction_result(pre_res):  # 翻译模块
    res = pre_res.split("\n")[0] + '\n'
    line = pre_res.split("\n")[1]
    print('line', line)
    s = translator.translate(line.split(',')[1])
    print('s', s)
    return s  # 返回翻译结果


pdt = TensorflowPredictor()  # 新建预测类(自己写的)

def selector_image(img_path):  # 选择图片按钮点击发生的事件
    pre_res = pdt.predict_image(image_path=img_path)  # 利用地址调用预测函数返回结果字符串
    print("pre_res:", pre_res)
    pre_res = translator_prediction_result(pre_res)  # 机器翻译结果字符串
    return pre_res

if __name__ == '__main__':
    res = selector_image("/Users/jiangc/Downloads/1711206604151.png")
    print("分类", res)
