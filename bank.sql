/*
 Navicat Premium Data Transfer

 Source Server         : root_5.7
 Source Server Type    : MySQL
 Source Server Version : 50726
 Source Host           : localhost:3306
 Source Schema         : bank

 Target Server Type    : MySQL
 Target Server Version : 50726
 File Encoding         : 65001

 Date: 20/05/2021 01:04:49
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '用户id',
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '用户姓名',
  `yhk` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '银行卡号',
  `password` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '银行卡密码',
  `callnumber` int(10) NULL DEFAULT NULL COMMENT '用户手机号',
  `money` float NULL DEFAULT NULL COMMENT '余额',
  `idcard` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '身份证号码',
  `block` char(2) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '是否锁定',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 40 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (1, 'test', '123', '123', NULL, 783575, '333', '0');
INSERT INTO `users` VALUES (2, 'test', 'yhk', 'pwd', 123, 23533.3, '123123', '0');
INSERT INTO `users` VALUES (3, 'user1', 'user', 'user', 123123, 1000, '1111111', '0');
INSERT INTO `users` VALUES (37, '斌斌子', '9db7ed328576840d5b56ba78dcc5a0bb', '123456', 123123132, 10000, '12312aa', '0');
INSERT INTO `users` VALUES (38, '11', '06c98dfed358f8c84200ff17377152f4', '123456', 22, 0, '33', '0');
INSERT INTO `users` VALUES (39, '1', '91d83cb744bca5e532ffc23bb2c8c892', '123456', 2, 0, '3', '0');

SET FOREIGN_KEY_CHECKS = 1;
