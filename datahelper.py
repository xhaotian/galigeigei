def dictPrint(dict_):
	#存在内部函数自身递归调用，将实参字典变为容易理解的文本
	#然后外部函数将该文本显示
	def dictScan(dic, snum = 0):
	#snum为递归调用时的重要参数，为换行后的对其值（即要在文本前显示的空格数）

	#函数正常运行		须	空格和字母宽度相同
	#由于制表符在本机占八个字符，由于键长度差异可能很大，为完善显示效果，故采用十二个字符的宽度
		result = ''
		space_head = snum*' '
		for i in dic:
			header = space_head + str(i) + '：\t\t'
			#如果键值对中值不再是键值对，直接显示
			if not isinstance(dic[i], dict):
				body = str(dic[i])
				if len(body) > 120:	#长度限制	最多只显示230个字符
					body = body[:120] + '\n' + len(header)*' ' + '\t\t' + body[120:230]
				result += header + body + '\n'
			#键值对中值仍为键值对，则换行后递归调用本函数获得值的文本
			else:
				result += header + '\n' + dictScan(dic[i], (len(header)//12+1)*12)

		return result

	print(dictScan(dict_))


if __name__ == '__main__':
	#测试dictPrint()
	info = {'nmap': {'command_line': 'nmap -oX - -p 80 -sV http://hntou.edu.cn/',
  'scaninfo': {'error': ['Unable to split netmask from target expression: "http://hntou.edu.cn/"\r\nWARNING: No targets were specified, so 0 hosts scanned.\r\n'],
   'warning': ['WARNING: No targets were specified, so 0 hosts scanned.\r\n'],
   'tcp': {'method': 'syn', 'services': '80'}},
  'scanstats': {'timestr': 'Sun Nov 11 08:37:19 2018',
   'elapsed': '1.92',
   'uphosts': '0',
   'downhosts': '0',
   'totalhosts': '0'}},
 	'scan': {}}
	dictPrint(info)		
