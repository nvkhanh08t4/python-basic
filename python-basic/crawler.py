import mathematicians
from bs4 import BeautifulSoup


class Crawler:

    def get_data(self, url):
        raw_html = mathematicians.simple_get(url)
        html = BeautifulSoup(raw_html, 'html.parser')
        jobTags = html.find_all('div', class_="job_content")
        info = []
        for tag in jobTags:
            logo = tag.find('div', class_="logo-wrapper")
            img = logo.find('img')
            title = tag.find('h2', class_="title").text
            print('URL logo: ', img['data-src'])
            print('Company Name:', img['alt'])
            print('Job nam', title)



def test(url):
    crawler = Crawler()
    crawler.get_data(url)


if __name__ == '__main__':
    # test('http://www.fabpedigree.com/james/mathmen.htm')
    test('https://itviec.com/it-jobs/da-nang')