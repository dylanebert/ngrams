with open('words') as f:
    words = f.read().splitlines()

dict = {}
with open('counts') as f:
    for line in f:
        ngram, count = line.rstrip().split('\t')
        ngram_split = ngram.split('_')
        if len(ngram_split) < 2:
            continue
        word = ngram_split[0]
        pos = ngram_split[-1]
        if word in words:
            if word not in dict:
                dict[word] = []
            dict[word].append((pos, int(count)))

frequent = []
for k, v in dict.items():
    v.sort(key=lambda x: x[1], reverse=True)
    frequent.append((k, v[0]))

with open('frequent', 'w+') as f:
    for line in frequent:
        f.write('{0}\t{1}\n'.format(line[0], line[1][0]))
