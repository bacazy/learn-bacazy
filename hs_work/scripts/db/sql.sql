-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.15 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             10.1.0.5464
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for hs_work
CREATE DATABASE IF NOT EXISTS `hs_work` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
USE `hs_work`;

-- Dumping structure for table hs_work.hs_price
CREATE TABLE IF NOT EXISTS `hs_price` (
  `item_id` varchar(64) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `item_type` varchar(64) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `item_price` decimal(10,10) NOT NULL,
  `item_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- Data exporting was unselected.
-- Dumping structure for table hs_work.hs_user
CREATE TABLE IF NOT EXISTS `hs_user` (
  `user_id` varchar(64) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `user_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `user_group` varchar(64) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- Data exporting was unselected.
-- Dumping structure for table hs_work.hs_work
CREATE TABLE IF NOT EXISTS `hs_work` (
  `work_id` varchar(64) COLLATE utf8_bin NOT NULL,
  `user_id` varchar(64) COLLATE utf8_bin NOT NULL,
  `work_item` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  `work_count` int(11) DEFAULT NULL,
  PRIMARY KEY (`work_id`),
  KEY `item_key` (`work_item`),
  KEY `user_key` (`user_id`),
  CONSTRAINT `item_key` FOREIGN KEY (`work_item`) REFERENCES `hs_price` (`item_id`),
  CONSTRAINT `user_key` FOREIGN KEY (`user_id`) REFERENCES `hs_user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- Data exporting was unselected.
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
