
--
-- Estructura de tabla para la tabla `products`
--
CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `price` float NOT NULL,
  `category` varchar(100) NOT NULL,
  `released` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `products`
--

INSERT INTO `products` (`id`, `name`, `price`, `category`, `released`) VALUES
(1, 'GOku Toys', 97500, 'Gifts', 1),
(2, 'Troll Lord of the rings', 70200, 'Gifts', 0),
(3, 'Futboll Soccer Grid', 25400, 'Sports', 1),
(4, 'Vegeta Toys', 65800, 'Gifts', 1);




--
-- Estructura de tabla para la tabla `users`
--
CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(1, 'admin', 'admin12345'),
(2, 'polo', 'qwerty12345');