import math
import pickle
from collections import Counter

class DecisionNode:
  def __init__(self, attribute: str, predicate: str|int, left_child, right_child):
    self.attribute = attribute  # 划分的属性
    self.predicate = predicate  # 划分的条件（例如某个属性值）
    self.left_child = left_child  # 左子树
    self.right_child = right_child  # 右子树

class LeafNode:
    def __init__(self, value):
        self.value = value  # 叶子节点存储的是分类的结果

class DecisionTree:
    def __init__(self):
        self.root = None

    # 训练决策树
    def fit(self, dataset, labels):
        self.labels = labels
        self.root = self.hunt(dataset)

    # Hunt 算法的实现，递归地构建决策树
    def hunt(self, S):
        print(len(S))
        print(len(S),"===1")
        # 1. 如果所有对象属于同一个类，则返回叶子节点
        classes = [record['income'] for record in S]
        if len(set(classes)) == 1:
            return LeafNode(classes[0])
        print(len(S),"===3")
        # 3. 如果所有对象具有相同的属性值，或者数据集大小太小，则返回占多数的类
        if self.is_same_attributes(S) or len(S) < 10:  # 设定一个最小样本数量为 10
            most_common_class = Counter(classes).most_common(1)[0][0]
            return LeafNode(most_common_class)
        print(len(S),"===5")
        # 5. 使用 GINI 指数找到最佳划分属性和条件
        best_attribute, best_predicate = self.find_best_split(S)
        print(len(S),"===6")
        # 6. 根据最优划分条件将数据集划分为两个子集
        S1 = [record for record in S if self.split(record, best_attribute, best_predicate)]
        S2 = [record for record in S if not self.split(record, best_attribute, best_predicate)]
        print(len(S),"===7")
        # 7. 如果划分结果使得一个子集为空，返回占多数的类，避免过拟合
        if not S1 or not S2:
            most_common_class = Counter(classes).most_common(1)[0][0]
            return LeafNode(most_common_class)
        print(len(S),"===RE")
        # 递归调用 hunt 构建左右子树
        left_child = self.hunt(S1)
        right_child = self.hunt(S2)
        print(len(S),"===8")
        # 8. 创建根节点，并将左右子树连接
        return DecisionNode(best_attribute, best_predicate, left_child, right_child)

    # 判断数据集中是否所有样本的属性值相同
    def is_same_attributes(self, S):
        for attribute in S[0].keys():
            if attribute == 'income':  # 跳过类标签
                continue
            values = [record[attribute] for record in S]
            if len(set(values)) > 1:
                return False
        return True

    # 找到最佳的划分属性和条件（使用 GINI 指数）
    def find_best_split(self, S):
        best_gini = float('inf')
        best_attribute = None
        best_predicate = None

        # 遍历每个属性，找到最好的划分点
        for attribute in S[0].keys():
            if attribute == 'income':  # 跳过类标签
                continue
            values = set([record[attribute] for record in S])  # 该属性的所有不同取值
            for value in values:
                gini = self.gini_index(S, attribute, value)
                if gini < best_gini:
                    best_gini = gini
                    best_attribute = attribute
                    best_predicate = value

        return best_attribute, best_predicate

    # 计算 GINI 指数
    def gini_index(self, S, attribute, predicate):
        S1 = [record for record in S if self.split(record, attribute, predicate)]
        S2 = [record for record in S if not self.split(record, attribute, predicate)]

        # 如果划分的子集为空，则返回最大 GINI 值 1.0
        if not S1 or not S2:
            return 1.0

        # 计算每个子集的 GINI 值
        def gini(subset):
            classes = [record['income'] for record in subset]
            total = len(subset)
            class_counts = Counter(classes)
            gini_value = 1.0 - sum((count / total) ** 2 for count in class_counts.values())
            return gini_value

        # 加权平均 GINI 值
        p1 = len(S1) / len(S)
        p2 = len(S2) / len(S)
        return p1 * gini(S1) + p2 * gini(S2)

    # 判断样本是否满足划分条件
    def split(self, record, attribute, predicate):
        return record[attribute] == predicate

    # 使用决策树预测
    def predict(self, row, node=None):
        if node is None:
            node = self.root

        # 如果当前节点是叶子节点，则返回预测的分类
        if isinstance(node, LeafNode):
            return node.value

        # 否则根据当前节点的划分条件递归地进行预测
        if self.split(row, node.attribute, node.predicate):
            return self.predict(row, node.left_child)
        else:
            return self.predict(row, node.right_child)

    # 测试模型在验证集上的表现
    def test(self, dataset):
        correct = 0
        for row in dataset:
            prediction = self.predict(row)
            if prediction == row['income']:
                correct += 1
        return correct / len(dataset)

    # 保存模型
    @staticmethod
    def save_model(model, filename):
        with open(filename, 'wb') as file:
            pickle.dump(model, file)
            print(f"Model saved at ./{filename}")

    # 加载模型
    @staticmethod
    def load_model(filename):
        with open(filename, 'rb') as file:
            model = pickle.load(file)
        return model
