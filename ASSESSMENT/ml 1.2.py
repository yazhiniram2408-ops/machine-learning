
data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Same', 'Yes'],
    ['Rainy', 'Warm', 'Normal', 'Weak', 'Warm', 'Same', 'No'],
    ['Sunny', 'Warm', 'Normal', 'Weak', 'Warm', 'Same', 'Yes']
]

h = ['0'] * (len(data[0]) - 1)

print("Steps of Find-S Algorithm:\n" + "-"*30)


for step, row in enumerate(data, 1):
    if row[-1] == 'Yes':
        if h[0] == '0':
           
            h = list(row[:-1])
        else:
           
            for i in range(len(h)):
                if h[i] != row[i]:
                    h[i] = '?'
    print(f"Instance {step} -> Hypothesis: {h}")

print("-"*30)
print("Final Hypothesis:", h)
