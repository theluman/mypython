#!/usr/bin/env python
# -*- coding: utf-8 -*-
#转换
import re
chd = {' ':'m','0':'零','1':'壹','2':'贰','3':'叁','4':'肆','5':'伍','6':'陆','7':'柒','8':'捌','9':'玖'}
und = {'S':'拾','B':'佰','Q':'仟','W':'万','Y':'亿'}

#判断输入内容(首位不为零的整数)
ips = raw_input('Please input a number: ')
while ips[0] == '0':
    ips = raw_input('Wrong,the first non-zero: ')
else:
    while ips.isdigit():
        break
    else:
        ips = raw_input('Wrong,please input a number: ')
if len(ips) <= 9:
    #输出9位字符，右对齐，补空格
    ips = ips.rjust(9) 
    #转换成大写
    ops = chd[ips[0]]+und['Y']+chd[ips[1]]+und['Q']+chd[ips[2]]+und['B']+chd[ips[3]]+und['S']+chd[ips[4]]+und['W']+chd[ips[5]]+und['Q']+chd[ips[6]]+und['B']+chd[ips[7]]+und['S']+chd[ips[8]]+'元'
    #无用的数字位替换为空
    ops = re.sub('(m...)+','',ops)
    #处理零
    ops = re.sub('零元$','元',ops)
    ops = re.sub('零万','万',ops)
    ops = re.sub('(零...)+','零',ops)
    ops = re.sub('亿零万','亿零',ops)
    ops = re.sub('零万','万',ops)
    ops = re.sub('零元$','元',ops)
    ops = re.sub('亿零元$','亿元',ops)
    print ops
else:
    print 'The number is too big.'
