from scraper_lib import PageReader
from site_data import PageData


class TestBot:
    # 'xpath' is just a string "path" from the page root (the 'html' element) to
    # the element we need
    # image the webpage as an "up-side down tree" of elements, with the root being 'html'
    # example
    # <html> <--- the root aka. top level
    #     <div id="content-blah"> <---- layout block with an ID
    #         <p class="regular-text"> <--- paragraph element with class 'regular-text'
    #             text paragraph             (these are used to apply styling / layout behaviour)
    #         </p>
    #     <div>
    # </html>
    get_started_title = '//*[@id="content"]/div/section/div[1]/div[1]/h2'
    get_started_description = '//*[@id="content"]/div/section/div[1]/div[1]/p[1]'
    url = "http://www.python.org"

    def read_page_data(self) -> PageData:
        #                   '-> PageData' lets whoever uses this method know what it returns
        #                            (functions on a class are called methods)
        with PageReader(self.url) as pythonHomePage:
            # 'with' statement ensures 'pythonHomePage.close()' is called automagically
            # when we exit this code block

            title = pythonHomePage.get_element(self.get_started_title).text
            description = pythonHomePage.get_element(self.get_started_description).text
            return PageData(title, self.url, description + self.asdasdas())
