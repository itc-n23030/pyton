import requests, os, bs4
url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    print(f'ページをダウンロード中 {url}...')
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    comic_elem = soup.select('#comic img')
    if comic_elem == []:
        print('コミック画像が見つかりませんでした。')
    else:
        comic_url = 'https:' + comic_elem[0].get('src')
        print(f'画像をダウンロード中 {comic_url}...')
        res = requests.get(comic_url)
        res.raise_for_status()

        image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
        
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()
    
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_link.get('href')
print('完了')