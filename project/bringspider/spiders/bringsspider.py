import scrapy
import re
import datetime
from dateutil import parser, tz
from datetime import datetime


class Bringsspider(scrapy.Spider):
    name = "bringsspider"
    allowed_domains = ["bringatrailer.com"]
    start_urls = ["https://bringatrailer.com"]

    def parse(self, response):
        """
        Parse the homepage of Bring a Trailer and extract all the links to car listings.
        """
        links = response.xpath("//a[contains(text(), 'Read More')]/@href").getall()
        next_page = response.xpath("//a/span[contains(.,'Older')]/../@href").get()
        for link in links:
            yield scrapy.Request(link, callback=self.parse_item, meta={'link': link, 'page': response.url})
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        else:
            self.crawler.engine.close_spider(self, 'No more pages to scrape')

    def parse_item(self, response):
        """
        Parse a car listing page and extract the title of the car.
        """
        global find_make
        link = response.meta["link"]
        page = response.meta['page']
        Ex_color_list = ['Paint', 'Metallic', 'Silver', 'Red', 'Blue', 'Black', 'Repainted', 'Mettallic', 'White', 'Gray', 'Green','Purple','Exterior','Repaint']
        Int_item_list = ['Upholstery', 'Leather', 'Cloth', 'Cobra', 'Seat', 'Seats', 'Interior', 'Vinyl']
        allowed_category = ['Truck & 4×4', 'Race Cars', 'Hot Rods', 'RVs & Campers', 'Convertibles', 'Station Wagons', 'Vans', 'Car','electric vehicles','pre war']
        car_makers = [
            "Toyota",
            "Volkswagen Group",
            "General Motors",
            "Ford",
            "Honda",
            "Nissan",
            "BMW",
            "Mercedes-Benz",
            "Fiat Chrysler Automobiles",
            "Hyundai",
            "Kia",
            "Subaru",
            "Tesla",
            "Mazda",
            "Renault",
            "Peugeot",
            "Volvo",
            "Jaguar Land Rover",
            "Aston Martin",
            "Ferrari",
            "McLaren",
            "Maserati",
            "Lamborghini",
            "Rolls-Royce",
            "Alfa Romeo"
        ]

        Category = response.xpath("//button/strong[contains(text(),'Category')]/../text()").get()
        Wining_Bid = response.xpath("//tr/td[contains(text(),'Winning Bid') or contains(text(), 'High Bid')]/following-sibling::td/span[1]/text()").get()
        if Wining_Bid is not None:
            Wining_Bid = Wining_Bid.strip().split("$")[1]
            if "(Reserve Not Met)" in Wining_Bid:
                Wining_Bid =Wining_Bid.replace('(Reserve Not Met)', '').strip()
            if Category is None or Category in allowed_category:
                title = response.xpath("//div[1]/div[1]//h1/text()").get()
                car_year = re.search(r'\d{4}', title)
                if car_year:
                    car_year = car_year.group()
                Find_Owner = re.findall(r'(Original-Owner|One-Owner|First-Owner|1st owner)', title)
                Find_Owner = ''.join(Find_Owner)
                if Find_Owner == "":
                    Find_Owner = response.xpath("//ul/li[contains(.,'Original Owner') or contains(., 'First Owner') or contains(.,'One Owner') or contains(.,'1st owner')]/text()").get()
                    if Find_Owner is None:
                        Find_Owner = "NAN"
                    else:
                        Find_Owner = "Original-Owner"
                else:
                    Find_Owner = "Original-Owner"
                Make = response.xpath("//button/strong[contains(text(),'Make')]/../text()").get()
                if Make is None:
                    for word in car_makers:
                        find_make = re.findall(word, title)
                        find_make = ''.join(find_make)
                    Make = find_make
                Project = response.xpath("(//button/strong[contains(text(),'Category')])[last()]/../text()").get()
                if "Projects" == Project:
                    Project = "Y"
                else:
                    Project = "N"
                Comments = response.xpath("//span/span[contains(text(),'Comments')]/preceding-sibling::span/text()").get()
                Reserve = response.xpath("//div/abbr/following-sibling::span/text()").get()
                if Reserve is None:
                    Reserve = "Reserve"

                Model = response.xpath("//button/strong[contains(text(),'Model')]/../text()").get()
                Era = response.xpath("//button/strong[contains(text(),'Era')]/../text()").get()
                Origin = response.xpath("//button/strong[contains(text(),'Origin')]/../text()").get()
                Seller = response.xpath("//div/strong[contains(text(),'Seller')]/following-sibling::a/text()").get()
                Seller_link = response.xpath("//div/strong[contains(text(),'Seller')]/following-sibling::a[1]/@href").get()
                location = response.xpath("//div/strong[contains(text(),'Location')]/following-sibling::a/text()").get()
                if location is None:
                    location = response.xpath("//div/b[contains(text(),'Location')]/a/text()").get()
                Chassis = response.xpath("//ul/li[contains(text(),'Chassis')]/a/text()").get()
                if Chassis is None:
                    Chassis = "Null"
                else:
                    Chassis = response.xpath("//ul/li[contains(text(),'Chassis')]/text()").get().split(":")[1].strip()
                TMU = response.xpath("//ul/li[contains(.,'Miles') or contains(.,'Kilometers') or contains(.,'TMU')]/text()").get()
                if TMU is not None:
                    mileage_in_number = TMU.split(" ")[0]
                    if 'k' in mileage_in_number:
                        mileage_in_number = int(mileage_in_number.replace('k', '')) * 1000
                    elif '-' in mileage_in_number:
                        mileage_in_number = mileage_in_number.split("-")[0]
                    elif mileage_in_number.isalpha():
                        mileage_in_number = "NAN"
                    else:
                        mileage_in_number = mileage_in_number
                    if "TMU" in TMU:
                        Mileage = "TMU"
                    else:
                        Mileage = TMU.split(" ")[1]
                else:
                    mileage_in_number = "Null"
                    Mileage = "NAN"

                Private_Party_or_Dealer =response.xpath("//div/strong[contains(text(),'Private Party or Dealer')]/../text()").get()
                if Private_Party_or_Dealer is None:
                    Private_Party_or_Dealer = response.xpath("//div[contains(text(),'Private Party or Dealer')]/text()").get().split(":")[1]
                else:
                    Private_Party_or_Dealer = Private_Party_or_Dealer.split(":")[1]
                Buyer = response.xpath("//tr/td[contains(text(),'Winning Bid')]/following-sibling::td/span[2]/a/text()").get()
                Views = response.xpath("//tr/td/span[contains(.,'views')]/text()").get()
                if Views is None:
                    Views = "No_Views"
                else:
                    Views = Views.split(" ")[0]
                get_year = response.xpath("//span/span[@class='date']/text()").get().split("/")[-1]
                # year = int(get_year) + 2000
                Watchers = response.xpath("//tr/td/span[contains(.,'watchers')]/text()").get()
                if Watchers is None:
                    Watchers ="No-Wachers"
                else:
                    Watchers = Watchers.split(" ")[0]
                Ext_Color = response.xpath("//ul/li[contains(.,'" + "') or contains(., '".join(Ex_color_list) + "')]/text()").get()
                Int_Color = response.xpath("//ul/li[contains(.,'" + "') or contains(., '".join(Int_item_list) + "')]/text()").get()
                Status = response.xpath("//span/span[@class='date']/../text()").get()
                Bids = response.xpath("//tr/td[contains(text(),'Bids')]/following-sibling::td/text()").get()
                Category = "Car"
                tzinfos = {"PT": tz.gettz("America")}
                Auction = parser.parse(response.xpath("//tr/td[contains(text(),'Auction Ended')]/following-sibling::td/span/text()").get(), tzinfos=tzinfos)
                Auction_obj = datetime.strftime(Auction, "%Y-%m-%d %H:%M:%S")
                Auction_Datetime = datetime.strptime(Auction_obj, "%Y-%m-%d %H:%M:%S")
                day = Auction_Datetime.strftime("%A")
                month = Auction_Datetime.strftime("%B")
                date = Auction_Datetime.strftime("%d")
                year = Auction_Datetime.strftime("%Y")
                time = Auction_Datetime.strftime("%I:%M %p")
                am_pm = time.split(" ")[1]
                proper_time = time.split(" ")[0]
                hour, minute = proper_time.split(":")
                if am_pm == "PM" or "pm":
                    if hour == "12":
                        pass
                    else:
                        hour = int(hour) + 12
                time = str(hour) + str(minute).zfill(2)


                yield {
                    "Page": page,
                    "Auction_url": link,
                    "Auction_title": title,
                    "Car_year": car_year,
                    "Find_Owner": Find_Owner,
                    "Reserve": Reserve,
                    "Exterior_Color": Ext_Color,
                    "Interior_Color": Int_Color,
                    "Year": year,
                    "Make": Make,
                    "Model": Model,
                    "Era": Era,
                    "Origin": Origin,
                    "Category": Category,
                    "Project": Project,
                    "Comments": Comments,
                    "Seller": Seller,
                    "Seller_link": Seller_link,
                    "Private_Party_or_Dealer": Private_Party_or_Dealer,
                    "Buyer": Buyer,
                    "Mileage_in_number": mileage_in_number,
                    "Mileage": Mileage,
                    "location": location,
                    "Chassis": Chassis,
                    "Status": Status,
                    "Winning_Bid": Wining_Bid,
                    "Week_Day": day,
                    "Month": month,
                    "Day": date,
                    "Auction_Year": year,
                    "Time": time,
                    "Bids": Bids,
                    "Views": Views,
                    "Watchers": Watchers,
                }

