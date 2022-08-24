--Creamos la base datos
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


CREATE TABLE `producto` (
  `codigo` varchar(10) NOT NULL,
  `descripcion` varchar(50) NOT NULL,
  `categoria` varchar(50) NOT NULL,
  `precio` decimal(9,2) NOT NULL,
  `stock` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--Insertamos los productos

INSERT INTO `producto` (`codigo`, `descripcion`, `categoria`, `precio`, `stock`) VALUES
('C001', 'Chocolate', 'Dulce', '2.00', 100),
('C002', 'Pepino', 'Frutos Verdes', '1.00', 120);

--PONEMOS UN PRIMARY KEY EN CODIGO CON PRODUCTOS
ALTER TABLE `producto`
  ADD PRIMARY KEY (`codigo`);
COMMIT;
