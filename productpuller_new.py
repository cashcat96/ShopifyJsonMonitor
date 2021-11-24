import requests
import json
import os

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'

# EDIT THE URL AT THE BOTTOM OF THE PAGE

def get_page(url):
    #print("\n💛 Getting page...")
    url = url
    full_url = 'https://' + url + '/products.json'

    req = requests.get(
        full_url,
        data = None,
        headers = { 'User-Agent': USER_AGENT}
    )
    data = req.text
    products = json.loads(data)['products']
    return products
    
def get_products(url):
    products = get_page(url)

    file = open('products_new.txt', 'w')
    file.write('')
    file.close()

#    if os.stat('products_new.txt').st_size == 0:
#        print("products_new.txt is empty")
#    else:

    #print("💛 Getting products...\n")
    for product in products:
        productID = product['id']
        productTitle = product['title']
        productType = product['product_type']
        productURL = url + '/products/' + product['handle']

        productTitle = productTitle.replace('\"', '')		#removes quotes from the product title that may screw things up down the line

        for variant in product['variants']:
            variantPrice = variant['price']
            size = variant['option2']
            color = variant['option1']
            sku = variant['sku']

            # the below if statements work to weed out nonetypes
            # which fuck up the notifications. feel free to add
            # any other product data that could be nonetype
            if size == None:
              size = 'no size data'
              
            if color == None:
              color = 'no color data'
              
            if sku == None:
              sku = 'no sku data'

            in_stock = True
            if not variant['available']:
                in_stock = False
            
            row = {'productID': productID, 'productType': productType, 'productTitle': productTitle, 'productColor': color, 
                    'productURL': productURL, 'sku': sku, 'size': size, 'price': variantPrice, 
                    'availability': in_stock}
            #print(row)
            
            path = 'products_new.txt'
            file = open(path, 'a')
            file.write(str(row) + '\n')
            file.close()
    return path

get_products('blonded.co')		#EDIT THIS URL
