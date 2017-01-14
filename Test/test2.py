# definition/function for the split the data

def data_split(data, index, value):
    left, right = list(), list()
    for row in data:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)

    return left, right

# definition/ function for calculating Gini

def gini_index(groups, class_values):
    gini = 0.0

    for c in class_values:

        for g in groups:

            size = len(g)
            if size == 0:
                continue

            p = [row[-1] for row in g].count(c)/float(size)

            gini += p*p*(1.0 -p)*(1.0 -p)

    return gini


def make_label(data):

    class_values = list(set(row[-1] for row in data))

    b_index, b_value, b_score, b_groups = 99, 99, 99, None

    for index in range(len(data[0])-1):

        for row in data:

            groups = data_split(data, index, row[index])

            gini = gini_index(groups, class_values)

            if gini < b_score:

                b_index = index
                b_value = row[index]
                b_score = gini
                b_groups = groups

    return {'index': b_index, 'value': b_value, 'groups': b_groups}



# function to calculate the outcome

def outcome(data):
  Last_coulm_of_data = [row[-1] for row in data]
  max_outcome = max(set(Last_coulm_of_data), key=Last_coulm_of_data.count)

  return max_outcome

# function to divide the node

def split_node(node, maximum_depth, minimum_sample, innitial_depth):

    left, right = node['groups']

    del(node['groups'])

    if not left or not right:

        node['left'] = node['right'] = outcome(left + right)
        return

    if innitial_depth >= maximum_depth:

        node['left'], node['right'] = outcome(left), outcome(right)
        return

    if len(left) <= minimum_sample:
        node['left'] = outcome(left)
        return
    else:
        node['left'] = make_label(left)
        split_node(node['left'], maximum_depth, minimum_sample, innitial_depth+1)

    if len(right) <= minimum_sample:
        node['right'] = outcome(right)
        return
    else:
        node['right'] = make_label(right)
        split_node(node['right'], maximum_depth, minimum_sample, innitial_depth+1)

# function to finally building tree

def build_tree(data, maximum_depth, minimum_sample):
    root = make_label(data)
    split_node(root, maximum_depth, minimum_sample, 1)
    return root


# function for printing the tree
def ptree(node):
    if isinstance(node, dict):
        print 'at index', node['index'], 'for value',  node['value']
        ptree(node['left'])
        ptree(node['right'])
    else:
        print 'final group', [node]


data =[[10,10,0],
   [20,10,0],
   [30,10,0],
   [40,10,0],
   [50,10,0],
   [60,10,0],
   [70,20,2],
   [80,20,2],
   [90,20,2],
   [100,20,2],
   [100,20,2],
   [200,20,0,1],
   [200,10,1],
   [201,10,1],
   [300,10,1],
   [150,10,1],
   [150,10,1],
   [160,10,1],
   [170,20,2],
   [180,20,2],
   [190,20,2],
   [120,20,2],
   [110,20,2],
   [111,20,2,]]



tree=build_tree(data, 1, 1)


ptree(tree)

# function for predicting a test data using the training tree


def predict(node,raw):
    if raw[node['index']] < node['value']:

        if isinstance(node['left'], dict):
            return predict(node['left'], raw)
        else:
            return node['left']
    else:
        if isinstance(node['right'], dict):
            return predict(node['right'], raw)
        else:
            return node['right']

Test_data = input('please input the values as [''a'',''b''] = ')


#Test_data = [float(x) for x in input().split()]

predicted_data = predict(tree,Test_data)
print predicted_data









