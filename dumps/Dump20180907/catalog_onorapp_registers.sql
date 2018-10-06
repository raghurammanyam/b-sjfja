-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: catalog
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.16.04.1

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
-- Table structure for table `onorapp_registers`
--

DROP TABLE IF EXISTS `onorapp_registers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `onorapp_registers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `mobile_no` varchar(10) NOT NULL,
  `email` varchar(254) NOT NULL,
  `enquiry` longtext NOT NULL,
  `acknowledge` tinyint(1) NOT NULL,
  `status` varchar(100) DEFAULT NULL,
  `acknowledge_by_id` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `file` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `onorapp_registers_acknowledge_by_id_f3428972_fk_onorapp_users_id` (`acknowledge_by_id`),
  CONSTRAINT `onorapp_registers_acknowledge_by_id_f3428972_fk_onorapp_users_id` FOREIGN KEY (`acknowledge_by_id`) REFERENCES `onorapp_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `onorapp_registers`
--

LOCK TABLES `onorapp_registers` WRITE;
/*!40000 ALTER TABLE `onorapp_registers` DISABLE KEYS */;
INSERT INTO `onorapp_registers` VALUES (1,'raghu','ram','9994445562','ganeshsingamaneni5@gmail.com','updated',1,'update',1,'2018-08-28 04:15:55.654415','2018-08-28 04:18:39.945859',NULL),(2,'raghu','ram','9994445564','ganeshsingamaneni5@gmail.com','updated',1,'update',1,'2018-08-29 03:56:50.871469','2018-08-29 03:56:50.871563',NULL),(3,'raghu','ram','9994445564','ganeshsingamaneni5@gmail.com','updated',0,'update',NULL,'2018-08-29 04:00:23.295033','2018-08-29 04:00:23.295119',NULL),(4,'reddy123','reddy','9878976786','ganeshsingamaneni5@gmail.com','fgjjjjjjjj',0,'upload',NULL,'2018-08-31 03:07:54.967916','2018-08-31 03:07:54.968074','files/Fun_Bucket_Juniors_-_Deadly_Laughing_Jokes_by_Junior_Brahmanandam.mp4');
/*!40000 ALTER TABLE `onorapp_registers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-07 14:41:07
