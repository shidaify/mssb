from numpy import *
import math

def read(name):
	"返回data列表，第一位是身高第二位是体重"
	#name=str(input("请输入文件名"))
	f=open(name,"r")
	data=[]
	for line in f.readlines():
		line=line.split()
		line=list(map(eval,line))
		data.append(line)
	f.close()
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

def covr(i,j,man,aver):
	sum=0
	for n in man:
		sum=sum+(n[i]-aver[i])*(n[j]-aver[j])
	return sum/len(man)

def deal2(name):
	"处理数据"
	man=read(name)
	height=mat(man).T[0]
	weight=mat(man).T[1]
	aver=[height.mean(),weight.mean()]
	print(aver)
	#cov=mat([[covr(0,0,man,aver),covr(0,1,man,aver)],[covr(1,0,man,aver),covr(1,1,man,aver)]])
	cov=mat([[covr(0,0,man,aver),0],[0,covr(1,1,man,aver)]])
	people=[aver,cov]
	return people

def cal(x,scale,boy,girl):
	# boy=deal()
	# girl=deal()
	#print(type(boy[0]),type(boy[1]))
	x=mat(x)
	boy[0]=mat(boy[0])
	girl[0]=mat(girl[0])
	
	p_boy=(math.exp(-0.5*((x-boy[0])*boy[1].I*(x-boy[0]).T)))/(2*math.pi*math.sqrt(linalg.det(boy[1])))
	p_girl=(math.exp(-0.5*((x-girl[0])*girl[1].I*(x-girl[0]).T)))/(2*math.pi*math.sqrt(linalg.det(girl[1])))
	if p_girl/p_boy-scale<0:
		return 1
	else:
		return 0

test_people=read_test()
data_b=deal2("male.txt")
data_g=deal2("female.txt")
scale=[1,3,9]
#scale=[2]
for i in scale:
	boy=girl=0
	for x in test_people:
		sex=cal(x[:2],i,data_b,data_g)
		if sex==1:
			if x[2]=='F'or x[2]=='f':
				boy+=1
		else:
			if x[2]=='M'or x[2]=='m':
				girl+=1
	print('当比例为',i,'时',(boy+girl)/len(test_people)*100,end='%\n')
