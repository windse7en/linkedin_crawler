import scrapy

class LoginSpider(scrapy.Spider):
    name="login"
    allowed_domains=["linkedin.com"]
    start_urls=[
        'http://www.linkedin.com/nhome/',
        'https://www.linkedin.com/vsearch/p?openAdvancedForm=true&locationType=Y&f_N=O&f_I=47&rsid=1999536361430933449298&orig=ADVS'
    ]

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'ession_key':'jerryc0502@gmail.com', 'session_password': 'zt885210'},
            callback=self.after_login
        )

    def after_login(self, response):
        filename = "after_login"
        with open(filename, 'wb') as f:
            f.write(response.body)

