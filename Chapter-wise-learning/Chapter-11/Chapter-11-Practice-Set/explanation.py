class Foo:
    x = 2


class Bar(Foo):

    y = Foo.x    # Access x outside of a function

    def bar(self):
        return self.x  # Access x using self
        # Could also be `return Foo.x`