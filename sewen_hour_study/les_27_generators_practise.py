import os
"""Creates list from the files on disk G with .txt format"""
# g=[os.path.join(z, i)  
# for z,x,c in os.walk('G:\\') 
# for i in c if '.txt' in i]
# print(str(len(g)))
# print(g)
"""Working with dictionaries"""
price = {'meat': 3, 'bread': 1, 'potato': 0.5, 'water': 0.2}
new_price={}
for i in price:
    new_price[i] = round((price[i] * 0.85), 2)  # 15% discount
print('Prises with discount 15% - ' + str(new_price))

new_d={i: round(price[i]*0.85,2) for i in price.keys()}
print(new_d,'\n')
print(new_price)