
# truecrime-spider

A Python Scrapy project to crawl and extract case data from [The True Crime Database](https://www.thetruecrimedatabase.com).
This project builds a structured dataset of true crime cases, including case titles, main characters, content, images, captions, videos, authors, and publication dates.

---

## Features

* Crawl all case pages from **thetruecrimedatabase.com**
* Extract structured information:

    * Case title
    * Main character name
    * Full content paragraphs
    * Header image URL
    * All images with captions
    * Embedded YouTube videos (converted to watch URLs)
    * Author
    * Publication date
* Robust parsing with error handling
* Handles inconsistent HTML structure
* Progress reporting in the console
* Ready for MongoDB pipeline integration

---

## Robots.txt Compliance

This project respects the robots.txt rules of thetruecrimedatabase.com
.

The spider only accesses URLs allowed for crawling.
It does not attempt to bypass any restrictions set by the site.
Requests are made responsibly with appropriate download delays to avoid overloading the server.

⚠️ Disclaimer: Before running this spider, users should verify the site's current robots.txt and ensure compliance with all applicable legal and ethical guidelines.

---

## Installation

1. Clone the repository:

```
git clone git@github.com:LinBlink/truecrime-spider.git
cd truecrime-spider
```

2. Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows
```

3. Install dependencies:

```
pip install -r requirements.txt
```

---

## Usage

1. Prepare a `doc_links.txt` file containing JSON list of URLs to crawl. Example:

```json
[
    "https://www.thetruecrimedatabase.com/case_file/1/",
    "https://www.thetruecrimedatabase.com/case_file/2/"
]
```

2. Run the spider:

```
scrapy crawl spider1 -o output.json
```

* This will save extracted case data to `output.json`.
* Progress will be displayed in the console.

---

## Project Structure

```
truecrime-knowledge-base/
│
├─ myspider/
│   ├─ __init__.py
│   ├─ items.py          # Scrapy Item definitions
│   ├─ pipelines.py      # Optional: MongoDB pipeline
│   └─ spiders/
│       └─ spider1.py    # Main spider
│
├─ doc_links.txt         # List of case URLs
├─ requirements.txt
└─ README.md
```

---

## Data Output Example

```json
{
  "org_url": "https://www.thetruecrimedatabase.com/case_file/0791/",
  "main_character_name": "Nancy Guthrie",
  "title": "The Arizona Mystery",
  "content": ["Paragraph 1 text...", "Paragraph 2 text..."],
  "source": "thetruecrimedatabase.com",
  "header_img_url": "https://www.thetruecrimedatabase.com/images/header.jpg",
  "img_urls_captions": [
    {"url": "https://www.thetruecrimedatabase.com/images/1.jpg", "caption": "Crime scene photo"},
    {"url": "https://www.thetruecrimedatabase.com/images/2.jpg", "caption": "Evidence"}
  ],
  "yt_video_urls": ["https://www.youtube.com/watch?v=abc123"],
  "author": "Nucleus",
  "created_at": "2026-02-14"
}
```

---

## Future Improvements

* MongoDB integration via Scrapy pipeline
* Pagination support to crawl all cases automatically
* Background image extraction from Elementor sections
* Build a knowledge graph or analytics dashboard for true crime cases
* API endpoints for front-end applications

---

## Contact

For questions or collaboration, reach out to **linkoku99@gmail.com**.

---

