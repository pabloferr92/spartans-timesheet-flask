CREATE DATABASE  IF NOT EXISTS `timesheet` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;
USE `timesheet`;
-- MySQL dump 10.13  Distrib 8.0.12, for Win64 (x86_64)
--
-- Host: localhost    Database: flasktest
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `categoria`
--

DROP TABLE IF EXISTS `categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `categoria` (
  `categoria_id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `descricao` varchar(5000) DEFAULT NULL,
  `criado_por` varchar(100) NOT NULL,
  `data_criacao` datetime NOT NULL,
  `atualizado_por` varchar(100) NOT NULL,
  `data_ultima_atualizacao` datetime NOT NULL,
  `ativo` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`categoria_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoria`
--

LOCK TABLES `categoria` WRITE;
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
INSERT INTO `categoria` VALUES (1,'categoriax','descricao_nova','luiz.h.lindner@gmail.com','2018-10-03 16:54:04','luiz.h.lindner@gmail.com','2018-10-03 17:38:01',1),(2,'categoria2','2','luiz.h.lindner@gmail.com','2018-10-03 16:55:07','luiz.h.lindner@gmail.com','2018-10-03 16:55:07',1),(3,'categoria2',NULL,'luiz.h.lindner@gmail.com','2018-10-03 16:55:44','luiz.h.lindner@gmail.com','2018-10-03 16:55:44',1),(4,'categoria2',NULL,'luiz.h.lindner@gmail.com','2018-10-03 16:55:54','luiz.h.lindner@gmail.com','2018-10-03 16:55:54',1),(5,'categoria2','teste','luiz.h.lindner@gmail.com','2018-10-03 16:56:13','luiz.h.lindner@gmail.com','2018-10-03 16:56:13',1),(6,'categoria2','teste','luiz.h.lindner@gmail.com','2018-10-03 16:56:28','luiz.h.lindner@gmail.com','2018-10-03 16:56:28',1),(7,'categoria2','teste','luiz.h.lindner@gmail.com','2018-10-03 17:21:15','luiz.h.lindner@gmail.com','2018-10-03 17:21:15',1),(8,'cat3','e agora?','luiz.h.lindner@gmail.com','2018-10-03 17:33:53','luiz.h.lindner@gmail.com','2018-10-03 17:33:53',1);
/*!40000 ALTER TABLE `categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `cliente` (
  `cliente_id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `criado_por` varchar(100) NOT NULL,
  `data_criacao` datetime NOT NULL,
  `atualizado_por` varchar(100) NOT NULL,
  `data_ultima_atualizacao` datetime NOT NULL,
  `ativo` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`cliente_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (1,'novo nome cliente','luiz.h.lindner@gmail.com','2018-10-03 17:41:00','luiz.h.lindner@gmail.com','2018-10-03 17:50:13',0),(2,'cliente novo','luiz.h.lindner@gmail.com','2018-10-03 17:48:57','luiz.h.lindner@gmail.com','2018-10-03 17:48:57',1);
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lancamento_horas`
--

DROP TABLE IF EXISTS `lancamento_horas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `lancamento_horas` (
  `lancamento_horas_id` int(11) NOT NULL AUTO_INCREMENT,
  `projeto_id` int(11) NOT NULL,
  `cliente_id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `categoria_id` int(11) NOT NULL,
  `data_inicio` datetime NOT NULL,
  `data_fim` datetime DEFAULT NULL,
  `descricao` varchar(5000) DEFAULT NULL,
  `criado_por` varchar(100) NOT NULL,
  `data_criacao` datetime NOT NULL,
  `atualizado_por` varchar(100) NOT NULL,
  `data_ultima_atualizacao` datetime NOT NULL,
  `ativo` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`lancamento_horas_id`),
  KEY `fk_lancamento_horas_projeto1_idx` (`projeto_id`),
  KEY `fk_lancamento_horas_cliente1_idx` (`cliente_id`),
  KEY `fk_lancamento_horas_usuario1_idx` (`usuario_id`),
  KEY `fk_lancamento_horas_categoria1_idx` (`categoria_id`),
  CONSTRAINT `fk_lancamento_horas_categoria1` FOREIGN KEY (`categoria_id`) REFERENCES `categoria` (`categoria_id`),
  CONSTRAINT `fk_lancamento_horas_cliente1` FOREIGN KEY (`cliente_id`) REFERENCES `cliente` (`cliente_id`),
  CONSTRAINT `fk_lancamento_horas_projeto1` FOREIGN KEY (`projeto_id`) REFERENCES `projeto` (`projeto_id`),
  CONSTRAINT `fk_lancamento_horas_usuario1` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`usuario_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lancamento_horas`
--

LOCK TABLES `lancamento_horas` WRITE;
/*!40000 ALTER TABLE `lancamento_horas` DISABLE KEYS */;
/*!40000 ALTER TABLE `lancamento_horas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `membros_squad`
--

DROP TABLE IF EXISTS `membros_squad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `membros_squad` (
  `membros_squad_id` int(11) NOT NULL AUTO_INCREMENT,
  `squad_id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `criado_por` varchar(100) NOT NULL,
  `data_criacao` datetime NOT NULL,
  `atualizado_por` varchar(100) NOT NULL,
  `data_ultima_atualizacao` datetime NOT NULL,
  `ativo` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`membros_squad_id`),
  KEY `fk_membros_squad_Squad1_idx` (`squad_id`),
  KEY `fk_membros_squad_usuario1_idx` (`usuario_id`),
  CONSTRAINT `fk_membros_squad_Squad1` FOREIGN KEY (`squad_id`) REFERENCES `squad` (`squad_id`),
  CONSTRAINT `fk_membros_squad_usuario1` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`usuario_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `membros_squad`
--

LOCK TABLES `membros_squad` WRITE;
/*!40000 ALTER TABLE `membros_squad` DISABLE KEYS */;
/*!40000 ALTER TABLE `membros_squad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `perfil`
--

DROP TABLE IF EXISTS `perfil`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `perfil` (
  `perfil_id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `criado_por` varchar(100) NOT NULL,
  `data_criacao` datetime NOT NULL,
  `atualizado_por` varchar(100) NOT NULL,
  `data_ultima_atualizacao` datetime NOT NULL,
  `ativo` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`perfil_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `perfil`
--

LOCK TABLES `perfil` WRITE;
/*!40000 ALTER TABLE `perfil` DISABLE KEYS */;
INSERT INTO `perfil` VALUES (1,'administrador','luiz.h.lindner@gmail.com','2018-09-30 20:17:00','luiz.h.lindner@gmail.com','2018-09-30 20:17:00',1),(2,'gerente','luiz.h.lindner@gmail.com','2018-10-03 02:02:24','luiz.h.lindner@gmail.com','2018-10-03 17:29:17',1),(3,'usuario','luiz.h.lindner@gmail.com','2018-10-03 02:22:58','luiz.h.lindner@gmail.com','2018-10-03 15:16:10',1),(5,'nome','luiz.h.lindner@gmail.com','2018-10-03 19:14:11','luiz.h.lindner@gmail.com','2018-10-03 19:14:11',1);
/*!40000 ALTER TABLE `perfil` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projeto`
--

DROP TABLE IF EXISTS `projeto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `projeto` (
  `projeto_id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `cliente_id` int(11) NOT NULL,
  `squad_id` int(11) DEFAULT NULL,
  `criado_por` varchar(100) NOT NULL,
  `data_criacao` datetime NOT NULL,
  `atualizado_por` varchar(100) NOT NULL,
  `data_ultima_atualizacao` datetime NOT NULL,
  `ativo` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`projeto_id`),
  KEY `fk_Projeto_Cliente1_idx` (`cliente_id`),
  KEY `fk_projeto_squad1_idx` (`squad_id`),
  CONSTRAINT `fk_Projeto_Cliente1` FOREIGN KEY (`cliente_id`) REFERENCES `cliente` (`cliente_id`),
  CONSTRAINT `fk_projeto_squad1` FOREIGN KEY (`squad_id`) REFERENCES `squad` (`squad_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projeto`
--

LOCK TABLES `projeto` WRITE;
/*!40000 ALTER TABLE `projeto` DISABLE KEYS */;
INSERT INTO `projeto` VALUES (1,'projeto 1',1,NULL,'luiz.h.lindner@gmail.com','2018-10-03 18:05:00','luiz.h.lindner@gmail.com','2018-10-03 18:05:00',1),(4,'projeto 2',1,NULL,'luiz.h.lindner@gmail.com','2018-10-03 18:25:49','luiz.h.lindner@gmail.com','2018-10-03 18:25:49',1);
/*!40000 ALTER TABLE `projeto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `squad`
--

DROP TABLE IF EXISTS `squad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `squad` (
  `squad_id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `administrador_id` int(11) NOT NULL,
  `criado_por` varchar(100) NOT NULL,
  `data_criacao` datetime NOT NULL,
  `atualizado_por` varchar(100) NOT NULL,
  `data_ultima_atualizacao` datetime NOT NULL,
  `ativo` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`squad_id`),
  KEY `fk_Squad_usuario1_idx` (`administrador_id`),
  CONSTRAINT `fk_Squad_usuario1` FOREIGN KEY (`administrador_id`) REFERENCES `usuario` (`usuario_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `squad`
--

LOCK TABLES `squad` WRITE;
/*!40000 ALTER TABLE `squad` DISABLE KEYS */;
/*!40000 ALTER TABLE `squad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `usuario` (
  `usuario_id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `telefone` varchar(12) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `perfil_id` int(11) NOT NULL,
  `valor_hora` float(10,2) DEFAULT NULL,
  `timezone` varchar(5) NOT NULL,
  `ultimo_login` datetime DEFAULT NULL,
  `confirmado` tinyint(1) DEFAULT '0',
  `criado_por` varchar(100) NOT NULL,
  `data_criacao` datetime NOT NULL,
  `atualizado_por` varchar(100) NOT NULL,
  `data_ultima_atualizacao` datetime NOT NULL,
  `ativo` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`usuario_id`),
  KEY `fk_usuario_perfil_idx` (`perfil_id`),
  CONSTRAINT `fk_usuario_perfil` FOREIGN KEY (`perfil_id`) REFERENCES `perfil` (`perfil_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'Novo Nome','11930017773','luiz.h.lindner@gmail.com','1234',1,9.90,'-3','2018-10-03 19:37:04',1,'luiz.h.lindner@gmail.com','2018-09-30 20:18:00','luiz.h.lindner@gmail.com','2018-10-03 19:37:39',1),(2,'Hellen Soares Lindner','11930018884','hellen0043@gmail.com','12345',2,19.90,'-3',NULL,0,'luiz.h.lindner@gmail.com','2018-09-30 23:13:00','luiz.h.lindner@gmail.com','2018-09-30 23:13:00',1),(3,'Luiz Henrique Lindner','123123123','luiz.lindner@aoop.com.br','123456',1,33.32,'-3','2018-10-03 19:28:23',0,'luiz.lindner@aoop.com.br','2018-10-03 19:28:23','luiz.lindner@aoop.com.br','2018-10-03 19:28:23',1),(4,'Luiz Henrique Lindner','123123123','luiz.lindne1r@aoop.com.br','123456',1,33.32,'-3','2018-10-03 19:29:08',0,'luiz.lindne1r@aoop.com.br','2018-10-03 19:29:08','luiz.lindne1r@aoop.com.br','2018-10-03 19:29:08',1),(5,'Luiz Henrique Lindner','123123123','luiz.lindne1r2@aoop.com.br','123456',1,33.32,'-3','2018-10-03 19:29:40',0,'luiz.lindne1r2@aoop.com.br','2018-10-03 19:29:40','luiz.lindne1r2@aoop.com.br','2018-10-03 19:29:40',1),(6,'Luiz Henrique Lindner',NULL,'luiz.lindxne1r2@aoop.com.br','123456',1,NULL,'-3','2018-10-03 19:30:06',0,'luiz.lindxne1r2@aoop.com.br','2018-10-03 19:30:06','luiz.lindxne1r2@aoop.com.br','2018-10-03 19:30:06',1);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-03 19:42:19
