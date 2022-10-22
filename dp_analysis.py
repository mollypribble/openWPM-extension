import sqlite3 as lite

# connect to the output database
openwpm_db = "./datadir/crawl-data.sqlite"
conn = lite.connect(openwpm_db)
cur = conn.cursor()

### EXAMPLE FROM DOCS ###
# # dummy user email and set of first-party sites on which email is leaked
# user_email = "alice.bob@insecure.com"
# fp_sites = set()

# # scans through the database, checking for first parties on which the email is leaked
# for url, top_url in cur.execute("SELECT DISTINCT h.url, v.site_url "
#                                 "FROM http_requests as h JOIN site_visits as v ON "
#                                 "h.visit_id = v.visit_id;"):
#     if user_email in url and url.startswith("http:"):
#         fp_sites.add(top_url)

# # outputs the results
# print(list(fp_sites))
#########################

# short example getting cookies from sites visited during crawl
cookies = set()

for name in cur.execute("SELECT DISTINCT j.name "
                        "FROM javascript_cookies as j "):
    cookies.add(name)

print("Cookies found: ", cookies, "----\n")

# headers
headers = set()

for header in cur.execute("SELECT DISTINCT h.headers "
                        "FROM http_requests as h "):
    headers.add(header)

print("Headers: \n")
for h in headers:
    print(h, "\n")
print("----\n")

