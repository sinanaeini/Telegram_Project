import hazm
import json
from wordcloud import WordCloud
# import arabic_reshaper
from bidi.algorithm import get_display
from typing import Union
from src.data import data_dir
from pathlib import Path


class ChatResults:
    def __init__(self, data_path: Union[Path, str]):
        with open(data_path) as f:
            self.messages = json.load(f)
        # Normalizing Data
            self.normalizer = hazm.Normalizer()

        # creating stop_words
            stop_words = open(data_dir / 'stop_word.txt')
            stop_words = stop_words.readlines()
            stop_words = map(str.strip, stop_words)
            self.stop_words = list(map(self.normalizer.normalize, stop_words))

    def word_cloud(self, output_dir: Union[Path, str]):
        all_messages = ''

        for item in self.messages['messages']:
            if type(item['text']) is str:
                normalized_messages = self.normalizer.normalize(item['text'])
                tokenized_messages = hazm.word_tokenize(normalized_messages)
                tokenized_messages = list(
                    filter(lambda item: item not in self.stop_words,
                           tokenized_messages))
                all_messages += f" {' '.join(tokenized_messages)}"
                # all_messages = all_messages[:2500]
        # text = arabic_reshaper.reshape(all_messages)
        text = get_display(all_messages)
        wordcloud = WordCloud(
            font_path=str(data_dir/'fonts/NotoNaskhArabic-Regular.ttf'),
            background_color='white'
            ).generate(text)
        # adding ro specific file
        wordcloud.to_file(str(output_dir))


if __name__ == '__main__':
    chatresults = ChatResults(data_dir/'result.json')
    chatresults.word_cloud(data_dir/'output.png')
print('done!')
