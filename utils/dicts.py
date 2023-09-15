def get_val(collection, key, default='git'):
	'''
	Функция возвращает значение по ключу, если ключ существует
	Иначе возвращает значение по умолчанию
	:param collection: словарь
	:param key: искомый ключ
	:param default: значение по умолчанию
	:return: найденное слово
	'''
	
	if len(collection) == 0 or key == None:
		return default
	
	if key in collection.keys():
		return collection[key]
	
	return default
