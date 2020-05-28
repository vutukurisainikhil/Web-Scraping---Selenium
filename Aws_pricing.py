from selenium import webdriver
from selenium.webdriver.common.by import By
import xlsxwriter
from selenium.webdriver.support.ui import Select

workbook = xlsxwriter.Workbook("C:\\Users\\vsaibrah\\Documents\\WebScraping\\AWS_Pricing.xlsx")
driver = webdriver.Chrome(executable_path=r"C:\Users\vsaibrah\Documents\WebScraping\chrome Driver\chromedriver.exe")

def function(worksheet, labelname, name, row):
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
        tbody = driver.find_element_by_xpath(name)
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


linkname = "https://aws.amazon.com/ec2/pricing/reserved-instances/pricing/"
driver.get(linkname)
worksheet = workbook.add_worksheet()
row = 2
header_length = len("/html/body/div[1]/main/div[1]/div/div/div[6]/div/div[2]/div/div/div")
i=1
while(i<=176):
    try:
        lbody = driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/div/div/div[6]/div/div[2]/div/div/div["+str(i)+"]")
    except:
        print("error...")
    header_row = lbody.find_elements(By.TAG_NAME, "h2")
    for index,num in enumerate(header_row):
        worksheet.write(row, index, num.text)
        row = row+1
    labelname = "/html/body/div[1]/main/div[1]/div/div/div[6]/div/div[2]/div/div/div["+str(i)+"]/table"    #["+str(i)+"]/thead" # /tr  [1]/th[1]"
    table_len = len(labelname)
    #print(table_len)
    j=1
    while(j<=4):
        label = "/html/body/div[1]/main/div[1]/div/div/div[6]/div/div[2]/div/div/div["+str(i)+"]/table["+str(j)+"]/thead" 
        name = "/html/body/div[1]/main/div[1]/div/div/div[6]/div/div[2]/div/div/div["+str(i)+"]/table["+str(j)+"]/tbody"
        row = function(worksheet, label, name, row)
        j=j+1
    i = i+1

workbook.close()
print("...end ...")