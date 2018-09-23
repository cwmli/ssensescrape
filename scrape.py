import requestwrap
import datetime
import csv
import sys

TARGET_URL = sys.argv[1]
print("TARGET: %s" % TARGET_URL)

src = requestwrap.get_json(TARGET_URL)
src_page = int(src['meta']['page'])
max_page = int(src['meta']['total_pages'])
product_urls = []

if src_page <= max_page:
  for obj in src['products']:
    product_urls.append(obj['url'])
    
  # get the next page if paginated
  src_page += 1
  src = requestwrap.get_json(TARGET_URL + "?page=%s" % src_page)

print(product_urls)

filename = datetime.datetime.today().strftime("%Y-%m-%d")

with open("%s.csv" % filename, 'w') as csvfile:
  fieldnames = ['isSaleEnabled', 'isSaleSoon', 'isCaptchaEnabled', 'isSkuCaptchaProtected',
                'productSku', 'productName', 'productGender', 
                'productComposition', 'productCategory', 'productOrigin', 
                'productInStock', 'productBrand', 'productRegPrice',
                'productSalePrice', 'productDiscPrice', 'productCurrency',
                'productIsUniSize', 'size', 'sizeSku', 'sizeInStock']

  writer = csv.writer(csvfile, dialect='excel')
  # Write header
  writer.writerow(fieldnames)

  for url in product_urls:
    src = requestwrap.get_json("https://www.ssense.com/en-ca%s.json" % url)
    
    isSaleEnabled         = src['context']['isSaleEnabled']
    isSaleSoon            = src['context']['isSaleSoon']
    isCaptchaEnabled      = src['context']['isCaptchaEnabled']
    isSkuCaptchaProtected = src['context']['isSkuCaptchaProtected']

    productSku            = src['product']['sku']
    productName           = src['product']['name']
    productGender         = src['product']['gender']
    productComposition    = src['product']['composition']
    productCategory       = src['product']['category']['name']
    productOrigin         = src['product']['countryOfOrigin']
    productInStock        = src['product']['inStock']
    productBrand          = src['product']['brand']['name']
    productRegPrice       = src['product']['price']['regular']
    productSalePrice      = src['product']['price']['sale']
    productDiscPrice      = src['product']['price']['discount']
    productCurrency       = src['product']['price']['currency']
    productIsUniSize      = src['product']['isUniSize']



    productSizes       = []
    productSizeSkus    = []
    productSizeInStock = []
    for sizeObj in src['product']['sizes']:
      productSizes.append(sizeObj['name'])
      productSizeSkus.append(sizeObj['sku'])
      productSizeInStock.append(sizeObj['inStock'])

    writer.writerow([isSaleEnabled, isSaleSoon, isCaptchaEnabled, isSkuCaptchaProtected,
                  productSku, productName, productGender, 
                  productComposition, productCategory, productOrigin, 
                  productInStock, productBrand, productRegPrice,
                  productSalePrice, productDiscPrice, productCurrency,
                  productIsUniSize, productSizes, productSizeSkus, productSizeInStock])