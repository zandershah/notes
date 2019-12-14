import argparse
import os
import random

parser = argparse.ArgumentParser(description='Study Vocabulary')
parser.add_argument('-c', '--character', action='store_true')
parser.add_argument('-p', '--pinyin', action='store_true')
parser.add_argument('-a', '--all', action='store_true')
args = parser.parse_args()
BATCH_SIZE = 10

vocab = []

for lesson in filter(lambda f: f.endswith('.txt'), os.listdir()):
    with open(lesson, 'r') as f:
        for line in f.readlines():
            vocab.append(line.rstrip('\n').split(' ', 1))

random.shuffle(vocab)

if args.all:
    for character, pinyin in vocab:
        print(character, pinyin)
else:
    v = 0
    while v < len(vocab):
        for i in range(v, min(v + BATCH_SIZE, len(vocab))):
            character, pinyin = vocab[i]

            if args.character:
                print(character)
            if args.pinyin:
                print(pinyin)

        _ = input()

        for i in range(v, min(v + BATCH_SIZE, len(vocab))):
            character, pinyin = vocab[i]
            print(character, pinyin)

        v += BATCH_SIZE
        print(f'\n{v}/{len(vocab)}')

        _ = input()

