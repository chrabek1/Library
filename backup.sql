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

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books` (
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

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (1,'Jak wystugać bałwana','Stefan Śliwka','Słów kilka o bałwanów struganiu',0),(2,'Komu bije dzwon','Stefan Kisiel','Słów kilka o dzownu biciu',0),(3,'A jakby tak ukraść słońce','Stefan Cień','Słów kilka o kradzieży słońca',0),(4,'Zygzak dla ubogich','Stefan Slalom','Słów kilka o nie wiem czym',0),(5,'Żyrafa - wysoki koń','Stefan Zebra','Słów kilka o wysokich koniach',0),(6,'Krokodyl - niski koń','Stefan Łuska','Słów kilka o niskich koniach',0),(7,'Zebra - prawie zwykły koń','Stefan Łuska','Słów kilka o prawie zwykłych koniach',0),(9,'Świnie','Stefan Bigos','Słów kilka o niskich koniach',0);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books_rentals`
--

DROP TABLE IF EXISTS `books_rentals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books_rentals` (
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

LOCK TABLES `books_rentals` WRITE;
/*!40000 ALTER TABLE `books_rentals` DISABLE KEYS */;
INSERT INTO `books_rentals` VALUES (1,1,1,'0000-00-00 00:00:00','2019-12-29 00:00:00'),(2,2,1,'0000-00-00 00:00:00','2019-12-29 00:00:00'),(3,3,1,'0000-00-00 00:00:00','2019-12-29 00:00:00'),(4,6,1,'2019-12-29 00:00:00','2019-12-29 00:00:00'),(5,7,1,'2019-12-29 00:00:00','2019-12-29 00:00:00'),(6,7,1,'2019-12-29 00:00:00','2019-12-30 00:00:00'),(7,8,1,'2019-12-30 00:00:00','2019-12-31 00:00:00');
/*!40000 ALTER TABLE `books_rentals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `routes`
--

DROP TABLE IF EXISTS `routes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `routes` (
  `source_address` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `route_id` int(11) NOT NULL AUTO_INCREMENT,
  `destination_address` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `distance` int(11) DEFAULT NULL,
  PRIMARY KEY (`route_id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `routes`
--

LOCK TABLES `routes` WRITE;
/*!40000 ALTER TABLE `routes` DISABLE KEYS */;
INSERT INTO `routes` VALUES ('ul. Zakręt 8, Poznań',6,'Złota 44, Warszawa',450,'2018-03-15 00:00:00',314089),('ul. Zakręt 8, Poznań',7,'Złota 44, Warszawa',450,'2018-03-15 00:00:00',314089),('ul. Zakręt 8, Poznań',8,'Złota 44, Warszawa',450,'2018-03-15 00:00:00',314089),('ul. Zakręt 8, Poznań',9,'Zwierzyniecka 33, Tarnobrzeg',450,'2018-03-15 00:00:00',469833),('Sandomierz',10,'Zwierzyniecka 33, Tarnobrzeg',450,'2018-03-15 00:00:00',14992),('Sandomierz',11,'Zwierzyniecka 33, Tarnobrzeg',450,'2019-12-15 00:00:00',14992),('Sandomierz',12,'Zwierzyniecka 33, Tarnobrzeg',450,'2019-03-15 00:00:00',14992),('Rzeszów',13,'Zwierzyniecka 33, Tarnobrzeg',150,'2019-03-17 00:00:00',74767),('Sopot',14,'Zwierzyniecka 33, Tarnobrzeg',50,'2019-03-11 00:00:00',589772),('Sopot',15,'Zwierzyniecka 33, Tarnobrzeg',50,'2019-12-11 00:00:00',589772),('Rzeszów',16,'Zwierzyniecka 33, Tarnobrzeg',2,'2019-12-08 00:00:00',74767),('Rzeszów',17,'Zwierzyniecka 33, Tarnobrzeg',2,'2019-12-08 00:00:00',74767),('Rzeszów',18,'Zwierzyniecka 33, Tarnobrzeg',2,'2019-12-08 00:00:00',74767),('Rzeszów',19,'Zwierzyniecka 33, Tarnobrzeg',3,'2019-12-08 00:00:00',74767),('Koniemłoty',20,'Zwierzyniecka 33, Tarnobrzeg',3,'2019-12-08 00:00:00',53275),('Lwowska 98B, Rzeszów',21,'Zwierzyniecka 33, Tarnobrzeg',3,'2019-12-08 00:00:00',82393),('Warszawa',22,'Zwierzyniecka 33, Tarnobrzeg',3,'2019-12-08 00:00:00',252727),('Gdańsk',23,'Zwierzyniecka 33, Tarnobrzeg',3,'2019-12-08 00:00:00',572541),('Katowice',24,'Zwierzyniecka 33, Tarnobrzeg',3,'2019-12-08 00:00:00',252046),('Bydgoszcz',25,'Zwierzyniecka 33, Tarnobrzeg',3,'2019-12-08 00:00:00',458309),('Wrocław',26,'Zwierzyniecka 33, Tarnobrzeg',3,'2019-12-08 00:00:00',443005),('Wrocławek',27,'Zwierzyniecka 33, Tarnobrzeg',3,'2019-12-08 00:00:00',361280),('Nowa Dęba',28,'Zwierzyniecka 33, Tarnobrzeg',3,'2019-12-08 00:00:00',21125),('Nowa Dęba',29,'Zwierzyniecka 33, Tarnobrzeg',3,'2019-12-08 00:00:00',21125);
/*!40000 ALTER TABLE `routes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-31 21:57:21
