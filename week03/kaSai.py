'''
凯撒密码是古罗马凯撒大帝用来对军事情报进行加解密的算法，它采用了替换方法对信息中的每一个英文字符循环替换为字母表序列中该字符后面的第三个字符，即，字母表的对应关系如下：

原文：A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

密文：D E F G H I J K L M N O P Q R S T U V W X Y Z A B C

对于原文字符P，其密文字符C满足如下条件：C=(P+3) mod 26

上述是凯撒密码的加密方法，解密方法反之，即：P=(C-3) mod 26

假设用户可能使用的输入仅包含小写字母a~z和空格，请编写一个程序，对输入字符串进行凯撒密码加密，直接输出结果，其中空格不用进行加密处理。使用input()获得输入。
'''




sr1="abcdefghijklmnopqrstuvwxyz"
sr2=sr1.upper()
sr=sr1+sr2
in_str=input("")
out_str=""
for j in in_str:
    if j==" ":
        out_str = out_str +" "
        continue
    i=sr.find(j)
    if(i>-1):
        out_str=out_str+sr[i+3]
print(out_str)
'''
sr1="abcdefghijklmnopqrstuvwxyz"
sr2=sr1.upper()
sr=sr1+sr1+sr2+sr2
in_str=input("")
out_str=""
for j in in_str:
    if j==" ":
        out_str = out_str +" "
        continue
    i=sr.find(j)
    if(i>-1):
        out_str=out_str+sr[i+3]
print(out_str)
'''

'''
class Caesar:
    def __init__(self,a,b):#初始化，接受程序需要的类型
        self.pass1=a
        self.type1=b
    def jiami(self,a):#加密的程序
        z=(ord(a)-97+self.pass1)%26+97#用ascii码值来完成移动
        return chr(z)
    def jiemi(self,a):#解密的程序
        z=(ord(a)-97-self.pass1)%26+97
        if z<97:
            z=z+26
        return chr(z)
    def show(self,x):#显示结果
        str=''
        if self.type1==0:#加密的时候进入
            for i in range (len(x)):
                x=x[:i]+self.jiami(x[i])+x[i+1:]
            for i in range (len(x)):
                str=str+x[i]
            print (str)
        else:#解密的时候进入
            for i in range (len(x)):
                x=x[:i]+self.jiemi(x[i])+x[i+1:]
            for i in range (len(x)):
                str=str+x[i]
            print (str)
if __name__=='__main__':#测试程序
    a=int(input('please input the pass (小于26！0：结束):'))
    while a:
        b=int(input('please input the type （0：加密；1：解密:）'))
        x=input('please input str:')
        user=Caesar(a,b)
        user.show(x)
        a=int(input('please input the pass (小于26！0：结束):'))

'''
