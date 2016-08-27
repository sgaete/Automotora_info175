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
        "SELECT id, marca_id, modelo, motor,"
        " peso, descripcion, rendimiento, fecha_creacion,"
        " precio_lista FROM modelo ORDER BY fecha_creacion")
    result = c.execute(query)
    modelos = result.fetchall()
    return modelos
