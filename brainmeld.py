import twint
import random

def followingDis(source, target, num = 100):
    if source is not None:
        s = twint.Config()
        s.Hide_output = True
        s.Limit = 25
        s.Username = source
        s.Store_object = True
        twint.run.Following(s)
        sFollowing = set([u.username for u in twint.output.users_list])
    else:
        sFollowing = set()
    print(sFollowing)
    t = twint.Config()
    t.Hide_output = True
    t.Limit = 25
    t.Username = target
    t.Store_object = True
    twint.run.Following(t)
    tFollowing = set([u.username for u in twint.output.users_list])
    ##optional lessening of random sample
    if len(tFollowing) <= num:
        return target
    else:
        ## go over edge case
        tFollowing = random.sample(source, 1000)    
    i = set()
    o = set()
    for x in tFollowing:
        if x in sFollowing:
            i.add(x)
        else: 
            o.add(x)

    if len(o) <= num:
        num -= len(o)
        ## make sure adding sets really is union and sort works with keys
        return o.union(random_top(num, sorted(weight(sFollowing, i))))
    return random.sample(o, num)


def random_top(num, d):
    ret = set()
    j = 0
    t = True
    for y, z in d.items():
        if num >= 0:
            ret.add(y)
            d.pop(y)
            num +=  -1
            j = z
        elif j is z:
            ret.add(y)
            d.pop(y)
            t = False
        else:
            break
    if not t:
        return random.sample(ret, num)
    return ret

def weight(s1, s2): ##returns ordered list
    ret = dict()
    for x in s2:
        i = 0
        t = twint.Config()
        t.Limit = 50
        t.Username = x
        t.Store_object = True
        twint.run.Following(t)
        tfollowing = set([u.username for u in twint.output.users_list])
        for y in tfollowing:
            if y in s1:
                i+= 1
                ret[x] = i
    return sorted(ret.values())

if __name__ == '__main__':
    res = followingDis("BarackObama","realDonaldTrump")
    print(res)


