from pathlib import Path

### IMPORT NEW COMMANDS HERE ###
from dp_custom_command import LinkCountingCommand
################################

from openwpm.command_sequence import CommandSequence
from openwpm.commands.browser_commands import GetCommand
from openwpm.config import BrowserParams, ManagerParams
from openwpm.storage.sql_provider import SQLiteStorageProvider
from openwpm.task_manager import TaskManager

### CHANGE (or pass in) URLS WE WANT TO CRAWL HERE ###
NUM_BROWSERS = 1
sites_original = [
    "http://www.example.com",
    "http://www.princeton.edu",
    "http://citp.princeton.edu/",
]

# testing out how long it takes to run on one site (15-18 secs to crawl and execute custom commands)
sites = [
    "http://www.princeton.edu",
    "https://mollypribble.github.io/openWPM-extension/",
    "http://www.example.com",
    "http://citp.princeton.edu/",

]

sites_final = [
    "https://www.google.com/",
    "https://www.youtube.com/",
    "https://www.northwestern.edu/",
    "http://www.princeton.edu",
    "http://www.example.com",
    "https://www.facebook.com/",
    "https://www.amazon.com/",
    "https://www.reddit.com/",
    "https://www.apple.com/",
    "https://www.yahoo.com/",
    "https://www.wikipedia.org/",
    "https://twitter.com/",
    "https://www.paypal.com/",
    "https://www.paypal.com/us/home",
    "https://www.instagram.com/",
    "https://www.fandom.com/",
    "https://www.bing.com/",
    "https://www.bing.com/?toWww=1&redig=5225224E51B84825A63F1DE1E0007417",
    "https://www.walmart.com/",
    "https://www.twitch.tv/",
    "https://duckduckgo.com/",
    "https://www.tiktok.com/",
    "https://www.linkedin.com/",
    "https://weather.com/",
    "https://www.indeed.com/",
    "https://www.quora.com/",
    "https://www.ebay.com/",
    "https://www.etsy.com/",
    "https://www.cnn.com/",
    "https://www.espn.com/",
    "https://www.fox.com/",
    "https://www.cbs.com/",
    "https://www.nytimes.com/",
    "https://www.imdb.com/",
    "https://www.rottentomatoes.com/",
    "https://www.usps.com/",
    "https://www.office.com/",
    "https://www.microsoft.com/",
    "https://www.microsoft.com/en-us/?ql=4",
    "https://www.zillow.com/",
    "https://www.apartments.com/",
    "https://www.hulu.com/",
    "https://www.hulu.com/welcome",
    "https://www.hbo.com/",
    "https://www.netflix.com/",
    "https://www.pinterest.com/",
    "https://www.wikimedia.org/",
    "https://discord.com/",
    "https://www.foxnews.com/",
    "https://open.spotify.com/",
    "https://spotify.com/",
    "https://www.target.com/",
    "https://www.chase.com/",
    "https://shein.com/",
    "https://us.shein.com/?ref=www&rep=dir&ret=us",
    "https://www.healthline.com/",
    "https://www.webmd.com/",
    "https://mangakakalot.com/",
    "https://www.mcdonalds.com/",
    "https://www.mcdonalds.com/us/en-us.html",
    "https://quizlet.com/",
    "https://github.com/",
    "https://www.samsung.com/",
    "https://www.samsung.com/us/",
    "https://www.msn.com/",
    "https://www.nbc.com/",
    "https://mangago.me/",
    "https://www.homedepot.com/",
    "https://www.att.com/",
    "https://bereal.com/en",
    "https://bereal.com/",
    "https://chicago.craigslist.org/"
    "https://craigslist.org/",
    "https://www.tumblr.com/explore/trending?source=homepage_explore",
    "https://www.tumblr.com/",
    "https://zoom.us",
    "https://stackoverflow.com/",
    "https://www.verizon.com/",
    "https://www.bestbuy.com/",
    "https://imgur.com/",
    "https://www.yelp.com/",
    "https://www.fedex.com/global/choose-location.html",
    "https://www.fedex.com/",
    "https://www.fedex.com/en-us/home.html",
    "https://www.t-mobile.com/",
    "https://www.adobe.com/",
    "https://www.dailymail.co.uk/ushome/index.html",
    "https://www.dailymail.co.uk/",
    "https://www.blogger.com/about/?bpli=1"
    "https://www.blogger.com/",
    "https://www.dickblick.com/?gclid=EAIaIQobChMIwomf7M6m-wIV-QFMCh3CFwIgEAAYASAAEgIT6fD_BwE",
    "https://www.dickblick.com/",
    "https://towardsdatascience.com/",
    "https://medium.com/",
    "https://www.accuweather.com/", 
    "https://www.ticketmaster.com/", 
    "https://www.patreon.com/", 
    "https://www.cvs.com/", 
    "https://www.capitalone.com/",
    "https://www.salesforce.com/",
    "https://www.washingtonpost.com/",
    "https://www.microsoft.com/en-us/microsoft-365/sharepoint/collaboration?ms.officeurl=sharepoint&rtc=1",
    "https://wordpress.com/",
    "https://www.uber.com/",
    "https://www.lyft.com/",
    "https://www.wellsfargo.com/",
    "https://www.nih.gov/",
    "https://www.instacart.com/",
    "https://www.hellofresh.com/",
    "https://steamcommunity.com/",
    "https://www.xfinity.com/overview",
    "https://www.xfinity.com/",
    "https://nypost.com/",
    "https://www.chicagotribune.com/",
    "http://myshopify.com/",
    "https://girlfriend.com/",
    "https://shop.lululemon.com/"
    "https://athleta.gap.com/",
    "https://www.alibaba.com/",
    "https://www.starbucks.com/",
    "https://colectivocoffee.com/",
    "https://www.chicago.gov/city/en.html",
    "https://www.chicago.gov/",
    "https://info.flip.com/",
    "https://neal.fun/deep-sea/",
    "https://www.sheddaquarium.org/",
    "https://disneyworld.disney.go.com/",
    "https://disneyland.disney.go.com/",
    "https://www.universalpictures.com/",
    "https://www.opentable.com/"
]
#######################################################

# Loads the default ManagerParams
# and NUM_BROWSERS copies of the default BrowserParams

# make browser_params display_mode "headless" to run crawl without GUI
manager_params = ManagerParams(num_browsers=NUM_BROWSERS)
browser_params = [BrowserParams(display_mode="headless") for _ in range(NUM_BROWSERS)]

# Update browser configuration (use this for per-browser settings)
for browser_param in browser_params:
    # Record HTTP Requests and Responses
    browser_param.http_instrument = True
    # Record cookie changes
    browser_param.cookie_instrument = True
    # Record Navigations
    browser_param.navigation_instrument = True
    # Record JS Web API calls
    browser_param.js_instrument = True
    # Record the callstack of all WebRequests made
    browser_param.callstack_instrument = True
    # Record DNS resolution
    browser_param.dns_instrument = True

# Update TaskManager configuration (use this for crawl-wide settings)
manager_params.data_directory = Path("./datadir/")
manager_params.log_path = Path("./datadir/openwpm.log")

# memory_watchdog and process_watchdog are useful for large scale cloud crawls.
# Please refer to docs/Configuration.md#platform-configuration-options for more information
# manager_params.memory_watchdog = True
# manager_params.process_watchdog = True


# Commands time out by default after 60 seconds
with TaskManager(
    manager_params,
    browser_params,
    SQLiteStorageProvider(Path("./datadir/dp_final.sqlite")),
    None,
) as manager:
    # Visits the sites
    for index, site in enumerate(sites_final):

        def callback(success: bool, val: str = site) -> None:
            print(
                f"CommandSequence for {val} ran {'successfully' if success else 'unsuccessfully'}"
            )

        # Parallelize sites over all number of browsers set above.
        command_sequence = CommandSequence(
            site,
            site_rank=index,
            callback=callback,
        )

        # Start by visiting the page
        command_sequence.append_command(GetCommand(url=site, sleep=3), timeout=60)

        ### CALL COMMANDS HERE ###
        command_sequence.append_command(LinkCountingCommand())
        ##########################

        # Run commands across all browsers (simple parallelization)
        manager.execute_command_sequence(command_sequence)