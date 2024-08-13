import instaloader

instance = instaloader.InstaloaderContext(iphone_support=False)

### Fill in login info here
instance.login(user="", passwd="")
### Fill in login info here
profile = instaloader.Profile.from_username(instance, "spazmattie")
hashtag = instaloader.Hashtag.from_name(instance, "olympics")
hashtag.get_posts_resumable()