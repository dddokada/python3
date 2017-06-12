import pymssql
cnn = pymssql.connect(host="DLWMTTSTDB1V.jdadelivers.com",user="dmzuser",password="F3110w$",database="walmart_jp_b")
cur = cnn.cursor()

print("�P����SELECT��==========================")
print("VARCHAR�̃G���R�[�h�������������Ƃ��m�F")
from_id = 45
to_id = 999
cur.execute("""SELECT TOP 1000 * FROM  [walmart_jp_b].[dbo].[Address] where address_id in(1,2,12, 189) """ , (from_id, to_id))
rows = cur.fetchall()
for row in rows:
    print(row)


print("VARCHAR�̃t�B�[���h�͈����Ȃ��̂�NVARCHAR�ɕϊ�����")
# VARCHAR�̃t�B�[���h�͈����Ȃ��̂�NVARCHAR�ɕϊ����ĕԂ�
cur.execute("""SELECT TOP 1000 * FROM  [walmart_jp_b].[dbo].[Address] where address_id in(1,2,12, 189) """ , (from_id, to_id))
rows = cur.fetchall()
for row in rows:
    print(row)
    print("%d %s" % (row[0], row[1]))

cur.close()
cnn.close()
