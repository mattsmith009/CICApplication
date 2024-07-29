import instaloader

L = instaloader.Instaloader()

L.login(user="mosebeety", passwd="06m03s04")
L.interactive_login(username="mosebeety")
L.load_session_from_file(username="mosebeety")