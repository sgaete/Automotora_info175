#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def connect():
	con = sqlite3.connect('automotora.db')
	con.row_factory = sqlite3.Row
	return con

def obtener_clientes():
	con = connect()
	c = con.cursor()
	query = (
		"SELECT cliente.*, COUNT(auto.cliente_rut) AS cantidad "
		"FROM cliente LEFT OUTER JOIN auto ON cliente.rut = auto.cliente_rut "
		"WHERE cliente.eliminado = ? GROUP BY cliente.rut;")
	result = c.execute(query,["N"])
	clientes = result.fetchall()
	con.close()
	return clientes

def cliente(rut):
	con = connect()
	c = con.cursor()
	query = "SELECT * FROM cliente WHERE rut = ?"
	result = c.execute(query, [rut])
	cliente = result.fetchone()
	con.close()
	return cliente

def crear_cliente(rut, nombres, apellidos, telefono, correo=None):
	con = connect()
	c = con.cursor()
	sql = (
		"INSERT INTO cliente (rut, nombres, apellidos, telefono, correo)"
		"VALUES (?, ?, ?, ?, ?)")
	c.execute(sql, (rut, nombres, apellidos, telefono, correo))
	con.commit()

def borrar(rut):
	exito = False
	con = connect()
	c = con.cursor()
	query = "DELETE FROM cliente WHERE rut = ?"
	try:
		result = c.execute(query, [rut])
		con.commit()
		exito = True
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	con.close()
	return exito

def valida(rut, old_rut=None):
	con = connect()
	c = con.cursor()
	if (old_rut == None):
		query = "SELECT rut FROM cliente WHERE rut = ? LIMIT 1"
		result = c.execute(query, [rut])
	else:
		query = "SELECT rut FROM cliente WHERE rut = ? AND rut <> ? LIMIT 1"
		result = c.execute(query, [rut, old_rut])
	dato = result.fetchone()
	con.close()
	return dato

def editar(old_rut, rut, nombres, apellidos, telefono, correo=None):
	con = connect()
	c = con.cursor()
	query = "UPDATE cliente SET rut=?, nombres=?, apellidos=?, telefono=?, correo=? WHERE rut=?"
	result = c.execute(query, (rut, nombres, apellidos, telefono, correo, old_rut))
	con.commit()
	con.close()

def consul_compra(rut):
	con = connect()
	c = con.cursor()
	query = "SELECT patente FROM auto WHERE cliente_rut=? LIMIT 1"
	result = c.execute(query, [rut])
	dato = result.fetchone()
	con.close()
	return dato

def cambia_estado(rut):
	con = connect()
	c = con.cursor()
	query = "UPDATE cliente SET eliminado=? WHERE rut=?"
	result = c.execute(query, ["S", rut])
	con.commit()
	con.close()