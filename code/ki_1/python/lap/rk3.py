file_in=open('in.txt','r')
file_out=open('out.txt','w')

si_max=-1
si_min=-1
t=0
smax=''
smin=''
Sen=''

while True:
    line=file_in.readline()
    if len(line)==0:
        break
    if line[-1]=='\n':
        line=line[:-1]+' '
    for i in range(len(line)):
        if (line[i]==' ' and line[i-1]!='.' and line[i-1]!='!' and line[i-1]!='?') or line[i]!=' ':
            Sen+=line[i]
        if line[i]=='.' or line[i]=='!' or line[i]=='?':
            if t>si_max:
                si_max=t
                smax=Sen
            elif si_min==-1 or (si_min!=-1 and si_min>t):
                si_min=t
                smin=Sen
            t=0
            Sen=''
        else:
            if line[i]==' ':
                if line[i-1]!='.' and line[i-1]!='!' and line[i-1]!='?':
                    t+=1

file_out.write(smin+'\n')
file_out.write(smax+'\n')

file_in.seek(0)

t=0
while True:
    line=file_in.readline()
    if len(line)==0:
        break
    if line[-1]=='\n':
        line=line[:-1]+' \n'
    for i in range(len(line)):
        if (line[i]==' ' and line[i-1]!='.' and line[i-1]!='!' and line[i-1]!='?') or line[i]!=' ':
            file_out.write(line[i])
        if line[i]=='.' or line[i]=='!' or line[i]=='?':
            file_out.write('('+str(t+1)+')')
            t=0
        else:
            if line[i]==' ':
                if line[i-1]!='.' and line[i-1]!='!' and line[i-1]!='?':
                    t+=1
                    
    
file_in.close()
file_out.close()
