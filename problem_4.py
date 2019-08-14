class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)


def is_user_in_group(user, group):
    if user in group.users:
        return True
    elif len(group.groups) == 0:
        return False
    else:
        for tempGroup in group.groups:
            return is_user_in_group(user, tempGroup)


if __name__ == "__main__":

    # Test case 1
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)
    print(is_user_in_group(sub_child_user, parent)) # True

    # Test case 2
    group1 = Group("group1")
    group2 = Group("group2")
    new_user="my_new_user"
    group2.add_user(new_user)
    group1.add_group(group2)
    print(is_user_in_group(new_user, group1))  # True

    # Test case 3
    print(is_user_in_group(new_user, parent))  # False


