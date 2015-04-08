import html_render as hr


class Test_Element:
    e = None

    def setup_method(self, method):
        self.e = hr.Element()

    def teardown_method(self, method):
        self.e = None

    def add_content(self):
        vals = c1, c2, c2e = "content1", "content2", hr.Element("content2")
        self.e.append(c1)
        self.e.append(c2e)
        return vals

    def test_init_empty(self):
        assert(self.e.content == [])
        assert(self.e.attrs == {})

    def test_init_args(self):
        content = "content"
        attrs = {"style": u"text-align:center"}
        self.e = hr.Element(content, **attrs)
        assert(self.e.content == [content])
        assert(self.e.attrs == attrs)

    def test_append(self):
        c1, c2, c2e = self.add_content()
        assert(self.e.content == [c1, c2e])

    def test_build_open_tag(self):
        attrs = {"style": u"text-align:center"}
        self.e = hr.Element(None, **attrs)
        self.e.tag = "p"
        assert(self.e.build_open_tag("") == "<p style=\"text-align:center\">")

    def test_build_content(self):
        c1, c2, c2e = self.add_content()
        i = hr.Element.indent
        assert(self.e.build_content("") ==
               "{i}{c1}\n"
               "{i}<>\n"
               "{i}{i}{c2}\n"
               "{i}</>".format(i=i, c1=c1, c2=c2))
        i2 = i + "  "
        assert(self.e.build_content("  ") ==
               "{i2}{c1}\n"
               "{i2}<>\n"
               "{i2}{i}{c2}\n"
               "{i2}</>".format(i=i, i2=i2, c1=c1, c2=c2))

    def test_build_close_tag(self):
        self.e.tag = "p"
        assert(self.e.build_close_tag("") == "</p>")
