import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import string

text = nltk.corpus.gutenberg.words('austen-sense.txt')
print("\nЗагальна кількість слів у тексті:", len(text))

from nltk.probability import FreqDist
fdist = FreqDist(text)
top_ten = fdist.most_common(10)
print("\nДесять найбільш вживаних слів у тексті (враховуючи артиклі та пунктуацію): ",top_ten)

words_raw = [w for w, _ in top_ten]
counts_raw = [c for _, c in top_ten]

plt.figure(figsize=(10,5))
plt.bar(words_raw, counts_raw)
plt.title("Десять найбільш вживаних слів (враховуючи артиклі та пунктуацію)")
plt.xlabel("Слова")
plt.ylabel("Частота")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
stop_words = set(stopwords.words("english"))
punct = set(string.punctuation)
cleaned_words = [
    w.lower() for w in text
    if w.lower() not in stop_words and
       w not in punct and
       w.isalpha()
]

fdist_clean = FreqDist(cleaned_words)
top_ten_clean = fdist_clean.most_common(10)

print("\nДесять найбільш вживаних слів після очищення (не враховуючи артиклі та пунктуацію):", top_ten_clean)

words_clean = [w for w, _ in top_ten_clean]
counts_clean = [c for _, c in top_ten_clean]

plt.figure(figsize=(10,5))
plt.bar(words_clean, counts_clean)
plt.title("Top 10 слів після видалення стоп-слів та пунктуації (не враховуючи артиклі та пунктуацію)")
plt.xlabel("Слова")
plt.ylabel("Частота")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

