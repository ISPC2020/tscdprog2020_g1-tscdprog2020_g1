import pymysql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#88958
#113229


class DataBase:
    def __init__(self):
        try:
            self.connection = pymysql.connect(
                host='localhost',
                port=3307,
                user='root',
                password='',
                db='employees')
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error al conectar: ", e)
    
    def Consulta(self):
        try:
            with self.connection.cursor() as cursor:
                consulta = "SELECT * FROM employees HAVING COUNT(*) > 10;"
                cursor.execute(consulta)
 
            # Con fetchall traemos todas las filas
            employees = cursor.fetchall()
 
            # Recorrer e imprimir
            for emp in employees:
                print(emp)
        finally:
            self.connection.close()
    #Cargamos Datos en un Data Frame
    def PdConsulta(self):
        self.employees_table = pd.read_sql_query("SELECT DISTINCT  e.emp_no, e.last_name, max(s.salary), s.from_date, s.to_date FROM salaries s INNER JOIN employees e ON s.emp_no=e.emp_no  group by e.emp_no having max(s.salary) LIMIT 10" ,self.connection)
        return self.employees_table



database= DataBase()
database.Consulta
pdquery = database.PdConsulta()
print(pdquery)
pdquery.plot(kind="scatter", x="last_name", y="max(s.salary)")
plt.show()


'''
try:
	conexion = pymysql.connect(host='localhost',
                             port=3307
                             user='root',
                             password='',
                             db='employees')
	print("Conexión correcta")
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)
 
 class MyLinearRegression:
        
    def __init__(self, fit_intercept=True):
        self.coef_ = None
        self.intercept_ = None
        self._fit_intercept = fit_intercept
    
    def __repr__(self):
        return "I am a Linear Regression model!"
        
        

mlr = MyLinearRegression()
mlr.coef_==None
mlr.intercept_ == None
print(mlr)
 
 '''
 
