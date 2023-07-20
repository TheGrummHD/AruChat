from colorama import init, Fore, Back, Style
init()

from googletrans import Translator
translator = Translator()

import time
import random
import os
import json

# os.chdir(r'%AppData%')
# os.getenv('APPDATA')
directory = os.getcwd()

def getCfg():
	with open('configArusen.json', 'r', encoding = 'utf-8') as f:
		file = json.load(f)

	return file

def saveCfg(data):
	with open('configArusen.json', 'w', encoding = 'utf-8') as f:
		json.dump(data, f, ensure_ascii = False, indent = 4)

# Setup Configurations
try:
	cfg = getCfg()

	if cfg['SETTINGS'] == {}:
		pass
except:
	with open('configArusen.json', 'w') as f: f.write(r"{}")
	
	cfg = getCfg()

	cfg['SETTINGS'] = {}
	cfg['SETTINGS']['USERNAME'] = "人間"
	cfg['SETTINGS']['HELLOLIST'] = ['ハローー！', 'こんにちは。', 'ハイ！', 'こんにちは', 'こんばんわ']
	cfg['SETTINGS']['CHANGENAME'] = ['名前', '名前を変える']

	saveCfg(cfg)


# NEW

# cfg = getCfg()

# cfg['SETTINGS'] = {}
# cfg['SETTINGS']['USERNAME'] = "人間"
# cfg['SETTINGS']['HELLOLIST'] = ['ハローー！', 'こんにちは。', 'ハイ！', 'こんにちは', 'こんばんわ']
# cfg['SETTINGS']['CHANGENAME'] = ['名前', '名前を変える']

# saveCfg(cfg)


# Load Configs
cfg = getCfg()

UserName = cfg['SETTINGS']['USERNAME']
helloList = cfg['SETTINGS']['HELLOLIST']
changenameList = cfg['SETTINGS']['CHANGENAME']

saveCfg(cfg)


# cmds list
cmdListM = (Fore.YELLOW + Style.BRIGHT + '・ ランダム\n・ 名前を変える\n・ 出る\n・ ファイル作成\n・ 開ける\n・ 道を変える\n・ ルート情報' + Style.RESET_ALL) #\n・ \n・ \n・ \n・ \n・ \n・ 


print(Fore.GREEN + Style.BRIGHT + 'こんにちは、アルチャットです。 \nコマンドリストは' + Fore.YELLOW + ' "help" ' + Fore.GREEN + 'で見れます' + Style.RESET_ALL)

while True:
	def aiMessage(user_message):
		message = ''
		if user_message in helloList:
			message = random.choice(helloList)

		elif user_message in changenameList:
			newUserName = str(input(Fore.YELLOW + '新しい名前を入力してください: ' + Style.RESET_ALL))

			data = getCfg()

			data['SETTINGS']['USERNAME'] = newUserName

			saveCfg(data)

			message = (Fore.YELLOW + f'\n* 新しい名前が 「{newUserName}」 になりました。' + Style.RESET_ALL)

		elif user_message == 'ランダム':
			a = str(input('A: '))
			b = str(input('B: '))

			message = ('答え: ' + Fore.YELLOW + random.choice([a, b]) + Style.RESET_ALL)

		elif user_message == 'ファイル作成':
			fileName = str(input(Style.BRIGHT + Fore.YELLOW + "ファイル名: " + Style.RESET_ALL))
			
			fileNameFull = '_.txt'

			DOTINNAME = False

			for i in fileName:
				if i == '.':
					DOTINNAME = True
					break

				else:
					pass

			if DOTINNAME == False:
				fileType = str(input(Style.BRIGHT + Fore.GREEN + 'ファイルタイプを入力してください。\nファイルタイプリスト: \n' + Style.BRIGHT + Fore.YELLOW + '・　txt' + Style.RESET_ALL + Fore.GREEN + '\n・　json\n・　html\n・　css\nファイルタイプ: ' + Style.RESET_ALL))
				fileNameFull = f'{fileName}.{fileType}'

			else:
				fileNameFull = fileName
			f = open(f'{fileNameFull}', 'w')

		elif user_message == 'ルート情報':
			message = (f'今のシステムルート: "' + Fore.YELLOW + Style.BRIGHT + directory + Style.RESET_ALL + f'"\n{os.system("tree")}')

		elif user_message == '道を変える': 
			root = str(input("ルートを書いてください: "))
			try:
				os.chdir(root)
				message = (Style.BRIGHT + 'システムルートが "' + Fore.YELLOW + root + Style.RESET_ALL + '" になりました。')
			except:
				message = '問題が発生しました。'
			

		elif user_message == '開ける':
			filename = input("ファイル名: ")
			try:
				os.system("start " + filename)

			except:
				message = f'{filename} が見つかりませんでした。'

		# elif user_message == 'ほんやく':
		# 	text = str(input(Fore.YELLOW + Style.BRIGHT + 'テキスト: ' + Style.RESET_ALL ))
		# 	language = str(input("jp, en: "))
			
		# 	result = translator.translate(text, src = 'en', dest = 'jp')

		# 	message = f'{text} ->\n{result}'



		elif user_message == '出る':
			quit()

		elif user_message.lower() == 'help':
			message = (f'\n{cmdListM}\n')

		else:
			message = '?\n'

		return message

	cfg = getCfg()

	UserName = cfg['SETTINGS']['USERNAME']
	uMessage = input(Fore.YELLOW + Style.BRIGHT + UserName + ' - .\\' + Style.RESET_ALL + Fore.GREEN + os.path.basename(directory) + Style.RESET_ALL + Fore.YELLOW + '\\ \n$ ' + Style.RESET_ALL)

	aiMessage = aiMessage(str(uMessage))
	print(aiMessage)
	# aiMessage = ''
