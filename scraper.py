import scraperwiki
import lxml.html
html = scraperwiki.scrape("http://www.globalcontact.com/gc/directory/search.php?table=USDIR&company=a&search=&search_sic=&page=2")
root = lxml.html.fromstring(html)
root.cssselect("div[align='left']")
scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
scraperwiki.sql.select("* from data where 'name'='peter'")
