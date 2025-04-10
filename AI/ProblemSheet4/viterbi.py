
def viterbi(initial_prob, trans_prob, obser_prob, sequence, observations, hidden_states):
    N = len(hidden_states)
    alpha = [[] for _ in range(N)]
    for i in range(len(sequence)):
        for j in range(N):
            if i == 0:
                alpha[j].append(initial_prob[j] * obser_prob[j][location(observations, sequence[i])])
            else:
                val = 0
                for k in range(N):
                    val = max(val, alpha[k][i-1] * trans_prob[k][j] * obser_prob[j][location(observations, sequence[i])])
                alpha[j].append(val)
    return alpha


def location(observations, seq):
    return observations.index(seq)

if __name__ == "__main__":
    hidden_states = ["hot", "cold"]
    observations = [1, 2, 3]
    initial_prob = [0.8, 0.2]
    trans_prob = [[0.6, 0.4], [0.5, 0.5]]
    obser_prob = [[0.2, 0.4, 0.4], [0.5, 0.4, 0.1]]
    sequence = [3, 1, 3]
    alpha = viterbi(initial_prob, trans_prob, obser_prob, sequence, observations, hidden_states)
    print("alpha : ", alpha)
    path = []
    for i in range(len(alpha[0])):
        index = 0
        val = 0
        for j in range(len(hidden_states)):
            if alpha[j][i] > val:
                index = j
                val = alpha[j][i]
        path.append(hidden_states[index])
    print("path : ", path)

