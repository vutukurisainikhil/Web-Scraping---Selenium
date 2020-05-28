from selenium import webdriver
from selenium.webdriver.common.by import By
import xlsxwriter
workbook = xlsxwriter.Workbook("C:\\Users\\vsaibrah\\Documents\\WebScraping\\AWS_Server.xlsx")
driver = webdriver.Chrome(executable_path=r"C:\Users\vsaibrah\Documents\WebScraping\chrome Driver\chromedriver.exe")
list = ["compute-optimized-instances", "memory-optimized-instances", "storage-optimized-instances", "accelerated-computing-instances"]
table_name = ["Hardware specifications","Network performance","SSD I/O performance","Instance features"]

def function(worksheet, content,table, row):
    labelname =content
    print("--"+table)
    worksheet.write( row,0, table)
    row = row+1
    try:
        lbody = driver.find_element_by_xpath(labelname)
    except:
        return row
    labelrows = lbody.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
    for rowtext in labelrows:       
        col = rowtext.find_elements(By.TAG_NAME, "th") #note: index start from 0, 1 is col 2
        #print(len(col))
        for index,num in enumerate(col):
            #print(num.text)
            worksheet.write(row, index, num.text)
        row=row+1
    try:
        tbody = driver.find_element_by_xpath(labelname)
    except:
        return row
    rows = tbody.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
    for rowtext in rows:
        col = rowtext.find_elements(By.TAG_NAME, "td") #note: index start from 0, 1 is col 2
        for index,num in enumerate(col):
            worksheet.write(row, index,num.text)
        row=row+1
    row= row +1
    return row


for index, item in enumerate(list):
    linkname = "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/"+item+".html"
    driver.get(linkname)
    if index == 0 :
        labelname = ["/html/body/div[1]/awsui-app-layout/div/main/div[2]/div/div/awsdocs-view/div/div/div[4]/div[1]/div[4]/div/table/tbody",
                "/html/body/div[1]/awsui-app-layout/div/main/div[2]/div/div/awsdocs-view/div/div/div[4]/div[1]/div[5]/div/table/tbody",
                "/html/body/div[1]/awsui-app-layout/div/main/div[2]/div/div/awsdocs-view/div/div/div[4]/div[1]/div[6]/div/table/tbody",
                "/html/body/div[1]/awsui-app-layout/div/main/div[2]/div/div/awsdocs-view/div/div/div[4]/div[1]/div[7]/div/table/tbody"]
    #name = ["/html/body/div[3]/div/section/div/div[1]/main/div/table/tbody"]
    elif index == 1 :
        labelname = ["/html/body/div[1]/awsui-app-layout/div/main/div[2]/div/div/awsdocs-view/div/div/div[4]/div[1]/div[9]/div/table/tbody",
                "/html/body/div[1]/awsui-app-layout/div/main/div[2]/div/div/awsdocs-view/div/div/div[4]/div[1]/div[10]/div/table/tbody",
                "/html/body/div[1]/awsui-app-layout/div/main/div[2]/div/div/awsdocs-view/div/div/div[4]/div[1]/div[11]/div/table/tbody",
                "/html/body/div[1]/awsui-app-layout/div/main/div[2]/div/div/awsdocs-view/div/div/div[4]/div[1]/div[12]/div/table/tbody"]
    #name = ["/html/body/div[3]/div/section/div/div[1]/main/div[1]/table/tbody"]
    elif index == 2:
        labelname=["/html/body/div[1]/awsui-app-layout/div/main/div[2]/div/div/awsdocs-view/div/div/div[4]/div[1]/div[7]/div/table/tbody",
                "/html/body/div[1]/awsui-app-layout/div/main/div[2]/div/div/awsdocs-view/div/div/div[4]/div[1]/div[8]/div/table/tbody",
                "/html/body/div[1]/awsui-app-layout/div/main/div[2]/div/div/awsdocs-view/div/div/div[4]/div[1]/div[9]/div/table/tbody",
                "/html/body/div[1]/awsui-app-layout/div/main/div[2]/div/div/awsdocs-view/div/div/div[4]/div[1]/div[10]/div/table/tbody"]
    else:
        labelname = ["/html/body/div[1]/awsui-app-layout/div/main/div[2]/div/div/awsdocs-view/div/div/div[4]/div[1]/div[4]/div/table/tbody",
                "/html/body/div[1]/awsui-app-layout/div/main/div[2]/div/div/awsdocs-view/div/div/div[4]/div[1]/div[5]/div/table/tbody",
                "",
                "/html/body/div[1]/awsui-app-layout/div/main/div[2]/div/div/awsdocs-view/div/div/div[4]/div[1]/div[6]/div/table/tbody"]
    #name= ["/html/body/div[3]/div/section/div/div[1]/main/div[1]/table/tbody", "/html/body/div[3]/div/section/div/div[1]/main/div[2]/table/tbody"]
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, item)
    print(item)
    row = 2
    for content,table in zip(labelname, table_name):
        #print(content)
        row = function(worksheet,content,table,row)

workbook.close()