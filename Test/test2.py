# definition/function for the split the data

def data_split(data, index, value):
    left = right = list()
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

            gini += p*(1.0 -p)

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

    if len(left) < minimum_sample:
        node['left'] = outcome(left)
    else:
        node['left'] = make_label(left)
        split_node(node['left'], maximum_depth, minimum_sample, innitial_depth+1)

    if len(right) < minimum_sample:
        node['right'] = outcome(right)
    else:
        node['right'] = make_label(right)
        split_node(node['right'], maximum_depth, minimum_sample, innitial_depth+1)
























