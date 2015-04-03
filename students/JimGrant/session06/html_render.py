#!/usr/bin/env python


class Element(object):
    tag = u""
    indent = u"    "

    def __init__(self, content=None):
        self.content = self.indent + str(content) if content else ""

    def append(self, s):
        add = ""
        try:
            add = self.indent + s.output(Element.indent)
        except AttributeError:
            add = self.indent + s
        finally:
            self.content = u"\n".join([self.content, add])

    def output(self, ind=u""):
        open_tag = u"".join([u"\n", ind, u"<", self.tag, u">"])
        close_tag = u"".join([ind, u"</", self.tag, u">"])
        output = u"\n".join([open_tag, self.content, close_tag])
        return output

    def render(self, file_out, ind=u""):
        file_out.write(self.output(ind))


class Html(Element):
    header = u"<!DOCTYPE html>"
    tag = u"html"

    def output(self, ind=u""):
        return Html.header + Element.output(self, ind)


class Body(Element):
    tag = u"body"


class P(Element):
    tag = u"p"