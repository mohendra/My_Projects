
## function to build a data spliting function:
def data_split(data, index, value):

    left, right = list(), list()

    for row in data:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right

## function for calculating gini index
def gini_index(groups , class_values):

    gini = 0.0

    for c in class_values:

        for g in groups:

            size = len(g)

            if size == 0:
                continue

            p = [row[-1] for row in g].count(c)/float(size)

            gini += p*(1-p)

    return gini

## function for making Label

def make_label(data):

    class_values=list(set(row[-1] for row in data))
    b_index, b_value, b_score, b_group = 99,99,99,None
    for index in range(len(data[0])-1):
        for row in data:

            groups = data_split(data, index, row[index])
            gini = gini_index(groups, class_values)

            if gini < b_score:

                b_index = index
                b_value = row[index]
                b_score = gini
                b_group = groups

    return {'index': b_index, 'value': b_value, 'groups': b_group}


## function for counting the outcome

def outcome(data):
    out = [row[-1] for row in data]
    return max(set(out), key=out.count)


## function for spliting the data to maximum depth

def split(label, max_depth, min_size, depth):
	left, right = label['groups']
	del(label['groups'])
	# check for a no split
	if not left or not right:
		label['left'] = label['right'] =outcome(left + right)
		return
	# check for max depth
	if depth >= max_depth:
		label['left'], label['right'] =outcome(left), outcome(right)
		return
	# process left child
	if len(left) <= min_size:
		label['left'] = outcome(left)
	else:
		label['left'] = make_label(left)
		split(label['left'], max_depth, min_size, depth+1)
	# process right child
	if len(right) <= min_size:
		label['right'] = outcome(right)
	else:
		label['right'] = make_label(right)
		split(label['right'], max_depth, min_size, depth+1)


## function to build final tree

def build_tree(data, maximum_deft, minimum_sample):
	root = make_label(data)
	split(root, maximum_deft, minimum_sample, 1)
	return root

## function to print tree view

def print_tree(node, depth=0):
    if isinstance(node, dict):
        print('%s[X%d < %.3f]' % ((depth*' ', (node['index']), node['value'])))
        print_tree(node['left'], depth)
        print_tree(node['right'], depth)
    else:
        print('%s[%s]' % ((depth*' ', node)))


data = [[2.771244718,1.784783929,0],
	[1.728571309,1.169761413,0],
	[3.678319846,2.81281357,0],
	[3.961043357,2.61995032,0],
	[2.999208922,2.209014212,0],
	[7.497545867,3.162953546,1],
	[9.00220326,3.339047188,1],
	[7.444542326,0.476683375,1],
	[10.12493903,3.234550982,1],
	[6.642287351,3.319983761,1]]
tree = build_tree(data,2,1)
print_tree(tree)
