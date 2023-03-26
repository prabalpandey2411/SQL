import mysql.connector
conn=mysql.connector.connect(
    host ='localhost', username='root',password='CDAC2022',database='prabal'
)

my_cursor=conn.cursor()
yes="insert into book(bid,bname,bauthor,bcategory,bprice) values (%s,%s,%s,%s,%s)"
yes1=(8,"THINK AND GROW RICH","Napolion hills","self help",500.00)
my_cursor.execute(yes,yes1)
conn.commit()
conn.close()
print("Successfully installed")


