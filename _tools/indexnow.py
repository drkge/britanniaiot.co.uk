#!/usr/bin/env python3
"""
Submit the site's URLs to IndexNow.

IndexNow notifies Bing, Yandex, Naver, Seznam and Yep in one call, and needs no
account — ownership is proven by the key file served from the site root. Google
does not participate; it only accepts sitemaps through Search Console, since it
retired its ping endpoint in June 2023.

    python3 _tools/indexnow.py

Run it after publishing new or changed pages. Re-submitting unchanged URLs is
pointless and, done often enough, counts against you.
"""
import json, re, urllib.request, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
HOST = "britanniaiot.co.uk"

cfg = (ROOT / "_config.yml").read_text()
key = re.search(r'indexnow_key:\s*"([^"]+)"', cfg).group(1)

urls = re.findall(r"<loc>(.*?)</loc>",
                  urllib.request.urlopen(f"https://{HOST}/sitemap.xml", timeout=20)
                  .read().decode())
if not urls:
    sys.exit("no URLs found in sitemap.xml")

payload = {"host": HOST, "key": key,
           "keyLocation": f"https://{HOST}/{key}.txt", "urlList": urls}
req = urllib.request.Request(
    "https://api.indexnow.org/IndexNow",
    data=json.dumps(payload).encode(),
    headers={"Content-Type": "application/json; charset=utf-8"})
with urllib.request.urlopen(req, timeout=30) as r:
    print(f"HTTP {r.status} — submitted {len(urls)} URLs")
    print("200 = accepted, 202 = accepted pending key validation")
