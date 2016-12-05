import math
import numpy as np
from sklearn import tree
x=[[3.567,3.52,3.117,2.813],[3.569,3.53,3.118,2.812],[3.568,3.54,3.119,2.814],[2.70,2.936,2.856,2.782],[2.71,2.937,2.857,2.783],[2.72,2.938,2.858,2.784],[2.72,1.575,1.93,1.032],[2.73,1.578,1.932,1.033],[2.74,1.58,1.935,1.039],[2.71,2.3,	1,1.35],[2.715,2.35,1.6,1.41],[2.78,2.4,1.7,1.5],[2.9,2.6,1.8,1.5],[2.95,2.62,1.83,1.57],[3,2.7,1.9,1.6]]
xx=(np.array(x)).astype(float)
y=[1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]
yy=(np.array(y)).astype(float)


clf=tree.DecisionTreeClassifier()
fitt=clf.fit(xx,yy)
yyy=fitt.predict([[2.9,2.6,1.8,1.5]])
print 'The prediction '
print yyy
pp=fitt.predict_proba([[2.9,2.6,1.8,1.5]])
print 'The probability'
print pp
