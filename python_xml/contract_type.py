# -*- coding: utf-8 -*-
import os
import xmlrpclib
import sys
import csv
import os

csv_file = csv.reader(open('contract_type.csv', 'rb'), delimiter=';')
f = open('contract_type_data.xml','w')
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
        xml += "        <record id='ctype_"+line[0]+"' model='"+ line[1]+ "'>\n"
        xml += "            <field name='name'>"+line[2]+"</field>\n"
        xml += "            <field name='code'>"+line[3]+"</field>\n"
        
        xml += "        </record>\n"
    cont+=1
    
    
xml += "    </data>\n"
xml += "</openerp>\n"


# print xml
f.write(xml)
f.close()
