from sklearn import tree

# [heigh, weight, shoes size]
X = [
    [181, 80, 44], [177, 70, 43], [160, 60, 38],
    [166, 65, 40], [190, 90, 47], [175, 64, 39],
    [177, 70, 40], [171, 75, 42], [181, 85, 43]
]
Y = [
    'male', 'female', 'female',
    'male', 'male', 'female',
    'female', 'male', 'male'
]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

prediction = clf.predict([[173, 83, 44]])

print(prediction)
