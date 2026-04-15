-- ============================================================
--  SISTEMA HOTELERO - Script DDL para SQL Server
--  Version 3.0
--  Cambios respecto v2:
--    - Nueva tabla TIPO_DOCUMENTO (DNI/Pasaporte/Carnet Extranjeria)
--    - HUESPEDES: id_tipo_documento, nro_documento, fecha_nacimiento
--      columna dni eliminada (reemplazada por nro_documento)
--    - RESERVAS: fechas cambiadas a DATETIME2, sin notas,
--      + nro_huespedes, + monto_adelantado
--    - CONSUMOS eliminada
--    - ESTANCIAS eliminada
--    - CAT_ESTADO_ESTANCIA eliminada
--    - Nueva tabla CATEGORIA
--    - Nueva tabla PRODUCTO
--    - Nueva tabla MOVIMIENTO_INVENTARIO
--    - FACTURACION renombrada a COMPROBANTE:
--        id_estancia eliminado
--        total_habitacion -> id_habitacion
--        total_consumos   -> subtotal
--        numero_comprobante -> generado automaticamente "FACT-XXXXXX"
--        + dias_estancia INT
--    - NOTIFICACIONES: eliminadas columnas id_referencia y leida
--    - Vistas actualizadas para reflejar nueva estructura
-- ============================================================

USE master;
GO

IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'HotelDB')
BEGIN
    CREATE DATABASE HotelDB;
END
GO

USE HotelDB;
GO

-- ============================================================
--  PASO 1: ELIMINAR OBJETOS EXISTENTES (orden inverso a FK)
-- ============================================================

-- Vistas y funciones primero
IF OBJECT_ID('dbo.VW_CIERRE_CAJA',              'V')  IS NOT NULL DROP VIEW     dbo.VW_CIERRE_CAJA;
IF OBJECT_ID('dbo.VW_REPORTE_VENTAS',           'V')  IS NOT NULL DROP VIEW     dbo.VW_REPORTE_VENTAS;
IF OBJECT_ID('dbo.VW_REPORTE_BASE',             'V')  IS NOT NULL DROP VIEW     dbo.VW_REPORTE_BASE;
IF OBJECT_ID('dbo.VW_DISPONIBILIDAD',           'V')  IS NOT NULL DROP VIEW     dbo.VW_DISPONIBILIDAD;
IF OBJECT_ID('dbo.FN_HabitacionesDisponibles',  'IF') IS NOT NULL DROP FUNCTION dbo.FN_HabitacionesDisponibles;
GO

-- Tablas en orden inverso a dependencias FK
IF OBJECT_ID('dbo.REPORTES_VENTAS',        'U') IS NOT NULL DROP TABLE dbo.REPORTES_VENTAS;
IF OBJECT_ID('dbo.CAJA_SESIONES',          'U') IS NOT NULL DROP TABLE dbo.CAJA_SESIONES;
IF OBJECT_ID('dbo.MOVIMIENTO_INVENTARIO',  'U') IS NOT NULL DROP TABLE dbo.MOVIMIENTO_INVENTARIO;
IF OBJECT_ID('dbo.PRODUCTO',               'U') IS NOT NULL DROP TABLE dbo.PRODUCTO;
IF OBJECT_ID('dbo.CATEGORIA',              'U') IS NOT NULL DROP TABLE dbo.CATEGORIA;
IF OBJECT_ID('dbo.BACKUPS',                'U') IS NOT NULL DROP TABLE dbo.BACKUPS;
IF OBJECT_ID('dbo.NOTIFICACIONES',         'U') IS NOT NULL DROP TABLE dbo.NOTIFICACIONES;
IF OBJECT_ID('dbo.COMPROBANTE',            'U') IS NOT NULL DROP TABLE dbo.COMPROBANTE;
IF OBJECT_ID('dbo.FACTURACION',            'U') IS NOT NULL DROP TABLE dbo.FACTURACION;
IF OBJECT_ID('dbo.CONSUMOS',               'U') IS NOT NULL DROP TABLE dbo.CONSUMOS;
IF OBJECT_ID('dbo.ESTANCIAS',              'U') IS NOT NULL DROP TABLE dbo.ESTANCIAS;
IF OBJECT_ID('dbo.RESERVAS',               'U') IS NOT NULL DROP TABLE dbo.RESERVAS;
IF OBJECT_ID('dbo.HUESPEDES',              'U') IS NOT NULL DROP TABLE dbo.HUESPEDES;
IF OBJECT_ID('dbo.USUARIOS',               'U') IS NOT NULL DROP TABLE dbo.USUARIOS;
IF OBJECT_ID('dbo.SEGURIDAD_PREGUNTAS',    'U') IS NOT NULL DROP TABLE dbo.SEGURIDAD_PREGUNTAS;
IF OBJECT_ID('dbo.HABITACIONES',           'U') IS NOT NULL DROP TABLE dbo.HABITACIONES;
IF OBJECT_ID('dbo.TIPO_HABITACION',        'U') IS NOT NULL DROP TABLE dbo.TIPO_HABITACION;
IF OBJECT_ID('dbo.TIPO_DOCUMENTO',         'U') IS NOT NULL DROP TABLE dbo.TIPO_DOCUMENTO;

-- Catalogos
IF OBJECT_ID('dbo.CAT_TURNO',              'U') IS NOT NULL DROP TABLE dbo.CAT_TURNO;
IF OBJECT_ID('dbo.CAT_ROL',                'U') IS NOT NULL DROP TABLE dbo.CAT_ROL;
IF OBJECT_ID('dbo.CAT_ESTADO_HABITACION',  'U') IS NOT NULL DROP TABLE dbo.CAT_ESTADO_HABITACION;
IF OBJECT_ID('dbo.CAT_ESTADO_RESERVA',     'U') IS NOT NULL DROP TABLE dbo.CAT_ESTADO_RESERVA;
IF OBJECT_ID('dbo.CAT_ESTADO_ESTANCIA',    'U') IS NOT NULL DROP TABLE dbo.CAT_ESTADO_ESTANCIA;
IF OBJECT_ID('dbo.CAT_METODO_PAGO',        'U') IS NOT NULL DROP TABLE dbo.CAT_METODO_PAGO;
IF OBJECT_ID('dbo.CAT_TIPO_NOTIFICACION',  'U') IS NOT NULL DROP TABLE dbo.CAT_TIPO_NOTIFICACION;
IF OBJECT_ID('dbo.CAT_ESTADO_BACKUP',      'U') IS NOT NULL DROP TABLE dbo.CAT_ESTADO_BACKUP;
GO

-- ============================================================
--  PASO 2: CATALOGOS
-- ============================================================

CREATE TABLE dbo.CAT_ROL (
    id_rol  TINYINT      IDENTITY(1,1) PRIMARY KEY,
    nombre  NVARCHAR(50) NOT NULL UNIQUE
);
INSERT INTO dbo.CAT_ROL (nombre) VALUES
    ('Administracion'), ('Recepcion'), ('Contabilidad');
GO

CREATE TABLE dbo.CAT_ESTADO_HABITACION (
    id_estado TINYINT      IDENTITY(1,1) PRIMARY KEY,
    nombre    NVARCHAR(30) NOT NULL UNIQUE
);
INSERT INTO dbo.CAT_ESTADO_HABITACION (nombre) VALUES
    ('Disponible'), ('Ocupada'), ('En Limpieza'), ('Mantenimiento');
GO

CREATE TABLE dbo.CAT_ESTADO_RESERVA (
    id_estado TINYINT      IDENTITY(1,1) PRIMARY KEY,
    nombre    NVARCHAR(30) NOT NULL UNIQUE
);
INSERT INTO dbo.CAT_ESTADO_RESERVA (nombre) VALUES
    ('Pendiente'), ('Confirmada'), ('Cancelada'), ('Completada');
GO

CREATE TABLE dbo.CAT_METODO_PAGO (
    id_metodo TINYINT      IDENTITY(1,1) PRIMARY KEY,
    nombre    NVARCHAR(30) NOT NULL UNIQUE
);
INSERT INTO dbo.CAT_METODO_PAGO (nombre) VALUES
    ('Efectivo'), ('Tarjeta'), ('Transferencia'), ('Otro');
GO

CREATE TABLE dbo.CAT_TIPO_NOTIFICACION (
    id_tipo TINYINT      IDENTITY(1,1) PRIMARY KEY,
    nombre  NVARCHAR(50) NOT NULL UNIQUE
);
INSERT INTO dbo.CAT_TIPO_NOTIFICACION (nombre) VALUES
    ('ReservaProxima'), ('HabitacionLimpia'), ('CheckoutPendiente'), ('Otro');
GO

CREATE TABLE dbo.CAT_ESTADO_BACKUP (
    id_estado TINYINT      IDENTITY(1,1) PRIMARY KEY,
    nombre    NVARCHAR(30) NOT NULL UNIQUE
);
INSERT INTO dbo.CAT_ESTADO_BACKUP (nombre) VALUES
    ('Exitoso'), ('Fallido'), ('En Proceso');
GO

CREATE TABLE dbo.CAT_TURNO (
    id_turno TINYINT      IDENTITY(1,1) PRIMARY KEY,
    nombre   NVARCHAR(20) NOT NULL UNIQUE
);
INSERT INTO dbo.CAT_TURNO (nombre) VALUES
    ('Manana'), ('Tarde'), ('Noche');
GO

-- ============================================================
--  PASO 3: TABLAS PRINCIPALES
-- ============================================================

-- ------------------------------------------------------------
--  TIPO_DOCUMENTO
--  Catalogo de documentos de identidad aceptados.
-- ------------------------------------------------------------
CREATE TABLE dbo.TIPO_DOCUMENTO (
    id_tipo_documento TINYINT      IDENTITY(1,1) PRIMARY KEY,
    nombre            NVARCHAR(50) NOT NULL UNIQUE
);
INSERT INTO dbo.TIPO_DOCUMENTO (nombre) VALUES
    ('DNI'), ('Pasaporte'), ('Carnet Extranjeria');
GO

-- ------------------------------------------------------------
--  TIPO_HABITACION  (REQ-02)
-- ------------------------------------------------------------
CREATE TABLE dbo.TIPO_HABITACION (
    id_tipo      INT            IDENTITY(1,1) PRIMARY KEY,
    nombre       NVARCHAR(80)   NOT NULL UNIQUE,
    descripcion  NVARCHAR(255)  NULL,
    tarifa_base  DECIMAL(10,2)  NOT NULL CHECK (tarifa_base > 0),
    activo       BIT            NOT NULL DEFAULT 1,
    created_at   DATETIME2      NOT NULL DEFAULT GETDATE()
);
GO

-- ------------------------------------------------------------
--  HABITACIONES  (REQ-02)
-- ------------------------------------------------------------
CREATE TABLE dbo.HABITACIONES (
    id_habitacion INT           IDENTITY(1,1) PRIMARY KEY,
    numero        NVARCHAR(10)  NOT NULL UNIQUE,
    id_tipo       INT           NOT NULL,
    id_estado     TINYINT       NOT NULL DEFAULT 1,  -- 1 = Disponible
    observaciones NVARCHAR(500) NULL,
    created_at    DATETIME2     NOT NULL DEFAULT GETDATE(),

    CONSTRAINT FK_HAB_TIPO   FOREIGN KEY (id_tipo)   REFERENCES dbo.TIPO_HABITACION(id_tipo),
    CONSTRAINT FK_HAB_ESTADO FOREIGN KEY (id_estado) REFERENCES dbo.CAT_ESTADO_HABITACION(id_estado)
);
GO

-- ------------------------------------------------------------
--  SEGURIDAD_PREGUNTAS  (REQ-13)
-- ------------------------------------------------------------
CREATE TABLE dbo.SEGURIDAD_PREGUNTAS (
    id_pregunta INT            IDENTITY(1,1) PRIMARY KEY,
    pregunta    NVARCHAR(255)  NOT NULL UNIQUE
);
INSERT INTO dbo.SEGURIDAD_PREGUNTAS (pregunta) VALUES
    ('Nombre de tu primera mascota'),
    ('Ciudad donde naciste'),
    ('Nombre de tu madre'),
    ('Nombre de tu colegio primario'),
    ('Apodo de infancia');
GO

-- ------------------------------------------------------------
--  USUARIOS  (REQ-01, REQ-13)
-- ------------------------------------------------------------
CREATE TABLE dbo.USUARIOS (
    id_usuario          INT            IDENTITY(1,1) PRIMARY KEY,
    nombre              NVARCHAR(100)  NOT NULL,
    email               NVARCHAR(150)  NOT NULL UNIQUE,
    -- Hash generado en Python con bcrypt. NUNCA texto plano.
    password_hash       NVARCHAR(256)  NOT NULL,
    id_rol              TINYINT        NOT NULL,
    id_pregunta         INT            NOT NULL,
    -- Normalizar en Python con .strip().lower() antes de guardar
    respuesta_seguridad NVARCHAR(150)  NOT NULL,
    activo              BIT            NOT NULL DEFAULT 1,
    ultimo_acceso       DATETIME2      NULL,
    created_at          DATETIME2      NOT NULL DEFAULT GETDATE(),

    CONSTRAINT FK_USR_ROL      FOREIGN KEY (id_rol)      REFERENCES dbo.CAT_ROL(id_rol),
    CONSTRAINT FK_USR_PREGUNTA FOREIGN KEY (id_pregunta) REFERENCES dbo.SEGURIDAD_PREGUNTAS(id_pregunta)
);
GO

-- ------------------------------------------------------------
--  HUESPEDES  (REQ-03)
--  - id_tipo_documento FK a TIPO_DOCUMENTO
--  - nro_documento reemplaza a dni (mas generico)
--  - fecha_nacimiento agregada
-- ------------------------------------------------------------
CREATE TABLE dbo.HUESPEDES (
    id_huesped         INT            IDENTITY(1,1) PRIMARY KEY,
    id_tipo_documento  TINYINT        NOT NULL,
    nro_documento      NVARCHAR(20)   NOT NULL UNIQUE,
    nombre             NVARCHAR(100)  NOT NULL,
    apellido           NVARCHAR(100)  NOT NULL,
    fecha_nacimiento   DATE           NOT NULL,
    telefono           NVARCHAR(20)   NULL,
    email              NVARCHAR(150)  NULL,
    fecha_registro     DATE           NOT NULL DEFAULT CAST(GETDATE() AS DATE),
    created_at         DATETIME2      NOT NULL DEFAULT GETDATE(),

    CONSTRAINT FK_HUE_TIPO_DOC FOREIGN KEY (id_tipo_documento)
        REFERENCES dbo.TIPO_DOCUMENTO(id_tipo_documento)
);
GO

-- ------------------------------------------------------------
--  RESERVAS  (REQ-04, REQ-05)
--  - fechas DATETIME2 (antes DATE)
--  - columna notas eliminada
--  - nro_huespedes agregada
--  - monto_adelantado agregada
-- ------------------------------------------------------------
CREATE TABLE dbo.RESERVAS (
    id_reserva       INT            IDENTITY(1,1) PRIMARY KEY,
    id_huesped       INT            NOT NULL,
    id_habitacion    INT            NOT NULL,
    fecha_checkin    DATETIME2      NOT NULL,
    fecha_checkout   DATETIME2      NOT NULL,
    id_estado        TINYINT        NOT NULL DEFAULT 1,  -- 1 = Pendiente
    nro_huespedes    TINYINT        NOT NULL DEFAULT 1 CHECK (nro_huespedes > 0),
    monto_adelantado DECIMAL(10,2)  NOT NULL DEFAULT 0  CHECK (monto_adelantado >= 0),
    id_usuario_crea  INT            NOT NULL,
    created_at       DATETIME2      NOT NULL DEFAULT GETDATE(),

    CONSTRAINT CK_RESERVAS_fechas CHECK (fecha_checkout > fecha_checkin),
    CONSTRAINT FK_RES_HUESPED     FOREIGN KEY (id_huesped)      REFERENCES dbo.HUESPEDES(id_huesped),
    CONSTRAINT FK_RES_HABITACION  FOREIGN KEY (id_habitacion)   REFERENCES dbo.HABITACIONES(id_habitacion),
    CONSTRAINT FK_RES_USUARIO     FOREIGN KEY (id_usuario_crea) REFERENCES dbo.USUARIOS(id_usuario),
    CONSTRAINT FK_RES_ESTADO      FOREIGN KEY (id_estado)       REFERENCES dbo.CAT_ESTADO_RESERVA(id_estado)
);
GO

-- Indice filtrado para consultas de disponibilidad (REQ-04)
CREATE INDEX IX_RESERVAS_HAB_FECHAS
    ON dbo.RESERVAS (id_habitacion, fecha_checkin, fecha_checkout)
    WHERE id_estado IN (1, 2);
GO

-- ------------------------------------------------------------
--  COMPROBANTE  (antes FACTURACION - REQ-09)
--  - numero_comprobante generado automaticamente "FACT-XXXXXX"
--  - id_habitacion en lugar de id_estancia
--  - subtotal en lugar de total_consumos
--  - dias_estancia agregada
-- ------------------------------------------------------------
CREATE TABLE dbo.COMPROBANTE (
    id_comprobante     INT            IDENTITY(1,1) PRIMARY KEY,
    -- Numero legible generado automaticamente por computed column
    numero_comprobante AS             (N'FACT-' + RIGHT('000000' + CAST(id_comprobante AS NVARCHAR(6)), 6)) PERSISTED,
    id_reserva         INT            NOT NULL,
    id_habitacion      INT            NOT NULL,
    dias_estancia      INT            NOT NULL CHECK (dias_estancia > 0),
    subtotal           DECIMAL(10,2)  NOT NULL DEFAULT 0  CHECK (subtotal >= 0),
    total_general      DECIMAL(10,2)  NOT NULL CHECK (total_general >= 0),
    id_metodo_pago     TINYINT        NOT NULL,
    fecha_pago         DATETIME2      NOT NULL DEFAULT GETDATE(),
    id_usuario         INT            NOT NULL,

    CONSTRAINT FK_COMP_RESERVA     FOREIGN KEY (id_reserva)    REFERENCES dbo.RESERVAS(id_reserva),
    CONSTRAINT FK_COMP_HABITACION  FOREIGN KEY (id_habitacion) REFERENCES dbo.HABITACIONES(id_habitacion),
    CONSTRAINT FK_COMP_METODO_PAGO FOREIGN KEY (id_metodo_pago) REFERENCES dbo.CAT_METODO_PAGO(id_metodo),
    CONSTRAINT FK_COMP_USUARIO     FOREIGN KEY (id_usuario)    REFERENCES dbo.USUARIOS(id_usuario)
);
GO

-- ------------------------------------------------------------
--  NOTIFICACIONES  (REQ-07)
--  - id_referencia eliminada
--  - leida eliminada
-- ------------------------------------------------------------
CREATE TABLE dbo.NOTIFICACIONES (
    id_notificacion INT            IDENTITY(1,1) PRIMARY KEY,
    id_tipo         TINYINT        NOT NULL,
    mensaje         NVARCHAR(500)  NOT NULL,
    created_at      DATETIME2      NOT NULL DEFAULT GETDATE(),

    CONSTRAINT FK_NOT_TIPO FOREIGN KEY (id_tipo) REFERENCES dbo.CAT_TIPO_NOTIFICACION(id_tipo)
);
GO

-- ------------------------------------------------------------
--  BACKUPS  (REQ-14)
-- ------------------------------------------------------------
CREATE TABLE dbo.BACKUPS (
    id_backup     INT            IDENTITY(1,1) PRIMARY KEY,
    fecha_hora    DATETIME2      NOT NULL DEFAULT GETDATE(),
    ruta_archivo  NVARCHAR(500)  NOT NULL,
    id_estado     TINYINT        NOT NULL,
    observaciones NVARCHAR(300)  NULL,
    id_usuario    INT            NOT NULL,

    CONSTRAINT FK_BAK_ESTADO  FOREIGN KEY (id_estado)  REFERENCES dbo.CAT_ESTADO_BACKUP(id_estado),
    CONSTRAINT FK_BAK_USUARIO FOREIGN KEY (id_usuario) REFERENCES dbo.USUARIOS(id_usuario)
);
GO

-- ============================================================
--  PASO 4: INVENTARIO
-- ============================================================

CREATE TABLE dbo.CATEGORIA (
    id     INT           NOT NULL IDENTITY(1,1),
    nombre NVARCHAR(100) NOT NULL,

    CONSTRAINT PK_CATEGORIA        PRIMARY KEY (id),
    CONSTRAINT UQ_CATEGORIA_NOMBRE UNIQUE (nombre)
);
GO

CREATE TABLE dbo.PRODUCTO (
    id           INT           NOT NULL IDENTITY(1,1),
    categoria_id INT           NOT NULL,
    nombre       NVARCHAR(150) NOT NULL,

    CONSTRAINT PK_PRODUCTO           PRIMARY KEY (id),
    CONSTRAINT UQ_PRODUCTO_NOMBRE    UNIQUE (nombre),
    CONSTRAINT FK_PRODUCTO_CATEGORIA FOREIGN KEY (categoria_id)
        REFERENCES dbo.CATEGORIA (id)
        ON UPDATE CASCADE
        ON DELETE NO ACTION
);
GO

CREATE TABLE dbo.MOVIMIENTO_INVENTARIO (
    id              INT           NOT NULL IDENTITY(1,1),
    producto_id     INT           NOT NULL,
    cantidad        INT           NOT NULL,
    tipo            NVARCHAR(10)  NOT NULL,   -- 'entrada' | 'salida'
    -- NULL = movimiento de stock interno (compra, ajuste)
    -- NOT NULL = salida vinculada a un comprobante de venta
    id_comprobante  INT           NULL,
    id_usuario      INT           NOT NULL,
    fecha           DATETIME2     NOT NULL DEFAULT SYSDATETIME(),

    CONSTRAINT PK_MOVIMIENTO           PRIMARY KEY (id),
    CONSTRAINT FK_MOVIMIENTO_PRODUCTO  FOREIGN KEY (producto_id)
        REFERENCES dbo.PRODUCTO (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT FK_MOVIMIENTO_COMPROB   FOREIGN KEY (id_comprobante)
        REFERENCES dbo.COMPROBANTE (id_comprobante),
    CONSTRAINT FK_MOVIMIENTO_USUARIO   FOREIGN KEY (id_usuario)
        REFERENCES dbo.USUARIOS (id_usuario),
    CONSTRAINT CK_MOVIMIENTO_CANTIDAD  CHECK (cantidad > 0),
    CONSTRAINT CK_MOVIMIENTO_TIPO      CHECK (tipo IN ('entrada', 'salida'))
);
GO

-- ============================================================
--  PASO 5: CAJA Y REPORTES DE VENTAS
-- ============================================================

CREATE TABLE dbo.CAJA_SESIONES (
    id_sesion         INT            IDENTITY(1,1) PRIMARY KEY,
    id_turno          TINYINT        NOT NULL,
    id_usuario_abre   INT            NOT NULL,
    fecha_apertura    DATETIME2      NOT NULL DEFAULT GETDATE(),
    monto_inicial     DECIMAL(10,2)  NOT NULL CHECK (monto_inicial >= 0),
    id_usuario_cierra INT            NULL,
    fecha_cierre      DATETIME2      NULL,
    monto_final       DECIMAL(10,2)  NULL CHECK (monto_final >= 0),
    observaciones     NVARCHAR(300)  NULL,

    CONSTRAINT FK_CAJA_TURNO      FOREIGN KEY (id_turno)          REFERENCES dbo.CAT_TURNO(id_turno),
    CONSTRAINT FK_CAJA_USR_ABRE   FOREIGN KEY (id_usuario_abre)   REFERENCES dbo.USUARIOS(id_usuario),
    CONSTRAINT FK_CAJA_USR_CIERRA FOREIGN KEY (id_usuario_cierra) REFERENCES dbo.USUARIOS(id_usuario)
);
GO

CREATE TABLE dbo.REPORTES_VENTAS (
    id_reporte      INT            IDENTITY(1,1) PRIMARY KEY,
    id_sesion       INT            NOT NULL UNIQUE,
    fecha_desde     DATETIME2      NOT NULL,
    fecha_hasta     DATETIME2      NOT NULL,
    cantidad_ventas INT            NOT NULL DEFAULT 0,
    total_general   DECIMAL(10,2)  NOT NULL DEFAULT 0,
    generado_por    INT            NOT NULL,
    generated_at    DATETIME2      NOT NULL DEFAULT GETDATE(),

    CONSTRAINT FK_RPT_SESION  FOREIGN KEY (id_sesion)    REFERENCES dbo.CAJA_SESIONES(id_sesion),
    CONSTRAINT FK_RPT_USUARIO FOREIGN KEY (generado_por) REFERENCES dbo.USUARIOS(id_usuario)
);
GO

-- ============================================================
--  PASO 6: VISTAS
-- ============================================================

-- Disponibilidad de habitaciones
CREATE OR ALTER VIEW dbo.VW_DISPONIBILIDAD AS
SELECT
    h.id_habitacion,
    h.numero,
    t.nombre      AS tipo,
    t.tarifa_base,
    e.nombre      AS estado
FROM dbo.HABITACIONES h
JOIN dbo.TIPO_HABITACION       t ON h.id_tipo   = t.id_tipo
JOIN dbo.CAT_ESTADO_HABITACION e ON h.id_estado = e.id_estado;
GO

-- Reporte base de ingresos (REQ-10)
CREATE OR ALTER VIEW dbo.VW_REPORTE_BASE AS
SELECT
    c.id_comprobante,
    c.numero_comprobante,
    r.fecha_checkin,
    r.fecha_checkout,
    c.dias_estancia,
    h.numero                          AS habitacion,
    t.nombre                          AS tipo,
    hu.nro_documento,
    td.nombre                         AS tipo_documento,
    hu.nombre + ' ' + hu.apellido     AS huesped,
    c.subtotal,
    c.total_general,
    mp.nombre                         AS metodo_pago,
    c.fecha_pago
FROM dbo.COMPROBANTE c
JOIN dbo.RESERVAS          r  ON c.id_reserva    = r.id_reserva
JOIN dbo.HABITACIONES      h  ON c.id_habitacion = h.id_habitacion
JOIN dbo.TIPO_HABITACION   t  ON h.id_tipo        = t.id_tipo
JOIN dbo.HUESPEDES         hu ON r.id_huesped     = hu.id_huesped
JOIN dbo.TIPO_DOCUMENTO    td ON hu.id_tipo_documento = td.id_tipo_documento
JOIN dbo.CAT_METODO_PAGO   mp ON c.id_metodo_pago = mp.id_metodo;
GO

-- Detalle de facturas por sesion de caja
CREATE OR ALTER VIEW dbo.VW_CIERRE_CAJA AS
SELECT
    cs.id_sesion,
    ct.nombre                          AS turno,
    ua.nombre                          AS abierto_por,
    cs.fecha_apertura,
    cs.monto_inicial,
    uc.nombre                          AS cerrado_por,
    cs.fecha_cierre,
    cs.monto_final,
    c.id_comprobante,
    c.numero_comprobante,
    hu.nro_documento,
    hu.nombre + ' ' + hu.apellido      AS huesped,
    h.numero                           AS habitacion,
    c.total_general,
    mp.nombre                          AS metodo_pago,
    c.fecha_pago
FROM dbo.CAJA_SESIONES cs
JOIN dbo.CAT_TURNO          ct ON cs.id_turno          = ct.id_turno
JOIN dbo.USUARIOS           ua ON cs.id_usuario_abre   = ua.id_usuario
LEFT JOIN dbo.USUARIOS      uc ON cs.id_usuario_cierra = uc.id_usuario
LEFT JOIN dbo.COMPROBANTE    c ON c.fecha_pago BETWEEN cs.fecha_apertura
                                             AND ISNULL(cs.fecha_cierre, GETDATE())
LEFT JOIN dbo.RESERVAS       r ON c.id_reserva          = r.id_reserva
LEFT JOIN dbo.HUESPEDES     hu ON r.id_huesped           = hu.id_huesped
LEFT JOIN dbo.HABITACIONES   h ON c.id_habitacion        = h.id_habitacion
LEFT JOIN dbo.CAT_METODO_PAGO mp ON c.id_metodo_pago     = mp.id_metodo;
GO

-- Resumen de ventas por sesion
CREATE OR ALTER VIEW dbo.VW_REPORTE_VENTAS AS
SELECT
    rv.id_reporte,
    ct.nombre        AS turno,
    rv.fecha_desde,
    rv.fecha_hasta,
    rv.cantidad_ventas,
    rv.total_general,
    u.nombre         AS generado_por,
    rv.generated_at
FROM dbo.REPORTES_VENTAS rv
JOIN dbo.CAJA_SESIONES cs ON rv.id_sesion    = cs.id_sesion
JOIN dbo.CAT_TURNO     ct ON cs.id_turno     = ct.id_turno
JOIN dbo.USUARIOS       u ON rv.generado_por = u.id_usuario;
GO

-- ============================================================
--  PASO 7: FUNCION DE DISPONIBILIDAD
-- ============================================================

CREATE OR ALTER FUNCTION dbo.FN_HabitacionesDisponibles
(
    @fecha_inicio DATETIME2,
    @fecha_fin    DATETIME2
)
RETURNS TABLE AS RETURN
(
    SELECT
        h.id_habitacion,
        h.numero,
        t.nombre      AS tipo,
        t.tarifa_base
    FROM dbo.HABITACIONES h
    JOIN dbo.TIPO_HABITACION t ON h.id_tipo = t.id_tipo
    WHERE h.id_estado <> 4  -- excluir Mantenimiento
      AND h.id_habitacion NOT IN
      (
          SELECT id_habitacion
          FROM dbo.RESERVAS
          WHERE id_estado IN (1, 2)  -- Pendiente o Confirmada
            AND fecha_checkin  < @fecha_fin
            AND fecha_checkout > @fecha_inicio
      )
);
GO

-- ============================================================
--  PASO 8: DATOS INICIALES
-- ============================================================

INSERT INTO dbo.TIPO_HABITACION (nombre, descripcion, tarifa_base) VALUES
('Simple', 'Habitacion individual con cama simple',    80.00),
('Doble',  'Habitacion con cama matrimonial',         120.00),
('Suite',  'Suite con sala, jacuzzi y vista al mar',  280.00),
('Triple', 'Habitacion con tres camas individuales',  150.00);
GO

-- IMPORTANTE: reemplazar password_hash con valor real generado en Python con bcrypt
-- Ejemplo: import bcrypt; bcrypt.hashpw(b'password', bcrypt.gensalt()).decode()
INSERT INTO dbo.USUARIOS (nombre, email, password_hash, id_rol, id_pregunta, respuesta_seguridad) VALUES
('Administrador', 'admin@hotel.com', 'REEMPLAZAR_CON_HASH_BCRYPT', 1, 1, 'REEMPLAZAR_CON_RESPUESTA');
GO

PRINT 'HotelDB v3.0 creada correctamente.';
GO
