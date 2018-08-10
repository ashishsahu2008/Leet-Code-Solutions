'''
https://leetcode.com/problems/encode-and-decode-tinyurl/description/

TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
'''

import random
class Codec:
    def __init__(self):
        self.charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        self.url_short = {}
        self.url_long = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        short = self.url_long.get(longUrl, None)
        if short:
            return short
        else:
            short =  "http://tinyurl.com/{}".format("".join(random.sample(self.charset,5)))
            self.url_short[short] = longUrl
            self.url_long[longUrl] = short
            return short



    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.url_short[shortUrl]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
