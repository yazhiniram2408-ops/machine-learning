data = [
    ['Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes'],
    ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes'],
    ['No', 'No', 'No', 'No', 'No', 'No'],
    ['Yes', 'No', 'Yes', 'No', 'Yes', 'Yes'],
    ['No', 'Yes', 'No', 'Yes', 'No', 'No'],
    ['Yes', 'Yes', 'Yes', 'No', 'No', 'Yes']
]
S = data[0][:-1]
G = ['?'] * len(S)
for x in data:
    if x[-1] == 'Yes':
        for i in range(len(S)):
            if S[i] != x[i]:
                S[i] = '?'
    else:
        for i in range(len(S)):
            if S[i] != x[i] and S[i] != '?':
                G[i] = S[i]
    print("S=", S, "G=", G)
print("Final S=", S)
print("Final G=", G)
