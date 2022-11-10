import sqlite3 as lite
import json

# connect to the output database
openwpm_db = "./datadir/crawl-data-new.sqlite"
conn = lite.connect(openwpm_db)
cur = conn.cursor()

urls = []

# get urls
for url, visit in cur.execute("SELECT DISTINCT sites.site_url, sites.visit_id "
                        "FROM site_visits as sites "):
    urls.append([url, visit])

cookies = []
http_only = []
host_only = []
num_cookies = []
most_common = []

# get stats for each url
for url in urls:
    cookies_intermediate = []
    http_intermediate = 0
    host_intermediate = 0
    for name, http, host in cur.execute("SELECT j.host, j.is_http_only, j.is_host_only "
                            "FROM javascript_cookies as j "
                            "WHERE visit_id="+str(url[1])):
        cookies_intermediate.append(name)
        if http==0:
            http_intermediate = http_intermediate + 1
        if host==0:
            host_intermediate = host_intermediate + 1
    cookies.append(cookies_intermediate)
    http_only.append(http_intermediate)
    host_only.append(host_intermediate)
    num = len(cookies_intermediate)
    num_unique = len(set(cookies_intermediate))
    num_cookies.append(num)
    if num_unique == 0:
        most_common.append(["", "", ""])
    elif num_unique < 3:
        inter = []
        for s in set(cookies_intermediate):
            inter.append(s)
        for i in range(3-num_unique):
            inter.append("")
        most_common.append(inter)
    else:
        common_1 = max(set(cookies_intermediate), key = cookies_intermediate.count)
        common_2 = max(set(cookies_intermediate).symmetric_difference(set([common_1])), key = cookies_intermediate.count)
        common_3 = max(set(cookies_intermediate).symmetric_difference(set([common_1, common_2])), key = cookies_intermediate.count)
        most_common.append([common_1, common_2, common_3])

# convert to json
data_dict = {}

for i in range(len(urls)):
    data_dict[urls[i][0]] = {"url": urls[i][0], "cookies": cookies[i], "num_cookies": num_cookies[i], "not_http": http_only[i], "not_host": host_only[i], "common": most_common[i]}

print(data_dict)
with open('data.json', 'w') as f:
    json.dump(data_dict, f)