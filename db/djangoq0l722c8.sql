-- MySQL dump 10.13  Distrib 5.7.31, for Linux (x86_64)
--
-- Host: localhost    Database: djangoq0l722c8
-- ------------------------------------------------------
-- Server version	5.7.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `djangoq0l722c8`
--

/*!40000 DROP DATABASE IF EXISTS `djangoq0l722c8`*/;

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `djangoq0l722c8` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `djangoq0l722c8`;

--
-- Table structure for table `chat`
--

DROP TABLE IF EXISTS `chat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chat` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `userid` bigint(20) NOT NULL COMMENT '用户id',
  `adminid` bigint(20) DEFAULT NULL COMMENT '管理员id',
  `ask` longtext COLLATE utf8mb4_unicode_ci COMMENT '提问',
  `reply` longtext COLLATE utf8mb4_unicode_ci COMMENT '回复',
  `isreply` int(11) DEFAULT NULL COMMENT '是否回复',
  `isread` int(11) DEFAULT '0' COMMENT '已读/未读(1:已读,0:未读)',
  `uname` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '用户名',
  `uimage` longtext COLLATE utf8mb4_unicode_ci COMMENT '用户头像',
  `type` int(11) DEFAULT '1' COMMENT '内容类型(1:文本,2:图片,3:视频,4:文件,5:表情)',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='在线客服';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat`
--

LOCK TABLES `chat` WRITE;
/*!40000 ALTER TABLE `chat` DISABLE KEYS */;
INSERT INTO `chat` VALUES (1,'2026-01-05 10:27:29',1,1,'提问1','回复1',1,1,'用户名1','upload/chat_uimage1.jpg,upload/chat_uimage2.jpg,upload/chat_uimage3.jpg',1),(2,'2026-01-05 10:27:29',2,2,'提问2','回复2',2,2,'用户名2','upload/chat_uimage2.jpg,upload/chat_uimage3.jpg,upload/chat_uimage4.jpg',2),(3,'2026-01-05 10:27:29',3,3,'提问3','回复3',3,3,'用户名3','upload/chat_uimage3.jpg,upload/chat_uimage4.jpg,upload/chat_uimage5.jpg',3),(4,'2026-01-05 10:27:29',4,4,'提问4','回复4',4,4,'用户名4','upload/chat_uimage4.jpg,upload/chat_uimage5.jpg,upload/chat_uimage6.jpg',4),(5,'2026-01-05 10:27:29',5,5,'提问5','回复5',5,5,'用户名5','upload/chat_uimage5.jpg,upload/chat_uimage6.jpg,upload/chat_uimage7.jpg',5),(6,'2026-01-05 10:27:29',6,6,'提问6','回复6',6,6,'用户名6','upload/chat_uimage6.jpg,upload/chat_uimage7.jpg,upload/chat_uimage8.jpg',6),(7,'2026-01-05 10:27:29',7,7,'提问7','回复7',7,7,'用户名7','upload/chat_uimage7.jpg,upload/chat_uimage8.jpg,upload/chat_uimage1.jpg',7),(8,'2026-01-05 10:27:29',8,8,'提问8','回复8',8,8,'用户名8','upload/chat_uimage8.jpg,upload/chat_uimage1.jpg,upload/chat_uimage2.jpg',8);
/*!40000 ALTER TABLE `chat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chongwudingdan`
--

DROP TABLE IF EXISTS `chongwudingdan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chongwudingdan` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `dingdanbianhao` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '订单编号',
  `chongwunicheng` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '宠物昵称',
  `chongwupinzhong` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '宠物品种',
  `chongwutupian` longtext COLLATE utf8mb4_unicode_ci COMMENT '宠物图片',
  `yanse` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '颜色',
  `jifen` double DEFAULT NULL COMMENT '售价',
  `xiadanriqi` date DEFAULT NULL COMMENT '下单日期',
  `beizhu` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '备注',
  `zhanghao` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '账号',
  `xingming` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '姓名',
  `shoujihaoma` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '手机号码',
  `sfsh` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT '待审核' COMMENT '是否审核',
  `shhf` longtext COLLATE utf8mb4_unicode_ci COMMENT '审核回复',
  `ispay` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT '未支付' COMMENT '是否支付',
  PRIMARY KEY (`id`),
  UNIQUE KEY `dingdanbianhao` (`dingdanbianhao`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='宠物订单';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chongwudingdan`
--

LOCK TABLES `chongwudingdan` WRITE;
/*!40000 ALTER TABLE `chongwudingdan` DISABLE KEYS */;
INSERT INTO `chongwudingdan` VALUES (1,'2026-01-05 10:27:29','978753428','团团','八哥鸟','upload/chongwudingdan_八哥鸟1.jpg,upload/chongwudingdan_八哥鸟2.jpg,upload/chongwudingdan_八哥鸟3.jpg','黑亮色',459,'2026-01-05','无','006','王若曦','13423456789','是','','已支付'),(2,'2026-01-05 10:27:29','978702013','妞妞','美短猫','upload/chongwudingdan_美短猫1.jpg,upload/chongwudingdan_美短猫2.jpg,upload/chongwudingdan_美短猫3.jpg','虎斑纹',476,'2026-01-05','无','002','孙雨晴','13490123456','是','','已支付'),(3,'2026-01-05 10:27:29','978711548','京京','三线仓鼠','upload/chongwudingdan_三线仓鼠1.jpg,upload/chongwudingdan_三线仓鼠2.jpg,upload/chongwudingdan_三线仓鼠3.jpg','棕黑相间',318,'2026-01-05','无','004','周雪','13523456789','是','','已支付'),(4,'2026-01-05 10:27:29','978757601','可可','玄凤鹦鹉','upload/chongwudingdan_玄凤鹦鹉1.jpg,upload/chongwudingdan_玄凤鹦鹉2.jpg,upload/chongwudingdan_玄凤鹦鹉3.jpg','黄白相间',369,'2026-01-05','无','001','刘浩然','13578901234','是','','已支付'),(5,'2026-01-05 10:27:29','978730129','奶糖','边境牧羊犬','upload/chongwudingdan_边境牧羊犬1.jpg,upload/chongwudingdan_边境牧羊犬2.jpg,upload/chongwudingdan_边境牧羊犬3.jpg','黑白相间',189,'2026-01-05','无','003','高雪','13589012345','是','','已支付'),(6,'2026-01-05 10:27:29','978703062','哈利','阿拉斯加','upload/chongwudingdan_阿拉斯加1.jpg,upload/chongwudingdan_阿拉斯加2.jpg,upload/chongwudingdan_阿拉斯加3.jpg','棕白相间',243,'2026-01-05','无','007','张明','13467890123','是','','已支付'),(7,'2026-01-05 10:27:29','978757020','贝贝','比熊犬','upload/chongwudingdan_比熊犬1.jpg,upload/chongwudingdan_比熊犬2.jpg,upload/chongwudingdan_比熊犬3.jpg','纯白色',489,'2026-01-05','无','008','郭阳','13545678901','是','','已支付'),(8,'2026-01-05 10:27:29','978750609','朵朵','布偶猫','upload/chongwudingdan_布偶猫1.jpg,upload/chongwudingdan_布偶猫2.jpg,upload/chongwudingdan_布偶猫3.jpg','白色加浅棕',412,'2026-01-05','无','005','王强','13456789012','是','','已支付');
/*!40000 ALTER TABLE `chongwudingdan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chongwufuwu`
--

DROP TABLE IF EXISTS `chongwufuwu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chongwufuwu` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `fuwumingcheng` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '服务名称',
  `fuwufengmian` longtext COLLATE utf8mb4_unicode_ci COMMENT '服务封面',
  `fuwuleixing` varchar(16) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '服务类型',
  `fuwufanwei` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '服务范围',
  `chongwuleixing` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '宠物类型',
  `jifen` double DEFAULT NULL COMMENT '服务价格',
  `fuwushizhang` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '服务时长',
  `fuwujieshao` longtext COLLATE utf8mb4_unicode_ci COMMENT '服务介绍',
  `clicktime` datetime DEFAULT NULL COMMENT '最近点击时间',
  `clicknum` int(11) DEFAULT '0' COMMENT '点击次数',
  `discussnum` int(11) DEFAULT '0' COMMENT '评论数',
  `storeupnum` int(11) DEFAULT '0' COMMENT '收藏数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='宠物服务';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chongwufuwu`
--

LOCK TABLES `chongwufuwu` WRITE;
/*!40000 ALTER TABLE `chongwufuwu` DISABLE KEYS */;
INSERT INTO `chongwufuwu` VALUES (1,'2026-01-05 10:27:28','流浪猫定点喂养服务','upload/chongwufuwu_流浪猫定点喂养服务1.jpg,upload/chongwufuwu_流浪猫定点喂养服务2.jpg,upload/chongwufuwu_流浪猫定点喂养服务3.jpg','公益喂养','指定社区范围','猫',58,'1小时','定点投放猫粮清洁喂食区补水','2026-01-05 18:27:28',1,0,1),(2,'2026-01-05 10:27:28','宠物犬上门洗护遛护套餐','upload/chongwufuwu_宠物犬上门洗护遛护套餐1.jpg,upload/chongwufuwu_宠物犬上门洗护遛护套餐2.jpg,upload/chongwufuwu_宠物犬上门洗护遛护套餐3.jpg','洗护遛护','近郊8公里内','犬',188,'3小时','上门洗护+耳道护理+喂养+户外遛放','2026-01-05 18:27:28',2,0,2),(3,'2026-01-05 10:27:28','日常萌宠喂养遛护服务','upload/chongwufuwu_日常萌宠喂养遛护服务1.jpg,upload/chongwufuwu_日常萌宠喂养遛护服务2.jpg,upload/chongwufuwu_日常萌宠喂养遛护服务3.jpg','喂养遛护','主城区3公里内','犬',88,'1小时','包含上门喂食遛弯基础清洁','2026-01-05 18:27:28',3,0,3),(4,'2026-01-05 10:27:28','护卫犬上门喂养训练服务','upload/chongwufuwu_护卫犬上门喂养训练服务1.jpg,upload/chongwufuwu_护卫犬上门喂养训练服务2.jpg,upload/chongwufuwu_护卫犬上门喂养训练服务3.jpg','喂养训练','近郊15公里内','犬',228,'3小时','定量喂养+专业训练+户外巡逻式遛放','2026-01-05 18:27:28',4,0,4),(5,'2026-01-05 10:27:28','异宠上门照料服务','upload/chongwufuwu_异宠上门照料服务1.jpg,upload/chongwufuwu_异宠上门照料服务2.jpg,upload/chongwufuwu_异宠上门照料服务3.jpg','异宠护理','市区5公里内','爬行类',138,'1.5小时','喂食补水环境清洁体温监测','2026-01-05 18:27:28',5,0,5),(6,'2026-01-05 10:27:28','赛级犬上门养护服务','upload/chongwufuwu_赛级犬上门养护服务1.jpg,upload/chongwufuwu_赛级犬上门养护服务2.jpg,upload/chongwufuwu_赛级犬上门养护服务3.jpg','赛级养护','近郊12公里内','犬',198,'3小时','定量喂养+毛发护理+专业遛放+体态调整','2026-01-05 18:27:28',6,0,6),(7,'2026-01-05 10:27:28','幼猫专属喂养照料服务','upload/chongwufuwu_幼猫专属喂养照料服务1.jpg,upload/chongwufuwu_幼猫专属喂养照料服务2.jpg,upload/chongwufuwu_幼猫专属喂养照料服务3.jpg','幼猫护理','市区4公里内','猫',108,'2小时','喂奶喂食清洁排便+保暖照料','2026-01-05 18:27:28',7,0,7),(8,'2026-01-05 10:27:28','宠物猫上门洗护喂养套餐','upload/chongwufuwu_宠物猫上门洗护喂养套餐1.jpg,upload/chongwufuwu_宠物猫上门洗护喂养套餐2.jpg,upload/chongwufuwu_宠物猫上门洗护喂养套餐3.jpg','洗护喂养','市区6公里内','猫',168,'2.5小时','上门喂食+基础洗护+耳道清洁','2026-01-05 18:27:28',8,0,8);
/*!40000 ALTER TABLE `chongwufuwu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chongwuhudong`
--

DROP TABLE IF EXISTS `chongwuhudong`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chongwuhudong` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `dingdanbianhao` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '订单编号',
  `fuwumingcheng` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '服务名称',
  `jifen` double DEFAULT NULL COMMENT '价格',
  `jiyangriqi` date DEFAULT NULL COMMENT '寄养日期',
  `chongwuxingming` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '宠物姓名',
  `pinzhong` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '品种',
  `gengxinriqi` date DEFAULT NULL COMMENT '更新日期',
  `zhanghao` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '账号',
  `chongwuzhaopian` longtext COLLATE utf8mb4_unicode_ci COMMENT '宠物照片',
  `chongwushipin` longtext COLLATE utf8mb4_unicode_ci COMMENT '宠物视频',
  `chongwudongtai` longtext COLLATE utf8mb4_unicode_ci COMMENT '宠物动态',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='宠物互动';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chongwuhudong`
--

LOCK TABLES `chongwuhudong` WRITE;
/*!40000 ALTER TABLE `chongwuhudong` DISABLE KEYS */;
INSERT INTO `chongwuhudong` VALUES (1,'2026-01-05 10:27:29','978753428','小型犬短期寄养',88,'2026-01-05','雪球','垂耳兔','2026-01-05','006','upload/chongwuhudong_雪球1.jpg,upload/chongwuhudong_雪球2.jpg,upload/chongwuhudong_雪球3.jpg','','仓鼠转滚轮'),(2,'2026-01-05 10:27:29','978702013','老年宠养护寄养',158,'2026-01-05','团团','侏儒兔','2026-01-05','002','upload/chongwuhudong_团团1.jpg,upload/chongwuhudong_团团2.jpg,upload/chongwuhudong_团团3.jpg','','狗狗接飞盘'),(3,'2026-01-05 10:27:29','978711548','结伴寄养服务',108,'2026-01-05','可乐','美短猫','2026-01-05','004','upload/chongwuhudong_可乐1.jpg,upload/chongwuhudong_可乐2.jpg,upload/chongwuhudong_可乐3.jpg','','布偶猫舔毛'),(4,'2026-01-05 10:27:29','978757601','驱虫防护寄养',88,'2026-01-05','大黄','金毛寻回犬','2026-01-05','001','upload/chongwuhudong_大黄1.jpg,upload/chongwuhudong_大黄2.jpg,upload/chongwuhudong_大黄3.jpg','','兔子啃菜叶'),(5,'2026-01-05 10:27:29','978730129','宠物度假寄养',268,'2026-01-05','咪宝','布偶猫','2026-01-05','003','upload/chongwuhudong_咪宝1.jpg,upload/chongwuhudong_咪宝2.jpg,upload/chongwuhudong_咪宝3.jpg','','喵星人踩奶'),(6,'2026-01-05 10:27:29','978703062','异宠基础寄养',68,'2026-01-05','虎子','狸花猫','2026-01-05','007','upload/chongwuhudong_虎子1.jpg,upload/chongwuhudong_虎子2.jpg,upload/chongwuhudong_虎子3.jpg','','鹦鹉学说话'),(7,'2026-01-05 10:27:29','978757020','基础单宠日托',35,'2026-01-05','花花','加菲猫','2026-01-05','008','upload/chongwuhudong_花花1.jpg,upload/chongwuhudong_花花2.jpg,upload/chongwuhudong_花花3.jpg','','猫咪蹭裤腿'),(8,'2026-01-05 10:27:29','978750609','全天候寄宿寄养',45,'2026-01-05','奶茶','柯基犬','2026-01-05','005','upload/chongwuhudong_奶茶1.jpg,upload/chongwuhudong_奶茶2.jpg,upload/chongwuhudong_奶茶3.jpg','','小橘猫打盹');
/*!40000 ALTER TABLE `chongwuhudong` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chongwuxinxi`
--

DROP TABLE IF EXISTS `chongwuxinxi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chongwuxinxi` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `chongwuxingming` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '宠物姓名',
  `chongwutupian` longtext COLLATE utf8mb4_unicode_ci COMMENT '宠物图片',
  `pinzhong` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '品种',
  `xingbie` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '性别',
  `chushengriqi` date DEFAULT NULL COMMENT '出生日期',
  `zhanghao` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '账号',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='宠物信息';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chongwuxinxi`
--

LOCK TABLES `chongwuxinxi` WRITE;
/*!40000 ALTER TABLE `chongwuxinxi` DISABLE KEYS */;
INSERT INTO `chongwuxinxi` VALUES (1,'2026-01-05 10:27:29','雪球','upload/chongwuxinxi_雪球1.jpg,upload/chongwuxinxi_雪球2.jpg,upload/chongwuxinxi_雪球3.jpg','垂耳兔','母','2025-06-12','006'),(2,'2026-01-05 10:27:29','团团','upload/chongwuxinxi_团团1.jpg,upload/chongwuxinxi_团团2.jpg,upload/chongwuxinxi_团团3.jpg','侏儒兔','母','2025-10-25','002'),(3,'2026-01-05 10:27:29','可乐','upload/chongwuxinxi_可乐1.jpg,upload/chongwuxinxi_可乐2.jpg,upload/chongwuxinxi_可乐3.jpg','美短猫','母','2025-11-15','004'),(4,'2026-01-05 10:27:29','大黄','upload/chongwuxinxi_大黄1.jpg,upload/chongwuxinxi_大黄2.jpg,upload/chongwuxinxi_大黄3.jpg','金毛寻回犬','母','2025-08-18','001'),(5,'2026-01-05 10:27:29','咪宝','upload/chongwuxinxi_咪宝1.jpg,upload/chongwuxinxi_咪宝2.jpg,upload/chongwuxinxi_咪宝3.jpg','布偶猫','公','2025-09-03','003'),(6,'2026-01-05 10:27:29','虎子','upload/chongwuxinxi_虎子1.jpg,upload/chongwuxinxi_虎子2.jpg,upload/chongwuxinxi_虎子3.jpg','狸花猫','公','2025-04-05','007'),(7,'2026-01-05 10:27:29','花花','upload/chongwuxinxi_花花1.jpg,upload/chongwuxinxi_花花2.jpg,upload/chongwuxinxi_花花3.jpg','加菲猫','公','2025-01-15','008'),(8,'2026-01-05 10:27:29','奶茶','upload/chongwuxinxi_奶茶1.jpg,upload/chongwuxinxi_奶茶2.jpg,upload/chongwuxinxi_奶茶3.jpg','柯基犬','公','2025-11-01','005');
/*!40000 ALTER TABLE `chongwuxinxi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chongwuyongpin`
--

DROP TABLE IF EXISTS `chongwuyongpin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chongwuyongpin` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `shangpinmingcheng` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '商品名称',
  `shangpinfengmian` longtext COLLATE utf8mb4_unicode_ci COMMENT '商品封面',
  `shangpinleixing` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '商品类型',
  `guige` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '规格',
  `pinpai` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '品牌',
  `chandi` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '产地',
  `shangpinjianjie` longtext COLLATE utf8mb4_unicode_ci COMMENT '商品简介',
  `jiage` double DEFAULT NULL COMMENT '价格',
  `kucun` int(11) DEFAULT NULL COMMENT '库存',
  `clicktime` datetime DEFAULT NULL COMMENT '最近点击时间',
  `clicknum` int(11) DEFAULT '0' COMMENT '点击次数',
  `discussnum` int(11) DEFAULT '0' COMMENT '评论数',
  `storeupnum` int(11) DEFAULT '0' COMMENT '收藏数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='宠物用品';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chongwuyongpin`
--

LOCK TABLES `chongwuyongpin` WRITE;
/*!40000 ALTER TABLE `chongwuyongpin` DISABLE KEYS */;
INSERT INTO `chongwuyongpin` VALUES (1,'2026-01-05 10:27:28','幼猫奶糕罐头','upload/chongwuyongpin_幼猫奶糕罐头1.jpg,upload/chongwuyongpin_幼猫奶糕罐头2.jpg,upload/chongwuyongpin_幼猫奶糕罐头3.jpg','幼猫罐头','85g6罐','猫主子','中国','慕斯质地易吞咽',58,29,'2026-01-05 18:27:28',1,0,1),(2,'2026-01-05 10:27:28','老年猫专用粮','upload/chongwuyongpin_老年猫专用粮1.jpg,upload/chongwuyongpin_老年猫专用粮2.jpg,upload/chongwuyongpin_老年猫专用粮3.jpg','老年猫粮','1kg','老猫咪','英国','低卡路里呵护肾脏',53,21,'2026-01-05 18:27:28',2,0,2),(3,'2026-01-05 10:27:28','大型犬专用狗粮','upload/chongwuyongpin_大型犬专用狗粮1.jpg,upload/chongwuyongpin_大型犬专用狗粮2.jpg,upload/chongwuyongpin_大型犬专用狗粮3.jpg','成犬粮','2.5kg','巨无霸','美国','均衡营养促进骨骼发育',37,23,'2026-01-05 18:27:28',3,0,3),(4,'2026-01-05 10:27:28','全价犬用磨牙棒','upload/chongwuyongpin_全价犬用磨牙棒1.jpg,upload/chongwuyongpin_全价犬用磨牙棒2.jpg,upload/chongwuyongpin_全价犬用磨牙棒3.jpg','零食','100g3包','汪汪乐','德国','清洁牙齿预防牙结石',44,27,'2026-01-05 18:27:28',4,0,4),(5,'2026-01-05 10:27:28','全期猫粮','upload/chongwuyongpin_全期猫粮1.jpg,upload/chongwuyongpin_全期猫粮2.jpg,upload/chongwuyongpin_全期猫粮3.jpg','全期粮','1.5kg','全能猫','加拿大','满足各阶段营养需求',55,11,'2026-01-05 18:29:34',7,0,5),(6,'2026-01-05 10:27:28','幼犬益生菌狗粮','upload/chongwuyongpin_幼犬益生菌狗粮1.jpg,upload/chongwuyongpin_幼犬益生菌狗粮2.jpg,upload/chongwuyongpin_幼犬益生菌狗粮3.jpg','功能粮','600g','益生菌世家','中国','调理肠胃促进消化',26,20,'2026-01-05 18:27:28',6,0,6),(7,'2026-01-05 10:27:28','冻干鸡肉猫零食','upload/chongwuyongpin_冻干鸡肉猫零食1.jpg,upload/chongwuyongpin_冻干鸡肉猫零食2.jpg,upload/chongwuyongpin_冻干鸡肉猫零食3.jpg','零食','50g','冻干世家','中国','高蛋白低脂肪增肥发腮',29,2,'2026-01-05 18:27:28',7,0,7),(8,'2026-01-05 10:27:28','小型犬幼犬奶糕','upload/chongwuyongpin_小型犬幼犬奶糕1.jpg,upload/chongwuyongpin_小型犬幼犬奶糕2.jpg,upload/chongwuyongpin_小型犬幼犬奶糕3.jpg','幼犬粮','400g','小不点','中国','小颗粒易咀嚼',46,12,'2026-01-05 18:27:28',8,0,8);
/*!40000 ALTER TABLE `chongwuyongpin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `config`
--

DROP TABLE IF EXISTS `config`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `config` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(100) NOT NULL COMMENT '配置参数名称',
  `value` varchar(200) DEFAULT NULL COMMENT '配置参数值',
  `url` varchar(500) DEFAULT NULL COMMENT 'url',
  `type` int(11) DEFAULT NULL COMMENT '参数类型',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8 COMMENT='配置文件';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `config`
--

LOCK TABLES `config` WRITE;
/*!40000 ALTER TABLE `config` DISABLE KEYS */;
INSERT INTO `config` VALUES (1,'picture1','upload/picture1.jpg',NULL,1),(2,'picture2','upload/picture2.jpg',NULL,1),(3,'picture3','upload/picture3.jpg',NULL,1),(11,'baidu','{\"appId\":\"\",\"apiKey\":\"\",\"secretKey\":\"\"}',NULL,2),(21,'bLoginBackgroundImg','',NULL,3),(22,'bRegisterBackgroundImg','',NULL,3),(23,'bIndexBackgroundImg','',NULL,3),(24,'bTopLogo','',NULL,3),(25,'bHomeLogo','',NULL,3),(26,'fLoginBackgroundImg','',NULL,3),(27,'fRegisterBackgroudImg','',NULL,3),(28,'fTopLogo','',NULL,3);
/*!40000 ALTER TABLE `config` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dianyuan`
--

DROP TABLE IF EXISTS `dianyuan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dianyuan` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `gonghao` varchar(16) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '工号',
  `mima` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '密码',
  `yuangongxingming` varchar(16) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '员工姓名',
  `xingbie` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '性别',
  `lianxifangshi` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '联系方式',
  `touxiang` longtext COLLATE utf8mb4_unicode_ci COMMENT '头像',
  `email` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '邮箱',
  PRIMARY KEY (`id`),
  UNIQUE KEY `gonghao` (`gonghao`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='店员';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dianyuan`
--

LOCK TABLES `dianyuan` WRITE;
/*!40000 ALTER TABLE `dianyuan` DISABLE KEYS */;
INSERT INTO `dianyuan` VALUES (21,'2026-01-05 10:27:28','103','123456','李军','女','13765432109','upload/dianyuan_touxiang1.jpg','773890001@qq.com'),(22,'2026-01-05 10:27:28','104','123456','刘洋','女','13987654321','upload/dianyuan_touxiang2.jpg','773890002@qq.com'),(23,'2026-01-05 10:27:28','105','123456','赵敏','女','13290123456','upload/dianyuan_touxiang3.jpg','773890003@qq.com'),(24,'2026-01-05 10:27:28','102','123456','孙俪','女','13654321098','upload/dianyuan_touxiang4.jpg','773890004@qq.com'),(25,'2026-01-05 10:27:28','106','123456','刘敏','女','15187654321','upload/dianyuan_touxiang5.jpg','773890005@qq.com'),(26,'2026-01-05 10:27:28','108','123456','李娜','女','15012345678','upload/dianyuan_touxiang6.jpg','773890006@qq.com'),(27,'2026-01-05 10:27:28','101','123456','赵芳','女','13012345678','upload/dianyuan_touxiang7.jpg','773890007@qq.com'),(28,'2026-01-05 10:27:28','107','123456','李静','男','15212345678','upload/dianyuan_touxiang8.jpg','773890008@qq.com');
/*!40000 ALTER TABLE `dianyuan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discusschongwufuwu`
--

DROP TABLE IF EXISTS `discusschongwufuwu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `discusschongwufuwu` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `refid` bigint(20) NOT NULL COMMENT '关联表id',
  `userid` bigint(20) NOT NULL COMMENT '用户id',
  `avatarurl` longtext COLLATE utf8mb4_unicode_ci COMMENT '头像',
  `nickname` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '用户名',
  `content` longtext COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '评论内容',
  `reply` longtext COLLATE utf8mb4_unicode_ci COMMENT '回复内容',
  `thumbsupnum` int(11) DEFAULT '0' COMMENT '赞',
  `crazilynum` int(11) DEFAULT '0' COMMENT '踩',
  `istop` int(11) DEFAULT '0' COMMENT '置顶',
  `tuserids` longtext COLLATE utf8mb4_unicode_ci COMMENT '赞用户ids',
  `cuserids` longtext COLLATE utf8mb4_unicode_ci COMMENT '踩用户ids',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='宠物服务评论';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discusschongwufuwu`
--

LOCK TABLES `discusschongwufuwu` WRITE;
/*!40000 ALTER TABLE `discusschongwufuwu` DISABLE KEYS */;
/*!40000 ALTER TABLE `discusschongwufuwu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discusschongwuyongpin`
--

DROP TABLE IF EXISTS `discusschongwuyongpin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `discusschongwuyongpin` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `refid` bigint(20) NOT NULL COMMENT '关联表id',
  `userid` bigint(20) NOT NULL COMMENT '用户id',
  `avatarurl` longtext COLLATE utf8mb4_unicode_ci COMMENT '头像',
  `nickname` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '用户名',
  `content` longtext COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '评论内容',
  `reply` longtext COLLATE utf8mb4_unicode_ci COMMENT '回复内容',
  `thumbsupnum` int(11) DEFAULT '0' COMMENT '赞',
  `crazilynum` int(11) DEFAULT '0' COMMENT '踩',
  `istop` int(11) DEFAULT '0' COMMENT '置顶',
  `tuserids` longtext COLLATE utf8mb4_unicode_ci COMMENT '赞用户ids',
  `cuserids` longtext COLLATE utf8mb4_unicode_ci COMMENT '踩用户ids',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='宠物用品评论';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discusschongwuyongpin`
--

LOCK TABLES `discusschongwuyongpin` WRITE;
/*!40000 ALTER TABLE `discusschongwuyongpin` DISABLE KEYS */;
/*!40000 ALTER TABLE `discusschongwuyongpin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discussjifenlipin`
--

DROP TABLE IF EXISTS `discussjifenlipin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `discussjifenlipin` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `refid` bigint(20) NOT NULL COMMENT '关联表id',
  `userid` bigint(20) NOT NULL COMMENT '用户id',
  `avatarurl` longtext COLLATE utf8mb4_unicode_ci COMMENT '头像',
  `nickname` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '用户名',
  `content` longtext COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '评论内容',
  `reply` longtext COLLATE utf8mb4_unicode_ci COMMENT '回复内容',
  `thumbsupnum` int(11) DEFAULT '0' COMMENT '赞',
  `crazilynum` int(11) DEFAULT '0' COMMENT '踩',
  `istop` int(11) DEFAULT '0' COMMENT '置顶',
  `tuserids` longtext COLLATE utf8mb4_unicode_ci COMMENT '赞用户ids',
  `cuserids` longtext COLLATE utf8mb4_unicode_ci COMMENT '踩用户ids',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='积分礼品评论';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discussjifenlipin`
--

LOCK TABLES `discussjifenlipin` WRITE;
/*!40000 ALTER TABLE `discussjifenlipin` DISABLE KEYS */;
/*!40000 ALTER TABLE `discussjifenlipin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discussjiyangfuwu`
--

DROP TABLE IF EXISTS `discussjiyangfuwu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `discussjiyangfuwu` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `refid` bigint(20) NOT NULL COMMENT '关联表id',
  `userid` bigint(20) NOT NULL COMMENT '用户id',
  `avatarurl` longtext COLLATE utf8mb4_unicode_ci COMMENT '头像',
  `nickname` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '用户名',
  `content` longtext COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '评论内容',
  `reply` longtext COLLATE utf8mb4_unicode_ci COMMENT '回复内容',
  `thumbsupnum` int(11) DEFAULT '0' COMMENT '赞',
  `crazilynum` int(11) DEFAULT '0' COMMENT '踩',
  `istop` int(11) DEFAULT '0' COMMENT '置顶',
  `tuserids` longtext COLLATE utf8mb4_unicode_ci COMMENT '赞用户ids',
  `cuserids` longtext COLLATE utf8mb4_unicode_ci COMMENT '踩用户ids',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='寄养服务评论';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discussjiyangfuwu`
--

LOCK TABLES `discussjiyangfuwu` WRITE;
/*!40000 ALTER TABLE `discussjiyangfuwu` DISABLE KEYS */;
/*!40000 ALTER TABLE `discussjiyangfuwu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discusslingyangchongwu`
--

DROP TABLE IF EXISTS `discusslingyangchongwu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `discusslingyangchongwu` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `refid` bigint(20) NOT NULL COMMENT '关联表id',
  `userid` bigint(20) NOT NULL COMMENT '用户id',
  `avatarurl` longtext COLLATE utf8mb4_unicode_ci COMMENT '头像',
  `nickname` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '用户名',
  `content` longtext COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '评论内容',
  `reply` longtext COLLATE utf8mb4_unicode_ci COMMENT '回复内容',
  `thumbsupnum` int(11) DEFAULT '0' COMMENT '赞',
  `crazilynum` int(11) DEFAULT '0' COMMENT '踩',
  `istop` int(11) DEFAULT '0' COMMENT '置顶',
  `tuserids` longtext COLLATE utf8mb4_unicode_ci COMMENT '赞用户ids',
  `cuserids` longtext COLLATE utf8mb4_unicode_ci COMMENT '踩用户ids',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='领养宠物评论';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discusslingyangchongwu`
--

LOCK TABLES `discusslingyangchongwu` WRITE;
/*!40000 ALTER TABLE `discusslingyangchongwu` DISABLE KEYS */;
/*!40000 ALTER TABLE `discusslingyangchongwu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discusszaishouchongwu`
--

DROP TABLE IF EXISTS `discusszaishouchongwu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `discusszaishouchongwu` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `refid` bigint(20) NOT NULL COMMENT '关联表id',
  `userid` bigint(20) NOT NULL COMMENT '用户id',
  `avatarurl` longtext COLLATE utf8mb4_unicode_ci COMMENT '头像',
  `nickname` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '用户名',
  `content` longtext COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '评论内容',
  `reply` longtext COLLATE utf8mb4_unicode_ci COMMENT '回复内容',
  `thumbsupnum` int(11) DEFAULT '0' COMMENT '赞',
  `crazilynum` int(11) DEFAULT '0' COMMENT '踩',
  `istop` int(11) DEFAULT '0' COMMENT '置顶',
  `tuserids` longtext COLLATE utf8mb4_unicode_ci COMMENT '赞用户ids',
  `cuserids` longtext COLLATE utf8mb4_unicode_ci COMMENT '踩用户ids',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='在售宠物评论';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discusszaishouchongwu`
--

LOCK TABLES `discusszaishouchongwu` WRITE;
/*!40000 ALTER TABLE `discusszaishouchongwu` DISABLE KEYS */;
/*!40000 ALTER TABLE `discusszaishouchongwu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `duihuandingdan`
--

DROP TABLE IF EXISTS `duihuandingdan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `duihuandingdan` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `duihuanbianhao` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '兑换编号',
  `lipinmingcheng` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '礼品名称',
  `lipinfengmian` longtext COLLATE utf8mb4_unicode_ci COMMENT '礼品封面',
  `lipinleixing` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '礼品类型',
  `guige` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '规格',
  `duihuanjifen` double DEFAULT NULL COMMENT '兑换积分',
  `kucun` int(11) NOT NULL COMMENT '兑换数量',
  `jifen` double DEFAULT NULL COMMENT '应付积分',
  `duihuanriqi` date DEFAULT NULL COMMENT '兑换日期',
  `duihuanbeizhu` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '兑换备注',
  `zhanghao` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '账号',
  `xingming` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '姓名',
  `shoujihaoma` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '手机号码',
  `sfsh` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT '待审核' COMMENT '是否审核',
  `shhf` longtext COLLATE utf8mb4_unicode_ci COMMENT '审核回复',
  PRIMARY KEY (`id`),
  UNIQUE KEY `duihuanbianhao` (`duihuanbianhao`)
) ENGINE=InnoDB AUTO_INCREMENT=1767608960380 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='兑换订单';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `duihuandingdan`
--

LOCK TABLES `duihuandingdan` WRITE;
/*!40000 ALTER TABLE `duihuandingdan` DISABLE KEYS */;
INSERT INTO `duihuandingdan` VALUES (1,'2026-01-05 10:27:29','978753428','互动羽毛逗猫棒','upload/duihuandingdan_互动羽毛逗猫棒1.jpg,upload/duihuandingdan_互动羽毛逗猫棒2.jpg,upload/duihuandingdan_互动羽毛逗猫棒3.jpg','逗猫玩具','45cm长',459,58,88,'2026-01-05','无','006','王若曦','13423456789','是',''),(2,'2026-01-05 10:27:29','978702013','咬胶洁齿骨','upload/duihuandingdan_咬胶洁齿骨1.jpg,upload/duihuandingdan_咬胶洁齿骨2.jpg,upload/duihuandingdan_咬胶洁齿骨3.jpg','咬胶','15cm长',476,53,158,'2026-01-05','无','002','孙雨晴','13490123456','是',''),(3,'2026-01-05 10:27:29','978711548','帆布磨牙结绳','upload/duihuandingdan_帆布磨牙结绳1.jpg,upload/duihuandingdan_帆布磨牙结绳2.jpg,upload/duihuandingdan_帆布磨牙结绳3.jpg','结绳玩具','30cm长',318,37,108,'2026-01-05','无','004','周雪','13523456789','是',''),(4,'2026-01-05 10:27:29','978757601','弹力发光球','upload/duihuandingdan_弹力发光球1.jpg,upload/duihuandingdan_弹力发光球2.jpg,upload/duihuandingdan_弹力发光球3.jpg','发光玩具','直径7cm',369,44,88,'2026-01-05','无','001','刘浩然','13578901234','是',''),(5,'2026-01-05 10:27:29','978730129','毛绒安抚熊','upload/duihuandingdan_毛绒安抚熊1.jpg,upload/duihuandingdan_毛绒安抚熊2.jpg,upload/duihuandingdan_毛绒安抚熊3.jpg','安抚玩具','20cm高',189,55,268,'2026-01-05','无','003','高雪','13589012345','是',''),(6,'2026-01-05 10:27:29','978703062','硅胶漏食球','upload/duihuandingdan_硅胶漏食球1.jpg,upload/duihuandingdan_硅胶漏食球2.jpg,upload/duihuandingdan_硅胶漏食球3.jpg','漏食玩具','直径9cm',243,26,68,'2026-01-05','无','007','张明','13467890123','是',''),(7,'2026-01-05 10:27:29','978757020','毛绒squeaker老鼠','upload/duihuandingdan_毛绒squeaker老鼠1.jpg,upload/duihuandingdan_毛绒squeaker老鼠2.jpg,upload/duihuandingdan_毛绒squeaker老鼠3.jpg','发声玩具','15cm长',489,29,35,'2026-01-05','无','008','郭阳','13545678901','是',''),(8,'2026-01-05 10:27:29','978750609','漏食益智骨头','upload/duihuandingdan_漏食益智骨头1.jpg,upload/duihuandingdan_漏食益智骨头2.jpg,upload/duihuandingdan_漏食益智骨头3.jpg','益智玩具','12cm长',412,46,45,'2026-01-05','无','005','王强','13456789012','是',''),(1767608960379,'2026-01-05 10:29:20','1767608959298','毛绒安抚熊','upload/jifenlipin_毛绒安抚熊1.jpg,upload/jifenlipin_毛绒安抚熊2.jpg,upload/jifenlipin_毛绒安抚熊3.jpg','安抚玩具','20cm高',189,1,189,'2026-01-05','无','008','郭阳','13545678901','待审核','');
/*!40000 ALTER TABLE `duihuandingdan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emailregistercode`
--

DROP TABLE IF EXISTS `emailregistercode`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `emailregistercode` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `email` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '邮箱',
  `role` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '角色',
  `code` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '验证码',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='邮箱验证码';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emailregistercode`
--

LOCK TABLES `emailregistercode` WRITE;
/*!40000 ALTER TABLE `emailregistercode` DISABLE KEYS */;
INSERT INTO `emailregistercode` VALUES (1,'2026-01-05 10:27:29','邮箱1','角色1','验证码1'),(2,'2026-01-05 10:27:29','邮箱2','角色2','验证码2'),(3,'2026-01-05 10:27:29','邮箱3','角色3','验证码3'),(4,'2026-01-05 10:27:29','邮箱4','角色4','验证码4'),(5,'2026-01-05 10:27:29','邮箱5','角色5','验证码5'),(6,'2026-01-05 10:27:29','邮箱6','角色6','验证码6'),(7,'2026-01-05 10:27:29','邮箱7','角色7','验证码7'),(8,'2026-01-05 10:27:29','邮箱8','角色8','验证码8');
/*!40000 ALTER TABLE `emailregistercode` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fahuojilu`
--

DROP TABLE IF EXISTS `fahuojilu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fahuojilu` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `dingdanbianhao` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '订单编号',
  `shangpinmingcheng` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '商品名称',
  `shangpinfengmian` longtext COLLATE utf8mb4_unicode_ci COMMENT '商品封面',
  `pinpai` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '品牌',
  `jiage` double DEFAULT NULL COMMENT '价格',
  `kucun` int(11) DEFAULT NULL COMMENT '购买数量',
  `jifen` double DEFAULT NULL COMMENT '应付金额',
  `xiadanriqi` date DEFAULT NULL COMMENT '下单日期',
  `zhanghao` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '账号',
  `xingming` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '姓名',
  `shoujihaoma` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '手机号码',
  `shouhuodizhi` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '收货地址',
  `fahuoriqi` date DEFAULT NULL COMMENT '发货日期',
  `duihuanma` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '兑换码',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1767609025865 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='发货记录';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fahuojilu`
--

LOCK TABLES `fahuojilu` WRITE;
/*!40000 ALTER TABLE `fahuojilu` DISABLE KEYS */;
INSERT INTO `fahuojilu` VALUES (1,'2026-01-05 10:27:29','978753428','幼猫奶糕罐头','upload/fahuojilu_幼猫奶糕罐头1.jpg,upload/fahuojilu_幼猫奶糕罐头2.jpg,upload/fahuojilu_幼猫奶糕罐头3.jpg','猫主子',58,58,88,'2026-01-05','006','王若曦','13423456789','江苏省无锡市梁溪区中山路343号','2026-01-05','RG-LAB-007'),(2,'2026-01-05 10:27:29','978702013','老年猫专用粮','upload/fahuojilu_老年猫专用粮1.jpg,upload/fahuojilu_老年猫专用粮2.jpg,upload/fahuojilu_老年猫专用粮3.jpg','老猫咪',53,53,158,'2026-01-05','002','孙雨晴','13490123456','江西省九江市浔阳区浔阳路2号','2026-01-05','RG-LAB-010'),(3,'2026-01-05 10:27:29','978711548','大型犬专用狗粮','upload/fahuojilu_大型犬专用狗粮1.jpg,upload/fahuojilu_大型犬专用狗粮2.jpg,upload/fahuojilu_大型犬专用狗粮3.jpg','巨无霸',37,37,108,'2026-01-05','004','周雪','13523456789','安徽省安庆市迎江区人民路48号','2026-01-05','RG-LAB-019'),(4,'2026-01-05 10:27:29','978757601','全价犬用磨牙棒','upload/fahuojilu_全价犬用磨牙棒1.jpg,upload/fahuojilu_全价犬用磨牙棒2.jpg,upload/fahuojilu_全价犬用磨牙棒3.jpg','汪汪乐',44,44,88,'2026-01-05','001','刘浩然','13578901234','浙江省温州市鹿城区五马街15号','2026-01-05','RG-LAB-014'),(5,'2026-01-05 10:27:29','978730129','全期猫粮','upload/fahuojilu_全期猫粮1.jpg,upload/fahuojilu_全期猫粮2.jpg,upload/fahuojilu_全期猫粮3.jpg','全能猫',55,55,268,'2026-01-05','003','高雪','13589012345','湖南省株洲市天元区长江北路2号','2026-01-05','RG-LAB-002'),(6,'2026-01-05 10:27:29','978703062','幼犬益生菌狗粮','upload/fahuojilu_幼犬益生菌狗粮1.jpg,upload/fahuojilu_幼犬益生菌狗粮2.jpg,upload/fahuojilu_幼犬益生菌狗粮3.jpg','益生菌世家',26,26,68,'2026-01-05','007','张明','13467890123','宁夏银川市兴庆区解放西街36号','2026-01-05','RG-LAB-005'),(7,'2026-01-05 10:27:29','978757020','冻干鸡肉猫零食','upload/fahuojilu_冻干鸡肉猫零食1.jpg,upload/fahuojilu_冻干鸡肉猫零食2.jpg,upload/fahuojilu_冻干鸡肉猫零食3.jpg','冻干世家',29,29,35,'2026-01-05','008','郭阳','13545678901','内蒙古呼和浩特市新城区新华大街69号','2026-01-05','RG-LAB-016'),(8,'2026-01-05 10:27:29','978750609','小型犬幼犬奶糕','upload/fahuojilu_小型犬幼犬奶糕1.jpg,upload/fahuojilu_小型犬幼犬奶糕2.jpg,upload/fahuojilu_小型犬幼犬奶糕3.jpg','小不点',46,46,45,'2026-01-05','005','王强','13456789012','四川省绵阳市游仙区剑南路东段209号','2026-01-05','RG-LAB-003'),(1767609025864,'2026-01-05 10:30:26','1767608972577','全期猫粮','upload/chongwuyongpin_全期猫粮1.jpg,upload/chongwuyongpin_全期猫粮2.jpg,upload/chongwuyongpin_全期猫粮3.jpg','全能猫',55,2,110,'2026-01-05','008','郭阳','13545678901','内蒙古呼和浩特市新城区新华大街69号','2026-01-05','发货操作1');
/*!40000 ALTER TABLE `fahuojilu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `forum`
--

DROP TABLE IF EXISTS `forum`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `forum` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `title` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '帖子标题',
  `content` longtext COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '帖子内容',
  `parentid` bigint(20) DEFAULT NULL COMMENT '父节点id',
  `username` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '用户名',
  `avatarurl` longtext COLLATE utf8mb4_unicode_ci COMMENT '头像',
  `isdone` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '状态',
  `istop` int(11) DEFAULT '0' COMMENT '是否置顶',
  `toptime` datetime DEFAULT NULL COMMENT '置顶时间',
  `cover` longtext COLLATE utf8mb4_unicode_ci COMMENT '封面',
  `isanon` int(11) DEFAULT '0' COMMENT '是否匿名(1:是,0:否)',
  `delflag` int(11) DEFAULT '0' COMMENT '是否删除(1:是,0:否)',
  `userid` bigint(20) DEFAULT NULL COMMENT '用户id',
  `storeupnum` int(11) DEFAULT '0' COMMENT '收藏数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='宠物论坛';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forum`
--

LOCK TABLES `forum` WRITE;
/*!40000 ALTER TABLE `forum` DISABLE KEYS */;
INSERT INTO `forum` VALUES (1,'2026-01-05 10:27:29','猫咪应激性尿闭','猫咪应激反应可能导致膀胱痉挛、尿道阻塞，表现为频繁蹲猫砂盆却无尿、痛苦嚎叫、腹部紧绷。发现症状需立即送医导尿，日常要保持猫砂盆清洁，搬家/来客时给猫咪准备安静空间，必要时使用猫用安抚喷雾',0,'用户名1','upload/forum_avatarurl1.jpg,upload/forum_avatarurl2.jpg,upload/forum_avatarurl3.jpg','开放',0,'2026-01-05 18:27:29','upload/forum_猫咪应激性尿闭1.jpg,upload/forum_猫咪应激性尿闭2.jpg,upload/forum_猫咪应激性尿闭3.jpg',1,0,1,1),(2,'2026-01-05 10:27:29','狗狗细小病毒感染','细小病毒通过粪便传播，感染后狗狗会出现剧烈呕吐、水样血便、脱水消瘦。未接种疫苗的幼犬死亡率高，确诊后需禁食禁水+静脉补液+抗病毒治疗，日常遛狗避免去脏乱区域，接触陌生狗狗后及时清洁爪子',0,'用户名2','upload/forum_avatarurl2.jpg,upload/forum_avatarurl3.jpg,upload/forum_avatarurl4.jpg','开放',0,'2026-01-05 18:27:29','upload/forum_狗狗细小病毒感染1.jpg,upload/forum_狗狗细小病毒感染2.jpg,upload/forum_狗狗细小病毒感染3.jpg',2,0,2,2),(3,'2026-01-05 10:27:29','狗狗牙周病','症状有牙龈红肿出血、口臭严重、牙齿松动，细菌可能通过血液影响心脏、肾脏。需从幼犬期培养狗狗刷牙习惯，每年做1次口腔检查，发现牙周病及时治疗，避免喂食过软食物，多给磨牙棒清洁牙齿',0,'用户名3','upload/forum_avatarurl3.jpg,upload/forum_avatarurl4.jpg,upload/forum_avatarurl5.jpg','开放',0,'2026-01-05 18:27:29','upload/forum_狗狗牙周病1.jpg,upload/forum_狗狗牙周病2.jpg,upload/forum_狗狗牙周病3.jpg',3,0,3,3),(4,'2026-01-05 10:27:29','猫咪结膜炎','症状表现为眼睛红肿、分泌物增多、频繁眨眼、流泪。日常要定期用棉签擦拭猫咪眼周分泌物，避免猫咪接触灰尘、烟雾等刺激物，若发现眼部异常，及时用宠物专用滴眼液治疗，防止交叉感染',0,'用户名4','upload/forum_avatarurl4.jpg,upload/forum_avatarurl5.jpg,upload/forum_avatarurl6.jpg','开放',0,'2026-01-05 18:27:29','upload/forum_猫咪结膜炎1.jpg,upload/forum_猫咪结膜炎2.jpg,upload/forum_猫咪结膜炎3.jpg',4,0,4,4),(5,'2026-01-05 10:27:29','猫咪糖尿病','患病猫咪会出现多饮多尿、食欲亢进但体重下降、精神萎靡等症状，需终身注射胰岛素。日常要避免给猫咪喂食人类零食、高糖食物，鼓励适度运动，老年猫咪每半年做1次血糖检查',0,'用户名5','upload/forum_avatarurl5.jpg,upload/forum_avatarurl6.jpg,upload/forum_avatarurl7.jpg','开放',0,'2026-01-05 18:27:29','upload/forum_猫咪糖尿病1.jpg,upload/forum_猫咪糖尿病2.jpg,upload/forum_猫咪糖尿病3.jpg',5,0,5,5),(6,'2026-01-05 10:27:29','狗狗皮肤病','常见症状有脱毛、皮屑增多、皮肤红肿、狗狗频繁抓挠。饲养时需每月给狗狗做体内外驱虫，洗澡后彻底吹干毛发，避免在草地、灌木丛等潮湿环境长时间停留，若出现皮肤异常及时做镜检确诊',0,'用户名6','upload/forum_avatarurl6.jpg,upload/forum_avatarurl7.jpg,upload/forum_avatarurl8.jpg','开放',0,'2026-01-05 18:27:29','upload/forum_狗狗皮肤病1.jpg,upload/forum_狗狗皮肤病2.jpg,upload/forum_狗狗皮肤病3.jpg',6,0,6,6),(7,'2026-01-05 10:27:29','狗狗感冒','症状有打喷嚏、流鼻涕、咳嗽、精神不振、体温轻微升高。冬季给狗狗保暖，避免在寒风中停留，洗澡后及时吹干；幼犬、老年犬抵抗力弱，感冒后需及时治疗，防止发展为肺炎，日常避免接触感冒病犬',0,'用户名7','upload/forum_avatarurl7.jpg,upload/forum_avatarurl8.jpg,upload/forum_avatarurl1.jpg','开放',0,'2026-01-05 18:27:29','upload/forum_狗狗感冒1.jpg,upload/forum_狗狗感冒2.jpg,upload/forum_狗狗感冒3.jpg',7,0,7,7),(8,'2026-01-05 10:27:29','宠物犬髋关节发育不良','患病狗狗会出现走路跛行、不愿爬楼梯、起身困难等症状，严重时需手术治疗。饲养金毛、拉布拉多等大型犬时，幼犬期应避免跳跃、长时间奔跑，定期做X光检查，补充软骨素保护关节',0,'用户名8','upload/forum_avatarurl8.jpg,upload/forum_avatarurl1.jpg,upload/forum_avatarurl2.jpg','开放',0,'2026-01-05 18:27:29','upload/forum_宠物犬髋关节发育不良1.jpg,upload/forum_宠物犬髋关节发育不良2.jpg,upload/forum_宠物犬髋关节发育不良3.jpg',8,0,8,8);
/*!40000 ALTER TABLE `forum` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fuwudingdan`
--

DROP TABLE IF EXISTS `fuwudingdan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fuwudingdan` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `dingdanbianhao` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '订单编号',
  `fuwumingcheng` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '服务名称',
  `fuwufengmian` longtext COLLATE utf8mb4_unicode_ci COMMENT '服务封面',
  `fuwuleixing` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '服务类型',
  `jifen` double DEFAULT NULL COMMENT '服务价格',
  `fuwushizhang` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '服务时长',
  `chongwuxingming` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '宠物姓名',
  `pinzhong` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '品种',
  `yuyueriqi` date NOT NULL COMMENT '预约日期',
  `beizhu` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '备注',
  `xiadanshijian` date DEFAULT NULL COMMENT '下单时间',
  `zhanghao` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '账号',
  `xingming` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '姓名',
  `shoujihaoma` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '手机号码',
  `sfsh` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT '待审核' COMMENT '是否审核',
  `shhf` longtext COLLATE utf8mb4_unicode_ci COMMENT '审核回复',
  `ispay` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT '未支付' COMMENT '是否支付',
  PRIMARY KEY (`id`),
  UNIQUE KEY `dingdanbianhao` (`dingdanbianhao`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='服务订单';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fuwudingdan`
--

LOCK TABLES `fuwudingdan` WRITE;
/*!40000 ALTER TABLE `fuwudingdan` DISABLE KEYS */;
INSERT INTO `fuwudingdan` VALUES (1,'2026-01-05 10:27:29','978753428','流浪猫定点喂养服务','upload/fuwudingdan_流浪猫定点喂养服务1.jpg,upload/fuwudingdan_流浪猫定点喂养服务2.jpg,upload/fuwudingdan_流浪猫定点喂养服务3.jpg','公益喂养',58,'1小时','雪球','垂耳兔','2026-01-05','无','2026-01-05','006','王若曦','13423456789','是','','已支付'),(2,'2026-01-05 10:27:29','978702013','宠物犬上门洗护遛护套餐','upload/fuwudingdan_宠物犬上门洗护遛护套餐1.jpg,upload/fuwudingdan_宠物犬上门洗护遛护套餐2.jpg,upload/fuwudingdan_宠物犬上门洗护遛护套餐3.jpg','洗护遛护',188,'3小时','团团','侏儒兔','2026-01-05','无','2026-01-05','002','孙雨晴','13490123456','是','','已支付'),(3,'2026-01-05 10:27:29','978711548','日常萌宠喂养遛护服务','upload/fuwudingdan_日常萌宠喂养遛护服务1.jpg,upload/fuwudingdan_日常萌宠喂养遛护服务2.jpg,upload/fuwudingdan_日常萌宠喂养遛护服务3.jpg','喂养遛护',88,'1小时','可乐','美短猫','2026-01-05','无','2026-01-05','004','周雪','13523456789','是','','已支付'),(4,'2026-01-05 10:27:29','978757601','护卫犬上门喂养训练服务','upload/fuwudingdan_护卫犬上门喂养训练服务1.jpg,upload/fuwudingdan_护卫犬上门喂养训练服务2.jpg,upload/fuwudingdan_护卫犬上门喂养训练服务3.jpg','喂养训练',228,'3小时','大黄','金毛寻回犬','2026-01-05','无','2026-01-05','001','刘浩然','13578901234','是','','已支付'),(5,'2026-01-05 10:27:29','978730129','异宠上门照料服务','upload/fuwudingdan_异宠上门照料服务1.jpg,upload/fuwudingdan_异宠上门照料服务2.jpg,upload/fuwudingdan_异宠上门照料服务3.jpg','异宠护理',138,'1.5小时','咪宝','布偶猫','2026-01-05','无','2026-01-05','003','高雪','13589012345','是','','已支付'),(6,'2026-01-05 10:27:29','978703062','赛级犬上门养护服务','upload/fuwudingdan_赛级犬上门养护服务1.jpg,upload/fuwudingdan_赛级犬上门养护服务2.jpg,upload/fuwudingdan_赛级犬上门养护服务3.jpg','赛级养护',198,'3小时','虎子','狸花猫','2026-01-05','无','2026-01-05','007','张明','13467890123','是','','已支付'),(7,'2026-01-05 10:27:29','978757020','幼猫专属喂养照料服务','upload/fuwudingdan_幼猫专属喂养照料服务1.jpg,upload/fuwudingdan_幼猫专属喂养照料服务2.jpg,upload/fuwudingdan_幼猫专属喂养照料服务3.jpg','幼猫护理',108,'2小时','花花','加菲猫','2026-01-05','无','2026-01-05','008','郭阳','13545678901','是','','已支付'),(8,'2026-01-05 10:27:29','978750609','宠物猫上门洗护喂养套餐','upload/fuwudingdan_宠物猫上门洗护喂养套餐1.jpg,upload/fuwudingdan_宠物猫上门洗护喂养套餐2.jpg,upload/fuwudingdan_宠物猫上门洗护喂养套餐3.jpg','洗护喂养',168,'2.5小时','奶茶','柯基犬','2026-01-05','无','2026-01-05','005','王强','13456789012','是','','已支付');
/*!40000 ALTER TABLE `fuwudingdan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jiankangshuju`
--

DROP TABLE IF EXISTS `jiankangshuju`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jiankangshuju` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `jilubianhao` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '记录编号',
  `chongwuxingming` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '宠物姓名',
  `chongwutupian` longtext COLLATE utf8mb4_unicode_ci COMMENT '宠物图片',
  `pinzhong` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '品种',
  `xingbie` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '性别',
  `zhanghao` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '账号',
  `shengao` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '身高cm',
  `tizhong` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '体重kg',
  `tiwen` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '体温℃',
  `shenghuoxiguan` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '生活习惯',
  `yinshipianhao` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '饮食偏好',
  `jiankangyuce` longtext COLLATE utf8mb4_unicode_ci COMMENT '健康预测',
  PRIMARY KEY (`id`),
  UNIQUE KEY `jilubianhao` (`jilubianhao`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='健康数据';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jiankangshuju`
--

LOCK TABLES `jiankangshuju` WRITE;
/*!40000 ALTER TABLE `jiankangshuju` DISABLE KEYS */;
INSERT INTO `jiankangshuju` VALUES (1,'2026-01-05 10:27:29','978753428','雪球','upload/jiankangshuju_雪球1.jpg,upload/jiankangshuju_雪球2.jpg,upload/jiankangshuju_雪球3.jpg','垂耳兔','母','006','25','0.3','38.0','白天活动喜欢跳跃夜间回巢休息','松子核桃榛子偶尔喂水果和蔬菜','健康预测1'),(2,'2026-01-05 10:27:29','978702013','团团','upload/jiankangshuju_团团1.jpg,upload/jiankangshuju_团团2.jpg,upload/jiankangshuju_团团3.jpg','侏儒兔','母','002','40','12','38.4','每天需要遛弯喜欢追球爱和其他狗狗玩耍','天然粮爱吃红薯偶尔喂冻干蛋黄','健康预测2'),(3,'2026-01-05 10:27:29','978711548','可乐','upload/jiankangshuju_可乐1.jpg,upload/jiankangshuju_可乐2.jpg,upload/jiankangshuju_可乐3.jpg','美短猫','母','004','30','4.5','38.3','白天睡觉夜间活跃喜欢独处','无谷猫粮爱吃金枪鱼偶尔喂猫条','健康预测3'),(4,'2026-01-05 10:27:29','978757601','大黄','upload/jiankangshuju_大黄1.jpg,upload/jiankangshuju_大黄2.jpg,upload/jiankangshuju_大黄3.jpg','金毛寻回犬','母','001','30','3.0','38.1','白天吃草晚上活动爱舔毛梳理','提摩西草苜蓿草兔粮少量胡萝卜','健康预测4'),(5,'2026-01-05 10:27:29','978730129','咪宝','upload/jiankangshuju_咪宝1.jpg,upload/jiankangshuju_咪宝2.jpg,upload/jiankangshuju_咪宝3.jpg','布偶猫','公','003','25','2.5','38.0','白天活动喜欢跳跃爱舔毛清洁身体','苜蓿草提摩西草专用兔粮少量苹果片','健康预测5'),(6,'2026-01-05 10:27:29','978703062','虎子','upload/jiankangshuju_虎子1.jpg,upload/jiankangshuju_虎子2.jpg,upload/jiankangshuju_虎子3.jpg','狸花猫','公','007','70','35','38.6','每天需要大量运动喜欢训练护院意识强','高蛋白狗粮爱吃牛肉偶尔啃牛骨','健康预测6'),(7,'2026-01-05 10:27:29','978757020','花花','upload/jiankangshuju_花花1.jpg,upload/jiankangshuju_花花2.jpg,upload/jiankangshuju_花花3.jpg','加菲猫','公','008','20','0.6','28.5','白天晒背夏季活跃冬季冬眠','龟粮小鱼干小虾干偶尔喂蔬菜','健康预测7'),(8,'2026-01-05 10:27:29','978750609','奶茶','upload/jiankangshuju_奶茶1.jpg,upload/jiankangshuju_奶茶2.jpg,upload/jiankangshuju_奶茶3.jpg','柯基犬','公','005','20','0.04','40.8','清晨鸣叫喜欢梳理羽毛爱站在高处','谷子稗子黍子偶尔喂蛋黄米和蔬菜','健康预测8');
/*!40000 ALTER TABLE `jiankangshuju` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jifenlipin`
--

DROP TABLE IF EXISTS `jifenlipin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jifenlipin` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `lipinmingcheng` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '礼品名称',
  `lipinfengmian` longtext COLLATE utf8mb4_unicode_ci COMMENT '礼品封面',
  `lipinleixing` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '礼品类型',
  `guige` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '规格',
  `lipinjianjie` longtext COLLATE utf8mb4_unicode_ci COMMENT '礼品简介',
  `duihuanjifen` double DEFAULT NULL COMMENT '兑换积分',
  `kucun` int(11) DEFAULT NULL COMMENT '库存',
  `discussnum` int(11) DEFAULT '0' COMMENT '评论数',
  `storeupnum` int(11) DEFAULT '0' COMMENT '收藏数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='积分礼品';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jifenlipin`
--

LOCK TABLES `jifenlipin` WRITE;
/*!40000 ALTER TABLE `jifenlipin` DISABLE KEYS */;
INSERT INTO `jifenlipin` VALUES (1,'2026-01-05 10:27:29','互动羽毛逗猫棒','upload/jifenlipin_互动羽毛逗猫棒1.jpg,upload/jifenlipin_互动羽毛逗猫棒2.jpg,upload/jifenlipin_互动羽毛逗猫棒3.jpg','逗猫玩具','45cm长','激发猫咪捕猎本能',459,58,0,1),(2,'2026-01-05 10:27:29','咬胶洁齿骨','upload/jifenlipin_咬胶洁齿骨1.jpg,upload/jifenlipin_咬胶洁齿骨2.jpg,upload/jifenlipin_咬胶洁齿骨3.jpg','咬胶','15cm长','去除牙菌斑清新口气',476,53,0,2),(3,'2026-01-05 10:27:29','帆布磨牙结绳','upload/jifenlipin_帆布磨牙结绳1.jpg,upload/jifenlipin_帆布磨牙结绳2.jpg,upload/jifenlipin_帆布磨牙结绳3.jpg','结绳玩具','30cm长','清洁牙齿按摩牙龈',318,37,0,3),(4,'2026-01-05 10:27:29','弹力发光球','upload/jifenlipin_弹力发光球1.jpg,upload/jifenlipin_弹力发光球2.jpg,upload/jifenlipin_弹力发光球3.jpg','发光玩具','直径7cm','夜间互动安全可视',369,44,0,4),(5,'2026-01-05 10:27:29','毛绒安抚熊','upload/jifenlipin_毛绒安抚熊1.jpg,upload/jifenlipin_毛绒安抚熊2.jpg,upload/jifenlipin_毛绒安抚熊3.jpg','安抚玩具','20cm高','缓解分离焦虑',189,55,0,5),(6,'2026-01-05 10:27:29','硅胶漏食球','upload/jifenlipin_硅胶漏食球1.jpg,upload/jifenlipin_硅胶漏食球2.jpg,upload/jifenlipin_硅胶漏食球3.jpg','漏食玩具','直径9cm','延长进食时间减少肥胖',243,26,0,6),(7,'2026-01-05 10:27:29','毛绒squeaker老鼠','upload/jifenlipin_毛绒squeaker老鼠1.jpg,upload/jifenlipin_毛绒squeaker老鼠2.jpg,upload/jifenlipin_毛绒squeaker老鼠3.jpg','发声玩具','15cm长','激发捕猎欲望',489,29,0,7),(8,'2026-01-05 10:27:29','漏食益智骨头','upload/jifenlipin_漏食益智骨头1.jpg,upload/jifenlipin_漏食益智骨头2.jpg,upload/jifenlipin_漏食益智骨头3.jpg','益智玩具','12cm长','延缓进食预防肥胖',412,46,0,8);
/*!40000 ALTER TABLE `jifenlipin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jiyangdingdan`
--

DROP TABLE IF EXISTS `jiyangdingdan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jiyangdingdan` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `dingdanbianhao` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '订单编号',
  `fuwumingcheng` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '服务名称',
  `fuwufengmian` longtext COLLATE utf8mb4_unicode_ci COMMENT '服务封面',
  `fuwuleixing` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '服务类型',
  `jifen` double DEFAULT NULL COMMENT '价格',
  `jiyangriqi` date NOT NULL COMMENT '寄养日期',
  `chongwuxingming` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '宠物姓名',
  `pinzhong` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '品种',
  `beizhu` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '备注',
  `xiadanshijian` date DEFAULT NULL COMMENT '下单时间',
  `zhanghao` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '账号',
  `xingming` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '姓名',
  `shoujihaoma` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '手机号码',
  `sfsh` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT '待审核' COMMENT '是否审核',
  `shhf` longtext COLLATE utf8mb4_unicode_ci COMMENT '审核回复',
  `ispay` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT '未支付' COMMENT '是否支付',
  PRIMARY KEY (`id`),
  UNIQUE KEY `dingdanbianhao` (`dingdanbianhao`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='寄养订单';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jiyangdingdan`
--

LOCK TABLES `jiyangdingdan` WRITE;
/*!40000 ALTER TABLE `jiyangdingdan` DISABLE KEYS */;
INSERT INTO `jiyangdingdan` VALUES (1,'2026-01-05 10:27:29','978753428','小型犬短期寄养','upload/jiyangdingdan_小型犬短期寄养1.jpg,upload/jiyangdingdan_小型犬短期寄养2.jpg,upload/jiyangdingdan_小型犬短期寄养3.jpg','短期寄养',88,'2026-01-05','雪球','垂耳兔','无','2026-01-05','006','王若曦','13423456789','是','','已支付'),(2,'2026-01-05 10:27:29','978702013','老年宠养护寄养','upload/jiyangdingdan_老年宠养护寄养1.jpg,upload/jiyangdingdan_老年宠养护寄养2.jpg,upload/jiyangdingdan_老年宠养护寄养3.jpg','养护寄养',158,'2026-01-05','团团','侏儒兔','无','2026-01-05','002','孙雨晴','13490123456','是','','已支付'),(3,'2026-01-05 10:27:29','978711548','结伴寄养服务','upload/jiyangdingdan_结伴寄养服务1.jpg,upload/jiyangdingdan_结伴寄养服务2.jpg,upload/jiyangdingdan_结伴寄养服务3.jpg','结伴寄养',108,'2026-01-05','可乐','美短猫','无','2026-01-05','004','周雪','13523456789','是','','已支付'),(4,'2026-01-05 10:27:29','978757601','驱虫防护寄养','upload/jiyangdingdan_驱虫防护寄养1.jpg,upload/jiyangdingdan_驱虫防护寄养2.jpg,upload/jiyangdingdan_驱虫防护寄养3.jpg','防护寄养',88,'2026-01-05','大黄','金毛寻回犬','无','2026-01-05','001','刘浩然','13578901234','是','','已支付'),(5,'2026-01-05 10:27:29','978730129','宠物度假寄养','upload/jiyangdingdan_宠物度假寄养1.jpg,upload/jiyangdingdan_宠物度假寄养2.jpg,upload/jiyangdingdan_宠物度假寄养3.jpg','度假寄养',268,'2026-01-05','咪宝','布偶猫','无','2026-01-05','003','高雪','13589012345','是','','已支付'),(6,'2026-01-05 10:27:29','978703062','异宠基础寄养','upload/jiyangdingdan_异宠基础寄养1.jpg,upload/jiyangdingdan_异宠基础寄养2.jpg,upload/jiyangdingdan_异宠基础寄养3.jpg','异宠寄养',68,'2026-01-05','虎子','狸花猫','无','2026-01-05','007','张明','13467890123','是','','已支付'),(7,'2026-01-05 10:27:29','978757020','基础单宠日托','upload/jiyangdingdan_基础单宠日托1.jpg,upload/jiyangdingdan_基础单宠日托2.jpg,upload/jiyangdingdan_基础单宠日托3.jpg','日托寄养',35,'2026-01-05','花花','加菲猫','无','2026-01-05','008','郭阳','13545678901','是','','已支付'),(8,'2026-01-05 10:27:29','978750609','全天候寄宿寄养','upload/jiyangdingdan_全天候寄宿寄养1.jpg,upload/jiyangdingdan_全天候寄宿寄养2.jpg,upload/jiyangdingdan_全天候寄宿寄养3.jpg','全天寄养',45,'2026-01-05','奶茶','柯基犬','无','2026-01-05','005','王强','13456789012','是','','已支付');
/*!40000 ALTER TABLE `jiyangdingdan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jiyangfuwu`
--

DROP TABLE IF EXISTS `jiyangfuwu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jiyangfuwu` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `fuwumingcheng` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '服务名称',
  `fuwufengmian` longtext COLLATE utf8mb4_unicode_ci COMMENT '服务封面',
  `fuwuleixing` varchar(16) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '服务类型',
  `chongwuleixing` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '宠物类型',
  `baohanxiangmu` longtext COLLATE utf8mb4_unicode_ci COMMENT '包含项目',
  `jifen` double DEFAULT NULL COMMENT '价格',
  `xiangqing` longtext COLLATE utf8mb4_unicode_ci COMMENT '详情',
  `discussnum` int(11) DEFAULT '0' COMMENT '评论数',
  `storeupnum` int(11) DEFAULT '0' COMMENT '收藏数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='寄养服务';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jiyangfuwu`
--

LOCK TABLES `jiyangfuwu` WRITE;
/*!40000 ALTER TABLE `jiyangfuwu` DISABLE KEYS */;
INSERT INTO `jiyangfuwu` VALUES (1,'2026-01-05 10:27:28','小型犬短期寄养','upload/jiyangfuwu_小型犬短期寄养1.jpg,upload/jiyangfuwu_小型犬短期寄养2.jpg,upload/jiyangfuwu_小型犬短期寄养3.jpg','短期寄养','小型犬','三餐投喂早晚遛弯毛发梳理',88,'每日清洁笼舍记录排便情况',0,1),(2,'2026-01-05 10:27:28','老年宠养护寄养','upload/jiyangfuwu_老年宠养护寄养1.jpg,upload/jiyangfuwu_老年宠养护寄养2.jpg,upload/jiyangfuwu_老年宠养护寄养3.jpg','养护寄养','老年犬猫','软粮投喂关节护理定时喂药',158,'专人24小时待命应对突发状况',0,2),(3,'2026-01-05 10:27:28','结伴寄养服务','upload/jiyangfuwu_结伴寄养服务1.jpg,upload/jiyangfuwu_结伴寄养服务2.jpg,upload/jiyangfuwu_结伴寄养服务3.jpg','结伴寄养','同主多宠','分宠投喂集体遛弯同步互动',108,'专人统筹避免宠物争抢',0,3),(4,'2026-01-05 10:27:28','驱虫防护寄养','upload/jiyangfuwu_驱虫防护寄养1.jpg,upload/jiyangfuwu_驱虫防护寄养2.jpg,upload/jiyangfuwu_驱虫防护寄养3.jpg','防护寄养','犬猫','基础驱虫定量投喂环境消杀',88,'入舍前全面驱虫保障环境安全',0,4),(5,'2026-01-05 10:27:28','宠物度假寄养','upload/jiyangfuwu_宠物度假寄养1.jpg,upload/jiyangfuwu_宠物度假寄养2.jpg,upload/jiyangfuwu_宠物度假寄养3.jpg','度假寄养','犬猫','豪华餐投喂泳池玩耍摄影留念',268,'每日制作度假相册反馈状态',0,5),(6,'2026-01-05 10:27:28','异宠基础寄养','upload/jiyangfuwu_异宠基础寄养1.jpg,upload/jiyangfuwu_异宠基础寄养2.jpg,upload/jiyangfuwu_异宠基础寄养3.jpg','异宠寄养','仓鼠龙猫','定时投食垫材更换环境控温',68,'每日监测温湿度记录进食量',0,6),(7,'2026-01-05 10:27:28','基础单宠日托','upload/jiyangfuwu_基础单宠日托1.jpg,upload/jiyangfuwu_基础单宠日托2.jpg,upload/jiyangfuwu_基础单宠日托3.jpg','日托寄养','犬类','基础喂食定时遛弯基础清洁',35,'每日提供活动视频基础健康记录',0,7),(8,'2026-01-05 10:27:28','全天候寄宿寄养','upload/jiyangfuwu_全天候寄宿寄养1.jpg,upload/jiyangfuwu_全天候寄宿寄养2.jpg,upload/jiyangfuwu_全天候寄宿寄养3.jpg','全天寄养','犬猫','24小时看护无限量饮水随时互动',45,'支持远程查看宠物实时状态',0,8);
/*!40000 ALTER TABLE `jiyangfuwu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lingyangchongwu`
--

DROP TABLE IF EXISTS `lingyangchongwu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lingyangchongwu` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `chongwunicheng` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '宠物昵称',
  `chongwupinzhong` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '宠物品种',
  `chongwutupian` longtext COLLATE utf8mb4_unicode_ci COMMENT '宠物图片',
  `xingbie` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '性别',
  `chushengriqi` date DEFAULT NULL COMMENT '出生日期',
  `xinggetedian` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '性格特点',
  `yimiaojilu` longtext COLLATE utf8mb4_unicode_ci COMMENT '疫苗记录',
  `lingyangzhuangtai` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '领养状态',
  `discussnum` int(11) DEFAULT '0' COMMENT '评论数',
  `storeupnum` int(11) DEFAULT '0' COMMENT '收藏数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='领养宠物';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lingyangchongwu`
--

LOCK TABLES `lingyangchongwu` WRITE;
/*!40000 ALTER TABLE `lingyangchongwu` DISABLE KEYS */;
INSERT INTO `lingyangchongwu` VALUES (1,'2026-01-05 10:27:29','小白','波斯猫','upload/lingyangchongwu_小白1.jpg,upload/lingyangchongwu_小白2.jpg,upload/lingyangchongwu_小白3.jpg','母','2025-06-12','优雅安静','猫三联','待领养',0,1),(2,'2026-01-05 10:27:29','大黑','拉布拉多','upload/lingyangchongwu_大黑1.jpg,upload/lingyangchongwu_大黑2.jpg,upload/lingyangchongwu_大黑3.jpg','公','2025-10-25','温顺稳重','犬四联狂犬','已领养',0,2),(3,'2026-01-05 10:27:29','贝贝','加菲猫','upload/lingyangchongwu_贝贝1.jpg,upload/lingyangchongwu_贝贝2.jpg,upload/lingyangchongwu_贝贝3.jpg','公','2025-11-15','温顺安静','猫三联狂犬','待领养',0,3),(4,'2026-01-05 10:27:29','元宝','金毛犬','upload/lingyangchongwu_元宝1.jpg,upload/lingyangchongwu_元宝2.jpg,upload/lingyangchongwu_元宝3.jpg','母','2025-08-18','活泼好动','犬四联','已领养',0,4),(5,'2026-01-05 10:27:29','灰灰','蓝猫','upload/lingyangchongwu_灰灰1.jpg,upload/lingyangchongwu_灰灰2.jpg,upload/lingyangchongwu_灰灰3.jpg','公','2025-09-03','慵懒嗜睡','猫三联','待领养',0,5),(6,'2026-01-05 10:27:29','来福','中华田园犬','upload/lingyangchongwu_来福1.jpg,upload/lingyangchongwu_来福2.jpg,upload/lingyangchongwu_来福3.jpg','公','2025-04-05','忠诚护主','犬四联','待领养',0,6),(7,'2026-01-05 10:27:29','布丁','银渐层','upload/lingyangchongwu_布丁1.jpg,upload/lingyangchongwu_布丁2.jpg,upload/lingyangchongwu_布丁3.jpg','母','2025-01-15','粘人亲人','猫三联狂犬','待领养',0,7),(8,'2026-01-05 10:27:29','糯米','布偶猫','upload/lingyangchongwu_糯米1.jpg,upload/lingyangchongwu_糯米2.jpg,upload/lingyangchongwu_糯米3.jpg','公','2025-11-01','温顺粘人','猫三联','待领养',0,8);
/*!40000 ALTER TABLE `lingyangchongwu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lingyangshenqing`
--

DROP TABLE IF EXISTS `lingyangshenqing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lingyangshenqing` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `shenqingbianhao` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '申请编号',
  `chongwunicheng` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '宠物昵称',
  `chongwupinzhong` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '宠物品种',
  `chongwutupian` longtext COLLATE utf8mb4_unicode_ci COMMENT '宠物图片',
  `xingbie` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '性别',
  `xinggetedian` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '性格特点',
  `shenqingriqi` date DEFAULT NULL COMMENT '申请日期',
  `lingyangshuoming` longtext COLLATE utf8mb4_unicode_ci COMMENT '领养说明',
  `zhanghao` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '账号',
  `xingming` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '姓名',
  `shoujihaoma` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '手机号码',
  `sfsh` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT '待审核' COMMENT '是否审核',
  `shhf` longtext COLLATE utf8mb4_unicode_ci COMMENT '审核回复',
  PRIMARY KEY (`id`),
  UNIQUE KEY `shenqingbianhao` (`shenqingbianhao`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='领养申请';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lingyangshenqing`
--

LOCK TABLES `lingyangshenqing` WRITE;
/*!40000 ALTER TABLE `lingyangshenqing` DISABLE KEYS */;
INSERT INTO `lingyangshenqing` VALUES (1,'2026-01-05 10:27:29','978753428','小白','波斯猫','upload/lingyangshenqing_小白1.jpg,upload/lingyangshenqing_小白2.jpg,upload/lingyangshenqing_小白3.jpg','母','优雅安静','2026-01-05','我承诺终身饲养宠物绝不中途遗弃','006','王若曦','13423456789','是',''),(2,'2026-01-05 10:27:29','978702013','大黑','拉布拉多','upload/lingyangshenqing_大黑1.jpg,upload/lingyangshenqing_大黑2.jpg,upload/lingyangshenqing_大黑3.jpg','公','温顺稳重','2026-01-05','我将严格遵守领养协议所有约定条款','002','孙雨晴','13490123456','是',''),(3,'2026-01-05 10:27:29','978711548','贝贝','加菲猫','upload/lingyangshenqing_贝贝1.jpg,upload/lingyangshenqing_贝贝2.jpg,upload/lingyangshenqing_贝贝3.jpg','公','温顺安静','2026-01-05','我将科学喂养不投喂有害食物不随意换粮','004','周雪','13523456789','是',''),(4,'2026-01-05 10:27:29','978757601','元宝','金毛犬','upload/lingyangshenqing_元宝1.jpg,upload/lingyangshenqing_元宝2.jpg,upload/lingyangshenqing_元宝3.jpg','母','活泼好动','2026-01-05','我不会因搬家、结婚、生子等原因弃养','001','刘浩然','13578901234','是',''),(5,'2026-01-05 10:27:29','978730129','灰灰','蓝猫','upload/lingyangshenqing_灰灰1.jpg,upload/lingyangshenqing_灰灰2.jpg,upload/lingyangshenqing_灰灰3.jpg','公','慵懒嗜睡','2026-01-05','我每日有充足时间陪伴宠物互动照料','003','高雪','13589012345','是',''),(6,'2026-01-05 10:27:29','978703062','来福','中华田园犬','upload/lingyangshenqing_来福1.jpg,upload/lingyangshenqing_来福2.jpg,upload/lingyangshenqing_来福3.jpg','公','忠诚护主','2026-01-05','我愿意主动学习宠物护理知识提升照料能力','007','张明','13467890123','是',''),(7,'2026-01-05 10:27:29','978757020','布丁','银渐层','upload/lingyangshenqing_布丁1.jpg,upload/lingyangshenqing_布丁2.jpg,upload/lingyangshenqing_布丁3.jpg','母','粘人亲人','2026-01-05','我接受宠物现有健康状况并承担后续医疗责任','008','郭阳','13545678901','是',''),(8,'2026-01-05 10:27:29','978750609','糯米','布偶猫','upload/lingyangshenqing_糯米1.jpg,upload/lingyangshenqing_糯米2.jpg,upload/lingyangshenqing_糯米3.jpg','公','温顺粘人','2026-01-05','我接受救助机构定期回访并如实反馈情况','005','王强','13456789012','是','');
/*!40000 ALTER TABLE `lingyangshenqing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news`
--

DROP TABLE IF EXISTS `news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `news` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `title` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '标题',
  `introduction` longtext COLLATE utf8mb4_unicode_ci COMMENT '简介',
  `picture` longtext COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '图片',
  `content` longtext COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '内容',
  `name` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '发布人',
  `headportrait` longtext COLLATE utf8mb4_unicode_ci COMMENT '头像',
  `storeupnum` int(11) DEFAULT '0' COMMENT '收藏数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='公告信息';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news`
--

LOCK TABLES `news` WRITE;
/*!40000 ALTER TABLE `news` DISABLE KEYS */;
INSERT INTO `news` VALUES (1,'2026-01-05 10:27:29','鹦鹉语言训练技巧','鹦鹉说话训练教程','upload/news_picture1.jpg','从基础发音引导到简单词汇教学，介绍鹦鹉训练的最佳时间、奖励方式和常见问题解决方案','鸟类饲养专家阿琳','upload/news_headportrait1.jpg',1),(2,'2026-01-05 10:27:29','萌系仓鼠habitat搭建','仓鼠居住环境布置方案','upload/news_picture2.jpg','讲解仓鼠笼子选择、垫料铺设、玩具搭配要点，推荐适合不同体型仓鼠的habitat组合','仓鼠爱好者小桃','upload/news_headportrait2.jpg',2),(3,'2026-01-05 10:27:29','老年金毛养护要点','老年金毛犬健康管理','upload/news_picture3.jpg','分享老年金毛的饮食调理（低钠低脂配方）、关节保护方法和定期体检项目，助力老年犬安度晚年','兽医老李','upload/news_headportrait3.jpg',3),(4,'2026-01-05 10:27:29','猫咪口腔护理实用技巧','猫咪牙齿清洁方法','upload/news_picture4.jpg','介绍猫咪口腔问题的危害，分享牙刷、漱口水等清洁工具的使用方式，以及预防牙结石的饮食建议','宠物牙医小敏','upload/news_headportrait4.jpg',4),(5,'2026-01-05 10:27:29','可爱布偶猫饲养指南','布偶猫喂养护理技巧','upload/news_picture5.jpg','详细介绍布偶猫的饮食搭配、毛发护理、健康监测方法，包括日常喂食频率、梳毛工具选择和常见疾病预防','宠物达人阿泽','upload/news_headportrait5.jpg',5),(6,'2026-01-05 10:27:29','鬃狮蜥饲养环境搭建','鬃狮蜥habitat布置','upload/news_picture6.jpg','讲解鬃狮蜥饲养箱尺寸选择、温度湿度控制、垫材和躲避屋搭配，推荐适合新手的设备清单','爬行宠物达人老周','upload/news_headportrait6.jpg',6),(7,'2026-01-05 10:27:29','猫咪应激反应应对策略','猫咪应激处理方法','upload/news_picture7.jpg','详解猫咪应激的常见诱因、表现症状，提供环境调整、情绪安抚和药物干预的具体方案','宠物行为咨询师阿雅','upload/news_headportrait7.jpg',7),(8,'2026-01-05 10:27:29','柯基犬髋关节养护指南','柯基犬关节健康管理','upload/news_picture8.jpg','针对柯基犬易患髋关节问题的特点，提供运动控制、营养补充（软骨素、钙）和定期检查的方案','犬类养护专家老杨','upload/news_headportrait8.jpg',8);
/*!40000 ALTER TABLE `news` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shangpindingdan`
--

DROP TABLE IF EXISTS `shangpindingdan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shangpindingdan` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `dingdanbianhao` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '订单编号',
  `shangpinmingcheng` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '商品名称',
  `shangpinfengmian` longtext COLLATE utf8mb4_unicode_ci COMMENT '商品封面',
  `shangpinleixing` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '商品类型',
  `guige` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '规格',
  `pinpai` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '品牌',
  `chandi` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '产地',
  `jiage` double DEFAULT NULL COMMENT '价格',
  `kucun` int(11) NOT NULL COMMENT '购买数量',
  `jifen` double DEFAULT NULL COMMENT '应付金额',
  `xiadanriqi` date DEFAULT NULL COMMENT '下单日期',
  `zhanghao` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '账号',
  `xingming` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '姓名',
  `shoujihaoma` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '手机号码',
  `shouhuodizhi` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '收货地址',
  `fahuozhuangtai` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '发货状态',
  `sfsh` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT '待审核' COMMENT '是否审核',
  `shhf` longtext COLLATE utf8mb4_unicode_ci COMMENT '审核回复',
  `ispay` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT '未支付' COMMENT '是否支付',
  PRIMARY KEY (`id`),
  UNIQUE KEY `dingdanbianhao` (`dingdanbianhao`)
) ENGINE=InnoDB AUTO_INCREMENT=1767608974163 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='商品订单';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shangpindingdan`
--

LOCK TABLES `shangpindingdan` WRITE;
/*!40000 ALTER TABLE `shangpindingdan` DISABLE KEYS */;
INSERT INTO `shangpindingdan` VALUES (1,'2026-01-05 10:27:29','978753428','幼猫奶糕罐头','upload/shangpindingdan_幼猫奶糕罐头1.jpg,upload/shangpindingdan_幼猫奶糕罐头2.jpg,upload/shangpindingdan_幼猫奶糕罐头3.jpg','幼猫罐头','45cm长','猫主子','中国',58,58,1,'2026-01-05','006','王若曦','13423456789','江苏省无锡市梁溪区中山路343号','已发货','是','','已支付'),(2,'2026-01-05 10:27:29','978702013','老年猫专用粮','upload/shangpindingdan_老年猫专用粮1.jpg,upload/shangpindingdan_老年猫专用粮2.jpg,upload/shangpindingdan_老年猫专用粮3.jpg','老年猫粮','15cm长','老猫咪','英国',53,53,2,'2026-01-05','002','孙雨晴','13490123456','江西省九江市浔阳区浔阳路2号','已发货','是','','已支付'),(3,'2026-01-05 10:27:29','978711548','大型犬专用狗粮','upload/shangpindingdan_大型犬专用狗粮1.jpg,upload/shangpindingdan_大型犬专用狗粮2.jpg,upload/shangpindingdan_大型犬专用狗粮3.jpg','成犬粮','30cm长','巨无霸','美国',37,37,3,'2026-01-05','004','周雪','13523456789','安徽省安庆市迎江区人民路48号','已发货','是','','已支付'),(4,'2026-01-05 10:27:29','978757601','全价犬用磨牙棒','upload/shangpindingdan_全价犬用磨牙棒1.jpg,upload/shangpindingdan_全价犬用磨牙棒2.jpg,upload/shangpindingdan_全价犬用磨牙棒3.jpg','零食','直径7cm','汪汪乐','德国',44,44,4,'2026-01-05','001','刘浩然','13578901234','浙江省温州市鹿城区五马街15号','已发货','是','','已支付'),(5,'2026-01-05 10:27:29','978730129','全期猫粮','upload/shangpindingdan_全期猫粮1.jpg,upload/shangpindingdan_全期猫粮2.jpg,upload/shangpindingdan_全期猫粮3.jpg','全期粮','20cm高','全能猫','加拿大',55,55,5,'2026-01-05','003','高雪','13589012345','湖南省株洲市天元区长江北路2号','已发货','是','','已支付'),(6,'2026-01-05 10:27:29','978703062','幼犬益生菌狗粮','upload/shangpindingdan_幼犬益生菌狗粮1.jpg,upload/shangpindingdan_幼犬益生菌狗粮2.jpg,upload/shangpindingdan_幼犬益生菌狗粮3.jpg','功能粮','直径9cm','益生菌世家','中国',26,26,6,'2026-01-05','007','张明','13467890123','宁夏银川市兴庆区解放西街36号','已发货','是','','已支付'),(7,'2026-01-05 10:27:29','978757020','冻干鸡肉猫零食','upload/shangpindingdan_冻干鸡肉猫零食1.jpg,upload/shangpindingdan_冻干鸡肉猫零食2.jpg,upload/shangpindingdan_冻干鸡肉猫零食3.jpg','零食','15cm长','冻干世家','中国',29,29,7,'2026-01-05','008','郭阳','13545678901','内蒙古呼和浩特市新城区新华大街69号','已发货','是','','已支付'),(8,'2026-01-05 10:27:29','978750609','小型犬幼犬奶糕','upload/shangpindingdan_小型犬幼犬奶糕1.jpg,upload/shangpindingdan_小型犬幼犬奶糕2.jpg,upload/shangpindingdan_小型犬幼犬奶糕3.jpg','幼犬粮','12cm长','小不点','中国',46,46,8,'2026-01-05','005','王强','13456789012','四川省绵阳市游仙区剑南路东段209号','已发货','是','','已支付'),(1767608974162,'2026-01-05 10:29:34','1767608972577','全期猫粮','upload/chongwuyongpin_全期猫粮1.jpg,upload/chongwuyongpin_全期猫粮2.jpg,upload/chongwuyongpin_全期猫粮3.jpg','全期粮','1.5kg','全能猫','加拿大',55,2,110,'2026-01-05','008','郭阳','13545678901','内蒙古呼和浩特市新城区新华大街69号','已发货','是','1','已支付');
/*!40000 ALTER TABLE `shangpindingdan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storeup`
--

DROP TABLE IF EXISTS `storeup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `storeup` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `userid` bigint(20) NOT NULL COMMENT '用户id',
  `refid` bigint(20) DEFAULT NULL COMMENT '商品id',
  `tablename` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '表名',
  `name` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '名称',
  `picture` longtext COLLATE utf8mb4_unicode_ci COMMENT '图片',
  `type` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT '1' COMMENT '类型',
  `inteltype` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '推荐类型',
  `remark` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='收藏表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storeup`
--

LOCK TABLES `storeup` WRITE;
/*!40000 ALTER TABLE `storeup` DISABLE KEYS */;
/*!40000 ALTER TABLE `storeup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `systemintro`
--

DROP TABLE IF EXISTS `systemintro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `systemintro` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `title` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '标题',
  `subtitle` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '副标题',
  `content` longtext COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '内容',
  `picture1` longtext COLLATE utf8mb4_unicode_ci COMMENT '图片1',
  `picture2` longtext COLLATE utf8mb4_unicode_ci COMMENT '图片2',
  `picture3` longtext COLLATE utf8mb4_unicode_ci COMMENT '图片3',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='系统简介';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `systemintro`
--

LOCK TABLES `systemintro` WRITE;
/*!40000 ALTER TABLE `systemintro` DISABLE KEYS */;
INSERT INTO `systemintro` VALUES (1,'2026-01-05 10:27:29','系统简介','SYSTEM INTRODUCTION','在平静的海平面上，每个人都可以成为领航员。但如果只有阳光而没有阴影，只有欢乐而没有痛苦，那就不是完整的人生。就拿最幸福的人来说吧——他的幸福是一团纠结的纱线。痛苦和幸福轮番而至，让我们悲喜交集，甚至死亡都让人生更加可爱。人在生命的严肃时刻，在悲伤与丧亲的阴影下，才最接近真实的自我。在生活和事业的各个方面，才智的功能远不如性格，头脑的功能远不如心性，天分远不如自制力、毅力与教养。我始终认为内心开始过严肃生活的人，他外在的生活会开始变得更为俭朴。在一个奢侈浪费的年代，但愿我能让世人了解：人类真正的需求是多么的稀少。不重蹈覆辙才是真正的醒悟。比别人优秀并无任何高贵之处，真正的高贵在于超越从前的自我。','upload/systemintro_picture1.jpg','upload/systemintro_picture2.jpg','upload/systemintro_picture3.jpg');
/*!40000 ALTER TABLE `systemintro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tuikuanshenqing`
--

DROP TABLE IF EXISTS `tuikuanshenqing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tuikuanshenqing` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `dingdanbianhao` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '订单编号',
  `shangpinmingcheng` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '商品名称',
  `shangpinfengmian` longtext COLLATE utf8mb4_unicode_ci COMMENT '商品封面',
  `pinpai` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '品牌',
  `jiage` double DEFAULT NULL COMMENT '价格',
  `kucun` int(11) DEFAULT NULL COMMENT '购买数量',
  `jifen` double DEFAULT NULL COMMENT '退款金额',
  `xiadanriqi` date DEFAULT NULL COMMENT '下单日期',
  `zhanghao` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '账号',
  `xingming` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '姓名',
  `shoujihaoma` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '手机号码',
  `shouhuodizhi` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '收货地址',
  `shenqingriqi` date DEFAULT NULL COMMENT '申请日期',
  `tuikuanyuanyin` longtext COLLATE utf8mb4_unicode_ci COMMENT '退款原因',
  `crossuserid` bigint(20) DEFAULT NULL COMMENT '跨表用户id',
  `crossrefid` bigint(20) DEFAULT NULL COMMENT '跨表主键id',
  `sfsh` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT '待审核' COMMENT '是否审核',
  `shhf` longtext COLLATE utf8mb4_unicode_ci COMMENT '审核回复',
  `ispay` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT '未支付' COMMENT '是否支付',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='退款申请';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tuikuanshenqing`
--

LOCK TABLES `tuikuanshenqing` WRITE;
/*!40000 ALTER TABLE `tuikuanshenqing` DISABLE KEYS */;
INSERT INTO `tuikuanshenqing` VALUES (1,'2026-01-05 10:27:29','978753428','幼猫奶糕罐头','upload/tuikuanshenqing_幼猫奶糕罐头1.jpg,upload/tuikuanshenqing_幼猫奶糕罐头2.jpg,upload/tuikuanshenqing_幼猫奶糕罐头3.jpg','猫主子',58,58,88,'2026-01-05','006','王若曦','13423456789','江苏省无锡市梁溪区中山路343号','2026-01-05','性价比不符预期',1,1,'是','','已支付'),(2,'2026-01-05 10:27:29','978702013','老年猫专用粮','upload/tuikuanshenqing_老年猫专用粮1.jpg,upload/tuikuanshenqing_老年猫专用粮2.jpg,upload/tuikuanshenqing_老年猫专用粮3.jpg','老猫咪',53,53,158,'2026-01-05','002','孙雨晴','13490123456','江西省九江市浔阳区浔阳路2号','2026-01-05','逾期交货退货',2,2,'是','','已支付'),(3,'2026-01-05 10:27:29','978711548','大型犬专用狗粮','upload/tuikuanshenqing_大型犬专用狗粮1.jpg,upload/tuikuanshenqing_大型犬专用狗粮2.jpg,upload/tuikuanshenqing_大型犬专用狗粮3.jpg','巨无霸',37,37,108,'2026-01-05','004','周雪','13523456789','安徽省安庆市迎江区人民路48号','2026-01-05','订单错发退回',3,3,'是','','已支付'),(4,'2026-01-05 10:27:29','978757601','全价犬用磨牙棒','upload/tuikuanshenqing_全价犬用磨牙棒1.jpg,upload/tuikuanshenqing_全价犬用磨牙棒2.jpg,upload/tuikuanshenqing_全价犬用磨牙棒3.jpg','汪汪乐',44,44,88,'2026-01-05','001','刘浩然','13578901234','浙江省温州市鹿城区五马街15号','2026-01-05','数量超额退回',4,4,'是','','已支付'),(5,'2026-01-05 10:27:29','978730129','全期猫粮','upload/tuikuanshenqing_全期猫粮1.jpg,upload/tuikuanshenqing_全期猫粮2.jpg,upload/tuikuanshenqing_全期猫粮3.jpg','全能猫',55,55,268,'2026-01-05','003','高雪','13589012345','湖南省株洲市天元区长江北路2号','2026-01-05','外观破损退货',5,5,'是','','已支付'),(6,'2026-01-05 10:27:29','978703062','幼犬益生菌狗粮','upload/tuikuanshenqing_幼犬益生菌狗粮1.jpg,upload/tuikuanshenqing_幼犬益生菌狗粮2.jpg,upload/tuikuanshenqing_幼犬益生菌狗粮3.jpg','益生菌世家',26,26,68,'2026-01-05','007','张明','13467890123','宁夏银川市兴庆区解放西街36号','2026-01-05','定制要求未满足',6,6,'是','','已支付'),(7,'2026-01-05 10:27:29','978757020','冻干鸡肉猫零食','upload/tuikuanshenqing_冻干鸡肉猫零食1.jpg,upload/tuikuanshenqing_冻干鸡肉猫零食2.jpg,upload/tuikuanshenqing_冻干鸡肉猫零食3.jpg','冻干世家',29,29,35,'2026-01-05','008','郭阳','13545678901','内蒙古呼和浩特市新城区新华大街69号','2026-01-05','包装损坏退货',7,7,'是','','已支付'),(8,'2026-01-05 10:27:29','978750609','小型犬幼犬奶糕','upload/tuikuanshenqing_小型犬幼犬奶糕1.jpg,upload/tuikuanshenqing_小型犬幼犬奶糕2.jpg,upload/tuikuanshenqing_小型犬幼犬奶糕3.jpg','小不点',46,46,45,'2026-01-05','005','王强','13456789012','四川省绵阳市游仙区剑南路东段209号','2026-01-05','规格型号不符',8,8,'是','','已支付');
/*!40000 ALTER TABLE `tuikuanshenqing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `username` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '用户名',
  `password` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '密码',
  `role` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT '管理员' COMMENT '角色',
  `image` longtext COLLATE utf8mb4_unicode_ci COMMENT '头像',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='管理员';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'2026-01-05 10:27:29','admin','admin','管理员','upload/image1.jpg');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `yonghu`
--

DROP TABLE IF EXISTS `yonghu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `yonghu` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `zhanghao` varchar(16) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '账号',
  `mima` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '密码',
  `xingming` varchar(16) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '姓名',
  `xingbie` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '性别',
  `shoujihaoma` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '手机号码',
  `shouhuodizhi` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '收货地址',
  `jifen` double DEFAULT NULL COMMENT '积分',
  `touxiang` longtext COLLATE utf8mb4_unicode_ci COMMENT '头像',
  `email` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '邮箱',
  `status` int(11) DEFAULT '0' COMMENT '状态',
  PRIMARY KEY (`id`),
  UNIQUE KEY `zhanghao` (`zhanghao`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='用户';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `yonghu`
--

LOCK TABLES `yonghu` WRITE;
/*!40000 ALTER TABLE `yonghu` DISABLE KEYS */;
INSERT INTO `yonghu` VALUES (11,'2026-01-05 10:27:28','006','123456','王若曦','女','13423456789','江苏省无锡市梁溪区中山路343号',88,'upload/yonghu_touxiang1.jpg','773890001@qq.com',0),(12,'2026-01-05 10:27:28','002','123456','孙雨晴','女','13490123456','江西省九江市浔阳区浔阳路2号',158,'upload/yonghu_touxiang2.jpg','773890002@qq.com',0),(13,'2026-01-05 10:27:28','004','123456','周雪','女','13523456789','安徽省安庆市迎江区人民路48号',108,'upload/yonghu_touxiang3.jpg','773890003@qq.com',0),(14,'2026-01-05 10:27:28','001','123456','刘浩然','女','13578901234','浙江省温州市鹿城区五马街15号',88,'upload/yonghu_touxiang4.jpg','773890004@qq.com',0),(15,'2026-01-05 10:27:28','003','123456','高雪','女','13589012345','湖南省株洲市天元区长江北路2号',268,'upload/yonghu_touxiang5.jpg','773890005@qq.com',0),(16,'2026-01-05 10:27:28','007','123456','张明','女','13467890123','宁夏银川市兴庆区解放西街36号',68,'upload/yonghu_touxiang6.jpg','773890006@qq.com',0),(17,'2026-01-05 10:27:28','008','123456','郭阳','女','13545678901','内蒙古呼和浩特市新城区新华大街69号',610,'upload/yonghu_touxiang7.jpg','773890007@qq.com',0),(18,'2026-01-05 10:27:28','005','123456','王强','男','13456789012','四川省绵阳市游仙区剑南路东段209号',45,'upload/yonghu_touxiang8.jpg','773890008@qq.com',0);
/*!40000 ALTER TABLE `yonghu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zaishouchongwu`
--

DROP TABLE IF EXISTS `zaishouchongwu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zaishouchongwu` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `chongwunicheng` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '宠物昵称',
  `chongwupinzhong` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '宠物品种',
  `chongwutupian` longtext COLLATE utf8mb4_unicode_ci COMMENT '宠物图片',
  `zhonglei` varchar(16) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '种类',
  `xingbie` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '性别',
  `chushengriqi` date DEFAULT NULL COMMENT '出生日期',
  `yanse` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '颜色',
  `aihao` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '爱好',
  `jifen` double DEFAULT NULL COMMENT '售价',
  `yimiaojilu` longtext COLLATE utf8mb4_unicode_ci COMMENT '疫苗记录',
  `quchongjilu` longtext COLLATE utf8mb4_unicode_ci COMMENT '驱虫记录',
  `chushouzhuangtai` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '出售状态',
  `discussnum` int(11) DEFAULT '0' COMMENT '评论数',
  `storeupnum` int(11) DEFAULT '0' COMMENT '收藏数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='在售宠物';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zaishouchongwu`
--

LOCK TABLES `zaishouchongwu` WRITE;
/*!40000 ALTER TABLE `zaishouchongwu` DISABLE KEYS */;
INSERT INTO `zaishouchongwu` VALUES (1,'2026-01-05 10:27:28','团团','八哥鸟','upload/zaishouchongwu_八哥鸟1.jpg,upload/zaishouchongwu_八哥鸟2.jpg,upload/zaishouchongwu_八哥鸟3.jpg','雀形目','公','2024-10-18','黑亮色','学说话和洗澡',459,'2024-01接种鸟类疫苗2024-07加强','2024-02外驱2024-05内驱','已出售',0,1),(2,'2026-01-05 10:27:28','妞妞','美短猫','upload/zaishouchongwu_美短猫1.jpg,upload/zaishouchongwu_美短猫2.jpg,upload/zaishouchongwu_美短猫3.jpg','猫科','公','2024-08-11','虎斑纹','玩激光笔和爬猫爬架',476,'2024-03接种猫三联2024-09加强','2024-04内外驱2024-07外驱','待出售',0,2),(3,'2026-01-05 10:27:28','京京','三线仓鼠','upload/zaishouchongwu_三线仓鼠1.jpg,upload/zaishouchongwu_三线仓鼠2.jpg,upload/zaishouchongwu_三线仓鼠3.jpg','啮齿科','母','2025-01-15','棕黑相间','跑轮和藏粮',318,'2024-02接种仓鼠专用疫苗','2024-03外驱2024-06外驱','已出售',0,3),(4,'2026-01-05 10:27:28','可可','玄凤鹦鹉','upload/zaishouchongwu_玄凤鹦鹉1.jpg,upload/zaishouchongwu_玄凤鹦鹉2.jpg,upload/zaishouchongwu_玄凤鹦鹉3.jpg','鹦形目','公','2025-08-23','黄白相间','模仿声音和飞笼顶',369,'2024-01接种鹦鹉疫苗2024-07加强','2024-02外驱2024-05外驱','已出售',0,4),(5,'2026-01-05 10:27:28','奶糖','边境牧羊犬','upload/zaishouchongwu_边境牧羊犬1.jpg,upload/zaishouchongwu_边境牧羊犬2.jpg,upload/zaishouchongwu_边境牧羊犬3.jpg','犬科','公','2025-02-20','黑白相间','接飞盘和听指令',189,'2024-04接种犬二联2024-10加强','2024-05内外驱2024-08外驱','已出售',0,5),(6,'2026-01-05 10:27:28','哈利','阿拉斯加','upload/zaishouchongwu_阿拉斯加1.jpg,upload/zaishouchongwu_阿拉斯加2.jpg,upload/zaishouchongwu_阿拉斯加3.jpg','犬科','母','2025-06-16','棕白相间','拉小车和睡觉',243,'2024-02接种犬四联2024-08加强','2024-03内外驱2024-06内驱','已出售',0,6),(7,'2026-01-05 10:27:28','贝贝','比熊犬','upload/zaishouchongwu_比熊犬1.jpg,upload/zaishouchongwu_比熊犬2.jpg,upload/zaishouchongwu_比熊犬3.jpg','犬科','母','2024-09-07','纯白色','玩毛绒球和被梳毛',489,'2024-03接种犬四联2024-09加强','2024-04内外驱2024-07内驱','已出售',0,7),(8,'2026-01-05 10:27:28','朵朵','布偶猫','upload/zaishouchongwu_布偶猫1.jpg,upload/zaishouchongwu_布偶猫2.jpg,upload/zaishouchongwu_布偶猫3.jpg','猫科','母','2025-04-12','白色加浅棕','蹭人和玩毛绒玩具',412,'2024-04接种猫三联2024-10加强','2024-05内外驱2024-08外驱','待出售',0,8);
/*!40000 ALTER TABLE `zaishouchongwu` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-01-05 19:30:04
