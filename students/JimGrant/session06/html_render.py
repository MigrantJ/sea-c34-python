#!/usr/bin/env python


class Element(object):
    tag = u""
    indent = u"    "

    def __init__(self, content=None):
        self.indent = ""
        self.content = Element.indent + str(content) if content else ""

    def append(self, s):
        add = ""
        try:
            s.indent = Element.indent + self.indent
            add = s.output(s.indent)
        except AttributeError:
            add = Element.indent + s
        finally:
            if self.content != "":
                self.content = u"\n".join([self.content, add])
            else:
                self.content = add

    def output(self, ind=u""):
        open_tag = u"".join([ind, u"<", self.tag, u">"])
        close_tag = u"".join([ind, u"</", self.tag, u">"])
        output = u"\n".join([open_tag, self.content, close_tag])
        return output

    def render(self, file_out, ind=u""):
        file_out.write(self.output(self.indent + ind))


class Html(Element):
    header = u"<!DOCTYPE html>"
    tag = u"html"

    def output(self, ind=u""):
        return u"\n".join([Html.header, Element.output(self, ind)])


class Body(Element):
    tag = u"body"


class P(Element):
    tag = u"p"