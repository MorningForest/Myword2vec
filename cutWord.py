import jieba
import logging

'''
  获取去停止词
  得到去停止词的集合
'''
def get_stopword(*filepaths):
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s",level=logging.INFO)
    stopWordList = set()
    for filepath in filepaths:
      with open(filepath,"r",encoding="utf-8") as f:
          for item in f:
              stopWordList.add(item.strip("\n"))
    return stopWordList

'''
使用结巴分词工具对数据集进行切词
并去停止词后写入新文件
'''
def cutword(stopWordList, filepath, savepath):
    file = open(filepath, "r", encoding="utf-8")
    output = open(savepath, "a+", encoding="utf-8")
    datas = file.readlines()
    content_line = ""
    for data in datas:
        items = jieba.cut(data.strip("\n"), cut_all=False)
        for item in items:
            if item not in stopWordList:
                content_line += item + " "
        output.write(content_line+"\n")
        content_line = ""
    file.close()
    output.close()

'''
对所有需要切词文件进行切词
'''
def main():
    stopWordList = get_stopword("wordTovec\data\stopwords.txt","wordTovec\data\stopwords01.txt")
    for i in range(3):
      cutword(stopWordList, "wordTovec\AA\wiki0"+str(i), "wordTovec\AA\output.txt")

if __name__ == "__main__":
    main()

