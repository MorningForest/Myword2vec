# -*- coding: utf-8 -*-
from gensim import models
import numpy as np 
import logging

'''
测试训练好的模型
'''
def test():
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s",level=logging.INFO)
    model = models.Word2Vec.load("wordTovec\model\wiki.model")
    word1 = u'农业'
    word2 = u'嘉伟'
    if word1 in model:
        print (u"'%s'的词向量为： " % word1)
        print (model[word1])
    else:
        print (u'单词不在字典中！')
    result = model.most_similar(word2)
    print (u"\n与'%s'最相似的词为： " % word2)
    for e in result:
        print ('%s: %f' % (e[0], e[1]))

if __name__ == "__main__":
    test()
