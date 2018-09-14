"""
:return a array of personal and family objects.
"""
from prettytable import PrettyTable
import time


def read_gedcom_file(path):
    '''
       Read a GEDCOM file and inspect the TAGs are valid or not, then output to a new file.
       :param infile: input file name
       :param outfile: output file name
       :return:
       '''
    f = open(path, 'r')
    result = list()
    for line in f.readlines():
        line = line.strip()
        msg = line.split(" ")
        level = msg[0]
        valid_tag_l0 = ['HEAD', 'TRLR', 'NOTE']
        valid_tag_l0_reverse = ['INDI', 'FAM']
        valid_tag_l1 = ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC',
                        'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV']
        valid_tag_l2 = ['DATE']
        if level == '0':
            if msg[1] in valid_tag_l0:
                tag = msg[1]
                flag = 'Y'
                argument = ' '.join(msg[2:])
                l = (level, tag, flag, argument)
            elif msg[2] in valid_tag_l0_reverse:
                tag = msg[2]
                flag = 'Y'
                ID = msg[1]
                l = (level, tag, flag, ID)
            else:
                tag = msg[1]
                flag = 'N'
                argument = ' '.join(msg[2:])
                l = (level, tag, flag, argument)

        elif level == '1':
            tag = msg[1]
            argument = ' '.join(msg[2:])
            if msg[1] in valid_tag_l1:
                flag = 'Y'
            else:
                flag = 'N'
            l = (level, tag, flag, argument)

        elif level == '2':
            tag = msg[1]
            argument = ' '.join(msg[2:])
            if msg[1] in valid_tag_l2:
                flag = 'Y'
            else:
                flag = 'N'
            l = (level, tag, flag, argument)

        else:
            tag = msg[1]
            flag = 'N'
            argument = ' '.join(msg[2:])
            l = (level, tag, flag, argument)

        result.append(l)
    f.close()
    return result


def write_gedcom_file(path, obj):
    pass


def parse_getcom(obj):
    indis = {}
    fams = {}
    current = ()
    for i in obj:
        if i[0] == "0":
            if ["HEAD", "NOTE", "TRLR"].count(i[1]) == 1:
                continue
            current = (i[1], i[3])
            if i[1] == "FAM":
                fams[i[3]] = {}
                fams[i[3]][i[1]] = i[3]
            if i[1] == "INDI":
                indis[i[3]] = {}
                indis[i[3]][i[1]] = i[3]
        elif i[0] == '1':
            has_l2 = ['BIRT', 'DEAT', 'MARR', 'DIV']
            if has_l2.count(i[1]) == 1:
                l1_name = i[1]
            elif current[0] == "FAM":
                if (fams[current[1]].get(i[1]) != None):
                    if (type(fams[current[1]][i[1]]) == type("")):
                        fams[current[1]][i[1]] = [fams[current[1]][i[1]]]
                    fams[current[1]][i[1]].append(i[3])
                else:
                    fams[current[1]][i[1]] = i[3]
            elif current[0] == "INDI":
                if (indis[current[1]].get(i[1]) != None):
                    if (type(indis[current[1]][i[1]]) == type("")):
                        indis[current[1]][i[1]] = [indis[current[1]][i[1]]]
                    indis[current[1]][i[1]].append(i[3])
                else:
                    indis[current[1]][i[1]] = i[3]
        elif i[0] == '2':
            if i[1] == "DATE":
                if current[0] == "FAM":
                    fams[current[1]][l1_name + i[1]] = i[3]
                elif current[0] == "INDI":
                    indis[current[1]][l1_name + i[1]] = i[3]

    return {"fams": fams, "indis": indis}

def print_fams(info):
    fams = info["fams"]
    indis = info["indis"]
    fams_table = PrettyTable(
        ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"])
    for id in fams:
        fam = fams[id]
        line = []
        line.append(fam["FAM"])
        line.append(fam["MARRDATE"])
        line.append(fam.get("DIVDATE"))
        line.append(fam["HUSB"])
        line.append(indis[fam["HUSB"]]["NAME"])
        line.append(fam["WIFE"])
        line.append(indis[fam["WIFE"]]["NAME"])
        line.append(fam.get("CHIL"))
        fams_table.add_row(line)
    print(fams_table)

def print_indis(info):
    indis = info["indis"]
    indis_table = PrettyTable(["ID", "Name", "GENDER", "BIRTHDAY", "Age", "Alive", "Death", "Child", "Spouse"])
    for id in indis:
        indi = indis[id]
        line = []
        line.append(indi["INDI"])
        line.append(indi["NAME"])
        line.append(indi["SEX"])
        line.append(indi["BIRTDATE"])
        year_birth = int(indi["BIRTDATE"].split(" ")[2])
        year_death = int(indi["DEATDATE"].split(' ')[2])
        if (year_death == None):
            now_year = int(time.strftime("%Y", time.localtime(time.time())))
            line.append(now_year - year_birth)
        else:
            line.append(year_death - year_birth)
        line.append(indi.get("DEATDATE") == None)
        line.append(indi.get("DEATDATE"))
        line.append(indi.get("FAMC"))
        line.append(indi.get("FAMS"))
        indis_table.add_row(line)
    print(indis_table)


def main():
    info = parse_getcom(read_gedcom_file('pp.txt'))
    print_indis(info)
    print_fams(info)


if __name__ == '__main__':
    main()