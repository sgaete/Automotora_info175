#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3


def connect():
    con = sqlite3.connect('automotora.db')
    con.row_factory = sqlite3.Row
    return con

def get_marcas():
    con = connect()
    c = con.cursor()
    query =(
        "SELECT id, imagen ,nombre, pais FROM marca ORDER BY id")
    result = c.execute(query)
    marcas = result.fetchall()
    con.close()
    return marcas
    
def crear_marca(imagen, nombre, pais):
    con = conectar()
    c = con.cursor()
    sql = (
        "INSERT INTO marca (imagen, nombre, pais)"
        "VALUES (?, ?, ?)")
    c.execute(sql, (imagen, nombre, pais))
    con.commit()

def editar_marca(imagen,nombre,pais):
	con = conectar()
	c = con.cursor()
	query = "SELECT * FROM marcas WHERE id = ?"
	sql=("INSERT INTO marca (imagen, nombre, pais)"
		 "VALUES(?,?,?)")
	resultado = c.execute(query,[id])
	marca = resultado.fetchone()
	con.close()
	return marca

def borrar(id):
    exito = False
    con = conectar()
    c = con.cursor()
    query = "DELETE FROM marca WHERE id = ?"
    try:
        resultado = c.execute(query, [id])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito
    
"""def filter_by_busca(cadena):
    con = connect()
    c = con.cursor()
    query = (
        "SELECT * FROM modelo WHERE ")"""
