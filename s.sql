-- MySQL dump 10.13  Distrib 5.5.44, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: xiecheng
-- ------------------------------------------------------
-- Server version	5.5.44-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `fly_xc`
--

DROP TABLE IF EXISTS `fly_xc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fly_xc` (
  `YearMonthDate1` varchar(250) DEFAULT NULL,
  `DepartPort` varchar(250) DEFAULT NULL,
  `ArrivePort` varchar(250) DEFAULT NULL,
  `Flight_No` varchar(250) DEFAULT NULL,
  `Flight_Price` varchar(250) DEFAULT NULL,
  `inVent` varchar(250) DEFAULT NULL,
  `xc_id` varchar(250) DEFAULT NULL,
  `all_uni` varchar(250) DEFAULT NULL,
  UNIQUE KEY `xc_id` (`xc_id`),
  UNIQUE KEY `all_uni` (`all_uni`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fly_xc`
--

LOCK TABLES `fly_xc` WRITE;
/*!40000 ALTER TABLE `fly_xc` DISABLE KEYS */;
INSERT INTO `fly_xc` VALUES ('2015-11-15','YIE','NAY','2986','468.0','3','136996542240','2015-11-15YIENAY2986');
/*!40000 ALTER TABLE `fly_xc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fly_xc2`
--

DROP TABLE IF EXISTS `fly_xc2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fly_xc2` (
  `YearMonthDate1` varchar(250) DEFAULT NULL,
  `DepartPort` varchar(250) DEFAULT NULL,
  `ArrivePort` varchar(250) DEFAULT NULL,
  `Flight_No` varchar(250) DEFAULT NULL,
  `Flight_Price` varchar(250) DEFAULT NULL,
  `inVent` varchar(250) DEFAULT NULL,
  `xc_id` varchar(250) DEFAULT NULL,
  `all_uni` varchar(250) DEFAULT NULL,
  `price` varchar(20) DEFAULT NULL,
  UNIQUE KEY `xc_id` (`xc_id`),
  UNIQUE KEY `all_uni` (`all_uni`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fly_xc2`
--

LOCK TABLES `fly_xc2` WRITE;
/*!40000 ALTER TABLE `fly_xc2` DISABLE KEYS */;
INSERT INTO `fly_xc2` VALUES ('2015-11-15','YIE','NAY','2986',NULL,'2','136996542240','2015-11-15YIENAY2986','590.78');
/*!40000 ALTER TABLE `fly_xc2` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-11-20  9:41:47
