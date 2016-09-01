#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3


def connect():
    con = sqlite3.connect('automotora.db')
    con.row_factory = sqlite3.Row
    return con


def get_all_modelos():
    con = connect()
    c = con.cursor()
    query = (
        "SELECT modelo.*, marca.nombre FROM modelo LEFT OUTER JOIN marca ON modelo.marca_id = marca.id;")
    result = c.execute(query)
    modelos = result.fetchall()
    con.close()
    
    return modelos

def get_marcas():
    con = connect()
    c = con.cursor()
    query =("SELECT nombre FROM marca ORDER BY nombre")
    result = c.execute(query)
    marcas = result.fetchall()
    con.close()
    return marcas

def filter_by_busca(cadena):
    cadena = "%"+cadena+"%"
    con = connect()
    c = con.cursor()
    query = (
        "SELECT modelo.*, marca.nombre FROM modelo LEFT OUTER JOIN marca ON modelo.marca_id = marca.id WHERE modelo.modelo LIKE ?;")
    result = c.execute(query,[cadena])
    modelos = result.fetchall()
    con.close()
    return modelos

def filter_by_marca(marca):
    con = connect()
    c = con.cursor()
    query = (
        "SELECT modelo.*, marca.nombre FROM modelo LEFT OUTER JOIN marca ON modelo.marca_id = marca.id WHERE marca.nombre = ?;")
    result = c.execute(query,[marca])
    modelos = result.fetchall()
    con.close()
    return modelos

def get_img(id_modelo, id_marca):
    con = connect()
    c = con.cursor()
    query = ("SELECT archivo FROM imagen WHERE modelo_id = ? AND modelo_marca_id = ?;")
    result = c.execute(query,[id_modelo, id_marca])
    imagen = result.fetchone()[0]
    con.close()
    return imagen


"""
def crear_alumno(rut, nombres, apellidos, correo=None):
    con = conectar()
    c = con.cursor()
    sql = (
        "INSERT INTO alumnos (rut, nombres, apellidos, correo)"
        "VALUES (?, ?, ?, ?)")
    c.execute(sql, (rut, nombres, apellidos, correo))
    con.commit()


def borrar(rut):
    exito = False
    con = conectar()
    c = con.cursor()
    query = "DELETE FROM alumnos WHERE rut = ?"
    try:
        resultado = c.execute(query, [rut])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito
"""






