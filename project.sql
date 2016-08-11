CREATE TABLE IF NOT EXISTS 'cliente'(
	'rut' 		INTEGER(8)	PRIMARY KEY	UNIQUE	NOT NULL,
  	'nombres' 	TEXT NOT NULL,
  	'apellidos' TEXT NOT NULL,
  	'telefono' 	TEXT NOT NULL,
  	'correo' 	TEXT
);
CREATE TABLE IF NOT EXISTS 'marca'(
	'id' 		INTEGER PRIMARY KEY	UNIQUE	NOT NULL,
	'imagen'	TEXT,
	'nombre'	TEXT	NOT NULL	UNIQUE,
	'pais'		TEXT	NOT NULL
);
CREATE TABLE IF NOT EXISTS 'modelo'(
	'id' 		INTEGER PRIMARY KEY	UNIQUE	NOT NULL,
	'marca_id' 	INTEGER	NOT NULL,
	'modelo' 	TEXT NOT NULL UNIQUE,
	'motor' 	TEXT NOT NULL,
	'peso' 		FLOAT NOT NULL,
	'descripcion' 		TEXT,
	'rendimiento' 		INTEGER NOT NULL,
	'fecha_creacion' 	DATE NOT NULL,
	'precio_lista' 		INTEGER NOT NULL,
	FOREIGN KEY(marca_id) REFERENCES marca(id)
);
CREATE TABLE IF NOT EXISTS 'auto'(
	'patente' 		VARCHAR(6) PRIMARY KEY	NOT NULL	UNIQUE,
	'cliente_rut' 	INTEGER(8) NOT NULL,
	'modelo_id' 		INTEGER NOT NULL,
	'modelo_marca_id' 	INTEGER NOT NULL,
	'color' 			TEXT NOT NULL,
	'precio_venta' 		INTEGER NOT NULL,
	FOREIGN KEY(cliente_rut) REFERENCES cliente(rut),
	FOREIGN KEY(modelo_id) REFERENCES modelo(id),
	FOREIGN KEY(modelo_marca_id) REFERENCES modelo(marca_id)
);
CREATE TABLE IF NOT EXISTS 'imagen'(
	'id'		INTEGER PRIMARY KEY	UNIQUE	NOT NULL,
	'archivo'	TEXT NOT NULL	UNIQUE,
	'modelo_id' 		INTEGER NOT NULL,
	'modelo_marca_id' 	INTEGER NOT NULL,
	FOREIGN KEY(modelo_id) REFERENCES modelo(id),
	FOREIGN KEY(modelo_marca_id) REFERENCES modelo(marca_id)
);