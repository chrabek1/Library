-- MySQL dump 10.13  Distrib 5.6.46, for Linux (x86_64)
--
-- Host: localhost    Database: transit
-- ------------------------------------------------------
-- Server version	5.6.46

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
-- Table structure for table `books`
--

CREATE DATABASE `library` CHARACTER SET UTF8mb4 COLLATE utf8mb4_bin;


DROP TABLE IF EXISTS `library`.`books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `library`.`books` (
  `book_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `author` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `description` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `library`.`books` WRITE;
/*!40000 ALTER TABLE `library`.`books` DISABLE KEYS */;
INSERT INTO `library`.`books` VALUES (1,'Jak wystugać bałwana','Stefan Śliwka','Słów kilka o bałwanów struganiu',0),(2,'Komu bije dzwon','Stefan Kisiel','Słów kilka o dzownu biciu',0),(3,'A jakby tak ukraść słońce','Stefan Cień','Słów kilka o kradzieży słońca',0),(4,'Zygzak dla ubogich','Stefan Slalom','Słów kilka o nie wiem czym',0),(5,'Żyrafa - wysoki koń','Stefan Zebra','Słów kilka o wysokich koniach',0),(6,'Krokodyl - niski koń','Stefan Łuska','Słów kilka o niskich koniach',0),(7,'Zebra - prawie zwykły koń','Stefan Łuska','Słów kilka o prawie zwykłych koniach',0),(9,'Świnie','Stefan Bigos','Słów kilka o niskich koniach',0);
/*!40000 ALTER TABLE `library`.`books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books_rentals`
--

DROP TABLE IF EXISTS `library`.`books_rentals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `library`.`books_rentals` (
  `rental_id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `start_date` datetime NOT NULL,
  `end_date` datetime DEFAULT NULL,
  PRIMARY KEY (`rental_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books_rentals`
--

LOCK TABLES `library`.`books_rentals` WRITE;
/*!40000 ALTER TABLE `library`.`books_rentals` DISABLE KEYS */;
INSERT INTO `library`.`books_rentals` VALUES (1,1,1,'0000-00-00 00:00:00','2019-12-29 00:00:00'),(2,2,1,'0000-00-00 00:00:00','2019-12-29 00:00:00'),(3,3,1,'0000-00-00 00:00:00','2019-12-29 00:00:00'),(4,6,1,'2019-12-29 00:00:00','2019-12-29 00:00:00'),(5,7,1,'2019-12-29 00:00:00','2019-12-29 00:00:00'),(6,7,1,'2019-12-29 00:00:00','2019-12-30 00:00:00'),(7,8,1,'2019-12-30 00:00:00','2019-12-31 00:00:00');
/*!40000 ALTER TABLE `library`.`books_rentals` ENABLE KEYS */;
UNLOCK TABLES;
