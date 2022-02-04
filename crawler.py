import re
import requests
from bs4 import BeautifulSoup


class Crawler:

    def text_extractor(self, text: str):
        final_text = re.sub("[^\w\s]", "", text)
        return final_text.split()

    def tabnak_crawler_job(self, date, to_date):
        pg = 1
        extracted_words = []
        while True:
            page = requests.get(f"https://www.tabnak.ir/fa/archive?service_id=-1&sec_id=-1&cat_id=-1&rpp=100&from_date={date}&to_date={to_date}&p={pg}")
            soup = BeautifulSoup(page.content, "html.parser")

            titles = soup.find_all("a", {"class": "title5"})
            for title in titles:
                for word in self.text_extractor(title.text):
                    extracted_words.append(word)
            
            if len(titles) == 0:
                break
            else:
                pg += 1
        return extracted_words

    def yjc_crawler_job(self, date, to_date):
        pg = 1
        extracted_words = []
        titles_set = set()
        while True:
            page = requests.get(
                f"https://www.yjc.news/fa/archive?service_id=-1&sec_id=-1&cat_id=-1&rpp=100&from_date={date}&to_date={to_date}&p={pg}")
            soup = BeautifulSoup(page.content, "html.parser")

            titles = soup.find_all("a", {"class": "title5"})
            for title in titles:
                if title in titles_set:
                    return extracted_words
                else:
                    titles_set.add(title)
                for word in self.text_extractor(title.text):
                    extracted_words.append(word)

            if len(titles) == 0:
                break
            else:
                pg += 1
        return extracted_words

if __name__ == "__main__":
    # x = Crawler().tabnak_crawler_job('1400/11/11', '1400/11/11')
    x = Crawler().yjc_crawler_job('1400/11/11', '1400/11/11')
    print(x)
    print(len(x))