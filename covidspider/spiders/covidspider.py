import scrapy

class covidspider(scrapy.Spider):

    name = "covidspider"

    start_urls = ['https://www.mygov.in/corona-data/covid19-statewise-status/']

    def parse(self,response):

        rows = response.css("div.field-item div.content")

        for row in rows:
            rowdata = {}
            for column in row.css("div.field"):
                rowdata[column.css("div.field-label::text").get()[:-2]] = column.css("div.field-item.even::text").get()
            yield rowdata