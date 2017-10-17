from flask import Flask
from flask import request
from flask import render_template
import re

app = Flask(__name__)
app.debug = True
@app.route('/')
def my_page1():
	return render_template("index.html")

@app.route('/cochrans.html', methods=['GET'])
def my_page2():
	return render_template('cochrans.html')

@app.route('/cochrans', methods=['POST'])
def cochransQ() :

	args = request.form['text1']
	args = re.sub(r'\s+', '', args).split('],[')
	temp_args = []
	for i in range(len(args)):
		row = args[i].replace('[','').replace(']','').split(',')
		row = [ float(x) for x in row ]
		temp_args.append(row)
	args = temp_args
	temp = []
	for x in args :
		if(sum(x)==len(x) or sum(x) == 0) :
			continue
		temp += [x]

	N = len(temp)
	Li = []
	Lisq = []

	for i in range(N) :
		sm = sum(temp[i])
		Li += [sm]
		Lisq += [sm*sm]

	Lisq_sum = sum(Lisq)
	Li_sum = sum(Li)

	Gi = []
	Gisq = []
	for j in range(len(temp[i])) :
		sm = 0
		for i in range(N) :
			sm += temp[i][j]
		Gi += [sm]
		Gisq += [sm*sm]

	Gi_sum = sum(Gi)
	Gisq_sum = sum(Gisq)

	k = len(args[0])
	Q = (k-1)*(k*Gisq_sum - Gi_sum*Gi_sum)/(k*Gi_sum - Lisq_sum)
	Q = "Answer : " + str(Q)
	return Q


@app.route('/fishers.html', methods = ['GET'])
def my_page3():
	return render_template("fishers.html")

@app.route('/fishers', methods=['POST'])
def fishersExactTest() :

	args = request.form['text2']
	args = re.sub(r'\s+', '', args).split('],[')
	temp_args = []
	for i in range(len(args)):
		row = args[i].replace('[','').replace(']','').split(',')
		row = [ float(x) for x in row ]
		temp_args.append(row)
	args = temp_args

	row_total_list =  []
	for x in args :
		sum1  = 0
		for k in x :
			sum1 = sum1 + k
		row_total_list = row_total_list + [sum1]
    #print(row_total_list)

	col_total_list = []
	for i in range(len(args)) :
		sum1 = 0
		for x in args :
			sum1 = sum1 + x[i]
		col_total_list = col_total_list + [sum1]
    #print(col_total_list)

	N = sum(col_total_list)
    #print(N)
	m = min(col_total_list + row_total_list)
    #print(m)

	if m in row_total_list :
		i = 0
		for x in row_total_list :
			if(x == m) :
				z = args[i]
				f = min(args[i])
			i += 1
		i = 0
		for x in z :
			if(z[i] == f) :
				M = col_total_list[i]
			i += 1
        #print(f,M)

	else :
		i = 0
		for x in col_total_list :
			if(x == m) :
				f = min(args[0][i] , args[1][i])
				z = [args[0][i]] + [args[1][i]]
			i += 1
		i = 0
		for x in z :
			if(z[i] == f) :
				M = row_total_list[i]
			i += 1
        #print(f , M)

	final_list = [N] + [m] + [M]
	final_list = "Final List : " + str(final_list)
	return final_list


if __name__ == '__main__':
	app.run()
