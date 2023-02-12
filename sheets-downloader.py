# Author: Bilal El Idrissi
# Github: https://github.com/bilalelidrissi171
# Linkedin: https://www.linkedin.com/in/bilalelidrissi171/
# Description: Fetch and Download files from Google Sheets, Excel or CVS files

import os
import google.auth
from googleapiclient.discovery import build
import requests
import pandas

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	BOLD = '\033[1m'
	ENDC = '\033[0m'

def get_data_from_google_sheets():
	checker = 0
	while checker == 0:
		os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = input(bcolors.BOLD + 'Enter the path of the JSON file : ' + bcolors.ENDC)
		try:
			creds, project = google.auth.default()
			service = build('sheets', 'v4', credentials=creds)
		except:
			print(bcolors.FAIL + bcolors.BOLD + 'ERROR: THE FILE OR THE PATH IS NOT VALID' + bcolors.ENDC)
		else:
			checker = 1
	checker = 0
	while checker == 0:
		sheet = input(bcolors.BOLD + 'Enter the link of the Google Sheets file : ' + bcolors.ENDC)
		if sheet.split('/')[0] == 'https:' or sheet.split('/')[0] == 'http:':
			sheet = sheet.replace('https://', '')
			sheet = sheet.replace('http://', '')
		try:
			sheet_id = sheet.split('/')[3]
			result = service.spreadsheets().values().get(spreadsheetId=sheet_id, range='A2:B').execute()
		except:
			print(sheet)
			print(bcolors.FAIL + bcolors.BOLD + 'ERROR: THE LINK IS NOT VALID OR THE SHEET IS EMPTY OR THE SHEET NOT PUBLIC' + bcolors.ENDC)
		else:
			checker = 1
	values = result.get('values', [])
	return values

def get_data_from_excel():
	checker = 0
	while checker == 0:
		excel = input(bcolors.BOLD + 'Enter the path of the Excel file : ' + bcolors.ENDC)
		if (os.path.exists(excel) == False):
			print(bcolors.FAIL + bcolors.BOLD + 'ERROR: THE FILE DOES NOT EXIST' + bcolors.ENDC)
		else:
			checker = 1
	try:
		data = pandas.read_excel(excel, header=None, skiprows=1)
	except:
		print(bcolors.FAIL + bcolors.BOLD + 'ERROR: THE FILE IS NOT VALID PLEASE CHECK THE FILE AND TRY AGAIN' + bcolors.ENDC)
		exit()
	values = data.values.tolist()
	return values

def get_data_from_cvs():
	checker = 0
	while checker == 0:
		cvs = input(bcolors.BOLD + 'Enter the path of the CVS file : ' + bcolors.ENDC)
		if (os.path.exists(cvs) == False):
			print(bcolors.FAIL + bcolors.BOLD + 'ERROR: THE FILE DOES NOT EXIST' + bcolors.ENDC)
		else:
			checker = 1
	try:
		data = pandas.read_csv(cvs, header=None, skiprows=1)
	except:
		print(bcolors.FAIL + bcolors.BOLD + 'ERROR: THE FILE IS NOT VALID PLEASE CHECK THE FILE AND TRY AGAIN' + bcolors.ENDC)
		exit()
	values = data.values.tolist()
	return values

def handel_file_exists(name_file, extension):
	directories = os.listdir()
	check = True
	if name_file in directories:
		replace = input(bcolors.WARNING + bcolors.BOLD + '\nThe file ' + name_file + ' already exists choose what to do :\nY- Replace the file\nR- Rename the new file\nN- Skip the file\nQ- Quit\nEnter your choice : ' + bcolors.ENDC)
		while True:
			if replace.lower() == 'y':
				os.remove(name_file)
				break
			elif replace.lower() == 'r':
				new_name = input(bcolors.BOLD + 'Enter a new name for the new file without the extension : ' + bcolors.ENDC)
				while new_name == '' or new_name + extension in directories:
					if new_name == '':
						print(bcolors.FAIL + bcolors.BOLD + 'ERROR: THE NAME IS EMPTY' + bcolors.ENDC)
					elif new_name + extension in directories:
						print(bcolors.FAIL + bcolors.BOLD + 'ERROR: THE NAME IS ALREADY USED' + bcolors.ENDC)
					new_name = input(bcolors.BOLD + 'Enter a new name for the new file without the extension : ' + bcolors.ENDC)
				name_file = new_name + extension
				break
			elif replace.lower() == 'n':
				check = False
				break
			elif replace.lower() == 'q':
				exit()
			else:
				print(bcolors.FAIL + bcolors.BOLD + 'INVALID CHOICE TRY AGAIN ' + bcolors.ENDC, end='')
				replace = input(bcolors.WARNING + bcolors.BOLD + '\nEnter your choice : ' + bcolors.ENDC)
	return check, name_file

def check_file_exists(name_file):
	while True:
		directories = os.listdir()
		if name_file in directories:
			break

def choose():
	print(bcolors.BOLD + 'Choose the source of the data : ')
	print('1- Google Sheets')
	print('2- Excel')
	print('3- CVS')
	print('4- Quit')
	print(bcolors.ENDC, end='')
	while True:
		choice = input(bcolors.BOLD + '\nEnter your choice : ' + bcolors.ENDC)
		if choice == '1':
			return 'Google Sheets'
		elif choice == '2':
			return 'Excel'
		elif choice == '3':
			return 'CVS'
		elif choice == '4':
			exit()
		else:
			print(bcolors.FAIL + bcolors.BOLD + 'INVALID CHOICE TRY AGAIN ' + bcolors.ENDC, end='')

def get_direct_download_link(url, type):
	if type == 'Google Drive':
		id = url.split('/')[3]
		if url.split('/')[1] == 'file' or url.split('/')[1] == 'open':
			url = 'https://drive.google.com/uc?id=' + id + '&confirm=t&uuid=385ee04a-3ba3-4124-b520-671b2f7961ef&at=ALgDtsxL8T-bsnt0ESUDp7hdqESg:1676157211028'
	return url

def check_domain_name(url):
	if (url.split('/')[0] == 'https:' or url.split('/')[0] == 'http:'):

		url = url.replace('https://', '')
		url = url.replace('http://', '')
	if url.split('/')[0] == 'www':
		url = url.replace('www.', '')
	if url.split('/')[0] == 'drive.google.com':
		url = get_direct_download_link(url, 'Google Drive')

	return url

def download_file(row):
	url = check_domain_name(str(row[1]))
	response = requests.get(url)
	if response.status_code != 200:
		print(bcolors.FAIL + bcolors.BOLD + 'ERROR: THE FILE ' + row[0] + ' DOES NOT EXIST' + bcolors.ENDC)
		return
	extension = '.' + response.headers['Content-Type'].split('/')[1]
	name_file = row[0] + extension
	check, name_file = handel_file_exists(name_file, extension)
	if check == True:
		with open(name_file, 'wb') as file:
			file.write(response.content)
		check_file_exists(name_file)
		print(bcolors.OKGREEN + bcolors.BOLD + '\nSUCCESS: THE FILE ' + name_file + ' DOWNLOADED SUCCESSFULLY' + bcolors.ENDC)

def main():
	print(bcolors.BOLD + bcolors.OKGREEN + '\nWELCOME TO THE FILE DOWNLOADER\n' + bcolors.ENDC)
	file_type = choose()
	if file_type == 'Google Sheets':
		values = get_data_from_google_sheets()
	elif file_type == 'Excel':
		values = get_data_from_excel()
	elif file_type == 'CVS':
		values = get_data_from_cvs()
	# download the files
	for row in values:
		download_file(row)

if __name__ == '__main__':
	main()
