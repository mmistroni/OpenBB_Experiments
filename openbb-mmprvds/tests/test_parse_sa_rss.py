import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        import feedparser

        d = feedparser.parse('https://seekingalpha.com/feed/dividends/editors-picks')
        #'https://seekingalpha.com/feed/stock-ideas')#)



        for item in d['entries']:
            print(f"title:{item['title']}, link:{item['link']}, published:{item['published']}")
            if 'category' in item:
                print(f"tickers:{item['category']}")


if __name__ == '__main__':
    unittest.main()
