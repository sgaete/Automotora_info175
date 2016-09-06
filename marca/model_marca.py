#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: 850 -*-

import sqlite3


def connect():
	con = sqlite3.connect('automotora.db')
	con.row_factory = sqlite3.Row
	return con

def get_marcas():
	con = connect()
	c = con.cursor()
	query =("SELECT imagen, nombre, pais, modelo as model, count(marca_id) as cantidad from marca left outer join modelo on marca.id = marca_id group by nombre order by nombre")
	#query =("select marca.imagen as imagen, marca.nombre as nombre, marca.pais as pais, count(marca.nombre) as cantidad from marca left join modelo on marca.id=modelo.marca_id group by marca.id")
		#"select marca.imagen as imagen, marca.nombre as nombre, marca.pais as pais, count(marca.nombre) as cantidad from modelo join marca on modelo.marca_id=marca.id group by marca.id")
		#"SELECT imagen ,nombre, pais FROM marca ORDER BY id")
	result = c.execute(query)
	marcas = result.fetchall()
	con.close()
	return marcas
	
def crear_marca(imagen, nombre, pais):
	con = connect()
	c = con.cursor()
	sql = ("INSERT INTO marca (imagen, nombre, pais)"
		"VALUES (?, ?, ?)")
	c.execute(sql, (imagen, nombre, pais))
	con.commit()

def edit_marca(imag,nom,pai,marc_id):
	print "en model de marca"
	con = connect()
	c = con.cursor()
	#query = "SELECT * FROM marca WHERE id = ?"
	sql=('UPDATE marca set imagen = ?, nombre = ?, pais = ? where nombre = ?')
	c.execute(sql, (imag, nom, pai, marc_id))
	con.commit()
	con.close()
	#resultado = c.execute(query,[marc_id])

def cantModelMarca(marc_id):
	con = connect()
	c = con.cursor()
	sql=("SELECT count(marca_id) as cantidad from marca left outer join modelo on marca.id = ? group by nombre")
	result = c.execute(sql, [marc_id])
	#print "	 :	"+marc_id[0]
	cantidad = result.fetchall()
	con.close()
	#return cantidad
	return cantidad

def delete(marca):
	exito = False
	con = connect()
	c = con.cursor()
	query = ("DELETE FROM marca WHERE nombre = ?")
	try:
		resultado = c.execute(query, [marca])
		con.commit()
		exito = True
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	con.close()
	return exito


def buscarI(marca):
	con = connect()
	c = con.cursor()
	query = ("SELECT imagen FROM marca WHERE nombre = ?")
	resultado = c.execute(query, [marca])
	img = resultado.fetchone()
	con.close()
	return img


def buscar_datos(marc_id):
	con = connect()
	c = con.cursor()
	query =("SELECT nombre,imagen,pais from marca where nombre = ?")
	result = c.execute(query,[marc_id])
	cantidad = result.fetchall()
	con.close()
	print cantidad
	return cantidad

def marca(marc_id):
	con = connect()
	c = con.cursor()
	query = ("SELECT nombre, pais, imagen FROM marca, modelo WHERE nombre = ?")
	resultado = c.execute(query,[marc_id])
	marca = resultado.fetchone()
	con.close()
	return marca

