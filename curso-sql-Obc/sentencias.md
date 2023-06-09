
                              ## Sentencias DML
                         Data Manipulation Language

Operaciones **CRUD**:

* ==C==: Create --> ``INSERT INTO``
* ==R==: Retrieve o Read --> ``SELECT FROM`` 
* ==U==: Update -->  ``UPDATE``
* ==D==: Delete -->  ``DELETE FROM``


### 1. Recuperar datos (SELECT)

Recuperar todos los empleados:

```sql
SELECT * FROM employees;
```


### 2. Insertar nuevos datos (INSERT)

Insertar un nuevo empleado:

```sql
INSERT INTO employees (married, name, email, genre, salary, birth_date, start_at) VALUES (TRUE, 'Employee2', 'employee1@company.com', 'M', 29567.23, '1990-12-25', '08:30:00');
```

### 3. Actualizar datos (UPDATE)


### 4. Borrar datos (DELETE)






///////////////////////////////////////////////////////////////////////////

                                    ## Sentencias DDL
                                Data Definition Language


Operaciones con **Bases de datos**:

* Crear base de datos: ``CREATE DATABASE employees2;``
* Borrar una base de datos: ``DROP DATABASE employees2;``


Operaciones con **Tablas**:

* Crear tablas: ``CREATE TABLE IF NOT EXISTS employees (...);``
* Borrar tablas: ``DROP TABLE IF EXISTS employees;``
* Cambiar el nombre de una tabla:
	*  ``ALTER TABLE IF EXISTS employees RENAME TO employees_2021;``
* Agregar columnas a una tabla:
	* ``ALTER TABLE employees ADD COLUMN email VARCHAR(100);``
* Borrar columnas de una tabla:
	* ``ALTER TABLE employees DROP COLUMN IF EXISTS salary;``


**Tipos de datos** en tablas:

* ``INT``
* ``BOOLEAN``
* ``CHAR``, ``VARCHAR``, ``TEXT``
* ``NUMERIC``
* ``DATE``
* ``TIME``
* ``SERIAL``

**Restricciones** en las columnas de las tablas:

* ``PRIMARY KEY``
* ``NOT NULL``
* ``UNIQUE``
* ``CHECK``