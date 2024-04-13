#dictionary用法
food = { # 使用大括弧
	'ramen': '拉麵', #'__': '' 前面為key；後面為value。 
	'apple': '蘋果' # key與key之間是使用","來區分
}

# 
menu = {
	'serial #' : [0, 1, 2, 3, 4],
	'item' : ['ramen', 'fruit', 'rice', 'water', 'icecream'],
	'price': [180, 50, 10, 12, 60] 
}

print(menu)
print(menu['serial #'][:]) # 從menu dictionary中，key'serial #' 所有對應的value。
print(menu['serial #'][:3]) # 對應value = 0, 1, 2
print(menu['serial #'][:-1]) # 對應value = 0, 1, 2, 3
print(menu['price'][:-1]) #key= price時，value = 180, 50, 10, 12；[:-1]是到end的前一個，且包含該數值
print(menu['price'][1:-1]) #value = 50, 10, 12
#print(menu[1]) #錯誤指令，再dictionary中，僅能輸入key，透過字典找出對應的value

#如何新增key、value在dictionary中
food['tea'] = '茶' # 左邊可視為key並定義(=)為'茶' value

print(food)
print(food['ramen'])
print(food['apple'])
#print(food['拉麵']) # 無法從value回推至key。
print(food['tea'])



# 沒有向pandas的情況，只能用個別項目使用{}後再裝入list[]中。
item01 = {
	'name': '麥香奶茶',
	'price': 10 # 字典可不用一定要裝同樣type屬性的內容
}
item02 = {
	'name': '珍珠奶茶',
	'price': 60
}
item03 = {
	'name': '牛奶',
	'price': 65
}

drink = [item01, item02, item03]
print(drink)
print(drink[0]['name']) #針對清單中，第一個item字典裏頭的'name'，#麥香奶茶
print(drink[1]['price']) #針對清單中，第二個item字典裏頭的'price'，# 60

