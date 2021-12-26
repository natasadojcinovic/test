#!/usr/bin/env python
# coding: utf-8

# In[4]:


from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


# In[5]:


df = pd.read_excel('AEA 17-11-2021.xlsx')


# In[6]:


browser = webdriver.Chrome(executable_path=r"C:\Users\ndojcinovic\Anaconda3\Chrome driver\chromedriver.exe")
browser.get('https://ux-ts5.egatesoln.com/#/login')

time.sleep(1)

username=browser.find_element_by_xpath('//*[@id="username"]')
username.send_keys('TYPE USER NAME HERE')

password=browser.find_element_by_xpath('//*[@id="password"]')
password.send_keys('TYPE PASSWORD HERE')


time.sleep(3)

Login = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/form/div/div/div[3]/button')
Login.click()

time.sleep(5)

Create_Item=browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/a/i')
Create_Item.click()

time.sleep(3)


for i in df.index:
    entry =df.loc[i]
    
   
    
    time.sleep(3)
    
    Retail_Item_Code = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/form/div/div[2]/div[1]/fieldset[1]/div[1]/input')
    Retail_Item_Code.send_keys(entry['Retail Item Code'])
    
    Retail_Item_Name = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/form/div/div[2]/div[1]/fieldset[1]/div[2]/input')
    Retail_Item_Name.send_keys(entry['Retail Item Name'])
    
    POS_Display_Name = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/form/div/div[2]/div[1]/fieldset[1]/div[3]/input')
    POS_Display_Name.send_keys(entry['POS Display Name'])
    
    Item_Description = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/form/div/div[2]/div[1]/fieldset[1]/div[5]/input')
    Item_Description.send_keys(entry['Retail Item Name'])
    
    Print_Receipt = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/form/div/div[2]/div[1]/fieldset[1]/div[9]/input')
    Print_Receipt.click()
   
    time.sleep(3)

    
    #drop menu 
    
    Sales_Category_drop_menu = Select(browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/form/div/div[2]/div[1]/fieldset[2]/div[1]/select'))
    Sales_Category_drop_menu.select_by_visible_text(entry['Child Sales Category Name'])
    
   #fix on "Regular", always the same!

    Item_Type_drop_menu = Select(browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/form/div/div[2]/div[1]/fieldset[2]/div[2]/select'))
    Item_Type_drop_menu.select_by_visible_text(entry['Item Type'])  
    
    #check inventory if necessary
    
    Item_Characteristics = browser.find_element_by_xpath('//*[@id="itemCharacteristics"]/div[1]/input')
    Item_Characteristics.send_keys(entry['Item Characteristics'])  
    Item_Characteristics.send_keys(Keys.ENTER)
    
    #counter for item tags

    Item_Tags_str = entry ['Item Tags']
    Tags = Item_Tags_str.split(', ')
    
    for i in Tags:
        Item_Tags_input = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/form/div/div[2]/div[2]/fieldset[1]/div[1]/div/div[1]/input')
        Item_Tags_input.send_keys(i)
        Item_Tags_input.send_keys(Keys.ENTER)
        time.sleep (3) 
        
    #date
    #date setup in field keywords 
    Date_from = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/form/div/div[2]/div[1]/fieldset[1]/div[7]/input')
    Date_from.send_keys(entry['Retail Item From Date'])
    

    #date setup in field unique selling points
    Date_to = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/form/div/div[2]/div[1]/fieldset[1]/div[8]/input')
    Date_to.send_keys(entry['Retail Item To Date'])
    


    #select date from

    actions= ActionChains(browser)
    actions.double_click(Date_from)
    actions.perform()
    actions.double_click(Date_from)
    actions.perform()

    #copy ctrl+c

    actions.key_down(Keys.CONTROL).send_keys('c').perform()

    #paste ctrl+v
    
    Date = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/form/div/div[2]/div[1]/div/div[1]/date-picker-field/fieldset/div/p/input')
    paste = ActionChains(browser)
    paste.move_to_element(Date).click()
    paste.perform()
    paste.send_keys(Keys.BACKSPACE)
    paste.key_down(Keys.CONTROL).send_keys('v').perform()
    Date.send_keys(Keys.ENTER)

    time.sleep(3)

    #select date to

    select_to= ActionChains(browser)
    select_to.double_click(Date_to)
    select_to.perform()
    select_to.double_click(Date_to)
    select_to.perform()

    select_to.key_down(Keys.CONTROL).send_keys('c').perform()

    Date_to = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/form/div/div[2]/div[1]/div/div[2]/date-picker-field/fieldset/div/p/input')
    paste_to = ActionChains(browser)
    paste_to.move_to_element(Date_to).click()
    paste_to.perform()
    paste_to.send_keys(Keys.BACKSPACE)
    paste_to.key_down(Keys.CONTROL).send_keys('v').perform()
    Date_to.send_keys(Keys.ENTER)
    
    time.sleep(3)
    
    delete_date_from = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/form/div/div[2]/div[1]/fieldset[1]/div[7]/input')
    delete_date_from.click()
    delete_date_from.clear()
    
    delete_date_to = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/form/div/div[2]/div[1]/fieldset[1]/div[8]/input')
    delete_date_to.click()
    delete_date_to.clear()
    
    time.sleep(2)
    
    #entering price
    
    Price_Effective_from = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/form/div/div[2]/div[1]/fieldset[1]/div[7]/input')
    Price_Effective_from.send_keys(entry['Price Effective From Date'])
    Price_Effective_to = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/form/div/div[2]/div[1]/fieldset[1]/div[8]/input')
    Price_Effective_to.send_keys(entry['Price Effective To Date'])

    actions= ActionChains(browser)
    actions.double_click(Price_Effective_from)
    actions.perform()
    actions.double_click(Price_Effective_from)
    actions.perform()

    actions.key_down(Keys.CONTROL).send_keys('c').perform()

    Date = browser.find_element_by_xpath('//*[@id="price-type-container"]/div/input-price-type/div/div[2]/div[1]/div[1]/div[1]/div[1]/date-picker-field/fieldset/div/p/input')
    paste = ActionChains(browser)
    paste.move_to_element(Date).click()
    paste.perform()
    paste.send_keys(Keys.BACKSPACE)
    paste.key_down(Keys.CONTROL).send_keys('v').perform()
    Date.send_keys(Keys.ENTER)
    
    select_to= ActionChains(browser)
    select_to.double_click(Price_Effective_to)
    select_to.perform()
    select_to.double_click(Price_Effective_to)
    select_to.perform()

    select_to.key_down(Keys.CONTROL).send_keys('c').perform()

    Date_to = browser.find_element_by_xpath('//*[@id="price-type-container"]/div/input-price-type/div/div[2]/div[1]/div[1]/div[1]/div[2]/date-picker-field/fieldset/div/p/input')
    paste_to = ActionChains(browser)
    paste_to.move_to_element(Date_to).click()
    paste_to.perform()
    paste_to.send_keys(Keys.BACKSPACE)
    paste_to.key_down(Keys.CONTROL).send_keys('v').perform()
    Date_to.send_keys(Keys.ENTER)
    
    time.sleep(2)
    
    Price_Type = browser.find_element_by_xpath('//*[@id="price-type-container"]/div/input-price-type/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/select')
    Price_Type.send_keys(entry['Price Type'])
    
    Tax_Is = browser.find_element_by_xpath('//*[@id="price-type-container"]/div/input-price-type/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/select')
    Tax_Is.send_keys(entry['Tax Is'])
    
    time.sleep(2)
    
    #price 
    
    Price_str = entry['Price']
    Price_value = str(Price_str)
    Price= browser.find_element_by_xpath('//*[@id="price-type-container"]/div/input-price-type/div/div[2]/div[1]/div[2]/div[1]/div/input')
    Price.send_keys(Price_value)
    
    time.sleep(2)
    
    #tax type
    
    Add_Tax_Type = browser.find_element_by_xpath('//*[@id="add-tax-type"]')
    Add_Tax_Type.click()
    
    time.sleep(2)
    
    #split in excel tax type and applied tax type
    Tax_Type = browser.find_element_by_xpath('//*[@id="tax-type-container"]/div/input-tax-type/div/div[2]/div/div[1]/div/select')
    Tax_Type.send_keys(entry['Tax Type'])
    
    Tax_Type = browser.find_element_by_xpath('//*[@id="tax-type-container"]/div/input-tax-type/div/div[2]/div/div[2]/div/select')
    Tax_Type.send_keys(entry['Applied Tax Type'])
    
    time.sleep(3)
    
    delete_entry = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/form/div/div[2]/div[1]/fieldset[1]/div[7]/input')
    delete = ActionChains(browser)
    delete.move_to_element(delete_entry).click()
    delete.perform()
    delete_entry.clear()
    
    delete_entry1 = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/form/div/div[2]/div[1]/fieldset[1]/div[8]/input')
    delete1 = ActionChains(browser)
    delete1.move_to_element(delete_entry1).click()
    delete1.perform()
    delete_entry1.clear()
    
    #delete exptra tax type!!! i'm not sure why is made automatically at all!
    delete_taxtype1 = browser.find_element_by_xpath('//*[@id="tax-type-container"]/div[2]/input-tax-type/div/div[1]/p/span')
    delete_taxtype1.click()
    

    
    time.sleep(5)
    
    Create=browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/div[1]/div/div[2]/fieldset/button[2]')
    Create.click()
    
    time.sleep(5)
    
    Add_Another=browser.find_element_by_xpath('//*[@id="create-success"]/div/div/div[2]/button[2]')
    Add_Another.click()
    
    time.sleep(5)
    
    


# In[ ]:




