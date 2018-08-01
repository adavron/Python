def mk_profile(first,last,**userinfo):
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key, value in userinfo.items():
        profile[key]=value
    return profile


print mk_profile('bek','dav',location='usa',age=12,city='chicago')
