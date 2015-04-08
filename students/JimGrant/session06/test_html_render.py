import html_render as hr


class Test_Element:
    e = None

    def setup_method(self, method):
        self.e = hr.Element()

    def teardown_method(self, method):
        self.e = None

    def add_content(self):
        content1 = "content1"
        content2 = "content2"
        content2e = hr.Element(content2)
        self.e.append(content1)
        self.e.append(content2e)
        return content1, content2, content2e

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
        assert(self.e.build_content("") ==
               "    {}\n"
               "    <>\n"
               "        {}\n"
               "    </>".format(c1, c2))

    def test_build_open_tag(self):
        attrs = {"style": u"text-align:center"}
        self.e = hr.Element(None, **attrs)
        self.e.tag = "p"
        assert(self.e.build_open_tag("") == "<p style=\"text-align:center\">")