# -*- coding: utf-8 -*-
# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


'''配置'''
'''
#http://player.youku.com/embed/XMTE2MDEyNDU2
#http://v.youku.com/v_show/id_XMTE2MDEyNDU2.html
MOVIES_LIST=[
    ["Toy Story",
     "http://g3.ykimg.com/0516000059634835859B5E09F705049A",
     "http://v.youku.com/v_show/id_XMTE2MDEyNDU2.html"],
    ["Avatar",
     "http://g1.ykimg.com/051600005962F79FADBC09036209EC12",
     "http://v.youku.com/v_show/id_XMTk4ODUyNDQ4.html"],
    ["Pulp Fiction",
     "http://g1.ykimg.com/0516000053548D7F67379F05BB00759C",
     "http://v.youku.com/v_show/id_XNzMwNTYxNzQw.html"],
    ["The Lego Movie",
     "http://g1.ykimg.com/0516000054D8739567379F6D620BFB61",
     "http://v.youku.com/v_show/id_XNjcxNTYzOTY4.html"],
    ["Jurassic World",
     "http://g1.ykimg.com/0516000057EDD71767BC3C356F0293CE",
     "http://v.youku.com/v_show/id_XODg1NDE3NTQ4.html"],
]
'''
SEARCH_PREFIX="http://www.soku.com/search_video/q_"

def search_info(film_name):
    '''从优酷搜索'''
    txt=requests.get(SEARCH_PREFIX+film_name).text
    #BeautifulSoup   ->  https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
    page=BeautifulSoup(txt,"lxml")
    movie_div=page.find(class_='s_dir')
    #图片url
    img_url=movie_div.find(class_='s_poster').find(class_='s_target').find('img')['src']
    #预告片
    trailer_url=movie_div.find(class_='s_related').find(class_='s_link').find('a')['href'].split('?')[0]
    return (img_url,trailer_url)

if __name__=='__main__':
    
#    toy_story = media.Movie()
#
#    avatar = media.Movie()
#
#    movies = [toy_story, avatar]
    movies=[]
    movies_name=["Toy Story","Avatar","Pulp Fiction","The Lego Movie","Jurassic World"]
#    从配置MOVIES_LIST提取
#    for cur_moive in MOVIES_LIST:
#        movie=media.Movie(cur_moive[0],cur_moive[1],cur_moive[2])
#        movies.append(movie)
    
    
    #从优酷提取信息
    for movie_name in movies_name:
        img_url,trailer_url=search_info(movie_name)
        movies.append(media.Movie(movie_name,img_url,trailer_url))
    
    fresh_tomatoes.open_movies_page(movies)
