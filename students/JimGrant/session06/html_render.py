#!/usr/bin/env python


class Element(object):
    name = u""
    indent = u"    "

    def __init__(self, content=None):
        self.content = self.indent + str(content) if content else content

    def append(self, s):
        try:
            self.content = u"\n".join([self.content, self.indent + s])
        except TypeError:
            self.content = self.indent + s

    def render(self, file_out, ind=u""):
        open_tag = u"".join([u"\n", ind, u"<", self.name, u">"])
        close_tag = u"".join([ind, u"</", self.name, u">"])
        output = u"\n".join([open_tag, self.content, close_tag])
        file_out.write(output)