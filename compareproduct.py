import ast
import subprocess

new_productList = []
old_productList = []

with open('products_new.txt', 'r') as newFile:
    for i in newFile:
        new_products = ast.literal_eval(i)
        new_productList.append(new_products)

with open('products_old.txt', 'r') as oldFile:
    for j in oldFile:
        old_products = ast.literal_eval(j)
        old_productList.append(old_products)

if len(new_productList) != len(old_productList):        #checking to see if one product list is longer than the rest
        subprocess.run(["./notify.sh","POSSIBLE NEW PRODUCT ADDED"])

for k, l in zip(new_productList, old_productList):
    if k['availability'] != l['availability']:
        print()
        if k['productType'] == 'SINGLE':
            print(k['productTitle'] + ' is back in stock!')
            c = str(k['productTitle'] + ' is back in stock! Grab one while you can! ' + k['productURL'])
            subprocess.Popen(["./notify.sh", c])
            print('grab one while you can! ' + k['productURL'])
        elif k['availability'] == True:
            print(k['productTitle'] + ' in color ' + k['productColor'] + ' in size ' + k['size'] + ' is back in stock! ')
            a = str(k['productTitle'] + ' in color ' + k['productColor'] + ' in size ' + k['size'] + ' is back in stock!' +'  Grab one while you can! ' + k['productURL'])
            print(a)
            subprocess.Popen(["./notify.sh", a])
            print('Grab one while you can! ' + k['productURL'])
        elif k['availability'] == False:
            print(k['productTitle'] + ' in color ' + k['productColor'] + ' in size ' + k['size'] + ' has just sold out! ')
            b = str(k['productTitle'] + ' in color ' + k['productColor'] + ' in size ' + k['size'] + ' has just sold out! ')
            subprocess.Popen(["./notify.sh", b])
