from lxml import html

body = html.fromstring('committees_2015.html')
committee_rows = body.xpath('//*[@id="committeeSearchResults"]/tbody/tr')
body.getchildren()
committee_rows
