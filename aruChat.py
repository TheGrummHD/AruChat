from colorama import init, Fore, Back, Style
init()

from googletrans import Translator
translator = Translator()

import time
import random
import os
import json
import shutil

# os.chdir(r'%AppData%')
appdata_path = os.getenv('APPDATA')

def getCfg():
	od = os.getcwd()
	os.chdir(appdata_path)

	with open('configArusen.json', 'r', encoding = 'utf-8') as f:
		file = json.load(f)

	os.chdir(od)

	return file

def saveCfg(data):
	od = os.getcwd()
	os.chdir(appdata_path)

	with open('configArusen.json', 'w', encoding = 'utf-8') as f:
		json.dump(data, f, ensure_ascii = False, indent = 4)

	os.chdir(od)

# Setup Configurations
try:
	cfg = getCfg()

	if cfg['SETTINGS'] == {}:
		pass
except:
	with open('configArusen.json', 'w') as f: f.write(r"{}")
	
	cfg = getCfg()

	cfg['SETTINGS'] = {}
	cfg['SETTINGS']['USERNAME'] = os.getlogin()
	cfg['SETTINGS']['HELLOLIST'] = ['ハローー！', 'こんにちは。', 'ハイ！', 'こんにちは', 'こんばんわ']
	cfg['SETTINGS']['CHANGENAME'] = ['名前', '名前を変える']
	cfg['SETTINGS']['COMMANDS'] = {}
	cfg['SETTINGS']['AruTextHelp'] = False

	
	# cfg['SETTINGS']['COMMANDS'][''] = ''
	# cfg['SETTINGS']['COMMANDS'][''] = ''
	# cfg['SETTINGS']['COMMANDS'][''] = ''
	# cfg['SETTINGS']['COMMANDS'][''] = ''
	# cfg['SETTINGS']['COMMANDS'][''] = ''
	# cfg['SETTINGS']['COMMANDS'][''] = ''
	# ランダム\n・ \n・ 出る

	saveCfg(cfg)

# cfg['SETTINGS']['COMMANDS']['ヘルプ / help'] = 'このメッセージを見せる'
# cfg['SETTINGS']['COMMANDS']['名前を変える / setname'] = '名前を変える'
# cfg['SETTINGS']['COMMANDS']['ルート情報 / ls, dir'] = '今入っているファイルの中の情報を見せる'
# cfg['SETTINGS']['COMMANDS']['ルートを変える / cd'] = 'ルートを変えるファイル (例: cd ..\\ - 今のファイルから一歩後ろへ移動する, cd C:\\Users\\(名前)\\Desktop - デスクトップへ移動する'
# cfg['SETTINGS']['COMMANDS']['開ける / start, open'] = 'ファイルを開ける 例: start 卵画像.jpg *注意 - もし開けたいファイルが違うルートにあったら開くことはできません。（ルートを変えるには - cd (ルート) で違うファイルに行けます）ls で今のフォルダーに入っているファイルやフォルダーが見られます。'
# cfg['SETTINGS']['COMMANDS']['ファイル作成 / cr'] = 'ファイル作成'
# cfg['SETTINGS']['COMMANDS']['ランダム / random'] = 'BETA A か B をてきとうで選ぶ'
# cfg['SETTINGS']['COMMANDS']['出る / exit, q'] = 'アプリが閉まる'

HelpList = {
	'ヘルプ / help': 'このメッセージを見せる',
	'名前を変える / setname': '名前を変える',
	'ルート情報 / ls, dir': '今入っているファイルの中の情報を見せる',
	'ルートを変える / cd': 'ルートを変えるファイル (例: cd ..\\ - 今のファイルから一歩後ろへ移動する, cd C:\\Users\\(名前)\\Desktop - デスクトップへ移動する',
	'開ける / start, open': 'ファイルを開ける 例: start 卵画像.jpg *注意 - もし開けたいファイルが違うルートにあったら開くことはできません。（ルートを変えるには - cd (ルート) で違うファイルに行けます）ls で今のフォルダーに入っているファイルやフォルダーが見られます。',
	'ファイル作成 / cr': 'ファイル作成',
	'taskkill / 殺す': 'タスク/アプリを終了する',
	'tasklist / タスクリスト': 'タスクのリスト',
	'フォルダー作成 / cr folder': 'フォルダーを作成する',
	'削除 / del': 'ファイル / フォルダー を削除する',
	'ランダム / random': 'BETA A か B をてきとうで選ぶ',
	'出る / exit, q': 'アプリが閉まる'
}

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
cmdListM = ('-'*4 + 'コマンドリスト' + '-'*4 + Fore.YELLOW + Style.BRIGHT + '\n・ ランダム\n・ 名前を変える\n・ 出る\n・ ファイル作成\n・ 開ける\n・ 道を変える\n・ ルート情報 \n' + Style.RESET_ALL + '-'*22) #\n・ \n・ \n・ \n・ \n・ \n・ 


# print(Fore.GREEN + Style.BRIGHT + 'こんにちは、アルチャットです。 \nコマンドリストは' + Fore.YELLOW + ' "help" ' + Fore.GREEN + 'で見れます' + Style.RESET_ALL)

print(Fore.CYAN + Style.BRIGHT + 'こんにちは、アルチャットです。')
print('コマンドリストは' + Fore.YELLOW + ' "help" ' + Fore.CYAN + 'で見れます' + Style.RESET_ALL)

while True:
	def aiMessage(user_message):
		message = ''
		if user_message in helloList:
			message = random.choice(helloList)

		elif user_message in ['名前を変える', 'setname']:
			newUserName = str(input(Fore.YELLOW + '新しい名前を入力してください: ' + Style.RESET_ALL))

			data = getCfg()

			data['SETTINGS']['USERNAME'] = newUserName

			saveCfg(data)

			message = (Fore.YELLOW + f'\n* 新しい名前が 「{newUserName}」 になりました。' + Style.RESET_ALL)

		elif user_message in ['ランダム', 'random']:
			a = str(input('A: '))
			b = str(input('B: '))

			message = ('答え: ' + Fore.YELLOW + random.choice([a, b]) + Style.RESET_ALL)

		elif user_message in ['ファイル作成', 'cr']:
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

		elif user_message in['ルート情報', 'ls', 'dir']:
			message = (f'\n今のシステムルート: \n"' + Fore.YELLOW + Style.BRIGHT + os.getcwd() + Style.RESET_ALL + '"') # + f'"\n{os.system("tree /F /A")}')
			
			current_directory = os.getcwd()

			for entry in os.listdir():
				entry_path = os.path.join(current_directory, entry)

				if os.path.isfile(entry_path):
					size = os.path.getsize(entry_path)

					print(f'{entry:>20} - {size} バイト')

				else:
					print(f'{entry:>20} - フォルダー')

			



		elif user_message in ['道を変える', 'ルートを変える', 'cd']: 
			root = str(input("ルートを書いてください: "))

			try:
				os.chdir(root)
				
				message = (Style.BRIGHT + 'システムルートが "' + Fore.YELLOW + root + Style.RESET_ALL + '" になりました。')
			except:
				Err = True
				message = '問題が発生しました。'

			

		elif user_message in ['開ける', 'start', 'open']:
			filename = input("ファイル名: ")
			try:
				os.system("start " + filename)

			except:
				message = f'{filename} が見つかりませんでした。'

		elif user_message in ['シャットダウン', 'shutdown']:
			sec = str(input('（「-」でキャンセルできます）\n何秒にシャットダウンしますか？: '))
			if sec == '-':
				os.system('shutdown /a')

			else:
				os.system('shutdown /s /t ' + sec)

		# elif user_message == 'ほんやく':
		# 	text = str(input(Fore.YELLOW + Style.BRIGHT + 'テキスト: ' + Style.RESET_ALL ))
		# 	language = str(input("jp, en: "))
			
		# 	result = translator.translate(text, src = 'en', dest = 'jp')

		# 	message = f'{text} ->\n{result}'
		elif user_message in ['ころす', 'taskkill', 'taskkill', 'kill']:
			taskName = str(input("「タスクリスト」で見れます。\nタスク名: "))
			os.system('taskkill /im ' + taskName + ' /f')

		elif user_message in ['tasklist','タスクリスト']:
			os.system('tasklist')

		elif user_message in ['フォルダー作成', 'cr folder']:
			folderName = str(input('フォルダー名: '))
			os.makedirs(f'./{folderName}')

		elif user_message in ['削除', 'remove', 'del', 'rm']:
			fileorfolder = str(input('1. ファイル\n2. フォルダー\n> '))
			fileName = str(input('ファイル / フォルダー 名: '))

			if fileorfolder == '1':
				os.remove(os.path.join(os.getcwd(), fileName))

			else:
				shutil.rmtree(os.path.join(os.getcwd(), fileName))

		elif user_message in ['出る', 'exit', 'q']:
			quit()


		elif user_message.lower() in ['help', 'ヘルプ']:
			# message = ''
			e = str(input('コマンド説明含み？\n1: はい\n2: いいえ\n> '))

			# for cmd, exp in HelpList.items():
			# 	print(f'{cmd}')

			if e in ['1', '１']:
				# print("ASDADSFEDWFDDSEWFWDSE")
				for cmd, expl in HelpList.items():
					print(f'{Fore.YELLOW + Style.BRIGHT}{cmd}{Style.RESET_ALL} - {Style.BRIGHT}{Fore.RESET}{expl}')

				cfg = getCfg()

				print(f'\n* ルートはフォルダーやファイルまでの道です\n例: C:\\Users\\{os.getlogin()}\\Desktop\\アルセンウイルス.txt')
				
				current_directory = os.getcwd()

				if cfg['SETTINGS']['AruTextHelp'] == False:
					os.chdir(os.path.join(f'C:\\Users\\{os.getlogin()}\\Desktop'))

					with open('アルセンウイルス.txt', 'w', encoding = 'utf-8') as f: f.write((('卵'*80) + '\n') * 70 )

					os.chdir(current_directory)

					cfg['SETTINGS']['AruTextHelp'] = True

				saveCfg(cfg)

			else:
				for cmd, exp in HelpList.items():
					print(f'{Fore.YELLOW + Style.BRIGHT}{cmd}')


		else:
			message = '?\n'

		return message

	# RELOAD CONFIGS

	cfg = getCfg()
	UserName = cfg['SETTINGS']['USERNAME']


	uMessage = input(Fore.YELLOW + Style.BRIGHT + UserName + ' ' + Style.RESET_ALL + Fore.GREEN + os.getcwd() + Style.RESET_ALL + Fore.LIGHTBLACK_EX + '\n$ ' + Style.RESET_ALL)

	aiMessage = aiMessage(str(uMessage))
	print(aiMessage)
	# aiMessage = ''
