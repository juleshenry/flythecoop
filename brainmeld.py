import twint
import random

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

if __name__ == '__main__':
    print(followingDis("BarackObama","KeltonMadden", 10))
