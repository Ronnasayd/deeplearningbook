#!/bin/bash
scrapy crawl deeplearningbookspyder -o data.json
python3 generate.py