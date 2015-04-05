#!/usr/bin/env python


class Element(object):
    tag = u""
    indent = u"    "

    def __init__(self, content=None):
        self.content = [str(content)] if content else []

    def append(self, s):
        self.content.append(s)

    def output(self, ind=u""):
        open_tag = u"".join([ind, u"<", self.tag, u">"])
        c_str = None
        for e in self.content:
            try:
                if c_str:
                    print("Next element")
                    c_str = u"\n".join([c_str, e.output(Element.indent + ind)])
                else:
                    print("First element")
                    c_str = e.output(Element.indent + ind)
            except AttributeError:
                if c_str:
                    c_str = u"\n".join([c_str, Element.indent + ind + e])
                else:
                    c_str = Element.indent + ind + e
        close_tag = u"".join([ind, u"</", self.tag, u">"])
        return u"\n".join([open_tag, c_str, close_tag])

    def render(self, file_out, ind=u""):
        file_out.write(self.output(ind))


class Html(Element):
    header = u"<!DOCTYPE html>"
    tag = u"html"

    def output(self, ind=u""):
        return u"\n".join([Html.header, Element.output(self, ind)])


class Body(Element):
    tag = u"body"


class P(Element):
    tag = u"p"