import pyodbc

con = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=EPRUPETW054C\SQLEXPRESS01;"
    "Database=TRN;"
    "Trusted_Connection=yes;"
)

def check_duplicates(sql):
    cursor = con.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if result == None:
        return []
    else:
        return result


def check_max_salary(sql):
    cursor = con.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    max_salary = 0
    for i in result:
        if i[0] > max_salary:
            max_salary = i[0]
        else:
            pass
    return max_salary

def table_contain_nulls(sql):
    cursor = con.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        if i[0] == None:
            return True
        else:
            pass
    return False

def count_func(sql):
    cursor = con.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

def check_avg(sql):
    cursor = con.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    avg = 0
    for i in result:
       avg = avg + i[0]
    return int(avg/len(result))

def check_region_names(sql):
    cursor = con.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    regions = []
    for i in result:
        regions.append(i[0])
    return regions


check_region_names("SELECT region_name FROM TRN.hr.regions WHERE region_name NOT IN ('Europe', 'Americas', 'Asia', 'Middle East and Africa')")








