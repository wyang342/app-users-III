from users.FreeUser import FreeUser
from users.PremiumUser import PremiumUser
from users.User import User

won = FreeUser("Won", "won@gatech.edu", "123321123")
bob = PremiumUser("Bob", "bob@gmail.com", "454454454")

won.add_post("My first post", "jun 3", "this is my first post")
won.add_post("My second post", "jun 3", "this is my second post")
won.add_post("My third post", "jun 3", "this is my third post")

print()
for post in User.all_posts:
    print(post.title, post.date, post.desc, post.author)
print()

bob.add_post("My first post", "jun 3", "this is my first post")
bob.add_post("My second post", "jun 3", "this is my second post")
bob.add_post("My third post", "jun 3", "this is my third post")

print()
for post in User.all_posts:
    print(post.title, post.date, post.desc, post.author)
