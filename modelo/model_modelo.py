#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

#crea punto de conexion
def connect():
	con = sqlite3.connect('automotora.db')
	con.row_factory = sqlite3.Row

	return con
def inserta_imagen(id_marca, id_modelo, ruta_img):
	con = connect()
	c = con.cursor()
	query = (
		"INSERT INTO imagen ("
		"modelo_marca_id, modelo_id, archivo)"
		"VALUES (?,?,?);")	
	c.execute(query, [id_marca, id_modelo, ruta_img])
	con.commit()


def insert_modelo(modelo):
	con = connect()
	c = con.cursor()
	query = (
		"INSERT INTO modelo ("
		"marca_id, modelo, motor, peso, descripcion, rendimiento, fecha_creacion, precio_lista)"
		"VALUES (?,?,?,?,?,?,?,?);")	
	c.execute(query, [modelo[0],modelo[1],modelo[2],modelo[3],modelo[4],modelo[5],modelo[6].toPython(),modelo[7]])
	con.commit()

def borra_modelo(id_modelo, id_marca):
	exito = False
	con = connect()
	c = con.cursor()
	query = (
		"DELETE FROM modelo WHERE id = ?;")
	try:
		resultado = c.execute(query, [id_modelo])
		con.commit()
		exito = True
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	query = ("DELETE FROM imagen WHERE modelo_id = ? AND modelo_marca_id = ?;")
	try:
		resultado = c.execute(query, [id_modelo, id_marca])
		con.commit()
		exito = True
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	con.close()
	return exito

def get_idmarca(id_modelo):
	con = connect()
	c = con.cursor()
	query = (
		"SELECT marca_id FROM modelo WHERE id = ?;")
	result = c.execute(query,[id_modelo])
	result = result.fetchone()[0]
	con.close()

	return result
	
def get_id_marca(nombre):
	con = connect()
	c = con.cursor()
	query = (
		"SELECT id FROM marca WHERE nombre = ?;")
	result = c.execute(query,[nombre])
	result = result.fetchone()[0]
	con.close()

	return result

def id_modelo(nombre):
	con = connect()
	c = con.cursor()
	query = (
		"SELECT id FROM modelo WHERE modelo = ?;")
	result = c.execute(query,[nombre])
	result = result.fetchone()[0]
	con.close()

	return result

#retorna solo un modelo segun id
def get_modelo(id_modelo):
	con = connect()
	c = con.cursor()
	query = "SELECT modelo.*, marca.nombre, imagen.archivo "
	query += "FROM modelo "
	query += "LEFT JOIN marca ON (modelo.marca_id = marca.id) "
	query += "LEFT JOIN imagen ON (modelo.marca_id = imagen.modelo_marca_id AND modelo.id = imagen.modelo_id) "
	query += "WHERE modelo.id = (%s);" % id_modelo
	result = c.execute(query)
	modelo = result.fetchone()
	con.close()

	return modelo

#envia todos los modelos con todos los datos y el nombre de la marca
def get_all_modelos():
	con = connect()
	c = con.cursor()
	query = (
		"SELECT modelo.*, marca.nombre FROM modelo LEFT OUTER JOIN marca ON modelo.marca_id = marca.id;")
	result = c.execute(query)
	modelos = result.fetchall()
	con.close()

	return modelos

#envia todas las marcas
def get_marcas():
	con = connect()
	c = con.cursor()
	query = ("SELECT nombre FROM marca ORDER BY nombre")
	result = c.execute(query)
	marcas = result.fetchall()
	con.close()

	return marcas

#filtro segun linea de texto
def filter_by_busca(cadena):
	cadena = "%" + cadena + "%"
	con = connect()
	c = con.cursor()
	query = (
		"SELECT modelo.*, marca.nombre FROM modelo LEFT OUTER JOIN marca ON modelo.marca_id = marca.id WHERE modelo.modelo LIKE ?;")
	result = c.execute(query, [cadena])
	modelos = result.fetchall()
	con.close()

	return modelos

#filtro segun marca
def filter_by_marca(marca):
	con = connect()
	c = con.cursor()
	query = (
		"SELECT modelo.*, marca.nombre FROM modelo LEFT OUTER JOIN marca ON modelo.marca_id = marca.id WHERE marca.nombre = ?;")
	result = c.execute(query, [marca])
	modelos = result.fetchall()
	con.close()

	return modelos

#retorna la imagen
def get_img(id_modelo, id_marca):
	con = connect()
	c = con.cursor()
	query = ("SELECT archivo FROM imagen WHERE modelo_id = ? AND modelo_marca_id = ?;")
	result = c.execute(query, [id_modelo, id_marca])
	imagen = result.fetchone()[0]
	
	con.close()

	return imagen

#valida si el modelo(segun id y marca) ya existe
def valida(modelo, nombre_marca, id_modelo=None):
	con = connect()
	c = con.cursor()
	#obtener el id de la marca que selecciono antes
	query = ("SELECT id FROM marca WHERE nombre = ?")
	result = c.execute(query, [nombre_marca])
	id_marca = result.fetchone()['id']
	#diferenciacion si es creacion o edicion
	if (id_modelo == None):
		#agregar: si coinciden modelo y marca es porque ya existe
		query = ("SELECT id FROM modelo WHERE modelo = ? AND marca_id = ? LIMIT 1")
		result = c.execute(query, [modelo, id_marca])
	else:
		#ediar: si coincide con modelo y marca excluyendo 
		#la id del que estamos editando es porque ya existe
		query = ("SELECT id FROM modelo WHERE modelo = ? AND marca_id = ? AND id <> ? LIMIT 1")
		result = c.execute(query, [modelo, id_marca, id_modelo])

	count = result.fetchone()
	con.close()
	
	return count

#retorna cantidad de ventas de este modelo
def vendidos(id_modelo, id_marca):
	con = connect()
	c = con.cursor()
	query = (
		"SELECT COUNT(*) AS cantidad FROM auto WHERE modelo_id = ? AND modelo_marca_id = ?;")
	result = c.execute(query, [id_modelo, id_marca])
	ventas = result.fetchall()[0]['cantidad']
	con.close()
	
	return ventas
