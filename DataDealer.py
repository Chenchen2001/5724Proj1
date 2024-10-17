"""
  This module is customized for the adult dataset.
  The dataset can be got from https://archive.ics.uci.edu/dataset/2/adult.
  Designed for CUHK CMSC5724 24Fall Project 1.
"""
from collections import defaultdict


def read_data(path: str, tHead: list['str'], paraNumeric: list[int]=[], paraRemove: list[int]=[], isTest: bool = False) -> list[dict]:
  """
    This function will read the named data and give out a list with dicts read from the file.
    Data line with '?' will not be stored and returned.
    Can customize for removeing named variable.
    
    Args:
      path: the path of the data to read
      tHead: the header of the table to be read
      paraNumeric: data in the file to be converted to integer
      varRemove: data in the file required to be removed
      isTest: whether the input data is 'adult.test' as it appears a more dot at the end of each line.
    
    Returns:
      A data list read from the file named. Each data line is presented in a dict.
  """
  resData = []
  with open(path, 'r') as data:
    for line in data:
      if(isTest):
        line = line[:-2]
      ldata = line.strip()
      if(ldata):
        ldata = ldata.split(", ")
        if('?' not in ldata and len(ldata) > 1):
          if(paraNumeric):
            for num in paraNumeric:
              ldata[num] = int(ldata[num])
          if(paraRemove): 
            for rem in paraRemove:
              del ldata[rem]
          assert len(ldata) == len(tHead)
          resData.append(dict(zip(tHead, ldata)))
  return resData

def count_frequencies(data: list[dict]) -> dict:
  """
    Statictic the frequence of each attribute in the data.
    
    Args:
      data: The data in type of list with dict as elements.

    Returns:
      A dict with statictical data.
  """
  frequency = {}
  for record in data:
    for key, value in record.items():
      if key not in frequency:
        frequency[key] = {}
      if value not in frequency[key]:
        frequency[key][value] = 0
      frequency[key][value] += 1
  return frequency

def get_sorted_list_value(data: dict, key: str|int ,desending=True) -> list:
  """
    Sort the frequence of each attribute in the data by value.

    Args:
      data: The data in type of list with dict as elements.
      key: The key of dict
      desending: True default, return desended list based on number of each value.
    
    Returns:
      A sorted data list with tuple (value, numbers).
  """
  return sorted(data[key].items(), key=lambda item: item[1], reverse=desending)

def get_sorted_list_key(data: dict, key: str | int, desending=False) -> list:
  """
    Sort the frequency of each attribute in the data by key.

    Args:
      data: The data in type of list with dict as elements.
      key: The key of dict.
      desending: False by default, return ascending list based on the key.
      
    Returns:
      A sorted data list with tuple (value, numbers).
  """
  return sorted(data[key].items(), key=lambda item: item[0], reverse=desending)

def label_encode(data: list[dict], value_dict : dict ={}) -> tuple:
  """
    Encode all non-numeric labels by using numbers.
    
    Args:
      data: the training set or evaluation set of adult dataset.
    
    Returns:
      encoded_data: The encoded data with all labels and parameters numeric
      value_dicts: The way the program encodes the non-numeric labels
  """
  value_dicts = defaultdict(lambda: {}) if not value_dict else value_dict
  encoded_data = []
  for entry in data:
    encoded_entry = {}
    for key, value in entry.items():
      if key == 'income':
        # encode label 'income' in adult dataset by encoding '<=50K' as 0 and '>50K' as 1
        encoded_entry[key] = 0 if value == '<=50K' else 1
      elif isinstance(value, str):
        # Use numeric to number strings
        if value not in value_dicts[key]:
            value_dicts[key][value] = len(value_dicts[key])
        encoded_entry[key] = value_dicts[key][value]
      else:
        encoded_entry[key] = value
    encoded_data.append(encoded_entry)
  return encoded_data, value_dicts

def evaluate_model(labels, predictions) -> tuple:
  """
    Calculate and the evaluation result of the model(decision tree) based on adult dataset.

    Args:
      labels: The list of label data
      predictions: The list of predicted label result of data

    Returns:
      tuple with accuracu, precision, recall and f1_score
  """
  tp = sum(1 for i in range(len(labels)) if labels[i] == 1 and predictions[i] == 1)
  tn = sum(1 for i in range(len(labels)) if labels[i] == 0 and predictions[i] == 0)
  fp = sum(1 for i in range(len(labels)) if labels[i] == 0 and predictions[i] == 1)
  fn = sum(1 for i in range(len(labels)) if labels[i] == 1 and predictions[i] == 0)
  accuracy = (tp + tn) / len(labels)
  precision = tp / (tp + fp) if (tp + fp) > 0 else 0
  recall = tp / (tp + fn) if (tp + fn) > 0 else 0
  f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
  return accuracy, precision, recall, f1_score

def print_model_evaluation_result(data: list, predictions: list):
  """
    Calculate and print the evaluation result of the model(decision tree) based on adult dataset.

    Args:
      data: The list of data encoded with labels
      predictions: The list of predicted label result of data
  """
  labels = [d['income'] for d in data]
  accuracy, precision, recall, f1_score = evaluate_model(labels, predictions)
  print(f"Accuracy: {accuracy:.2f}")
  print(f"Precision: {precision:.2f}")
  print(f"Recall: {recall:.2f}")
  print(f"F1 Score: {f1_score:.2f}")

class TreePrinter:
  """
    This class is for printing the decision tree(binary tree). Customized for course project.

    Attributes: 
      tree: The model(decision tree) which was trained for classification.
      paraLabel: The list of parameters of dataset
      paraValue: The dict of how labels of each parameter is encoded
  """
  def __init__(self, tree: tuple, paraLabel: list[str] = None, paraValue: dict = None):
    self.tree = tree
    self.paraLabel = paraLabel
    self.paraValue = paraValue

  def print_tree(self) -> None:
    """
      Print the tree given to the object in the style as following:
        |- capital-gain <= 5060
        L   |- martial-status is Never-married
        L   L   |- education-num <= 14
        L   L   L   |- capital-loss <= 2339
        L   L   L   L   |- education-num <= 12
        L   L   L   R   |- >50k
        L   L   R   |- age <= 32
        L   L   R   L   |- fnlwgt <= 431637
        L   L   R   L   L   |- <=50k
        L   L   R   L   R   |- >50k
        L   L   R   R   |- capital-loss <= 0
        L   L   R   R   L   |- >50k
        L   L   R   R   R   |- >50k
        L   R   |- education-num <= 12
    """
    self._print_tree(self.tree)

  def _print_tree(self, node, prefix='') -> None:
    if isinstance(node, tuple):
      variable, decision_value, left, right = node
      if(self.paraValue[self.paraLabel[variable]]):
        print(f"{prefix}|- {self.paraLabel[variable]} is {[k for k, v in self.paraValue[self.paraLabel[variable]].items() if v == decision_value][0]}")
      else:
        print(f"{prefix}|- {self.paraLabel[variable]} <= {decision_value}")
      if left or right:
        self._print_tree(left, prefix + 'L   ')
        self._print_tree(right, prefix + 'R   ')
    else:
      print(f"{prefix}|- INCOME {'<=50k' if node == 0 else '>50k'}")