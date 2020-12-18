import re
import random
import simhash
import timeit
import logging

TEXT = """
Николай Ушаков.
"Четвёрка".

Их четверка боевая, а фамилии бойцов -
Иваненко, Иванбаев, Иванидзе, Иванов.

Вместе шли они в сраженья через минные поля,
на узлах сопротивленья славу поровну деля.
Не страшили дождь и ночь их, и немало огневых
подавили они точек, не считая запятых.
Воевала дело зная та четверка храбрецов -
Иваненко, Иванбаев, Иванидзе, Иванов.

Шли за Нарев, шли за Вислу и за Одером рекой
стало гитлеровцам кисло от четверки дорогой.
Стало тесно распроклятым – одолел фашистов страх,
та четверка в 45-м заскочила к ним в рейхстаг.
Расписалась боевая на стене без лишних слов:
Иваненко, Иванбаев, Иванидзе, Иванов.

И конец войне – Победа! Все на Родину свою:
на Донец, на Каму едут, на Рион, на Сырдарью.
У друзей такой характер – полон рот у них забот:
тот на шахту, тот на трактор, эти двое на завод.
Трудятся не забывают сотоварищей-бойцов:
Иваненко, Иванбаев, Иванидзе, Иванов."""

_WRE = re.compile(r'\b\S+\b')

words = _WRE.findall(TEXT)

MIN_SAMPLE_WORDS = 10
MAX_SAMPLE_WORDS = 25
NUM_SAMPLES = 1000
TOLERANCE = 6  # <--- Вот это очень влияет на производительность!
SEARCHES = 100

samples = [
    random.sample(
        words,
        random.randint(MIN_SAMPLE_WORDS, MAX_SAMPLE_WORDS)
    ) for _ in range(NUM_SAMPLES)
]
simhashes = [simhash.Simhash(s) for s in samples]

shi = simhash.SimhashIndex([
    (' '.join(s), sh) for s, sh in zip(samples, simhashes)
], k = TOLERANCE)
shi.log.setLevel(logging.ERROR)

def test_dummy():
    result = []
    rsh = random.choice(simhashes)
    for j in range(len(samples)):
        if rsh.distance(simhashes[j]) <= TOLERANCE:
            result.append(samples[j])
    return result

def test_indexed():
    rsh = random.choice(simhashes)
    result = shi.get_near_dups(
        rsh
    )
    return result

print(timeit.timeit(test_dummy, number=SEARCHES))
print(timeit.timeit(test_indexed, number=SEARCHES))
