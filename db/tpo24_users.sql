-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: tpo24
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `acc_type` enum('občan','naročnik','voznik pluga','vodja izmene','admin') NOT NULL,
  `note` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'test1','test1','občan',NULL),(2,'test2','test2','občan',NULL),(3,'aa','$2b$12$LV7lQduv.p8kudRz7.cm4e8N8Q.tYNNOUndFYyGDwkzesss6RuyQa','občan',NULL),(4,'FilipG','$2b$12$6witxYcQ3SJmik9AIB8Hdump1RqZMEzSVjDQUkM0wqoB/aFv.GMzK','občan',NULL),(5,'as','$2b$12$05bqdHB.5ntksM2BLwY5GuWYIOX.Lwq6XHHFmw3OWsfScE4/Ff69q','občan',NULL),(6,'temp','hashed_password','občan',NULL),(7,'aae','$2b$12$XBoXJHAMJkC6TmYLGztVl.LWjK2HJqD0kvVfGo2Gv2cLtTnhZLyja','občan',NULL),(8,'naročnik','$2b$12$Z0vBW9ADw7MM7Mexk/F4J.FMQDIKBm0NyEtxxF4qWhwU.HL47ucUK','naročnik',NULL),(9,'tvoja mami','$2b$12$OS/lQ7TuVUAOEcCf/KKuJ.B3IYjIUFofZiSvnpKLtje6cB54N4QJW','voznik pluga',NULL),(10,'tvoja mami!','$2b$12$rCnxN4ZHZqtrIrbn9yBHseJVbaMob1hddzPX1Wra62DlWy7rHzutq','voznik pluga',NULL),(11,'ss','$2b$12$CCdZ2nj9U4BH86SogBYXcOBantYbJAF3Fw6w31VgeukPISjnzkkMe','naročnik',NULL),(12,'sfsd','$2b$12$2H81O.N3UKp5VT/VeXGnO.i1FS38Xrmj0V7CPNeGz.yOa.tQUNY0q','občan',NULL),(13,'tpouser','$2b$12$U4S4tC6MOcWzHzcS5XSKbO/Z82.LRzY2bpyZQNCkpAY51IMYDFN0i','voznik pluga',NULL),(14,'temp','hashed_password','občan',NULL),(15,'temp','hashed_password','občan',NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-05 16:09:24
