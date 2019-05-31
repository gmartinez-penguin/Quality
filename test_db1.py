#!/usr/bin/python36

import sys
import re
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

#mb_type = "MG21-OP0"
#mb_count = 1

#cpu_type = "Gold 6148"
#cpu_count = 2

mem = {"\tSize: 64 GB": "24"}


dbi = {"Motherboard: ": ["MG21-OP0", 1, "10026290 "],
       "CPU: ": ["Gold 6148", 2, "10023894 "],
       "Memory: ": ["\tSize: 64 GB", 24, "10026598 "]}


#mem_type = "\tSize: 64 GB"
#mem_count = 24


#pci = {"Tesla V100": "4", "ConnectX-6]": "1", "X520":"2"}

#disk = {"ST2000NX0243": 1}
disk = {"Disk: ": ["ST2000NX0243", 1, "10020361 "]}


pci = {"Tesla V100": [4, 1, "10026186 "],
       "ConnectX-6]":[1, 1, "10025751 "],
       "X520":[1, 2, "10012600 "]}


pid = input("Please enter a Penguin Serial Number: " ).strip()
pid = pid.upper()
#pid = "P100197457"

pids = []

if (pid.startswith("P")):
    print ("PID starts wtih P:", pid)
    pids = pid.split()

else:
    print("PID does not start with P:",  pid)
    nums = pid.split()

    beg = int(nums[0])
    end = int(nums[1])

    for sn in range(beg,end):
        print ("SN: ", 'P' + str(sn))
        pids.append('P' + str(sn))

print ("pids:", pids)

for pid in (pids):
    print("PID in array:", pid)


    db = MySQLdb.connect("192.168.5.47", "finalqc","r0ckh0pp3rch1n5tr4p","uberkonsole")

    cursor = db.cursor()



#sql = "show tables"
#sql = "select id,serial_no,partitions from machine_hwlog where serial_no='p100197457' and id=129281"
#sql = "select id,serial_no,partitions from machine_hwlog where serial_no='p100197457' "
    sql = "select id,serial_no,lspci_vvv from machine_hwlog where serial_no= " + "'" + pid + "'"


    cursor.execute(sql)

    res = cursor.fetchall()
    hi_id = 0

    for row in res:
       if hi_id < row[0]:
          hi_id = row[0]
#          print(row)

    print ("hi_id = ", hi_id)

    if hi_id == 0:
        print ("The P Serial Number " + pid + " was not found.")
#        sys.exit()
        continue




    sql = "select id,lspci_vvv,dmidecode,smartctl from machine_hwlog where serial_no="  + "'"  + pid + "'" + " and id=" + str(hi_id)


#sql = "select id,serial_no,dmidecode from machine_hwlog where serial_no='p100197457' and id=" + str(hi_id)

    cursor.execute(sql)

    res = cursor.fetchall()

    cpu = "Gold 6148"
    files = "/Penguin/" + pid
    outfile = open( files, "w")

    for row in res:
#      print(row[2].count(cpu_type))
#      x = re.findall(mem_type, row[2])

        for key in dbi:
            x = re.findall(dbi[key][0], row[2])
            dbi_counts = len(x)
            if (dbi_counts == dbi[key][1]):
                print(dbi[key][2] + key + dbi[key][0] + " type and count is correct")
                dbi_pass = dbi[key][2] + "," + key + dbi[key][0] + "," + str(dbi[key][1]) + "," + "PASS\n"
                outfile.write(dbi_pass)
            else:
                print(dbi[key][2] + key + dbi[key][0] + " type and count is NOT correct")
                dbi_fail = dbi[key][2] + "," + key + dbi[key][0] + "," + "S/B " + str(dbi[key][1]) + " was " + str(dbi_counts) + "," + "FAIL\n"
                outfile.write(dbi_fail)



        for key in disk:
            x = re.findall(disk[key][0], row[3])
#          print(len(x))
            disk_counts = len(x)

            if (disk[key][1] == disk_counts):
                print(disk[key][2] + key + disk[key][0] +  " type and count is correct.")
                disk_pass = disk[key][2] + ","  + key + disk[key][0] + "," + str(disk_counts) + "," + "PASS\n"
                outfile.write(disk_pass)

            else:
                print(disk[key][2] + key + disk[key][0] +  " type and count is NOT correct.")
                disk_fail = disk[key][2] + "," + key + disk[key][0] + "," + "S/B " + str(disk[key][1]) + " was " + str(disk_counts) + "," + "FAIL\n"
                outfile.write(disk_fail)


        for key in pci:
             x = re.findall(key, row[1])
#         print(len(x))
             pci_counts = len(x) // pci[key][1]
             if (int(pci[key][0]) == pci_counts):
                 print (pci[key][2] + "PCI: " + key + " type and count is correct.")
                 pci_pass = pci[key][2] + "," + "PCI: " + key + "," + str(pci_counts) + "," + "PASS\n"
                 outfile.write(pci_pass)

             else:
                 print (pci[key][2] + "PCI: " + key + " type and count is NOT correct.")
                 pci_fail = pci[key][2] + "," + "PCI: " + key + "," + "S/B " + str(pci[key][0]) + " was " + str(pci_counts) + "," + "FAIL\n"
                 outfile.write(pci_fail)



    outfile.close()


