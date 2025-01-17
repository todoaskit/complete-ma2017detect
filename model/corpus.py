import numpy as np


class BaseCorpus:

    def __init__(self, vocab, word_ids, word_cnt, n_topic):
        self.vocab = np.array(vocab)
        self.n_voca = len(vocab)

        self.word_ids = word_ids
        self.M = len(word_ids)

        self.word_cnt = word_cnt

        self.A = np.random.gamma(shape=1, scale=1, size=[self.M, n_topic])
        self.B = np.random.gamma(shape=1, scale=1, size=[self.M, n_topic])

        self.Nm = np.array([sum(word_cnt[i]) for i in range(self.M)])
