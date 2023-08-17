import pyodbc, openpyxl


def import_file():

    connection_string = (
                        'Driver={SQL Server};'
                        'Server=nome_servidor;'
                        'Database=luan;'
                        'UID=usuario;'
                        'PWD=senha'
                        )
    connection = pyodbc.connect(connection_string)




    if(connection):
        workbook = openpyxl.load_workbook('C:\\Pasta1.xlsx', read_only=True, data_only=True)
        sheet = workbook['planilha1']
        cursor = connection.cursor()

        for rows in sheet.iter_rows(min_row=2, max_row=10):
            #print(rows[0].value)
            if(rows[0].value == None):
                connection.close()
                exit()
            else:    
                #print(rows[0].value, rows[1].value, rows[2].value, rows[3].value)
                cursor.execute("insert into pessoa(nome, idade) values (?, ?)", rows[0].value, rows[1].value)
                connection.commit()
            

        connection.close()
        exit()
        
                
    else:
        print("Nao conectou")




print(import_file())

exit()


