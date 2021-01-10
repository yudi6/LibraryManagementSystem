-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: bookmanagement
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book` (
  `BookID` varchar(8) NOT NULL,
  `BookName` varchar(40) DEFAULT NULL,
  `Author` varchar(40) DEFAULT NULL,
  `Publisher` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`BookID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES ('10000','MySQL数据库技术与实验指导','钱雪忠','清华大学出版社'),('10001','并行程序设计导论','Peter S. Pacheco','机械工业出版社'),('10002','数据库系统概念','Abraham Silberschatz','机械工业出版社'),('10003','机器学习','周志华','清华大学出版社');
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `refund`
--

DROP TABLE IF EXISTS `refund`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `refund` (
  `SaleID` int DEFAULT NULL,
  KEY `SaleID` (`SaleID`),
  CONSTRAINT `refund_ibfk_1` FOREIGN KEY (`SaleID`) REFERENCES `sale` (`SaleID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `refund`
--

LOCK TABLES `refund` WRITE;
/*!40000 ALTER TABLE `refund` DISABLE KEYS */;
INSERT INTO `refund` VALUES (1610215415),(1610215449),(1610216299),(1610216610),(1610217365),(1610275136),(1610278710),(1618051279);
/*!40000 ALTER TABLE `refund` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `tr_after_in_refund` AFTER INSERT ON `refund` FOR EACH ROW BEGIN 
        update storehouse, (SELECT BookID, Amount 
			from sale
			where sale.SaleID = new.SaleID) as bookid_amount
        set storehouse.Amount = storehouse.Amount + bookid_amount.Amount
        where storehouse.BookID = bookid_amount.BookID;
    END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `sale`
--

DROP TABLE IF EXISTS `sale`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sale` (
  `SaleID` int NOT NULL,
  `BookID` varchar(8) NOT NULL,
  `Amount` int DEFAULT NULL,
  `sellTime` int DEFAULT NULL,
  `saleSum` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`SaleID`,`BookID`),
  KEY `BookID` (`BookID`),
  CONSTRAINT `sale_ibfk_1` FOREIGN KEY (`BookID`) REFERENCES `book` (`BookID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sale`
--

LOCK TABLES `sale` WRITE;
/*!40000 ALTER TABLE `sale` DISABLE KEYS */;
INSERT INTO `sale` VALUES (1610215415,'10000',8,1610215415,40.00),(1610215449,'10001',8,1610215449,40.00),(1610216299,'10002',10,1610216299,50.00),(1610216610,'10002',50,1610216610,250.00),(1610216634,'10002',50,1610216634,250.00),(1610216634,'10003',60,1610216634,300.00),(1610217365,'10000',8,1610217365,40.00),(1610275123,'10001',15,1610275123,75.00),(1610275136,'10001',15,1610275136,75.00),(1610275174,'10001',15,1610275174,75.00),(1610275174,'10003',15,1610275174,75.00),(1610277999,'10002',2,1610277999,10.00),(1610277999,'10003',3,1610277999,15.00),(1610278044,'10002',5,1610278044,25.00),(1610278044,'10003',1,1610278044,5.00),(1610278053,'10002',5,1610278053,25.00),(1610278053,'10003',1,1610278053,5.00),(1610278366,'10002',6,1610278366,30.00),(1610278378,'10002',6,1610278378,30.00),(1610278424,'10002',2,1610278424,10.00),(1610278443,'10001',3,1610278443,15.00),(1610278449,'10001',3,1610278449,15.00),(1610278541,'10001',3,1610278541,15.00),(1610278553,'10001',2,1610278553,10.00),(1610278554,'10001',2,1610278554,10.00),(1610278694,'10000',3,1610278694,15.00),(1610278696,'10000',3,1610278696,15.00),(1610278707,'10000',1,1610278707,5.00),(1610278710,'10000',1,1610278710,5.00),(1618051279,'10001',20,1618051279,100.00);
/*!40000 ALTER TABLE `sale` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `tr_after_in_sale` AFTER INSERT ON `sale` FOR EACH ROW BEGIN 
        update storehouse 
        set storehouse.Amount = storehouse.Amount - new.Amount 
        where storehouse.BookID = new.BookID;
    END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `storehouse`
--

DROP TABLE IF EXISTS `storehouse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `storehouse` (
  `BookID` varchar(8) NOT NULL,
  `Amount` int DEFAULT NULL,
  `Price` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`BookID`),
  CONSTRAINT `storehouse_ibfk_1` FOREIGN KEY (`BookID`) REFERENCES `book` (`BookID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storehouse`
--

LOCK TABLES `storehouse` WRITE;
/*!40000 ALTER TABLE `storehouse` DISABLE KEYS */;
INSERT INTO `storehouse` VALUES ('10000',74,5.00),('10001',80,5.00),('10002',39,5.00),('10003',31,5.00);
/*!40000 ALTER TABLE `storehouse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplier`
--

DROP TABLE IF EXISTS `supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supplier` (
  `supplierID` varchar(8) NOT NULL,
  `supplierName` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`supplierID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier`
--

LOCK TABLES `supplier` WRITE;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
INSERT INTO `supplier` VALUES ('20001','广州图书集团'),('20002','北京图书集团');
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplierprice`
--

DROP TABLE IF EXISTS `supplierprice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supplierprice` (
  `supplierID` varchar(8) NOT NULL,
  `BookID` varchar(8) NOT NULL,
  `Price` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`supplierID`,`BookID`),
  KEY `BookID` (`BookID`),
  CONSTRAINT `supplierprice_ibfk_1` FOREIGN KEY (`supplierID`) REFERENCES `supplier` (`supplierID`),
  CONSTRAINT `supplierprice_ibfk_2` FOREIGN KEY (`BookID`) REFERENCES `book` (`BookID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplierprice`
--

LOCK TABLES `supplierprice` WRITE;
/*!40000 ALTER TABLE `supplierprice` DISABLE KEYS */;
INSERT INTO `supplierprice` VALUES ('20001','10000',10.00),('20001','10001',40.00),('20001','10002',99.00),('20001','10003',88.00),('20002','10000',11.00),('20002','10001',32.00),('20002','10002',50.00),('20002','10003',50.00);
/*!40000 ALTER TABLE `supplierprice` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-10 21:10:21
