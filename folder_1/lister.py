def main():
	l = []
	while True:
		s = input()
		if s == 'break':
			break
		else:
			l.append(s)

	l.sort(key=str.lower)

	with open('s.txt','a+') as f:
		for i in l:
			f.write(f'{i}\n')

	f.close()

if __name__ == '__main__':
	main()