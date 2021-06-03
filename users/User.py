from post import Post


class User:
    all_posts = []

    def __init__(self, name, email_address, license_number):
        self.name = name
        self.email_address = email_address
        self.license_number = license_number
        self.posts = []

    def __str__(self):
        return "I am {}, my email is {}, and my license number is {}.".format(self.name, self.email_address, self.license_number)

    def interact(self):
        return "interacted!"

    def add_post(self, title, date, desc):
        new_post_data = {"title": title,
                         "date": date,
                         "desc": desc,
                         "author": self.name}
        new_post = Post(**new_post_data)
        self.posts.append(new_post)
        User.all_posts.append(new_post)
        print("Post added!")


def run_user():
    rob = User("Rob", "rob@gmail.com", 123321123)
    print(rob)
    rob.add_post("My first post", "Jun 1", "This is my first post.")
    for post in User.all_posts:
        print(post.title, post.date, post.desc)


if __name__ == "__main__":
    run_user()
