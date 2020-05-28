from selenium import webdriver
from selenium.webdriver.common.by import By
import xlsxwriter
workbook = xlsxwriter.Workbook('main.xlsx')
worksheet = workbook.add_worksheet()
driver = webdriver.Chrome(executable_path=r"C:\Users\vallarir\.wdm\drivers\chromedriver\81.0.4044.138\win32\chromedriver.exe");
driver.get(r"https://docs.microsoft.com/en-us/azure/virtual-machines/linux/compute-benchmark-scores?toc=/azure/virtual-machines/linux/toc.json");
rownum= 0
i=1
rownum=0
#//*[@id="compute-optimized-tab-content"]/div[1]/div[2]/div[2]/table/tbody
#/html/body/div[3]/div/section/div/div[1]/main/div[7]/table/thead
while(i <=26):
  headingname = "/html/body/div[3]/div/section/div/div[1]/main/h2[" + str(i) + "]"
  t=i
  if i ==6:
    t=i+1
  elif i>6:
    t=i+2
  name = "/html/body/div[3]/div/section/div/div[1]/main/div[" + str(t) + "]/table/tbody"
  labelsname = "/html/body/div[3]/div/section/div/div[1]/main/div[" + str(t) + "]/table/thead"
  try:
    hbody = driver.find_element_by_xpath(headingname)
  except:
    i=i+1
    continue
  worksheet.write(rownum,0,hbody.text)
  try:
    lbody = driver.find_element_by_xpath(labelsname)
    print('done')
  except:
    i=i+1
    rownum= rownum+2
    continue
  labelrows = lbody.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
  for row in labelrows:       
    print('----')
    col = row.find_elements(By.TAG_NAME, "th") #note: index start from 0, 1 is col 2
    print(len(col))
    for index,num in enumerate(col):
      worksheet.write(rownum, index+1,num.text)
    rownum=rownum+1
  i=i+1
  try:
    tbody = driver.find_element_by_xpath(name)
  except:
    continue
  rows = tbody.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
  for row in rows:
    col = row.find_elements(By.TAG_NAME, "td") #note: index start from 0, 1 is col 2
    for index,num in enumerate(col):
      worksheet.write(rownum, index+1,num.text)
    rownum=rownum+1
  rownum= rownum +1
workbook.close()

#/html/body/div[3]/div/section/div/div[1]/main/h2[5]
#/html/body/div[3]/div/section/div/div[1]/main/div[5]/table/thead

#/html/body/div[3]/div/section/div/div[1]/main/h2[6]
#/html/body/div[3]/div/section/div/div[1]/main/div[7]/table/tbody

#/html/body/div[3]/div/section/div/div[1]/main/h2[7]
#/html/body/div[3]/div/section/div/div[1]/main/div[9]/table/tbody

#/html/body/div[3]/div/section/div/div[1]/main/h2[8]
#/html/body/div[3]/div/section/div/div[1]/main/div[10]/table/tbody

#/html/body/div[3]/div/section/div/div[1]/main/h2[9]
#/html/body/div[3]/div/section/div/div[1]/main/div[11]/table/tbody

#/html/body/div[3]/div/section/div/div[1]/main/div[12]/table/tbody

#/html/body/div[3]/div/section/div/div[1]/main/h2[26]
#/html/body/div[3]/div/section/div/div[1]/main/div[28]/table/tbody