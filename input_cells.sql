-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: localhost    Database: klazor_dev
-- ------------------------------------------------------
-- Server version	5.7.27-0ubuntu0.18.04.1

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
-- Table structure for table `file_cell`
--

DROP TABLE IF EXISTS `file_cell`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `file_cell` (
  `cell_ptr_id` int(11) NOT NULL,
  `title` varchar(64) DEFAULT NULL,
  `file` longtext,
  PRIMARY KEY (`cell_ptr_id`),
  CONSTRAINT `file_cell_cell_ptr_id_75b23342_fk_cell_id` FOREIGN KEY (`cell_ptr_id`) REFERENCES `cell` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `file_cell`
--

LOCK TABLES `file_cell` WRITE;
/*!40000 ALTER TABLE `file_cell` DISABLE KEYS */;
/*!40000 ALTER TABLE `file_cell` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `multiple_choice_input_cell`
--

DROP TABLE IF EXISTS `multiple_choice_input_cell`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `multiple_choice_input_cell` (
  `cell_ptr_id` int(11) NOT NULL,
  PRIMARY KEY (`cell_ptr_id`),
  CONSTRAINT `multiple_choice_input_cell_cell_ptr_id_588dd92a_fk_cell_id` FOREIGN KEY (`cell_ptr_id`) REFERENCES `cell` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `multiple_choice_input_cell`
--

LOCK TABLES `multiple_choice_input_cell` WRITE;
/*!40000 ALTER TABLE `multiple_choice_input_cell` DISABLE KEYS */;
/*!40000 ALTER TABLE `multiple_choice_input_cell` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `numerical_input_cell`
--

DROP TABLE IF EXISTS `numerical_input_cell`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `numerical_input_cell` (
  `cell_ptr_id` int(11) NOT NULL,
  `answer` double DEFAULT NULL,
  PRIMARY KEY (`cell_ptr_id`),
  CONSTRAINT `numerical_input_cell_cell_ptr_id_540b07b6_fk_cell_id` FOREIGN KEY (`cell_ptr_id`) REFERENCES `cell` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `numerical_input_cell`
--

LOCK TABLES `numerical_input_cell` WRITE;
/*!40000 ALTER TABLE `numerical_input_cell` DISABLE KEYS */;
/*!40000 ALTER TABLE `numerical_input_cell` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `open_ended_input_cell`
--

DROP TABLE IF EXISTS `open_ended_input_cell`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `open_ended_input_cell` (
  `cell_ptr_id` int(11) NOT NULL,
  `answer` longtext,
  PRIMARY KEY (`cell_ptr_id`),
  CONSTRAINT `open_ended_input_cell_cell_ptr_id_415301a7_fk_cell_id` FOREIGN KEY (`cell_ptr_id`) REFERENCES `cell` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `open_ended_input_cell`
--

LOCK TABLES `open_ended_input_cell` WRITE;
/*!40000 ALTER TABLE `open_ended_input_cell` DISABLE KEYS */;
/*!40000 ALTER TABLE `open_ended_input_cell` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proposition`
--

DROP TABLE IF EXISTS `proposition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `proposition` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `statement` longtext,
  `is_true` tinyint(1) NOT NULL,
  `input_cell_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `klazor_proposition_input_cell_id_f91de8cc_fk_multiple_` (`input_cell_id`),
  CONSTRAINT `klazor_proposition_input_cell_id_f91de8cc_fk_multiple_` FOREIGN KEY (`input_cell_id`) REFERENCES `multiple_choice_input_cell` (`cell_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proposition`
--

LOCK TABLES `proposition` WRITE;
/*!40000 ALTER TABLE `proposition` DISABLE KEYS */;
/*!40000 ALTER TABLE `proposition` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-16 14:09:50
