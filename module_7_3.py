import string# - import string позволяет работать с предопределенными строковыми константами,
# например, с символами пунктуации.

class WordsFinder:
    def __init__(self, *file_names):#  # Конструктор класса принимает произвольное количество названий файлов
        self.file_names = file_names# # Сохраняем названия файлов в виде аргументов
# Метод get_all_words
#    - Создает словарь all_words, который будет хранить названия файлов как ключи и списки слов как значения.
    def get_all_words(self):
        all_words = {}# Создаем пустой словарь для хранения слов из файлов
        for file_name in self.file_names:# Перебираем все названия файлов
            with open(file_name, 'r', encoding='utf-8') as file:# Открываем файл с кодировкой UTF-8
                words = file.read().lower()# Считываем содержимое файла и переводим в нижний регистр
                for punct in string.punctuation.replace('-', ''):# Убираем пунктуацию, кроме '-'
                    words = words.replace(punct, '') # Заменяем пунктуацию на пустую строку
                all_words[file_name] = words.split()# Разбиваем строку на слова и сохраняем в словарь
        return all_words# Возвращаем словарь с названиями файлов и списками слов

# Метод find ищет заданное слово в файлах. Создает словарь word_position, где ключ - название файла,
# а значение - список позиций (индексов) вхождений слова.
    def find(self, word):
        word_position = {} #  # Словарь для хранения позиций искомого слова
        for name, words in self.get_all_words().items(): # Перебираем файлы и их слова
            for i, w in enumerate(words): # Перебираем слова с индексами
                if w == word.lower():# Если слово совпадает с искомым (в нижнем регистре)
                    if name not in word_position.keys():# Проверяем наличие файла в словаре
                        word_position[name] = []# Если нет, создаем список
                    word_position[name].append(i+1)# Сохраняем позицию (индекс + 1)
        return word_position # Возвращаем словарь с позициями

#   Метод find ищет заданное слово в файлах. Создает словарь word_position, где ключ - название файла,
#    а значение - список позиций (индексов) вхождений слова.
    def count(self, word):
        word_counts = {} # Словарь для хранения количества искомого слова
        for name, words in self.get_all_words().items():  # Перебираем файлы
            word_counts[name] = words.count(word.lower()) # Считаем количество вхождений слова
        return word_counts # Возвращаем словарь с количеством слов
finder = WordsFinder('module_7/test_file.txt')
print(finder.get_all_words())
print(finder.find('TEXT'))
print(finder.count('teXT'))


