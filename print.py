def pretty_table(a,b):
    print("Individuals")
    lista=[]
    listb=[]
    x = PrettyTable(field_names=["ID", "Name", "Gender", "Birthday","Age","Alive","Death","Child","Spouse"])
    y = PrettyTable(field_names=["ID", "Married", "Divorced", "Husband ID","Husband Name","Wife ID","Wife Name","Children"])
    y.align["name"] = "1"
    y.padding_width = 1
    x.align["name"] = "l"  # 以name字段左对齐
    x.padding_width = 1   # 填充宽度
    i=0
    j=0
    while i< len(a):
        lista=[a[i]['INDI'],a[i]['NAME'],a[i]['SEX'],a[i]['BIRT'],a[i]['AGE'],a[i]['ALIVE'],a[i]['DEAT'],a[i]['CHIL'],a[i]['SPOUSE']];
        x.add_row(lista)    #x.add_row(a[1])
        i+=1
        #x.add_row(a[2])
    print(x)
    print("Families")
        #print(lista)
    while j< len(b):
        listb=[b[j]['FAM'],b[j]['MARR'],b[j]['DIV'],b[j]['HUSB'],b[j]['HUSB_NAME'],b[j]['WIFE'],b[j]['WIFE_NAME'],b[j]['CHIL']];
        y.add_row(listb)    #x.add_row(a[1])
        j+=1
        #x.add_row(a[2])
    print(y)


    pass
