from selenium import webdriver
from selenium.webdriver.common.by import By
import xlsxwriter
workbook = xlsxwriter.Workbook("C:\Users\vsaibrah\Documents\WebScraping\test_mainextra.xlsx")
driver = webdriver.Chrome(executable_path=r"C:\Users\vsaibrah\Documents\WebScraping\chrome Driver\chromedriver.exe");
list = ["av2-series", "sizes-b-series-burstable", "dcv2-series", "dv2-dsv2-series", "dv3-dsv3-series", "dav4-dasv4-series"]

def function(item, worksheet, content, row):
  #[] = list(content)
  (labelname, name) = content
  try:
    lbody = driver.find_element_by_xpath(labelname)
  except:
    return row
  labelrows = lbody.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
  for rowtext in labelrows:       
    col = rowtext.find_elements(By.TAG_NAME, "th") #note: index start from 0, 1 is col 2
    print(len(col))
    for index,num in enumerate(col):
      worksheet.write(row, index,num.text)
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


for index, item in enumerate(list):
  linkname = "https://docs.microsoft.com/en-us/azure/virtual-machines/" +item + "?toc=/azure/virtual-machines/linux/toc.json&bc=/azure/virtual-machines/linux/breadcrumb/toc.json"
  driver.get(linkname);
  if index == 0 or index==2:
    labelname = ["/html/body/div[3]/div/section/div/div[1]/main/div/table/thead"]
    name = ["/html/body/div[3]/div/section/div/div[1]/main/div/table/tbody"]
  elif index ==1:
    labelname = ["/html/body/div[3]/div/section/div/div[1]/main/div[1]/table/thead"]
    name = ["/html/body/div[3]/div/section/div/div[1]/main/div[1]/table/tbody"]
  else:
    labelname = ["/html/body/div[3]/div/section/div/div[1]/main/div[1]/table/thead", "/html/body/div[3]/div/section/div/div[1]/main/div[2]/table/thead"]
    name= ["/html/body/div[3]/div/section/div/div[1]/main/div[1]/table/tbody", "/html/body/div[3]/div/section/div/div[1]/main/div[2]/table/tbody"]
  worksheet = workbook.add_worksheet()
  worksheet.write(0, 0,item)
  row = 2
  for content in zip(labelname,name):
    print(content)
    row = function(item, worksheet, content,row)

workbook.close()