import feedparser
from plyer import notification
import time

def parseFeed():
    f = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")
    i = 0
    for newsitem in f['items']:
        notification.notify(
            title=newsitem['title'][:64], # since windows is giving error ValueError: string too long (67, maximum length 64)
            message=newsitem['summary'][:128],
            timeout=15  # Display time (seconds)
        )
        time.sleep(1)
        break # for testing purpose

if __name__ == '__main__':
    parseFeed()
