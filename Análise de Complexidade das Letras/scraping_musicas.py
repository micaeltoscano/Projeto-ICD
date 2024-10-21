import requests
from bs4 import BeautifulSoup
import pandas as pd

musicas = {
    "the-river": "bruce-springsteen",
    "for-the-love-of-money": "the-o-jays",
    "the-unknown-soldier": "the-doors",
    "solsbury-hill": "peter-gabriel",
    "strange-fruit": "billie-holiday",
    "the-fight-songs": "the-lumineers",
    "the-impression-that-i-get": "the-mighty-mighty-bosstones",
    "paper-thin-hymn": "the-format",
    "fast-car": "tracy-chapman",
    "mister-tambourine-man": "bob-dylan",
    "a-pair-of-jesus-sandals": "the-arcade-fire",
    "the-hurricane": "bob-dylan",
    "let-it-be": "the-beatles",
    "the-wait": "the-band",
    "the-box": "the-jayhawks",
    "a-whiter-shade-of-pale": "procol-harum",
    "the-mountain": "hozier",
    "the-pusher": "steppenwolf",
    "zombie": "the-cranberries",
    "the-last-dance": "elton-john",
    "sitting-on-top-of-the-world": "the-rawlings",
    "somebody-that-i-used-to-know": "gotye",
    "the-future": "leonard-cohen",
    "the-boy-is-mine": "brandy-and-monica",
    "the-winter": "the-winter",
    "feeling-good": "michael-buble",
    "the-philosophers-stone": "van-morrison",
    "i-am-a-rock": "paul-simon",
    "fanfare-for-the-common-man": "aaron-copland",
    "dreams-are-my-reality": "the-alexander-brothers",
    "the-prophecy": "the-who",
    "the-moon-song": "karmin",
    "the-crucifixion": "the-pitch",
    "the-old-man": "the-old-man",
    "foolish-games": "jewel",
    "the-riddle": "nik-kershaw",
    "the-sorrows": "the-sorrows",
    "the-hitchhiker": "the-hitchhiker",
    "the-painting": "the-painting",
    "the-comforting-sound": "mew",
    "the-last-great-american-novel": "the-last-great-american-novel",
    "the-garden": "the-garden",
    "the-storm": "the-storm",
    "the-call": "regina-spektor",
    "the-lighthouse": "the-lighthouse",
    "the-beat-goes-on": "sonny-and-cher",
    "the-age-of-adaline": "the-age-of-adaline",
    "the-story": "brandi-carlile"
}

dic = {"artist": [], "track_name": [], "lyrics": []}

try:
    df = pd.read_csv('dataset_complexo.csv')
except FileNotFoundError:
    df = pd.DataFrame(dic)

for track_name, artist in musicas.items():
    url = f'https://www.letras.mus.br/{artist}/{track_name}/'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        lyric_div = soup.find('div', class_='lyric-original')
        
        if lyric_div:
            lyrics_with_breaks = lyric_div.decode_contents()

            if ((df['track_name'] == track_name) & (df['artist'] == artist)).any():
                df.loc[(df['track_name'] == track_name) & (df['artist'] == artist), 'lyrics'] = lyrics_with_breaks
            else:
                new_row = pd.DataFrame({'artist': [artist], 'track_name': [track_name], 'lyrics': [lyrics_with_breaks]})
                df = pd.concat([df, new_row], ignore_index=True)
        else:
            print("Div não encontrada.")

    else:
        print("Falha ao acessar a página:", response.status_code)

df.to_csv('dataset_complexo.csv', index=False)