# -*- coding: UTF-8 -*-
import sys
from xpinyin import Pinyin
str3=["吴盈波",
"陈东贤",
"徐建利",
"胡才燕",
"杨世扬",
"王为民",
"葛贤稳",
"林娇娜",
"葛文婷",
"蒋美琼",
"李巧玲",
"王映懿",
"葛潇潇",
"虞琼琼",
"郑晓岚",
"毛婉飞",
"王  静",
"魏蕾蕾",
"葛璐曼",
"邹美琪",
"金竺瑾",
"胡美燕",
"孙旭丽",
"葛晓晴",
"胡佳莉",
"薛巧亚",
"王黎云",
"赵星心",
"徐  博",
"丁慧慧",
"童嘉纹",
"陈碧云",
"舒爱琴",
"刘甜甜",
"应珊真",
"冯静帆",
"冯存存",
"卢宇楠",
"冯冰冰",
"崔瑞巧",
"何  欣",
"葛  琤",
"胡余印",
"胡维娟",
"张丽芬",
"金璐莹",
"张伟珍",
"杨小娟",
"周月飞",
"张  琴",
"邬  婕",
"蔡学燕",
"潘哲宁",
"陈臆巧",
"麻莉莉",
"王寅玮",
"汪瑞蕊",
"陈露露",
"范亚芬",
"金婷婷",
"金莹",
"方艺璇",
"陈尔暄",
"葛春赞",
"许凊毓",
"吴咪咪",
"何善友",
"王朝有",
"潘静霞",
"江维维",
"陈  琼",
"储璐潞",
"张伟伟",
"林根长",
"奚敏敏",
"陈小芳",
"褚爱田",
"刘梦迪",
"卢金飞",
"储巧霞",
"王远怀",
"王晓芳",
"徐孝辉",
"应玲娜",
"傅松佳",
"李媛媛",
"徐彩虹",
"杨贤富",
"杨贤求",
"严再望",
"葛永平",
"朱番身",
"何善炉"]

p = Pinyin()
for i in str3:
    #print(len(i),i)
    tmp=i[0]
    tmp2=i[1:3]
    print(p.get_pinyin(tmp,"" )+p.get_initials(tmp2,"").lower())