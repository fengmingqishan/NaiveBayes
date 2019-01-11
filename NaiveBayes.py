import math


class NaiveBayes(object):

    def wordlist2p(self, wordlists, labels):

        all_words = {}
        for wordList in wordlists:
            for key in set(wordList):
                all_words[key] = all_words.get(key, 0) + 1

        vocab = {}
        pc = {}
        for wordList, label in zip(wordlists, labels):
            pc[label] = pc.get(label, 0) + 1
            for key in set(wordList):
                vocab[label] = vocab.get(label, {})
                vocab[label][key] = vocab[label].get(key, 0) + 1

        sumc = sum(pc.values())
        for key in pc:
            pc[key] = math.log(pc[key] / sumc)

        pwc = {}
        for key in pc:
            sump = sum(vocab[key].values()) + 2
            pwc[key] = {}
            for s in all_words:
                pwc[key][s] = math.log((vocab[key].get(s, 0) + 1) / sump)

        return pwc, pc

    def perdictbydict(self, wordLists, pwc, pc):
        pcw = []
        for wordList in wordLists:
            pcx = {}
            for c in pc:
                pcx[c] = pc[c]
            for word in set(wordList):
                for c in pwc:
                    if word in pwc[c]:
                        pcx[c] += pwc[c][word]
            pcw.append(pcx)
        return pcw

    def pcw2c(self, pcw):
        c = []
        for d in pcw:
            ma = max(d.values())
            cl = [k for k in d if ma == d[k]]
            c.append(cl[0])
        return c
