# Lists for kiterunner

https://github.com/assetnote/kiterunner

Kiterunner's default wordlists containt different API's baseurls:
- /api/v1/
- /v1/
- /rest/
- /api/
- etc.

Wordlists were crafted based on real-world examples - swaggers, github and other.

But what should we do if we know exact API baseurl on target website?

We can't use `kr scan https://example.com/api`, as kiterunner will add baseurls - `/api/api/`, `/api/rest`, etc. will appear.

Using `kr scan https://example.com` is pointless too - a lot of queries for `/rest/`, `/v1` will be useless.

So I removed trailing API's baseurls from default dictionaries and compile .kite files. JSONs are too large and were removed. Here script for JSON transform.


