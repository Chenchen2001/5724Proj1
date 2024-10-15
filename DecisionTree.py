"""
 algorithm Hunt(S)
 /* S is the training set; the function returns the root of a decision tree */
 1. if all the objects in S belong to the same class
 2.   return a leaf node with the value of this class
 3. if (all the objects in S have the same attribute values) or (|S| is too small)
 4.   return a leaf node whose class value is the majority one in S
 5. find the “best” split attribute A∗ and predicate P∗ using GINI
 6. S1 ← the set of objects in R satisfying P∗; S2 ← S \S1
 7. u1 ← Hunt(R1); u2 ← Hunt(R2)
 8. create a root u with left child u1 and right child u2
 9. set Au ← A∗ and Pu ←P∗
 10. return u
"""
import pickle
import DataDealer as dd

class DecisionNode: # For store the nodes of tree
  def __init__(self, attribute=None, predicate=None, left_child=None, right_child=None):
    self.attribute = attribute
    self.predicate = predicate
    self.left_child = left_child
    self.right_child = right_child

class ResultTree: # For store the result
  def __init__(self, value):
    self.value = value

class DecisionTree:
  def __init__(self, dataset: list[dict], label: str, SMALLEST_DATASIZE:int = 10):
    self.root = DecisionNode() # 根节点
    self.dataset = dataset # 数据集
    self.label = label # 目标变量
    self.SMALLEST_DATASIZE = SMALLEST_DATASIZE
    self.freq = dd.count_frequencies(self.dataset)

  def fit(self, dataset, labels):
    self.labels = labels
    self.root = self.hunt(dataset)

  def hunt(self, dataset: list[dict]):
    # Algo line 1-2
    label_types = set([e[self.label] for e in dataset])
    if(len(label_types) == 1):
      return ResultTree(
        DecisionNode(self.label, dd.get_sorted_list_value(self.freq, self.label)[0][0])
        )
    # Algo line 3-4
    if(self.if_all_attr_has_same_value_inside() or len(dataset) <= self.SMALLEST_DATASIZE):
      return ResultTree(
        DecisionNode(self.label, dd.get_sorted_list_value(self.freq, self.label)[0][0])
        )
    # Algo line 5
    best_attribute, best_predicate = self.find_best_split(dataset)

  def if_all_attr_has_same_value_inside(self) -> bool:
    local_freq = dict(self.freq)
    local_freq.pop(self.label)
    for attr in local_freq:
      if len(local_freq[attr]) > 1:
        return False
    return True
  
  def get_gini(self, key: str , split: int|str) -> float:
    p_y = 0
    p_n = 0
    if(type(split) is int):
      for i in dd.get_sorted_list_key(self.freq, key):
        if(i[0] < split):
          p_y += i[1]
        else: 
          p_n += i[1]
    elif(type(split) is str):
      for i in dd.get_sorted_list_key(self.freq, key):
        if(i[0] == split):
          p_y += i[1]
        else: 
          p_n += i[1]
    return 1-(p_y/(p_y+p_n))**2-(p_n/(p_y+p_n))**2
    
  def find_best_split(self, dataset):
    ...

  def predict(self, row, node):
    ...

  def test(self, dataset):
    ...
    
  def save_model(model, filename):
    with open(filename, 'wb') as file:
      pickle.dump(model, file)
      print(f"model saved at ./{filename}")

  def load_model(filename):
    with open(filename, 'rb') as file:
      model = pickle.load(file)
    return model