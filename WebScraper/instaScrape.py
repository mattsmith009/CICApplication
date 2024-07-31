import instaloader

instance = instaloader.Instaloader()

# L.login(user="mosebeety", passwd="06m03s04")
instance.interactive_login(username="mosebeety")
profile = instaloader.Profile.from_username(instance, "spazmattie").get_posts()
# L.load_session_from_file(username="mosebeety")
