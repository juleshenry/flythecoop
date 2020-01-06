def followingDis(num = 1000, source, target):
    if source is not None:
        s = twint.Config()
        s.Limit = 2500
        s.Username = source
        s.Store_object = true
        twint.run.Following(s)
        sfollowing = set(twint.output.following_list)
    else: sFollowing = set()

    t = twint.Config()
    t.Limit = 2500
    t.Username = target
    t.Store_object = true
    twint.run.Following(t)
    tfollowing = set(twint.output.following_list)
    ##optional lessening of random sample
    if len(tFollowing) <= num:
        return target
    else:
        ## go over edge case
        tFollowing = tFollowing.random.sample(source, 1000)    
    i = set()
    o = set()
    for x in tFollowing:
        if x in sFollowing:
            i.add(x)
        else: 
            o.add(x)

    if len(o) <= num:
        num -= len(o)
        ret = o
        ## make sure adding sets really is union and sort works with keys
        return o.union(random_top(num, sort(weight(sFollowing, i))))
    return random.sample(o, num)


def random_top(num, d):
    ret = set()
    x = true;
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

def weight(s1, s2):
##returns ordered list
    ret = dict()
    for x in s2:
        i = 0;
        t = twint.Config()
        t.Limit = 5000
        t.Username = x
        t.Store_object = true
        twint.run.Following(t)
        tfollowing = set(twint.output.following_list)
        for y in tfollowing:
            if y in s1:
                i+= 1
                ret[x] = i
    return sorted(ret.values())

if _name_ == '__main__':
    #main

       