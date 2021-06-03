from users.User import User
from post import Post


class FreeUser(User):
    def __init__(self, name, email_address, license_number):
        super().__init__(name, email_address, license_number)
        self.posts = []
        self.post_count = 0

    def add_post(self, title, date, desc):
        if self.post_count >= 2:
            print("Can't post more than 2 posts!")
            return

        new_post_data = {"title": title,
                         "date": date,
                         "desc": desc,
                         "author": self.name}
        new_post = Post(**new_post_data)
        self.posts.append(new_post)
        User.all_posts.append(new_post)
        print("Post added!")
        self.post_count += 1
