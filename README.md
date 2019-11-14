训练词向量模型
========

1.准备工作
-----
+ 下载语料
  wiki百科的语料库，大概1.5g左右([下载路径](https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2))
+ 下载WikiExtractor
  专门用来提取维基百科语料中文章的工具([下载地址](https://github.com/attardi/wikiextractor))
+ 下载OpenCC
  由于维基百科中语料有繁体字，故可用Opencc来化繁为简([下载地址](https://github.com/BYVoid/OpenCC))
+ 安装分词工具
  需要安装一种分词工具来切词([下载地址](https://github.com/fxsjy/jieba))
  使用jieba库 `pip install jieba`来安装
  也可以使用hanlp库 `pip install pyhanlp`
+ 安装word2Vec库
  安装gensim库，其有word2Vec的模型
  python中采用` pip install -i https://pypi.douban.com/simple gensim`

2.提取文章
-----
  + 下载完WikiExtractor后,解压，使用WikiExtractor.py脚本，通过一下命令来提取文章
  `python WikiExtractor.py -b 500M -o zhwiki zhwiki-20180720-pages-articles.xml.bz2`
  + **参数介绍**  
    + -b 提取文章后每个文章大小
    + -o 指定输出文件保存的目录
    + zhwiki-20180720-pages-articles.xml.bz2, 下载维基百科语料的地址

  + 使用WikiExtractor提取的文章格式如下：
  `<doc id="" revid="" url="" title="">...<\doc>`

3.中文简体和繁体转换
-----
  下载解压opencc文件,其文件opencc\share\opencc下有一系列配置文件，其中t2s.json是把繁体转为简体的文件。CMD下使用一下命令可以把文件繁体转为简体`opencc -i 需要转换文件路径 -o 转换后文件路径 -c 配置文件路径(t2s.json的路径)`

4.正则表达式提取文章内容
-----
  由于提取的文章包含许多`<doc></doc>`,故需要过滤。使用filter.py文件即可过滤

5.分词并合并文件
-----
  使用jieba分词工具, hanlp工具或者斯坦福切词工具对文件进行分词处理并合并文件。

6.Word2Vec模型训练
-----
  调用gensim的word2Vec模型，对已经分词好文件训练。时间大概为1个小时左右,具体训练情况与电脑配置有关

7.word2Vec模型使用
-----
  调用训练好模型,测试结果。
