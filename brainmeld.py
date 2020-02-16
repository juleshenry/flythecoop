import twint
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def followingDis(source, target, num = 100):
    sou_lim = 25
    sFollowing, tFollowing = set(), set()
    s = twint.Config()
    s.Hide_output = True
    s.Limit = sou_lim
    s.Username = source
    s.Store_object = True
    twint.run.Following(s)
    sFollowing = set(twint.output.follows_list)

    t = twint.Config()
    t.Hide_output = True
    t.Limit = sou_lim
    t.Username = target
    t.Store_object = True
    twint.run.Following(t)
    tFollowing = set(twint.output.follows_list)

    #optional lessening of random sample
    if len(tFollowing) <= num:
        return target
    else:
        ## go over edge case
        tFollowing = random.sample(tFollowing, sou_lim)    
    i = set()
    o = set()
    for x in tFollowing:
        if x in sFollowing:
            i.add(x)
        else: 
            o.add(x)
    print('followingDis succeeded')
    if len(o) <= num:
        num -= len(o)
        ## make sure adding sets really is union and sort works with keys
        return o.union(random_top(num, weight(sFollowing, i)))
    return random.sample(o, num)

def random_top(num, d):
    ret = set()
    j = 0
    t = True
    print(d)
    nummer = num
    for k, v in d.items():
        if num >= 0:
            ret.add(k)
            num -= 1
            j = v

        elif j == v:
            ret.add(k)
            t = False
        else:
            break
    if not t:
        return random.sample(ret, nummer)

    return ret

def weight(sFollowing, in_set): ##returns ordered list
    ret = dict()
    sou_lim = 25
    print(sFollowing)
    for x in in_set:
        i = 0
        t = twint.Config()
        t.Limit = sou_lim
        t.Username = x
        t.Hide_output = True
        t.Store_object = True
        twint.run.Following(t)
        tfollowing = set(twint.output.follows_list)
        # tfollowing = set(['n5','n7', 'n4'])
        for y in tfollowing:
            if y in sFollowing:
                i += 1
        ret[x] = i
    return {k: v for k, v in sorted(ret.items(), key=lambda item: item[1])}



def get_probes(node, probe_cnt):
    probes = []
    s = twint.Config()
    s.Hide_output = True
    s.Limit = 3
    s.Username = node
    s.Store_object = True
    twint.run.Following(s)
    sFollowing = set(twint.output.follows_list)
    return probes

def probe(source, target):
    #while
    source_probes = get_probes(source, 16)
    target_probes = get_probes(target, 16)
    for i in source_probes: print(i)
    for j in target_probes: print(j)

class probe_twitter:
    def __init__(self,source,target):
        self.driver = webdriver.Chrome() #chrome 76.0.3809.126
        self.driver.implicitly_wait(2)
        self.get_followers(source)
    
    def get_followers(self, node):
        self.driver.get('https://twitter.com/' + node + '/following')
        self.driver.find_element_by_css_selector('#react-root > div > div > div > header > div.css-1dbjc4n.r-yfoy6g.r-o4zss7.r-rull8r.r-qklmqi.r-1d2f490.r-1xcajam.r-zchlnj.r-ipm5af.r-1siec45.r-o7ynqc.r-axxi2z.r-136ojw6 > div.css-1dbjc4n.r-1jgb5lz.r-sb58tz.r-13qz1uu > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1h3ijdo.r-58zi21 > div.css-1dbjc4n.r-1awozwy.r-1pz39u2.r-18u37iz.r-16y2uox > div:nth-child(1) > a > div > span > span').click()
        time.sleep(4)
        self.driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-1pi2tsx.r-13qz1uu.r-417010 > main > div > div > form > div > div:nth-child(6) > label > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1udh08x > div > input").click() # Click Login
        time.sleep(4)
        input_user = self.driver.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[1]/main/div/div/form/div/div[1]/label/div[2]/div/input')[0]
        input_user.click()
        input_user.send_keys('julianplushenry@gmail.com') # send username
        time.sleep(4)
        input_pass = self.driver.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[1]/main/div/div/form/div/div[2]/label/div[2]/div/input')[0]
        input_pass.click()
        input_pass.send_keys('passPasspazz') # send pass
        time.sleep(4)
        self.driver.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[1]/main/div/div/form/div/div[3]/div/div/span/span')[0].click() # Do Login
        time.sleep(10)
        for i in range(1,16):
            print(self.driver.find_element_by_css_selector('#react-root > div > div > div > main > div > div > div > div > div > div:nth-child(2) > section > div > div > div > div:nth-child('+ str(i) + ') > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-5f2r5o > div > div.css-1dbjc4n.r-1wbh5a2.r-dnmrzs > a > div > div.css-1dbjc4n.r-18u37iz.r-1wbh5a2 > div > span').text)

    def sel_probe(source, target):
        pass
    #react-root > div > div > div > main > div > div > div > div > div > div:nth-child(2) > section > div > div > div > div:nth-child(3) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-5f2r5o > div > div.css-1dbjc4n.r-1wbh5a2.r-dnmrzs > a > div > div.css-1dbjc4n.r-18u37iz.r-1wbh5a2 > div > span
if __name__ == '__main__':
    probe_twitter('BarackObama', 'KeltonMadden')
