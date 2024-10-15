import DataDealer as dd
import DecisionTreeGPT as DecisionTree
import random

tHead = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 
         'martial-status', 'occupation', 'relationship', 'race', 'sex', 
         'capital-gain', 'capital-loss', 'hours-per-week', 'income']
training_set = dd.read_data('./adult/adult.data', tHead, 
                           paraNumeric=[0, 2, 4, 10, 11, 12], 
                           paraRemove=[-2])
evaluation_set = dd.read_data('./adult/adult.test', tHead, 
                             paraNumeric=[0, 2, 4, 10, 11, 12], 
                             paraRemove=[-2])

print(f"<<<<<<<<<<TRAIN<<SIZE<<{len(training_set)}<<<")
print(f"<<<<<<<<<<EVALU<<SIZE<<{len(evaluation_set)}<<<")
# print("========DATA SAMPLE============")
# rlst = [random.randint(0, len(training_set)) for _ in range(10)]
# for i in rlst:
#   print(training_set[i])
# print("========DATA SAMPLE============")

tree = DecisionTree.DecisionTree()
tree.fit(training_set, tHead)
# tree.save_model("tree.pkl")
accuracy = tree.test(evaluation_set)
print(f"Model accuracy on evaluation set: {accuracy * 100:.2f}%")