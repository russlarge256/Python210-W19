#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = "  "

    def __init__(self, content=None, **kwargs):

        if kwargs is not None:
            self.attributes = " ".join(['{}="{}"'.format(key, val) for key, val in kwargs.items()])
        if kwargs is None:
            pass

        if content is None:
            self.contents = []
        elif content is not None:
            self.contents = [content]
            self.kwargs = kwargs

    def append(self, new_content):
        self.contents.append(new_content)


    def render(self, out_file):

        out_file.write("<{}{}>".format(self.tag, self.attributes))
        out_file.write("\n")

        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
                out_file.write("\n")

        out_file.write("</{}>\n".format(self.tag))



class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"

class OneLineTag(Element):

    def render(self, out_file):
        out_file.write(("<{}{}>".format(self.tag, self.attributes)+self.contents[0]+"</{}>\n".format(self.tag)))
    def append(self, new_content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):

    def render(self, out_file):
        if len(self.attributes) < 1:
            out_file.write("<{} />\n".format(self.tag))
        else:

            out_file.write("<{} {} />\n".format(self.tag, self.attributes))

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "hr"


class A(OneLineTag):
    tag = "a "

    def __init__(self, link, *args, **kwargs):
        kwargs['href'] = link
        super().__init__(*args, **kwargs)


class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"


class H(OneLineTag):
    tag = "H"

    def __init__(self, level, *args, **kwargs):
        self.level = level
        self.tag = "{}{}".format(self.tag, self.level)
        super().__init__(*args, **kwargs)

class Meta(SelfClosingTag):
    tag = "meta"