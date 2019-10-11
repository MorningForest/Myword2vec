from gensim import models
import numpy as np 
import matplotlib.pyplot as plt 
from pylab import mpl
from wordcloud import WordCloud
import logging

'''
画词汇图
'''
def mask():
    x,y = np.ogrid[:300,:300]
    mask = (x-150) ** 2 + (y-150)**2 > 130 ** 2
    mask = 255 * mask.astype(int)
    return mask

'''
需要导入字体
可以在C盘windows下fonts中选择一项字体
'''
def draw_word_cloud(word_cloud):    
    font = r"wordTovec\wikiextractor-master\wikiData\AA\STSONG.TTF"
    wc = WordCloud(background_color="white",mask=mask(),font_path=font)
    wc.generate_from_frequencies(word_cloud)
    plt.axis("off")
    plt.imshow(wc,interpolation="bilinear")
    plt.show()
  
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
    # one_corpus = ["智能"]
    # result = model.most_similar(one_corpus[0], topn=100)
    # word_dict = dict()
    # for item in result:
    #     word_dict[item[0]] = item[1]
    #     print(item)

    # draw_word_cloud(word_dict)
    # two_corpus = ["腾讯", "阿里巴巴"]
    # res = model.wv.most_similar(two_corpus[0], two_corpus[1])
    # print("similarity:", res)

    # # 输入三个词类比
    # three_corpus = ["北京", "上海", "广州"]
    # res = model.wv.most_similar([three_corpus[0], three_corpus[1], three_corpus[2]], topn=100)
    # # 将返回的结果转换为字典,便于绘制词云
    # word_cloud = dict()
    # for sim in res:
    #     # print(sim[0],":",sim[1])
    #     word_cloud[sim[0]] = sim[1]
    # # 绘制词云
    # draw_word_cloud(word_cloud)

if __name__ == "__main__":
    test()
