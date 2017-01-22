def data_split(data,index,value):
    left=list()
    right=list()
    for row in data:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left,right

# function to check gini index value for a perticular grup

def gini_index(groups,class_values):
    gini=0.0

    for c in class_values:
        for g in groups:
            size=len(g)
            if size == 0:
                continue
            proba_lity=[row[-1] for row in g].count(c)/float(size)
            gini +=(proba_lity*(1.0-proba_lity))*(proba_lity*(1.0-proba_lity))
    return gini


def get_label(data):
    class_values = list(set(row[-1] for row in data))

    b_index, b_value, b_score, b_groups = 99, 99, 99, None
    for index in range(len(data[0])-1):
        for row in data:
            groups=data_split(data,index,row[index])
            gini=gini_index(groups,class_values)

            if gini< b_score:
                b_index=index
                b_value=row[index]
                b_score=gini
                b_groups=groups

    return {'index':b_index,'value':b_value,'groups':b_groups}



# function to calculate the maximum outcome to determine the group

def outcome(data):

    r=[row[-1] for row in data]
    m=max(set(r), key=r.count)
    return m


# function to split the nodes


def split_node(node,maxdepth, minsample,initialdepth):
    left,right = node['groups']
    del(node['groups'])
    if not left or not right:
        node['left'] = node['right'] = outcome(left+right)
        return
    if initialdepth >= maxdepth:
        node['left']=outcome(left)
        node['right']=outcome(right)
        return
    if len(left)<minsample:
        node['left']=outcome(left)
        return
    else:
        node['left']=get_label(left)
        split_node(node['left'],maxdepth, minsample,initialdepth+1)

    if len(right)<minsample:
        node['right']=outcome(right)
        return
    else:
        node['right']=get_label(right)
        split_node(node['right'],maxdepth, minsample,initialdepth+1)


# function for making final tree

def make_tree(data,maximumdepth, minimumsample):

    node=get_label(data)
    split_node(node,maximumdepth, minimumsample,1)
    return node


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
   [200,20,1],
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

make_tree(data,2,1)
def ptree(node):
    if isinstance(node, dict):
        print 'at index', node['index'], 'for value',  node['value']
        ptree(node['left'])
        ptree(node['right'])
    else:
        print 'final group', [node]

tree=make_tree(data, 1, 1)


ptree(tree)
