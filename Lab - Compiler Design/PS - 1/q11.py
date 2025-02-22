from collections import deque, defaultdict

def ndfa_to_dfa(transitions, no_of_states):
    dic = {i: [i] for i in range(no_of_states)}
    for k in range(no_of_states):
        q = deque([k])
        while q:
            to_check_from = q.popleft()
            for i_s, f_s, t_s in transitions: 
                if i_s == to_check_from:
                    if t_s == 'e':
                        if f_s not in dic[k]:
                            dic[k].append(f_s)
                            q.append(f_s)
    print(f"e-closure {dic}")
    return dic

def create_dfa(dic, transitions):   
    transitions_dfa = defaultdict(list)
    for i, f, t in transitions:
        if t != 'e':
            transitions_dfa[t].append((i, f))
        else:
            continue
    
    dfa = {}
    dfa_states = {'A': tuple(dic[0])}
    visited = set()
    visited.add(tuple(dic[0]))
    cnt = 1

    for key, val in dic.items():
        for t in transitions_dfa:
            list_dfa = []
            for value in val:
                for start, end in transitions_dfa[t]:
                    if value == start:
                        list_dfa.extend(dic[end])
            list_dfa = list(set(list_dfa))  
            list_dfa_tuple = tuple(sorted(list_dfa))  

            if list_dfa_tuple not in visited:
                dfa[f'A{cnt}'] = list_dfa_tuple
                visited.add(list_dfa_tuple)
                cnt += 1

    print(f"DFA {dfa}")

if __name__ == '__main__':
    no_of_states = 4
    transitions = [(0, 1, 'e'), (1, 2, 'a'), (2, 1, 'e'), (2, 3, 'e'), (0, 3, 'e')]
    dic = ndfa_to_dfa(transitions, no_of_states)
    create_dfa(dic, transitions)
