import argparse
import os
import re
import filecmp
import subprocess
from requests_html import HTMLSession

session = HTMLSession()

WORKING_DIR = os.getcwd()
dir_path = f'{WORKING_DIR}/samples'

# parser = argparse.ArgumentParser()

# load_help = "Provide the URL to the problem"
# test_help = "No arguments"
# parser.add_argument("-l", "--load", help=load_help)
# parser.add_argument("-t", "--test", help=test_help, action="store_true")

# args = parser.parse_args()

# if args.load:
# 	print(args.load)

# if args.test:
# 	print(args.test)


def create_samples():
	if not os.path.isdir(dir_path):
		os.mkdir(dir_path)

	for i in range(1, 3):
		samples_input_file = f'{dir_path}/sin{i}.txt'
		samples_output_file = f'{dir_path}/sout{i}.txt'
		user_output_file = f'{dir_path}/out{i}.txt'
		fil = open(samples_input_file, "w")
		fil.close()
		fil = open(samples_output_file, "w")
		fil.close()
		fil = open(user_output_file, "w")
		fil.close()


def load_problem(problem_url):
	create_samples()
	if re.search('atcoder', problem_url):
		atcoder(problem_url)

	elif re.search('codeforces', problem_url):
		codeforces(problem_url)

	else:
		codechef(problem_url)


def codechef(problem_url):
	pass


def codeforces(problem_url):
	pass


def atcoder(problem_url):
	r = session.get(problem_url)
	# print(r.text)
	task = r.html.find("#task-statement", first=True)
	print(task.html)


def execute(fin, fout):
	subprocess.run(['g++', '-std=c++17', '-D=CPTEST', 'main.cpp'])
	subprocess.run(['./a.out', fin, fout])


def compare_output():
	verdict = []
	verdict.append(True)
	for i in range(1, 3):
		samples_output_file = f'{dir_path}/sout{i}.txt'
		user_output_file = f'{dir_path}/out{i}.txt'
		if os.stat(samples_output_file).st_size == 0:
			break

		ver = filecmp.cmp(samples_output_file, user_output_file)
		verdict.append(ver)

	for i in range(1, 3):
		print(verdict[i])

	return verdict


def execute_on_all():
	for i in range(1, 3):
		output_file = f'{dir_path}/out{i}.txt'
		input_file = f'{dir_path}/in{i}.txt'
		execute(input_file, output_file)

















