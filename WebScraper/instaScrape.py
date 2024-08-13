import instaloader

instance = instaloader.InstaloaderContext(iphone_support=False)

instance.login(user="mosebeety", passwd="06m03s04")
profile = instaloader.Profile.from_username(instance, "spazmattie")
hashtag = instaloader.Hashtag.from_name(instance, "olympics")
hashtag.get_posts_resumable()