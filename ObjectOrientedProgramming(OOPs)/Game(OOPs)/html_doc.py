class Tag(object):
    def __init__(self, name, contents):                 # now here, 'tag' class constructor initializes the init method, accepts a name for the tag and its contents
        self.start_tag = '<{}>'.format(name)            # it then uses string formatting to create the start and end tags and stores the contents in the self.contents data attribute
        self.end_tag = '<{}>'.format(name)              # Now the string method, the __str__method will return the complete string for the tag so that's the opening tag followed by the contents and finishing ith closing tags
        self.contents = contents                        # and also created display() method tto display instance out

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):
    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = ''      # DOCTYPE doesn't have an end tag


# So, DocType inherits from tag & uses super method to initialize itself with DTD, now 'doctype' doesn't have any contents and there's also no closing tag
# so, we are setting that the closing tag to an empty string

class Head(Tag):
    def __init__(self, head):               # title=None
        super().__init__('head', '')
        # if title:
        #     self._title_tag = Tag('title')        # title
        #     self.contents = str(self._title_tag)


class Body(Tag):
    def __init__(self):
        super().__init__('body', '')            # Body contents will be built up separately
        self._body_contents = []

    def add_tag(self, name, contents):                # for body class we're inheriting from the tag class,
        new_tag = Tag(name, contents)                 # but we initialize the contents to an empty string when calling the super method because we don't want to 'contents' to be created just yet
        self._body_contents.append(new_tag)           # that's because we're going to store all the contents and list as you can probably ascertain in the attribute self._body_contents.

    def display(self, file=None):                                # so we initialize that to an empty list in the constructor
        for tag in self._body_contents:               # add_tag method is used to add the contents to our body & we give it a name of a tag & contents & it creates a new tag instance & appends that to the body contents list
            self.contents += str(tag)

        super().display(file=file)


class HtmlDoc(object):              # our HtmlDoc class is made up of instances of 3 other classes

    def __init__(self, doc_type, head, body):                 # title=None
        self._doc_type = doc_type                      # DocType()
        self._head = head                    # Head()             # title
        self._body = body                           # Body()

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)            # DTD is displayed by calling the doc type instances display method
        print("<html>", file=file)                     # now after DTD everything else is enclosed in HTML opening and closing tag
        self._head.display(file=file)
        self._body.display(file=file)
        print("<html>", file=file)


if __name__ == '__main__':
    # my_page = HtmlDoc()                     # 'Demo HTML Document'
    # my_page.add_tag('H1', 'Main Heading')
    # my_page.add_tag('H2', 'Sub-heading')
    # my_page.add_tag('p', 'this is a paragraph what will appear on the webpage')
    # with open('test.html', 'w') as test_doc:
    #     my_page.display(file=test_doc)
    # my_page.display()

    new_body = Body()
    new_body.add_tag('h1', 'Aggregation')
    new_body.add_tag('p', "Unlike <strong>composition</strong>, aggregation uses existing instances"
                          "of objects to build up another object.")
    new_body.add_tag('p', " The supposed object doesn't actually own the objects that it's composed of "
                          " - If it's destroyed, those objects continue to exists")

    new_docType = DocType()
    new_header = Head("Aggregation document")
    my_page = HtmlDoc(new_docType, new_header, new_body)

    with open('test3.html', 'w') as test_doc:
        my_page.display(file=test_doc)

# Give our document new content by switching its body
# my_page._body = new_body
# with open('test2.html', 'w') as test_doc:
#     my_page.display(file=test_doc)


#
# So in this program we've implemented polymorphism without using inheritance, we've used composition instead.
# Now program itself does use inheritance all our other classes inherit from tag but the HtmlDoc type isn't a subclass of tag,
# It provides the same methods as their tags, but does so by defining same names & then delegating the implementation of those methods to the classes that is composed of.
































































