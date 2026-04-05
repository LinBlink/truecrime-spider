import scrapy
import json
from datetime import datetime
from myspider.items import MyspiderItem

class Spider1Spider(scrapy.Spider):
    name = "spider1"
    allowed_domains = ["www.thetruecrimedatabase.com"]
    start_urls = ["https://www.thetruecrimedatabase.com"]
    progress = 0

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs )

        with open("doc_links.txt", "r", encoding='utf-8') as f:
            self.start_urls = json.load(f)

        # TODO delete
        # self.start_urls = [ self.start_urls[12] ]

        print( self.start_urls )

    def parse(self, response):
        item = MyspiderItem()

        print("🤖Analyzing URL : " + response.url)

        item['org_url'] = response.url

        item['main_character_name'] = response.xpath("""//*[@id="content"]/div/div/section[1]/div/div[1]/div/div[3]/div/h2//text()""").get()

        item['title'] = response.xpath("""
        //*[@id="content"]/div/div/section[1]/div/div[1]/div/div[4]/div/h2//text()
        """).get()

        item['content'] = [
            t.strip()
            for t in response.xpath(
                """
        //*[@id="content"]/div/div/section/div/div/div/section/div/div/div/div/div/p//text()
        """
            ).getall()
            if t.strip()
        ]

        item['source'] = "thetruecrimedatabase.com"

        item['header_img_url'] = response.xpath("""
        /html/head/meta[13]/@content
        """).get()


        img_path_set = response.xpath("""
        /html/body/div[1]/div[2]/div/div/section[2]/div/div[1]/div/section/div/div/div/div/div/figure/img/@data-src
        """).getall()

        img_cap_set = response.xpath("""
        //*[@id="content"]//figure/figcaption/text()
        """).getall()

        img_urls_captions_set = []

        # len of img_cap_set is longer

        for url, caption in zip(img_path_set, img_cap_set):
            img_urls_captions_set.append({
                "url": url,
                "caption": caption.strip()
            })

        item['img_urls_captions'] = img_urls_captions_set

        yt_video_urls = response.xpath("""
        //*[@id="content"]/div/div/section//iframe/@src
        """).getall()

        if yt_video_urls:
            if yt_video_urls[0].startswith("https://www.youtube.com/"):
                for i in range( len(yt_video_urls) ):
                    video_id = yt_video_urls[i].split("/embed/")[-1].split("?")[0]
                    watch_url =  f"https://www.youtube.com/watch?v={video_id}"
                    yt_video_urls[i] = watch_url

        item['yt_video_urls'] = yt_video_urls

        item['author'] = 'Nucleus'

        created_at = response.xpath("""
        //time/text()
        """).get()

        item['created_at'] = datetime.strptime( created_at, "%B %d, %Y" ).strftime("%Y-%m-%d")

        print("✅ DONE Analyzing URL : " + response.url)
        self.progress = self.progress + 1
        print(f"🤔 PROGRESS : {self.progress} / {len(self.start_urls)}")

        yield item