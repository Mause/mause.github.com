# /// script
# requires-python = ">=3.14"
# dependencies = ['pytest']
# ///


from html.parser import HTMLParser
from urllib.request import urlopen
import pytest
from pytest import mark


@mark.parametrize(
    "url,title",
    [
        ("/", "Home"),
        ("/blog", "Blog"),
        ("/projects/bytemore", "Bytemore"),
        # "/.well-known/webfinger",
        ("/post/blog/2019-10-14-NDC", "NDC Sydney 2019"),
    ],
)
def test_main(url: str, title: str) -> None:
    r = urlopen("http://localhost:1313/" + url).read().decode()

    parser = GetTitle()
    parser.feed(r)
    parser.close()

    actual_title = parser.data

    assert f"{title} | Elliana May" == actual_title


class GetTitle(HTMLParser):
    catch = False

    def handle_starttag(self, tag, attrs):
        self.catch = tag == "title"

    def handle_data(self, data):
        if self.catch:
            self.data = data

    def handle_endtag(self, tag):
        if self.catch and (tag == "title"):
            self.catch = False


if __name__ == "__main__":
    pytest.main([__file__])
