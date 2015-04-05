#!/usr/bin/env python


class Element(object):
    tag = u""
    indent = u"    "
    tagjoin = u"\n"

    def __init__(self, content=None, **kwargs):
        self.content = [str(content)] if content else []
        self.attrs = kwargs if kwargs else {}

    def append(self, s):
        self.content.append(s)

    def build_open_tag(self, ind):
        attr_str = ""
        for key, val in self.attrs.iteritems():
            attr_str = u" ".join([attr_str, "%s=\"%s\"" % (key, val)])
        return u"".join([ind, u"<", self.tag, attr_str, u">"])

    def build_content(self, ind):
        c_str = ""
        for e in self.content:
            try:
                # e is an Element:
                add = e.output(Element.indent + ind)
            except AttributeError:
                # e is a string:
                add = Element.indent + ind + e
            c_str = u"\n".join([c_str, add]) if c_str else add
        return c_str

    def build_close_tag(self, ind):
        return u"".join([ind, u"</", self.tag, u">"])

    def output(self, ind=u""):
        """build a string form of the Element for printing."""
        open_tag = self.build_open_tag(ind)
        content = self.build_content(ind)
        close_tag = self.build_close_tag(ind)
        return self.tagjoin.join([open_tag, content, close_tag])

    def render(self, file_out, ind=u""):
        file_out.write(self.output(ind))


class OneLineTag(Element):
    tagjoin = u""

    def build_content(self, ind):
        c_str = None
        for e in self.content:
            try:
                # e is an Element:
                add = e.output()
            except AttributeError:
                # e is a string:
                add = e
            c_str = u"\n".join([c_str, add]) if c_str else add
        return c_str

    def build_close_tag(self, ind):
        return u"".join([u"</", self.tag, u">"])


class SelfClosingTag(Element):
    tagjoin = u""

    def build_open_tag(self, ind):
        attr_str = ""
        for key, val in self.attrs.iteritems():
            attr_str = u" ".join([attr_str, "%s=\"%s\"" % (key, val)])
        return u"".join([ind, u"<", self.tag, attr_str])

    def build_close_tag(self, ind):
        return u" />"


class Html(Element):
    header = u"<!DOCTYPE html>"
    tag = u"html"

    def output(self, ind=u""):
        return u"\n".join([Html.header, Element.output(self, ind)])


class Head(Element):
    tag = u"head"


class Title(OneLineTag):
    tag = u"title"


class Body(Element):
    tag = u"body"


class P(Element):
    tag = u"p"


class Hr(SelfClosingTag):
    tag = u"hr"


class Br(SelfClosingTag):
    tag = u"br"