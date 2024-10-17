import DataDealer as DD
from DecisionTreeGini import DecisionTreeGini as DT

tHead = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 
         'martial-status', 'occupation', 'relationship', 'race', 'sex', 
         'capital-gain', 'capital-loss', 'hours-per-week', 'income']
numericIndex = [0, 2, 4, 10, 11, 12]
training_set = DD.read_data('./adult/adult.data', tHead, 
                           paraNumeric= numericIndex, 
                           paraRemove=[-2])
evaluation_set = DD.read_data('./adult/adult.test', tHead, 
                             paraNumeric=numericIndex, 
                             paraRemove=[-2], isTest=True)
TREE_MIN_SAMPLE_SPLIT = 10
TREE_MAX_DEPTH = 5

print(f"traing data size: {len(training_set)}\t evaluation data set: {len(evaluation_set)}")
print(f"min_samples_split={TREE_MIN_SAMPLE_SPLIT}, max_depth={TREE_MAX_DEPTH}")

tEncoded_data, tValue_dicts = DD.label_encode(training_set)
tFeatures = [list(data.values())[:-1] for data in tEncoded_data]
tLabels = [data['income'] for data in tEncoded_data]
print("========== TRAINING MODEL on Training SET ==========")
tree = DT(TREE_MIN_SAMPLE_SPLIT, TREE_MAX_DEPTH, numericIndex)
tree.tree = tree.fit(tFeatures, tLabels)
print("========== TRAINING MODEL FINISHED ==========")

print("========== EVALUATION on Training SET ==========")
tPredictions = tree.predict(tFeatures)
DD.print_model_evaluation_result(tEncoded_data, tPredictions)

print("========== EVALUATION on Evaluation SET ==========")
eEncoded_data, eValue_dicts = DD.label_encode(evaluation_set, tValue_dicts)
assert eValue_dicts == tValue_dicts
eFeatures = [list(data.values())[:-1] for data in eEncoded_data]
ePredictions = tree.predict(eFeatures)
DD.print_model_evaluation_result(eEncoded_data, ePredictions)

print("========== DECISION TREE RESULT ==========")
DD.TreePrinter(tree.tree, tHead, eValue_dicts).print_tree()