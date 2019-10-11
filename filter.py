# -*- coding: utf-8 -*-
'''
使用正则表达式来过滤掉WikiExtractor提取文章
'''
import re

'''
 提取文章，清除无用数据
'''
def parse_wikiData(read_filePath, save_filePath):
  file = open(read_filePath, "r", encoding="utf-8")
  ouputfile = open(save_filePath, "a+", encoding="utf-8")
  regex_str = "[^<doc.*>$]|[^</doc>$]"
  readLine = file.readline()
  while readLine:
    content = re.match(regex_str, readLine)
    if content:
        ouputfile.write(readLine)
    readLine = file.readline()

if __name__ == "__main__":
    read_filePath = r""
    save_filePath = r"wordTovec\data"
    parse_wikiData(read_filePath, save_filePath)
