import json

I = [{'http':'http://yemao:yemao@103.43.11.18:6666'},
{'http':'http://yemao:yemao@103.43.11.19:6666'},
{'http':'http://yemao:yemao@103.43.11.20:6666'},
{'http':'http://yemao:yemao@103.43.11.21:6666'},
{'http':'http://yemao:yemao@103.43.11.22:6666'},
{'http':'http://yemao:yemao@45.113.2.130:6666'},
{'http':'http://yemao:yemao@45.113.2.131:6666'},
{'http':'http://yemao:yemao@45.113.2.132:6666'},
{'http':'http://yemao:yemao@45.113.2.133:6666'},
{'http':'http://yemao:yemao@45.113.2.134:6666'},
{'http':'http://yemao:yemao@103.52.153.248:6666'},
{'http':'http://yemao:yemao@103.52.153.249:6666'},
{'http':'http://yemao:yemao@103.52.153.250:6666'},
{'http':'http://yemao:yemao@103.52.153.251:6666'},
{'http':'http://yemao:yemao@103.52.153.252:6666'},
{'http':'http://yemao:yemao@103.52.153.253:6666'},
{'http':'http://yemao:yemao@103.52.153.254:6666'},
{'http':'http://yemao:yemao@43.251.224.18:6666'},
{'http':'http://yemao:yemao@43.251.224.19:6666'},
{'http':'http://yemao:yemao@43.251.224.20:6666'},
{'http':'http://yemao:yemao@43.251.224.21:6666'},
{'http':'http://yemao:yemao@43.251.224.22:6666'},
{'http':'http://yemao:yemao@43.251.224.23:6666'},
{'http':'http://yemao:yemao@43.251.224.24:6666'},
{'http':'http://yemao:yemao@43.251.224.25:6666'},
{'http':'http://yemao:yemao@43.251.224.26:6666'},
{'http':'http://yemao:yemao@43.251.224.27:6666'},
{'http':'http://yemao:yemao@43.251.224.28:6666'},
{'http':'http://yemao:yemao@43.251.224.29:6666'},
{'http':'http://yemao:yemao@43.251.224.30:6666'}]

def write_in(content):
    print('do wirte')
    f = open("ip.txt", "w")
    f.writelines(content)
    f.close()

def read_out2():
    write_in(json.dumps(I, ensure_ascii=False))
    f = open('ip.txt')
    content = f.read()
    f.close()
    return content


if __name__ == '__main__':
    content = read_out2()
    print(content)
    IP_list0 = json.loads(content)
    print(IP_list0)
