from scrapy.contrib.spiders.init import InitSpider
from scrapy.http import Request, FormRequest
from scrapy.selector import HtmlXPathSelector
# from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
# from scrapy.contrib.spiders import Rule

class LinkedinSpider(InitSpider):
    name="linkedin"
    allowed_domains=["linkedin.com"]
    login_page='https://www.linkedin.com/uas/login'
    start_urls = [
        "https://www.linkedin.com/vsearch/p?openAdvancedForm=true&locationType=Y&f_N=O&f_I=14&rsid=1999536361430921346774&orig=ADVS"
    ]

    def init_request(self):
        return Request(url=self.login_page, callback=self.login)

    def login(self, response):
        return FormRequest.from_response(
            response,
            formdata={'session_key': 'jerryc0502@gmail.com', 'session_password': 'zt885210'},
            callback=self.check_login_response)

    def check_login_response(self, response):
        if "Sign Out" in response.body:
            self.log("\n\n\nSuccessfully logged in. Let's start crawling!\n\n\n")
            return self.initialized()
        else:
            self.log("\n\n\nFailed, Bad times :(\n\n\n")



    def parse(self, response):
        self.log("\n\n\n We got data! \n\n\n")
        filename = "linked_test"
        hxs = HtmlXPathSelector(response)
        code_js = hxs.select('//code[@id=\'voltron_srp_main-content\']')
        with open(filename, 'wb') as f:
            f.write(str(code_js.extract()))
