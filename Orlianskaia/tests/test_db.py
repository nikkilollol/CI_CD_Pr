#import functions from confest
from conftest import check_duplicates, check_max_salary, con, table_contain_nulls, count_func, check_avg, check_region_names

#Create test cases
class TestDB:

     def test_duplicates(self):
         sql_code = "SELECT job_id FROM TRN.hr.jobs GROUP BY job_id HAVING COUNT (*) > 1"
         result = check_duplicates(sql_code)
         assert len(result) == 0, f'Expected: "No duplicates";\n' \
                                  f'Actual:   {result}'


     def test_max_salary(self):
         cursor = con.cursor()
         cursor.execute("SELECT MAX(max_salary) FROM TRN.hr.jobs")
         result = cursor.fetchone()
         sql_code = "SELECT max_salary FROM TRN.hr.jobs"
         max_salary = check_max_salary(sql_code)
         assert max_salary == result[0], f'Expected:{max_salary}={result[0]};\n' \
                                         f'Actual:  {max_salary}!={result[0]}"'


     def test_table_contain_nulls(self):
         sql_code = "SELECT phone_number FROM TRN.hr.employees"
         nulls_value = table_contain_nulls(sql_code)
         assert nulls_value == False, f'Expected: "No nulls";\n' \
                                      f'Actual:   True != False'


     def test_count_func(self):
         sql_code = "SELECT Count(*) FROM TRN.hr.employees"
         count_of_rows = count_func(sql_code)
         assert count_of_rows[0] == 40, f'Expected: "40";\n' \
                                        f'Actual:   {count_of_rows}'


     def test_check_avg(self):
         cursor = con.cursor()
         cursor.execute("SELECT AVG(max_salary) FROM TRN.hr.jobs")
         result = cursor.fetchone()
         sql_code = "SELECT max_salary FROM TRN.hr.jobs"
         avg_salary = check_avg(sql_code)
         assert avg_salary == int(result[0]), f'Expected:{avg_salary}={result[0]};\n' \
                                              f'Actual:  {avg_salary}!={result[0]}"'

#function cheking that 'regions' contains only 'Europe', 'Americas', 'Asia', 'Middle East and Africa'.
     def test_check_region_names(self):
         cursor = con.cursor()
         cursor.execute("SELECT region_name FROM TRN.hr.regions WHERE region_name IN ('Europe', 'Americas', 'Asia', 'Middle East and Africa')")
         result = cursor.fetchall()
         result = [i[0] for i in result]
         sql_code = "SELECT region_name FROM TRN.hr.regions "
         regions = check_region_names(sql_code)
         assert regions == result, f'Expected:{regions}={result};\n' \
                                   f'Actual: {regions}!={result}"'



