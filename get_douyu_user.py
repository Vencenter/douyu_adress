
# -*- coding: utf-8 -*-

from douyu import main
import requests
import json,sys


reload(sys)
sys.setdefaultencoding("utf-8")

Max=165

list={
        'https://www.douyu.com/gapi/rkc/directory/0_0/list':u"all",
        'https://www.douyu.com/gapi/rkc/directory/0_0/{}':u"all",
        'https://www.douyu.com/gapi/rkc/directory/1_1/{}':u"绝地求生",
        'https://www.douyu.com/gapi/rkc/directory/2_124/{}':u"户外",
        'https://www.douyu.com/gapi/rkc/directory/2_1/{}':u"英雄联盟",
        'https://www.douyu.com/gapi/rkc/directory/2_2/{}':u"炉石传说",
        'https://www.douyu.com/gapi/rkc/directory/2_3/{}':u"DOTA2",
        'https://www.douyu.com/gapi/rkc/directory/2_4/{}':u"星际争霸",
        'https://www.douyu.com/gapi/rkc/directory/2_5/{}':u"魔兽世界",
        'https://www.douyu.com/gapi/rkc/directory/2_6/{}':u"CS",
        'https://www.douyu.com/gapi/rkc/directory/3_1/{}':u" ",
        'https://www.douyu.com/gapi/rkc/directory/2_174/{}':u"二次元",
        'https://www.douyu.com/gapi/rkc/directory/3_5/{}':u"CF手游",
        
        

    }

p = 0
urls = ['https://www.douyu.com/gapi/rkc/directory/0_0/{}'.format(page) for page in range(1, Max)]

#urls = ['https://www.douyu.com/gapi/rkc/directory/0_0/{}'.format(list) ]
fp=open("abc.txt","w")
for url in urls:
    res = requests.get(url)
    j = json.loads(res.text)
    l1 = j['data']
    l2 = l1['rl']
    p = p+1
    for i in range(len(l2)):
        Anchor = l2[i]['nn']              # 获取主播名字
        print Anchor
        RoomNumber = l2[i]['rid']         # 获取房间号
        #Heat = l2[i]['ol']                # 获取热度
        RoomName = l2[i]['rn']            # 获取房间名
        fp.write(Anchor+","+main(RoomNumber)+"\n")

fp.write("\n")

fp.close()
   

print(u'斗鱼房间数据已保存')
