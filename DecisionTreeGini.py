class DecisionTreeGini:
  """
  This class is designed for realizing the algorithm below to construct a decision tree for 
  income classification by using adult dataset.

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

    Attributes:
      min_samples_split: key argument of Algo Line 3-4, the minimize size of |S|.
      max_depth: the largest depth of the decision tree.
      numeric_feature_index: The index of feature whose data is numeric istead of string.
  """
  def __init__(self, min_samples_split: int = 5, max_depth: int = None, numeric_feature_index: list[int] = None):
    self.min_samples_split = min_samples_split
    self.max_depth = max_depth
    self.numeric_feature_index = numeric_feature_index
    self.tree = None

  def split_dataset(self, features, labels, feature_index, split) -> tuple[list]:
    """
      A tool function to split the features and labels based on given feature index and split point.
      For numeric data take "<=" split while for non-numeric, take "==" split.

      Args:
        features: The list of data with non-numeric label encoded.
        labels: The list of label data encoded.
        feature_index: The feature to be split based on.
        split: The split point of the data.

      Returns:
        The split dataset tuple with 2 groups of features and labels.
    """
    left_features, left_labels = [], []
    right_features, right_labels = [], []
    for i in range(len(features)):
      if feature_index in self.numeric_feature_index: # For numeric
        if features[i][feature_index] <= split:
          left_features.append(features[i])
          left_labels.append(labels[i])
        else:
          right_features.append(features[i])
          right_labels.append(labels[i])
      else: # For non-numeric
        if features[i][feature_index] == split:
          left_features.append(features[i])
          left_labels.append(labels[i])
        else:
          right_features.append(features[i])
          right_labels.append(labels[i])
    return left_features, left_labels, right_features, right_labels

  def gini(slef, labels: list) -> float:
    """
      Calculate the GINI index of the given label.

      Args:
        labels: The list of label for calculating the GINI index.

      Returns:
        The GINI index value.
    """
    total = len(labels)
    if total == 0:
      return 0
    return 1 - ((labels.count(0) / total) ** 2 + (labels.count(1) / total) ** 2)

  def gini_split(self, left_labels: list, right_labels: list) -> float:
    """
      Calculate the GINI index of the given **two** labels.

      Args:
        left_labels: The list of label for calculating the GINI index.
        right_labels: The list of label for calculating the GINI index.

      Returns:
        The GINI index value of the two labels.
    """
    total = len(left_labels) + len(right_labels)
    gini_left = self.gini(left_labels)
    gini_right = self.gini(right_labels)
    return (len(left_labels) / total) * gini_left + (len(right_labels) / total) * gini_right

  def find_best_split_gini(self, features, labels) -> tuple:
    """
      Find the best split of the features given based on labels' GINI index.
      The evaluation of GINI index is the smaller the better.

      Args:
        features: The list of data with non-numeric label encoded.
        labels: The list of label data encoded.

      Returns:
        A tuple with the feature index and split point to split the data.
    """
    best_feature_index = None
    best_split = None
    best_gini = float('inf')
    n_features = len(features[0])
    # old version
    # for feature_index in range(n_features):
    #   splits = set([row[feature_index] for row in features])
    #   for split in splits:
    #     _, left_labels, _, right_labels = self.split_dataset(features, labels, feature_index, split)
    #     if len(left_labels) == 0 or len(right_labels) == 0:
    #       continue
    #     current_gini = self.gini_split(left_labels, right_labels)
    #     if current_gini < best_gini:
    #       best_gini = current_gini
    #       best_feature_index = feature_index
    #       best_split = split
    # return best_feature_index, best_split

    for feature_index in range(n_features):
      # 1. 对数据按特征值排序
      feature_and_labels = sorted(zip(features, labels), key=lambda x: x[0][feature_index])
      sorted_features = [f for f, _ in feature_and_labels]
      sorted_labels = [l for _, l in feature_and_labels]

      # 2. 累积统计左右子集的 "yes" 和 "no" 计数
      left_yes_count = 0
      left_no_count = 0
      right_yes_count = sorted_labels.count(1)
      right_no_count = len(sorted_labels) - right_yes_count

      # 3. 遍历所有可能的分割点，更新左右子集计数并计算基尼指数
      for i in range(1, len(sorted_features)):
        if sorted_labels[i - 1] == 1:
          left_yes_count += 1
          right_yes_count -= 1
        else:
          left_no_count += 1
          right_no_count -= 1

        # 确保每个分割点都是有效的
        if sorted_features[i][feature_index] == sorted_features[i - 1][feature_index]:
          continue

        # 4. 计算当前分割点的基尼指数
        total_left = left_yes_count + left_no_count
        total_right = right_yes_count + right_no_count
        gini_left = 1 - (left_yes_count / total_left) ** 2 - (left_no_count / total_left) ** 2
        gini_right = 1 - (right_yes_count / total_right) ** 2 - (right_no_count / total_right) ** 2
        weighted_gini = (total_left / len(labels)) * gini_left + (total_right / len(labels)) * gini_right

        # 5. 更新最佳分割点
        if weighted_gini < best_gini:
          best_gini = weighted_gini
          best_feature_index = feature_index
          best_split = (sorted_features[i - 1][feature_index] + sorted_features[i][feature_index]) / 2

    return best_feature_index, best_split

  def fit(self, features: list, labels: list, depth=0) -> tuple:

    n_samples = len(labels)

    # 如果所有标签相同，返回该标签
    if len(set(labels)) == 1:
      return labels[0]

    # 检查是否没有特征或样本数小于最小分割样本数，或超过了最大深度
    if len(features) == 0 or \
            n_samples < self.min_samples_split or \
            (self.max_depth is not None and depth >= self.max_depth):
      # 确保 labels 不为空，否则返回 None 或一个默认值
      return max(set(labels), key=labels.count) if labels else None

    # 找到最佳的特征和分割点
    best_feature_index, best_split = self.find_best_split_gini(features, labels)

    # 如果没有找到合适的分割点，返回当前节点的多数类
    if best_feature_index is None:
      return max(set(labels), key=labels.count) if labels else None

    # 根据最佳分割点进行划分
    left_features, left_labels, right_features, right_labels = self.split_dataset(features, labels, best_feature_index,
                                                                                  best_split)

    # 避免递归到空子集
    if len(left_labels) == 0 or len(right_labels) == 0:
      return max(set(labels), key=labels.count) if labels else None

    # 递归生成左子树和右子树
    left_subtree = self.fit(left_features, left_labels, depth + 1)
    right_subtree = self.fit(right_features, right_labels, depth + 1)

    return (best_feature_index, best_split, left_subtree, right_subtree)

  def _predict(self, sample, tree):
    if not isinstance(tree, tuple):
      return tree
    feature_index, split, left_subtree, right_subtree = tree
    if feature_index in self.numeric_feature_index:
      if sample[feature_index] <= split:  # For numeric
        return self._predict(sample, left_subtree)
      else:
        return self._predict(sample, right_subtree)
    else:  # For non-numeric
      if sample[feature_index] == split:
        return self._predict(sample, left_subtree)
      else:
        return self._predict(sample, right_subtree)

  def predict(self, features: list[list]) -> list:
    return [self._predict(sample, self.tree) for sample in features]