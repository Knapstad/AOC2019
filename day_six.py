class Celestial()

    def __init__(self, name: str, parent: Celestial):
        self.name = name
        self.parent = parent
        self.children = []

    def add_child(self, child)
        if child not in self.children:
            self.children.append(child)