# -*- coding: utf-8 -*-
from gensim.models import word2vec
import logging

'''
  调用gensim包训练模型
'''
def train(filePath, savePath):
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s",level=logging.INFO)
    sentences = word2vec.LineSentence(filePath)
    model = word2vec.Word2Vec(sentences,size=250)
    model.save(savePath)



if __name__ == "__main__":
    filePath = r"wordTovec\data\output.txt"
    savePath = r"wordTovec\model\wiki.model"
    train(filePath, savePath)