from numpy import *
import math

def read(name):
	"返回data列表，第一位是身高第二位是体重"
	#name=str(input("请输入文件名"))
	f=open(name,"r")
	data1=[]
	data2=[]
	for line in f.readlines():
		line=line.split()
		line=list(map(eval,line))
		data1.append(line[0])
		data2.append(line[1])
	f.close()
	data=[data1,data2]
	print (data)
	return data

def read_test():
	name=str(input("请输入测试文件名"))
	f=open(name,"r")
	data=[]
	for line in f.readlines():
		line=line.split()
		line[:2]=list(map(eval,line[:2]))
		data.append(line)
	f.close()
	return data


def deal(name):
	"处理数据"
	man=read(name)#读取男生,女生
	height=mat(man[0][:])
	#print(height)
	aver=height.mean()
	variance=0
	for x in height:
		temp=(x-aver)*(x-aver).T
		variance=variance+temp
	variance=variance/50
	people=[aver,variance]
	return people

def cal(x,scale,boy,girl):
	# boy=deal()
	# girl=deal()
	#print(type(boy[0]),type(boy[1]))
	x=float(x)
	p_boy=(math.exp(-0.5*((x-boy[0])**2/boy[1])))/(math.sqrt(2*math.pi*boy[1]))
	p_girl=(math.exp(-0.5*((x-girl[0])**2/girl[1])))/(math.sqrt(2*math.pi*girl[1]))
	if p_girl/p_boy-scale<0:
		return 1
	else:
		return 0

test_people=read_test()
data_b=deal("male.txt")
data_g=deal("female.txt")
scale=[1,3,9]
for i in scale:
	boy=girl=0
	for x in test_people:
		sex=cal(x[0],i,data_b,data_g)
		if sex==1:
			if x[2]=='F'or x[2]=='f':
				boy+=1
		else:
			if x[2]=='M'or x[2]=='m':
				girl+=1
	print('当比例为',i,'时',(boy+girl)/len(test_people)*100,end='%\n')
