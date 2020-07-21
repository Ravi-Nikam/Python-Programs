import psycopg2


try:
    sql="create table demo1(did int,dname varchar(20));"
    sql1="insert into demo1(did,dname) values(3,'Sales');"
    dname="G_Man"
    sql2="update demo1 set dname='"+dname+"' where did=1"
    sql3="delete from demo1 where did=1"
    sql4="select did,dname from demo1"
    conn= psycopg2.connect(host="localhost",user="postgres",password=1234,database="postgres")                          
    cur = conn.cursor()
    result=cur.execute(sql4)
    if result==None:
        print("Done")
    list1=result.fetchall()
    print(list1)
    for r in list1:
        print(f"did {r[0]} dname {r[1]}")
    conn.commit()
    conn.close()
except Exception as e:
    print(e)


