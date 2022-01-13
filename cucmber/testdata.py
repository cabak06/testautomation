from faker import Faker
from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active


#for i in range(1,21):

testdata = [['Name','Adress','Phone number', 'Email', 'Color code', 'Job', 'Date']]

#['Rama','Bangalore'],['Sam','London']]

for data in testdata:
    ws.append(data)

#wb.save("demoexcel.xlsx")

fake_data = Faker()



for i in range(200):
   
    name = fake_data.name()
    address = fake_data.address()
    number = fake_data.phone_number()
    email = fake_data.email()
    color = fake_data.color()
    job = fake_data.job()
    dat = fake_data.date_time()
    dat_toStrng = str(dat)
    
    data_body = [name, address,number, email, color, job, dat_toStrng]
    ws.append(data_body)

wb.save('demoexcel.xlsx')

"""
fake_data = Faker()

name = fake_data.name()
address = fake_data.address()
number = fake_data.phone_number()
email = fake_data.email()
color = fake_data.color()
job = fake_data.job()
dat = fake_data.date_time()
"""


