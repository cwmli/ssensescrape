import requestwrap
import datetime
import csv
import sys
import os

BRANDS = os.environ['BRAND_LIST'].split()

def get_content():

  filename = datetime.datetime.today().strftime("%Y-%m-%d")
  product_urls = []

  for brand in BRANDS:
    target_url = 'https://www.ssense.com/en-ca/men/designers/%s.json' % brand
    
    src = requestwrap.get_json(target_url)
    src_page = int(src['meta']['page'])
    max_page = int(src['meta']['total_pages'])
    
    if src_page <= max_page:
      for obj in src['products']:
        product_urls.append(obj['url'])
        
      # get the next page if paginated
      src_page += 1
      src = requestwrap.get_json(target_url + "?page=%s" % src_page)
    
  
  with open("/tmp/%s.csv" % filename, 'w') as csvfile:
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
        productSizeInStock.append(str(sizeObj['inStock']))

      # convert product(Sizes|SizeSkus|SizeInStock) to strings delimited by spaces
      productSizes       = " ".join(productSizes)
      productSizeSkus    = " ".join(productSizeSkus)
      productSizeInStock = " ".join(productSizeInStock)
  
      writer.writerow([isSaleEnabled, isSaleSoon, isCaptchaEnabled, isSkuCaptchaProtected,
                    productSku, productName, productGender, 
                    productComposition, productCategory, productOrigin, 
                    productInStock, productBrand, productRegPrice,
                    productSalePrice, productDiscPrice, productCurrency,
                    productIsUniSize, productSizes, productSizeSkus, productSizeInStock])

  return filename
