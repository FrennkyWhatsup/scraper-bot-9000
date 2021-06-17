class PageData:
    # adding this is not required, but allows us to see hints when using autocomplete on "PageData('','')."
    # the shortcut for autocomplete is usually "ctrl+space"
    address: str
    description: str
    title: str
    url: str
    # I highly recommend doing:
    # "ctrl+alt+S" -> Plugins -> type "Sublime Text"
    # -> install "Sublime Text Keymap" -> Plugins -> select "Sublime Text"

    # this method defines how we instantiate (create) a PageData object, it is often called the "constructor"
    # examples:
    #       PageData('some title', 'www.python.org', 'some desc')
    #       PageData(description = None, title = "some title", url = "www.python.org", address = "Piccadilly, London")
    #       PageData(None, None)
    # - note that some parameters are required, while others have default values (with "param: type = blah")
    # - also, the order matters, unless you explicitly say PageData(address=None, title="title", ....)
    # - in python, you can use either single quotes or double quotes for strings:
    #   'hello world' is the same as "hello world"
    def __init__(self, title: str, url: str, description: str = "", address: str = None):
        # here we save values of the passed in parameters to our current instance of PageData (stored in "self")
        self.title = title
        self.description = description
        self.url = url
        self.address = address
