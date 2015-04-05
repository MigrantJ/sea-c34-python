#!/usr/bin/env python


class Element(object):
    tag = u""
    indent = u"    "

    def __init__(self, content=None):
        self.content = [str(content)] if content else []

    def append(self, s):
        self.content.append(s)

    def output(self, ind=u""):
        """build a string form of the Element for printing."""
        open_tag = u"".join([ind, u"<", self.tag, u">"])
        c_str = None
        for e in self.content:
            try:
                # e is an Element:
                add = e.output(Element.indent + ind)
            except AttributeError:
                # e is a string:
                add = Element.indent + ind + e
            c_str = u"\n".join([c_str, add]) if c_str else add
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