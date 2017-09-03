import os
import xlsxwriter
from datetime import datetime


def read_bank_line(line):
    columns = line.strip("\r\n").split('\t')
    return {
        "date": datetime.strptime(columns[2], '%Y%m%d'),
        "amount": float(columns[6].replace(",", ".")),
        "description": "".join(columns[7:])}


def create_xls(file, content):
    workbook = xlsxwriter.Workbook(file + '.xlsx')
    worksheet = workbook.add_worksheet()
    money_format = workbook.add_format({
        'num_format': '$#.##'})
    date_format = workbook.add_format({
        'num_format': 'dd/mm/yyyy'})
    worksheet.write('A1', 'Data')
    worksheet.write('B1', 'Historico')
    worksheet.write('C1', 'Valor')
    for line in range(len(content)):
        worksheet.write_datetime(line+1, 0,
                                 content[line]['date'],
                                 date_format)
        worksheet.write(line+1, 1,
                        content[line]['description'])
        worksheet.write(line+1, 2,
                        content[line]['amount'],
                        money_format)
    workbook.close()


def convert_file(file):
    bank_statement = open(file, 'r')
    data = [read_bank_line(line) for line in bank_statement]
    bank_statement.close()
    create_xls(file, data)


if __name__ == "__main__":
    for file in os.listdir("./"):
        if file.endswith(".txt"):
            convert_file(file)
