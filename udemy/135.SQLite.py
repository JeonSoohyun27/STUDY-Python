import sqlite3

conn = sqlite3.connect('test_sqlite.db')

# 메모리 상에서 테스트해볼때 :memory:를 적어주면 된다.
# conn = sqlite3.connect(':memory:')


curs = conn.cursor()

#테이블 생성
curs.execute(\
    'CREATE TABLE persons(id INTEGER PRIMARY KEY \
        AUTOINCREMENT, name STRING)')
conn.commit()

#데이터 생성과정
curs.execute(
    'INSERT INTO persons(name) values("MIKE")')
curs.execute(
    'INSERT INTO persons(name) values("NANCY")')
curs.execute(
    'INSERT INTO persons(name) values("JUNE")')
conn.commit()

# 데이터 내용 업데이트 과정 
curs.execute('UPDATE persons SET name = "Michel" WHERE name = "MIKE"')
conn.commit()

# 데이터 내용 삭제 과정
curs.execute('DELETE FROM persons WHERE name = "Michel"')
conn.commit()

curs.execute('SELECT * FROM persons')
print(curs.fetchall())

# 종료 과정
curs.close()
conn.close()
