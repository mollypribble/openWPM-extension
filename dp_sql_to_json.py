import sqlite3 as lite
import json

# connect to the output database
openwpm_db = "./datadir/dp_final.sqlite"
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
cookies_color = []
http_color = []
host_color = []

# set percentiles for cookies, http_only, host_only
cookies_25 = 20.0
cookies_75 = 143.5
http_25 = 13.0
http_75 = 126.5
host_25 = 14.5
host_75 = 122.5

# get stats for each url
for url in urls:

    # get all cookies, http_only counts, and host_only counts
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
    
    # append cookies, http, host counts
    cookies.append(cookies_intermediate)
    http_only.append(http_intermediate)
    host_only.append(host_intermediate)
    num = len(cookies_intermediate)
    num_cookies.append(num)

    # append set of 3 most common cookies (if exist)
    num_unique = len(set(cookies_intermediate))
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
    
    # append class for num cookies, http, host
    if num >= cookies_75:
        cookies_color.append("#F7B0BB");
    elif num <= cookies_25:
        cookies_color.append("#C6E7BD");
    else:
        cookies_color.append("#B7D5EB");

    if http_intermediate >= http_75:
        http_color.append("#F7B0BB");
    elif http_intermediate <= http_25:
        http_color.append("#C6E7BD");
    else:
        http_color.append("#B7D5EB");

    if host_intermediate >= host_75:
        host_color.append("#F7B0BB");
    elif host_intermediate <= host_25:
        host_color.append("#C6E7BD");
    else:
        host_color.append("#B7D5EB");

# convert to json
data_dict = {}

for i in range(len(urls)):
    data_dict[urls[i][0]] = {"url": urls[i][0], "cookies": cookies[i], "num_cookies": num_cookies[i], "not_http": http_only[i], "not_host": host_only[i], "common": most_common[i], "cookie_color": cookies_color[i], "http_color": http_color[i], "host_color": host_color[i]}

# add this for debugging on gh site
data_dict['https://mollypribble.github.io/openWPM-extension/'] = {"url": 'https://mollypribble.github.io/openWPM-extension/', "cookies": [], "num_cookies": 3, "not_http": 2, "not_host": 1, "common": ["this", "is", "fake"], "cookie_color": "#F7B0BB", "http_color": "#C6E7BD", "host_color": "#B7D5EB"}

print("Converted data from", len(data_dict), "sites to JSON.")
print(data_dict)

with open('data.json', 'w') as f:
    json.dump(data_dict, f)