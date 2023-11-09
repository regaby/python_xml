# -*- coding: utf-8 -*-
import os
import xmlrpclib
import sys
import csv
import os

csv_file = csv.reader(open('contract.csv', 'rb'), delimiter=';')
f = open('contract_data.xml','w')
bool={
    't':'True',
    'f':'False',
}
xml = "<?xml version='1.0' encoding='UTF-8'?>\n"
xml += "    <openerp>\n"
xml += "        <data noupdate='1'>\n"
cont=0
for line in csv_file:
    print line
    if  cont >0:
        xml += "        <record id='con_"+line[0]+"' model='"+ line[1]+ "'>\n"
        xml += "            <field name='name'>"+line[8]+"</field>\n"
        xml += "            <field ref='"+line[2]+"' name='employee_id'/>\n"
        xml += "            <field ref='"+line[3]+"' name='type_id'/>\n"
        xml += "            <field name='date_start'>"+line[4]+"</field>\n"
        xml += "            <field name='date_end'>"+line[5]+"</field>\n"
        xml += "            <field name='encasillamiento'>"+line[6]+"</field>\n"
        xml += "            <field name='fecha_promocion'>"+line[7]+"</field>\n"
        xml += "            <field name='fecha_antig'>"+line[9]+"</field>\n"
        xml += "            <field name='wage'>0.0</field>\n"
        xml += "        </record>\n"
    cont+=1
    
    
xml += "    </data>\n"
xml += "</openerp>\n"


print xml
f.write(xml)
f.close()
