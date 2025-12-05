CREATE DATABASE  IF NOT EXISTS `login_data` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `login_data`;
-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: 192.168.29.204    Database: login_data
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `blockchain_metadata`
--

DROP TABLE IF EXISTS `blockchain_metadata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blockchain_metadata` (
  `block_index` int NOT NULL,
  `timestamp` bigint NOT NULL,
  `transaction_hash` varchar(64) NOT NULL,
  `previous_hash` varchar(64) NOT NULL,
  `block_hash` varchar(64) NOT NULL,
  PRIMARY KEY (`block_index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blockchain_metadata`
--

LOCK TABLES `blockchain_metadata` WRITE;
/*!40000 ALTER TABLE `blockchain_metadata` DISABLE KEYS */;
INSERT INTO `blockchain_metadata` VALUES (0,1725631701,'89eb0ac031a63d2421cd05a2fbe41f3ea35f5c3712ca839cbf6b85c4ee07b7a3','0','de717c7183a18bfa452a31b507cb13a52018f715cf9a8cfe162f59069393a842'),(1,1725631909,'04d16fcc728f7c20b84b34f19a44393c5ef69d8167163f65d4b2f877c6a2b2c2','de717c7183a18bfa452a31b507cb13a52018f715cf9a8cfe162f59069393a842','b4bbb5842438725fda9c5b21b02dfc2872f947190aa43831f7099989074bc992'),(2,1725631980,'04d16fcc728f7c20b84b34f19a44393c5ef69d8167163f65d4b2f877c6a2b2c2','b4bbb5842438725fda9c5b21b02dfc2872f947190aa43831f7099989074bc992','6791be01e1329ab51549d3034d6eaee3204196b3a2076dabc4cab9268da4af70'),(3,1725632079,'202cf5a0e54cdafbd0ce2f2b14b94a5708d6d2a2c701017f10a340bccc12af2a','6791be01e1329ab51549d3034d6eaee3204196b3a2076dabc4cab9268da4af70','5bd458bb3966e158bd87849d5458b7a70bbad547f08a44c1184e05c9e6fd92fa'),(4,1725632191,'c24e9f5da0d04b3d5a9caf5e36c54e5f3d7381571ec1f10ce2dcab32a992752e','5bd458bb3966e158bd87849d5458b7a70bbad547f08a44c1184e05c9e6fd92fa','3d1f821a3f5fc0ed745d5635bfbb500a30f371f29d3bb1b986f5cfd02912c8b1'),(5,1725632245,'8fc9ff9bc87df7b5d1521cb94c0869b86f779625a1479d6fe144d90820d6b1dd','3d1f821a3f5fc0ed745d5635bfbb500a30f371f29d3bb1b986f5cfd02912c8b1','cd474d08f88c20692c3c61e7fd9bd7f51e4ae9e68abe2974c99402191ea4c9c0'),(6,1725632544,'606333613cc3097d3bc52106a0fb0931221fa8cf9367789159ff99962fcabbaa','cd474d08f88c20692c3c61e7fd9bd7f51e4ae9e68abe2974c99402191ea4c9c0','2b04cc35565bdc06a642201f05318b920d1dc96967857fffe2b3d8a00447fad6'),(7,1725632624,'606333613cc3097d3bc52106a0fb0931221fa8cf9367789159ff99962fcabbaa','2b04cc35565bdc06a642201f05318b920d1dc96967857fffe2b3d8a00447fad6','8ac5d93dd5bed5a05ae0b44e0e0fea5f22572d56d00901d64076c5d9eb12202a'),(8,1726750247,'324944c173e70ae5125bfb225e550f7a91932f96df1525502c0e2f487f0895a2','8ac5d93dd5bed5a05ae0b44e0e0fea5f22572d56d00901d64076c5d9eb12202a','9b22f27298c1cdb7c368c46a3ec63cbc8e670eb83c6d6f8945f7dac0b07d4fb3'),(9,1727786756,'bfaeaee26f2b0bfcf515940ac36a1a98a1f69c4ccc29ccd25cef42d4f0d4362b','9b22f27298c1cdb7c368c46a3ec63cbc8e670eb83c6d6f8945f7dac0b07d4fb3','f830ceaffb95530f4af87ba4071a2fd95e8d08903ff810c8077e502730bcb703'),(10,1735582784,'b225c0fe10f29896994cc3c4c863ffd53a4bac513cdb9998a9b56df5e295b39c','f830ceaffb95530f4af87ba4071a2fd95e8d08903ff810c8077e502730bcb703','4c4f0a7de5e608ed6fcc7b5d0d85415168fded1124da798d67d63c6784676ae7');
/*!40000 ALTER TABLE `blockchain_metadata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `candidates`
--

DROP TABLE IF EXISTS `candidates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `candidates` (
  `name_cand` varchar(100) NOT NULL,
  `house_party` varchar(200) NOT NULL,
  `votes` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `candidates`
--

LOCK TABLES `candidates` WRITE;
/*!40000 ALTER TABLE `candidates` DISABLE KEYS */;
INSERT INTO `candidates` VALUES ('Joe Biden','Green House',7);
/*!40000 ALTER TABLE `candidates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `data_main`
--

DROP TABLE IF EXISTS `data_main`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `data_main` (
  `user_name` varchar(200) NOT NULL,
  `user_age` int NOT NULL,
  `user_aadhar` varchar(12) NOT NULL,
  `user_state` varchar(50) NOT NULL,
  `user_accountno` varchar(6) NOT NULL,
  `user_pass` varchar(222) NOT NULL,
  `VoteCn` tinyint DEFAULT '1',
  UNIQUE KEY `user_accountno` (`user_accountno`),
  CONSTRAINT `data_main_chk_1` CHECK ((`user_age` >= 18)),
  CONSTRAINT `data_main_chk_2` CHECK (((`VoteCn` <= 1) and (`VoteCn` >= 0))),
  CONSTRAINT `data_main_chk_3` CHECK (((`VoteCn` <= 1) and (`VoteCn` >= 0))),
  CONSTRAINT `data_main_chk_4` CHECK (((`VoteCn` <= 1) and (`VoteCn` >= 0)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_main`
--

LOCK TABLES `data_main` WRITE;
/*!40000 ALTER TABLE `data_main` DISABLE KEYS */;
INSERT INTO `data_main` VALUES ('Ashutosh Pawar',18,'400012344321','Maharashtra','000105','ashu@123',0),('Quandale Dingleberry',32,'211235647894','Uttar Pradesh','183846','quando@humperdink',0),('Sample Sample',53,'789845651232','Kerala','364517','sample@sample',0),('Sample User',18,'123456784321','Goa','410061','sample@1',0),('Sample Three',42,'565489872321','Bihar','468423','sample@3',0),('why',44,'456578981232','Mizoram','494239','why@1',1),('Project Sample',32,'789456123216','Maharashtra','852547','sample@project',0),('adidada',22,'123412341234','maharashtra','873653','873653',0),('smam',20,'789456123214','Goa','898152','1234234',0),('Exe Sample',19,'78945620321','Ladakh','994520','exe@sample',1);
/*!40000 ALTER TABLE `data_main` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mod_logs`
--

DROP TABLE IF EXISTS `mod_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mod_logs` (
  `User_Id` char(10) NOT NULL,
  `pass` varchar(222) NOT NULL,
  UNIQUE KEY `User_Id` (`User_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mod_logs`
--

LOCK TABLES `mod_logs` WRITE;
/*!40000 ALTER TABLE `mod_logs` DISABLE KEYS */;
INSERT INTO `mod_logs` VALUES ('5316920326','2hxnc3xndk');
/*!40000 ALTER TABLE `mod_logs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'login_data'
--

--
-- Dumping routines for database 'login_data'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-05 20:32:51
