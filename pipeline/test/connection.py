"""
=========================================================================
Project:
- <project-name>

Module:
- pipeline/test

File: connection.py

Purpose:
- MySQL 데이터베이스 연결 테스트
- Docker 환경에서 MySQL 컨테이너 연결 상태 확인

Author: (조동휘)
Created: 2026-03-06

Updated:
- 2026-03-06: initial version (조동휘)
=========================================================================
"""
import pymysql

conn = pymysql.connect(
    host='mysql',
    user='root',
    password='1234',
    port=3306,
)

cursor = conn.cursor()
cursor.execute("SHOW DATABASES")

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
