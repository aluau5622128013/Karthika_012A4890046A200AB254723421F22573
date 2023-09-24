
def linearsearchproduct(productList,targetproduct):
    indices=[]
    for index,product in enumerate(productList):
      if product== targetproduct:
       indices.append(index)
    return indices

products=["shoes","boot","loafer","shoes","sandal","shoes"]

target="shoes"
target2="apple"
result=linearsearchproduct(products,target2)
print(result)