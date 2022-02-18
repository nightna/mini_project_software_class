-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 18, 2022 at 02:54 PM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 8.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mini_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `node`
--

CREATE TABLE `node` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `temperature` float NOT NULL,
  `humidity` float NOT NULL,
  `created_at` varchar(50) NOT NULL,
  `updated_at` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `node`
--

INSERT INTO `node` (`id`, `name`, `temperature`, `humidity`, `created_at`, `updated_at`) VALUES
(1, 'node1', 20, 30, '2022-02-15 22:26:07', '2022-02-17 22:15:47');

-- --------------------------------------------------------

--
-- Table structure for table `sensor_data`
--

CREATE TABLE `sensor_data` (
  `id` int(11) NOT NULL,
  `node_id` int(11) NOT NULL,
  `temperature` float NOT NULL,
  `humidity` float NOT NULL,
  `created_at` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `sensor_data`
--

INSERT INTO `sensor_data` (`id`, `node_id`, `temperature`, `humidity`, `created_at`) VALUES
(1, 1, 33, 44, '2022-02-01 00:00:00'),
(2, 1, 25, 43, '2022-02-01 01:00:00'),
(3, 1, 32, 43, '2022-02-01 02:00:00'),
(4, 1, 30, 41, '2022-02-01 03:00:00'),
(5, 1, 30, 47, '2022-02-01 04:00:00'),
(6, 1, 26, 49, '2022-02-01 05:00:00'),
(7, 1, 31, 44, '2022-02-01 06:00:00'),
(8, 1, 33, 48, '2022-02-01 07:00:00'),
(9, 1, 28, 46, '2022-02-01 08:00:00'),
(10, 1, 25, 49, '2022-02-01 09:00:00'),
(11, 1, 32, 49, '2022-02-01 10:00:00'),
(12, 1, 32, 42, '2022-02-01 11:00:00'),
(13, 1, 29, 40, '2022-02-01 12:00:00'),
(14, 1, 26, 42, '2022-02-01 13:00:00'),
(15, 1, 32, 43, '2022-02-01 14:00:00'),
(16, 1, 26, 48, '2022-02-01 15:00:00'),
(17, 1, 32, 41, '2022-02-01 16:00:00'),
(18, 1, 31, 48, '2022-02-01 17:00:00'),
(19, 1, 26, 48, '2022-02-01 18:00:00'),
(20, 1, 28, 43, '2022-02-01 19:00:00'),
(21, 1, 32, 48, '2022-02-01 20:00:00'),
(22, 1, 31, 44, '2022-02-01 21:00:00'),
(23, 1, 29, 43, '2022-02-01 22:00:00'),
(24, 1, 33, 40, '2022-02-01 23:00:00'),
(25, 1, 33, 41, '2022-02-02 00:00:00'),
(26, 1, 27, 41, '2022-02-02 01:00:00'),
(27, 1, 31, 49, '2022-02-02 02:00:00'),
(28, 1, 28, 41, '2022-02-02 03:00:00'),
(29, 1, 27, 48, '2022-02-02 04:00:00'),
(30, 1, 33, 41, '2022-02-02 05:00:00'),
(31, 1, 30, 48, '2022-02-02 06:00:00'),
(32, 1, 25, 41, '2022-02-02 07:00:00'),
(33, 1, 31, 49, '2022-02-02 08:00:00'),
(34, 1, 27, 40, '2022-02-02 09:00:00'),
(35, 1, 30, 49, '2022-02-02 10:00:00'),
(36, 1, 34, 49, '2022-02-02 11:00:00'),
(37, 1, 30, 40, '2022-02-02 12:00:00'),
(38, 1, 31, 43, '2022-02-02 13:00:00'),
(39, 1, 27, 47, '2022-02-02 14:00:00'),
(40, 1, 31, 45, '2022-02-02 15:00:00'),
(41, 1, 27, 45, '2022-02-02 16:00:00'),
(42, 1, 32, 40, '2022-02-02 17:00:00'),
(43, 1, 29, 46, '2022-02-02 18:00:00'),
(44, 1, 30, 48, '2022-02-02 19:00:00'),
(45, 1, 27, 46, '2022-02-02 20:00:00'),
(46, 1, 30, 40, '2022-02-02 21:00:00'),
(47, 1, 26, 47, '2022-02-02 22:00:00'),
(48, 1, 33, 43, '2022-02-02 23:00:00'),
(49, 1, 30, 43, '2022-02-03 00:00:00'),
(50, 1, 26, 43, '2022-02-03 01:00:00'),
(51, 1, 34, 46, '2022-02-03 02:00:00'),
(52, 1, 25, 48, '2022-02-03 03:00:00'),
(53, 1, 28, 45, '2022-02-03 04:00:00'),
(54, 1, 27, 43, '2022-02-03 05:00:00'),
(55, 1, 32, 49, '2022-02-03 06:00:00'),
(56, 1, 28, 41, '2022-02-03 07:00:00'),
(57, 1, 28, 43, '2022-02-03 08:00:00'),
(58, 1, 34, 48, '2022-02-03 09:00:00'),
(59, 1, 34, 45, '2022-02-03 10:00:00'),
(60, 1, 25, 44, '2022-02-03 11:00:00'),
(61, 1, 26, 46, '2022-02-03 12:00:00'),
(62, 1, 31, 41, '2022-02-03 13:00:00'),
(63, 1, 28, 47, '2022-02-03 14:00:00'),
(64, 1, 32, 41, '2022-02-03 15:00:00'),
(65, 1, 29, 44, '2022-02-03 16:00:00'),
(66, 1, 29, 40, '2022-02-03 17:00:00'),
(67, 1, 33, 46, '2022-02-03 18:00:00'),
(68, 1, 26, 46, '2022-02-03 19:00:00'),
(69, 1, 25, 44, '2022-02-03 20:00:00'),
(70, 1, 25, 44, '2022-02-03 21:00:00'),
(71, 1, 27, 45, '2022-02-03 22:00:00'),
(72, 1, 33, 41, '2022-02-03 23:00:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `node`
--
ALTER TABLE `node`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sensor_data`
--
ALTER TABLE `sensor_data`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `node`
--
ALTER TABLE `node`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `sensor_data`
--
ALTER TABLE `sensor_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
