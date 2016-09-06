#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def connect():
	"""conecta la base de datis"""
	con = sqlite3.connect('automotora.db')
	con.row_factory = sqlite3.Row
	return con

def obtener_datos():
	"""obtiene los datos de autos de la base de datos"""
	con =connect()
	c = con.cursor()
	query ="SELECT cliente.rut,cliente.nombres, cliente.apellidos, modelo.modelo, marca.nombre AS marca, auto.patente ,auto.color, auto.precio_venta FROM auto INNER JOIN modelo ON auto.modelo_id = modelo.id INNER JOIN marca ON auto.modelo_marca_id= marca.id INNER JOIN cliente ON auto.cliente_rut = cliente.rut;"
	resultado = c.execute(query)
	autos = resultado.fetchall()
	con.close()
	return autos

def crear_venta(rut, marca, modelo, patente, color, precio_venta):
	"""ingresa la venta a la base de dato"""
	con = connect()
	c = con.cursor()
	marca_id = obtener_id_marca(marca)
	modelo_id = obtener_id_modelo(modelo,marca_id)
	sql = ("INSERT INTO auto (cliente_rut, modelo_marca_id, modelo_id, patente, color, precio_venta) VALUES (?, ?, ?, ?, ?, ?)")
	c.execute(sql, (rut, marca_id, modelo_id, patente, color, precio_venta))
	con.commit()

def obtener_id_marca(marca):
	"""obtiene el id de marca"""
	con = connect()
	c = con.cursor()
	query = "select id from marca where  nombre = ?;"
	resultado = c.execute(query, [marca])
	tupla = resultado.fetchone()
	id_marca = max(tupla)
	con.close()
	return id_marca

def obtener_id_modelo(modelo,marca):
	"""obtiene el id del modelo y marca descrito"""
	con = connect()
	c = con.cursor()
	query = "select id from modelo where   modelo = ? AND marca_id = ?;"
	resultado = c.execute(query,( modelo, marca))
	tupla2 = resultado.fetchone()
	id_modelo = max(tupla2)
	con.close()
	return id_modelo

def borrar(patente):
	"""elimia de la base de datos ena venta segun la patente descrita"""
	exito = False
	con = connect()
	c = con.cursor()
	query = "DELETE FROM auto WHERE patente = ?"
	try:
		resultado = c.execute(query, [patente])
		con.commit()
		exito = True
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	con.close()
	return exito


def obtenermarcas():
	"""obtiene el nombre de todas las marcas desde la base de datos"""
	con =connect()
	c = con.cursor()
	query ="SELECT nombre FROM marca;"
	resultado = c.execute(query)
	s = resultado.fetchall()
	con.close()
	return s

def obtenermodelos(marca):
	"""obtiene el nombre de todos los modelos desde la base de datos"""
	con =connect()
	c = con.cursor()
	query ="select modelo from modelo where marca_id = ?;"
	id_marca =obtener_id_marca(marca)
	resultado = c.execute(query, [id_marca])
	s = resultado.fetchall()
	con.close()
	return s

def obtenercliente():
	"""obtiene el rut de todos los clientes desde la base de datos"""
	con =connect()
	c = con.cursor()
	query ="select rut from cliente;"
	resultado = c.execute(query)
	s = resultado.fetchall()
	con.close()
	return s

def obtener_precio(modelo):
	"""obtiene el precio de un modelo desde la base de datos"""
	con =connect()
	c = con.cursor()
	query ="select precio_lista from modelo where modelo = ?;"
	resultado = c.execute(query, [modelo])
	s = resultado.fetchone()
	con.close()
	return s