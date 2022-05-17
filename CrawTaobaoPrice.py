# -*- coding: utf-8 -*-
import xlsxwriter as xw
import requests
import re
def getHTMLText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'cookie': 'cna=4EY9GBCGi24CAX0hoxPCSh3o; lgc=tb016326075; tracknick=tb016326075; enc=vAQP3%2BDiMCsmpBTPzOYmEIf8ck2VCf7vC7nkQZ8%2FaWvOxPgNQ%2Bq9Tqk7CeUAsuxbNycLP1m34NetTpzAHUGLY6%2BIoDKIGwerwubCYx%2BRGgU%3D; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; miid=2129683386431328771; uc3=nk2=F5RFgYsblJqh%2Fxg%3D&lg2=URm48syIIVrSKA%3D%3D&id2=UUphyu%2BMQePK3ZcJpg%3D%3D&vt3=F8dCuAAj3fWCuQmoFRA%3D; sgcookie=E1001PKHlEpHPIwgZdgXqmuN4zNC5c2rLh0ZZl2qrrU2tpqYBo4DeiGoYkBtV2vrW8la5C5mno3THPQIol2aGJP%2B1g%3D%3D; uc4=id4=0%40U2grEanNorSHEVC%2FCJPnu1dyk6%2Fm%2Blb%2B&nk4=0%40FY4O6GMel1dzoUGz33V%2BnooVPIKaeQ%3D%3D; _cc_=V32FPkk%2Fhw%3D%3D; mt=ci=-1_0; t=d6a7916c433234b48b3736ab03124eb3; _tb_token_=ebb07d739b617; _m_h5_tk=1552cdc6833858830d8b3ce0002ff6a3_1610964559834; _m_h5_tk_enc=e17584be300f3e8c02a520783ff33afe; xlly_s=1; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; cookie2=1b2930486c1a521557fda231d6bea006; uc1=cookie14=Uoe1gqFMHiHajw%3D%3D; l=eBxIxLbROluIR8QEBO5Zhurza77T3IOfGsPzaNbMiInca6OF6e2h0NCINVIeJdtjgtCXhetyAv1yVdHyJNUKg2HvCbKrCyCuQxJO.; tfstk=c2jFB009-kEFUAx7kHtrO0JWacndaWRkGcJ2-aCGJq4z1mTpgsfSwdqLJdJyMlYh.; isg=BNLSjHOo5mgFdCUsNcrbgSaEI5i049Z9mBe_c5wq5AVJr3aphHPPjYYNHwuT304V; JSESSIONID=2D6B9CE4E9E5A60BCE2129936E482C77'}
        r=requests.get(url,headers=kv,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "error"
def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)#纯数字re表达式
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        salt = re.findall(r'\"view_sales\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(":")[1])
            title = eval(tlt[i].split(":")[1])
            sales = eval(salt[i].split(":")[1])
            ilt.append([price,title,sales])
    except:
        print("parsr Error")

def printList(ilt):
    tplt = "{:4}\t{:8}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","销量","商品信息"))
    count = 0
    for g in ilt:
        count +=1
        print(tplt.format(count,g[0],g[2],g[1]))



def xw_toExcel(ilt, fileName):  # xlsxwriter库储存数据到excel
    workbook = xw.Workbook(fileName)  # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.activate()  # 激活表
    title = [ '价格', '销量','商品信息']  # 设置表头
    worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
    i = 2  # 从第二行开始写入数据
    for j in range(len(ilt)):
        insertData = [ilt[j][0], ilt[j][2], ilt[j][1]]
        row = 'A' + str(i)
        worksheet1.write_row(row, insertData)
        i += 1
    workbook.close()  # 关闭表

def main():
    goods = input("输入搜索项:")
    depth = 2 #检索深度
    start_url = "https://s.taobao.com/search?q=" + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url +"&s="+str(44*i)
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printList(infoList)
    fileName = '测试.xlsx'
    xw_toExcel(infoList,fileName)

main()