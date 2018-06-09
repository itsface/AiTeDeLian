/*
 Navicat MySQL Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 50720
 Source Host           : localhost:3306
 Source Schema         : it_show

 Target Server Type    : MySQL
 Target Server Version : 50720
 File Encoding         : 65001

 Date: 05/06/2018 08:04:26
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 49 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (5, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (8, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (9, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (10, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (11, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (12, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (13, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (14, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (15, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (16, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (17, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (18, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (19, 'Can add 报名者', 7, 'add_fresher');
INSERT INTO `auth_permission` VALUES (20, 'Can change 报名者', 7, 'change_fresher');
INSERT INTO `auth_permission` VALUES (21, 'Can delete 报名者', 7, 'delete_fresher');
INSERT INTO `auth_permission` VALUES (22, 'Can add 部门', 8, 'add_department');
INSERT INTO `auth_permission` VALUES (23, 'Can change 部门', 8, 'change_department');
INSERT INTO `auth_permission` VALUES (24, 'Can delete 部门', 8, 'delete_department');
INSERT INTO `auth_permission` VALUES (25, 'Can add 爱特大事记', 9, 'add_event');
INSERT INTO `auth_permission` VALUES (26, 'Can change 爱特大事记', 9, 'change_event');
INSERT INTO `auth_permission` VALUES (27, 'Can delete 爱特大事记', 9, 'delete_event');
INSERT INTO `auth_permission` VALUES (28, 'Can add 成员信息', 10, 'add_member');
INSERT INTO `auth_permission` VALUES (29, 'Can change 成员信息', 10, 'change_member');
INSERT INTO `auth_permission` VALUES (30, 'Can delete 成员信息', 10, 'delete_member');
INSERT INTO `auth_permission` VALUES (31, 'Can add 成果展示', 11, 'add_worksshow');
INSERT INTO `auth_permission` VALUES (32, 'Can change 成果展示', 11, 'change_worksshow');
INSERT INTO `auth_permission` VALUES (33, 'Can delete 成果展示', 11, 'delete_worksshow');
INSERT INTO `auth_permission` VALUES (34, 'Can add status details', 12, 'add_statusdetails');
INSERT INTO `auth_permission` VALUES (35, 'Can change status details', 12, 'change_statusdetails');
INSERT INTO `auth_permission` VALUES (36, 'Can delete status details', 12, 'delete_statusdetails');
INSERT INTO `auth_permission` VALUES (37, 'Can add status info', 13, 'add_statusinfo');
INSERT INTO `auth_permission` VALUES (38, 'Can change status info', 13, 'change_statusinfo');
INSERT INTO `auth_permission` VALUES (39, 'Can delete status info', 13, 'delete_statusinfo');
INSERT INTO `auth_permission` VALUES (40, 'Can add 匿名评论', 14, 'add_comment');
INSERT INTO `auth_permission` VALUES (41, 'Can change 匿名评论', 14, 'change_comment');
INSERT INTO `auth_permission` VALUES (42, 'Can delete 匿名评论', 14, 'delete_comment');
INSERT INTO `auth_permission` VALUES (43, 'Can add 匿名评论头像', 15, 'add_headpicture');
INSERT INTO `auth_permission` VALUES (44, 'Can change 匿名评论头像', 15, 'change_headpicture');
INSERT INTO `auth_permission` VALUES (45, 'Can delete 匿名评论头像', 15, 'delete_headpicture');
INSERT INTO `auth_permission` VALUES (46, 'Can add profile', 16, 'add_profile');
INSERT INTO `auth_permission` VALUES (47, 'Can change profile', 16, 'change_profile');
INSERT INTO `auth_permission` VALUES (48, 'Can delete profile', 16, 'delete_profile');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES (1, 'pbkdf2_sha256$36000$GB5zKzvODIH4$ejUZiMMA1xVeApqw5HEK2lF9i5cctszgkpJWvmTSzhg=', '2018-05-26 03:42:50.180418', 1, 'root', '', '', '10086@qq.com', 1, 1, '2018-05-05 18:34:58.402120');
INSERT INTO `auth_user` VALUES (2, 'pbkdf2_sha256$30000$F7eHgI9NYrdo$k6vTxwADvz8XhIr+6fZSaOnLlT476NvyxF9wbKm2NmY=', '2018-05-26 06:44:35.304427', 1, 'ming', '', '', '10086@qq.com', 1, 1, '2018-05-26 06:44:06.249458');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_general_ci,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 161 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES (1, '2018-05-05 18:42:57.572688', '1', '浦泽元', 1, '[{\"added\": {}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (2, '2018-05-05 18:46:47.121633', '1', '浦泽元', 2, '[{\"changed\": {\"fields\": [\"sex\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (3, '2018-05-05 18:52:09.646987', '1', '前端开发', 1, '[{\"added\": {}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (4, '2018-05-05 18:52:40.750439', '2', '程序开发', 1, '[{\"added\": {}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (5, '2018-05-05 18:52:45.355948', '1', '前端开发', 2, '[{\"changed\": {\"fields\": [\"pic\"]}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (6, '2018-05-05 18:53:00.752799', '3', 'UI设计', 1, '[{\"added\": {}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (7, '2018-05-05 18:53:25.979726', '4', 'APP开发', 1, '[{\"added\": {}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (8, '2018-05-05 18:54:17.538398', '1', 'Android Ap', 1, '[{\"added\": {}}]', 9, 1);
INSERT INTO `django_admin_log` VALUES (9, '2018-05-05 18:55:03.020191', '1', '海洋技术系网站', 1, '[{\"added\": {}}]', 11, 1);
INSERT INTO `django_admin_log` VALUES (10, '2018-05-05 19:25:16.432133', '1', '浦泽元', 1, '[{\"added\": {}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (11, '2018-05-05 20:49:53.897265', '4', '0', 2, '[{\"changed\": {\"fields\": [\"info\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (12, '2018-05-05 20:49:57.481429', '4', '0', 2, '[{\"changed\": {\"fields\": [\"info\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (13, '2018-05-05 20:50:31.944995', '1', '浦泽元', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (14, '2018-05-05 21:51:54.459967', '1', '浦泽元', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (15, '2018-05-05 21:53:07.808758', '1', '报名表审核受理中...by Pu', 2, '[{\"changed\": {\"fields\": [\"info\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (16, '2018-05-05 21:53:19.543085', '1', '报名表审核受理中...', 2, '[{\"changed\": {\"fields\": [\"info\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (17, '2018-05-06 06:17:49.603064', '1', '浦泽元', 2, '[{\"changed\": {\"fields\": [\"email\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (18, '2018-05-06 06:28:55.318473', '1', '报名表审核受理中...', 2, '[{\"changed\": {\"fields\": [\"emailText\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (19, '2018-05-06 06:32:38.613834', '1', '浦泽元', 2, '[{\"changed\": {\"fields\": [\"userCode\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (20, '2018-05-06 08:26:57.595329', '2', '阿浦', 1, '[{\"added\": {}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (21, '2018-05-06 08:33:14.988152', '1', '面试', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (22, '2018-05-06 08:33:38.030022', '2', '笔试', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (23, '2018-05-06 08:49:55.198476', '1', '浦泽元', 2, '[{\"changed\": {\"fields\": [\"status\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (24, '2018-05-06 08:50:41.494753', '3', '退出', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (25, '2018-05-06 08:58:39.086122', '1', '浦泽元', 2, '[{\"changed\": {\"fields\": [\"status\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (26, '2018-05-06 08:58:49.965761', '2', '阿浦', 2, '[{\"changed\": {\"fields\": [\"email\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (27, '2018-05-06 11:32:01.899652', '4', '未处理', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (28, '2018-05-06 11:32:39.423610', '2', '阿浦', 2, '[{\"changed\": {\"fields\": [\"email\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (29, '2018-05-06 11:34:01.193802', '2', '阿浦', 2, '[{\"changed\": {\"fields\": [\"email\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (30, '2018-05-06 11:34:48.335395', '1', '面试', 2, '[{\"changed\": {\"fields\": [\"emailText\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (31, '2018-05-06 11:35:04.585829', '2', '阿浦', 2, '[{\"changed\": {\"fields\": [\"status\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (32, '2018-05-09 11:13:34.085354', '0', '报名表审核受理中test...', 2, '[{\"changed\": {\"fields\": [\"info\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (33, '2018-05-09 11:13:57.865248', '0', '报名表审核受理中...', 2, '[{\"changed\": {\"fields\": [\"info\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (34, '2018-05-09 11:30:07.688273', '1', '浦泽元', 2, '[{\"changed\": {\"fields\": [\"wantDepartment\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (35, '2018-05-10 07:45:39.079520', '0', '报名表审核受理中...', 2, '[{\"changed\": {\"fields\": [\"nextStatus\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (36, '2018-05-10 07:49:46.844264', '0', '报名表审核受理中...', 2, '[]', 13, 1);
INSERT INTO `django_admin_log` VALUES (37, '2018-05-10 07:49:55.477631', '1', '面试', 2, '[{\"changed\": {\"fields\": [\"nextStatus\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (38, '2018-05-10 07:50:04.542424', '3', '退出', 2, '[{\"changed\": {\"fields\": [\"nextStatus\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (39, '2018-05-10 07:50:40.362377', '2', '笔试', 2, '[{\"changed\": {\"fields\": [\"nextStatus\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (40, '2018-05-10 07:51:04.257549', '4', '未处理', 2, '[{\"changed\": {\"fields\": [\"nextStatus\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (41, '2018-05-10 07:59:35.760715', '2', '阿浦', 2, '[{\"changed\": {\"fields\": [\"wantDepartment\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (42, '2018-05-10 14:42:51.285105', '2', '阿浦', 2, '[{\"changed\": {\"fields\": [\"wantDepartment\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (43, '2018-05-10 14:43:31.718836', '5', '游戏开发', 1, '[{\"added\": {}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (44, '2018-05-10 14:43:41.773371', '2', '阿浦', 2, '[{\"changed\": {\"fields\": [\"wantDepartment\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (45, '2018-05-10 14:47:09.658867', '5', '游戏开发', 3, '', 8, 1);
INSERT INTO `django_admin_log` VALUES (46, '2018-05-10 15:02:58.670389', '0', '报名表审核受理中...', 2, '[]', 13, 1);
INSERT INTO `django_admin_log` VALUES (47, '2018-05-10 15:12:21.789329', '0', '报名表审核受理中...', 2, '[{\"changed\": {\"fields\": [\"nextStatus\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (48, '2018-05-10 15:16:11.186906', '4', '未处理', 2, '[]', 13, 1);
INSERT INTO `django_admin_log` VALUES (49, '2018-05-10 15:16:35.432388', '6', '', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (50, '2018-05-10 15:16:47.959217', '6', '', 2, '[]', 13, 1);
INSERT INTO `django_admin_log` VALUES (51, '2018-05-11 00:31:44.037859', '0', '报名表审核受理中...', 2, '[{\"changed\": {\"fields\": [\"emailText\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (52, '2018-05-11 00:32:31.254346', '0', '报名表审核受理中...', 2, '[{\"changed\": {\"fields\": [\"nextStatus\", \"emailText\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (53, '2018-05-11 00:32:44.918875', '0', '报名表审核受理中...', 2, '[{\"changed\": {\"fields\": [\"emailText\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (54, '2018-05-11 00:33:05.576298', '1', '浦泽元', 2, '[{\"changed\": {\"fields\": [\"status\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (55, '2018-05-11 00:38:21.785882', '0', '报名表审核受理中...', 2, '[{\"changed\": {\"fields\": [\"nextStatus\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (56, '2018-05-11 00:40:21.029601', '4', '未处理', 2, '[{\"changed\": {\"fields\": [\"info\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (57, '2018-05-11 00:49:49.385273', '1', '浦泽元', 2, '[{\"changed\": {\"fields\": [\"photo\"]}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (58, '2018-05-11 00:50:07.412345', '1', '浦泽元', 2, '[{\"changed\": {\"fields\": [\"photo\"]}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (59, '2018-05-11 00:50:26.422992', '1', '浦泽元', 2, '[{\"changed\": {\"fields\": [\"photo\"]}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (60, '2018-05-11 11:27:45.536722', '2', '浦泽元', 1, '[{\"added\": {}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (61, '2018-05-11 11:29:17.185395', '2', '浦泽元', 2, '[{\"changed\": {\"fields\": [\"photo\"]}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (62, '2018-05-11 13:00:04.735080', '2', '浦泽元', 2, '[{\"changed\": {\"fields\": [\"photo\"]}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (63, '2018-05-11 13:01:34.802739', '1', '谢哲勇', 2, '[{\"changed\": {\"fields\": [\"name\", \"intro\", \"photo\"]}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (64, '2018-05-11 13:01:59.208701', '3', '陈尊龙', 1, '[{\"added\": {}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (65, '2018-05-11 13:02:13.360466', '4', '陈开拓', 1, '[{\"added\": {}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (66, '2018-05-11 13:02:25.667290', '5', '丁进仁', 1, '[{\"added\": {}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (67, '2018-05-11 13:02:49.598394', '6', '李林宇', 1, '[{\"added\": {}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (68, '2018-05-11 13:02:58.552290', '3', '陈尊龙', 2, '[{\"changed\": {\"fields\": [\"year\"]}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (69, '2018-05-11 13:03:03.772139', '4', '陈开拓', 2, '[{\"changed\": {\"fields\": [\"year\"]}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (70, '2018-05-11 13:03:08.761683', '5', '丁进仁', 2, '[{\"changed\": {\"fields\": [\"year\"]}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (71, '2018-05-11 13:03:13.299596', '6', '李林宇', 2, '[{\"changed\": {\"fields\": [\"year\"]}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (72, '2018-05-11 13:45:44.244204', '2', '浦泽元', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (73, '2018-05-11 13:46:12.699515', '1', '浦泽元', 2, '[{\"changed\": {\"fields\": [\"code\", \"info\"]}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (74, '2018-05-11 13:47:19.937267', '1', '浦泽元', 2, '[{\"changed\": {\"fields\": [\"info\"]}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (75, '2018-05-11 13:47:32.114669', '2', '浦泽元', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (76, '2018-05-11 13:47:47.881294', '1', '浦泽元', 3, '', 7, 1);
INSERT INTO `django_admin_log` VALUES (77, '2018-05-11 13:49:08.363950', '2', '浦泽元', 1, '[{\"added\": {}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (78, '2018-05-11 13:49:35.524758', '2', '浦泽元', 2, '[{\"changed\": {\"fields\": [\"status\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (79, '2018-05-11 14:03:15.838366', '1', '啦啦啦', 1, '[{\"added\": {}}]', 15, 1);
INSERT INTO `django_admin_log` VALUES (80, '2018-05-11 14:03:39.908362', '1', '爱特重量担当', 1, '[{\"added\": {}}]', 14, 1);
INSERT INTO `django_admin_log` VALUES (81, '2018-05-12 02:06:33.084848', '3', '浦泽元', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (82, '2018-05-12 13:46:18.007459', '2', '浦泽元', 2, '[{\"changed\": {\"fields\": [\"status\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (83, '2018-05-12 13:46:40.727869', '4', '未处理', 3, '', 13, 1);
INSERT INTO `django_admin_log` VALUES (84, '2018-05-12 13:52:49.672195', '3', '阿浦', 1, '[{\"added\": {}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (85, '2018-05-12 13:53:00.509687', '3', '阿浦', 2, '[]', 7, 1);
INSERT INTO `django_admin_log` VALUES (86, '2018-05-12 13:53:03.081308', '3', '阿浦', 2, '[]', 7, 1);
INSERT INTO `django_admin_log` VALUES (87, '2018-05-12 13:53:05.115867', '3', '阿浦', 2, '[]', 7, 1);
INSERT INTO `django_admin_log` VALUES (88, '2018-05-12 13:53:28.974282', '0', '报名表审核受理中...', 3, '', 13, 1);
INSERT INTO `django_admin_log` VALUES (89, '2018-05-12 13:53:50.832921', '0', '报名状态未受理', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (90, '2018-05-12 13:53:57.385959', '0', '报名状态未受理', 2, '[{\"changed\": {\"fields\": [\"nextStatus\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (91, '2018-05-12 13:57:21.739509', '4', '21', 1, '[{\"added\": {}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (92, '2018-05-12 14:02:47.826982', '0', '报名状态未受理', 3, '', 13, 1);
INSERT INTO `django_admin_log` VALUES (93, '2018-05-12 14:04:41.319905', '4', '21', 2, '[]', 7, 1);
INSERT INTO `django_admin_log` VALUES (94, '2018-05-12 14:04:58.318863', '4', '21', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (95, '2018-05-12 14:16:00.855624', '4', '21', 2, '[{\"changed\": {\"fields\": [\"status\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (96, '2018-05-12 14:16:11.685687', '5', '21', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (97, '2018-05-12 14:16:11.690671', '4', '21', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (98, '2018-05-12 14:16:22.592448', '4', '21', 2, '[]', 7, 1);
INSERT INTO `django_admin_log` VALUES (99, '2018-05-12 14:21:43.121872', '4', '21', 2, '[{\"changed\": {\"fields\": [\"email\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (100, '2018-05-12 14:22:35.806190', '4', '21', 2, '[{\"changed\": {\"fields\": [\"status\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (101, '2018-05-12 14:29:29.371380', '3', '退出', 2, '[{\"changed\": {\"fields\": [\"nextStatus\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (102, '2018-05-12 15:02:31.402345', '4', '21', 2, '[{\"changed\": {\"fields\": [\"status\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (103, '2018-05-12 15:09:28.644991', '21', '21', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (104, '2018-05-12 15:09:28.652941', '20', '21', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (105, '2018-05-12 15:09:28.666898', '19', '21', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (106, '2018-05-12 15:09:28.673912', '18', '21', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (107, '2018-05-12 15:09:28.679864', '17', '21', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (108, '2018-05-12 15:09:28.684858', '16', '21', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (109, '2018-05-12 15:09:28.690836', '15', '21', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (110, '2018-05-12 15:09:28.696820', '14', '21', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (111, '2018-05-12 15:09:28.702802', '13', '21', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (112, '2018-05-12 15:09:28.706791', '12', '21', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (113, '2018-05-12 15:09:28.711794', '11', '21', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (114, '2018-05-12 15:09:28.719765', '10', '21', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (115, '2018-05-12 15:09:28.725743', '9', '21', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (116, '2018-05-12 15:09:28.731727', '8', '21', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (117, '2018-05-12 15:09:28.736722', '7', '21', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (118, '2018-05-12 15:09:28.742697', '6', '21', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (119, '2018-05-12 15:09:32.579555', '4', '21', 2, '[]', 7, 1);
INSERT INTO `django_admin_log` VALUES (120, '2018-05-12 15:17:41.295599', '24', '21', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (121, '2018-05-12 15:17:41.316542', '23', '21', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (122, '2018-05-12 15:17:41.322527', '22', '21', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (123, '2018-05-12 15:17:49.611478', '25', '21', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (124, '2018-05-12 15:18:52.512570', '26', '21', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (125, '2018-05-12 15:20:20.281650', '28', '21', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (126, '2018-05-12 15:24:53.397291', '4', '21', 2, '[{\"changed\": {\"fields\": [\"status\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (127, '2018-05-12 15:25:23.124282', '4', '21', 2, '[{\"changed\": {\"fields\": [\"status\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (128, '2018-05-12 15:26:24.027378', '32', '21', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (129, '2018-05-12 15:26:57.889158', '4', '21', 2, '[]', 7, 1);
INSERT INTO `django_admin_log` VALUES (130, '2018-05-12 15:28:34.859730', '4', '21', 2, '[{\"changed\": {\"fields\": [\"status\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (131, '2018-05-12 15:28:54.203341', '4', '21', 2, '[{\"changed\": {\"fields\": [\"status\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (132, '2018-05-12 15:29:55.635201', '4', '21', 2, '[{\"changed\": {\"fields\": [\"status\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (133, '2018-05-12 15:30:00.892145', '4', '21', 2, '[{\"changed\": {\"fields\": [\"status\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (134, '2018-05-13 08:41:13.668108', '31', '21', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (135, '2018-05-13 08:41:13.708998', '27', '21', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (136, '2018-05-13 08:41:40.341629', '32', '21', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (137, '2018-05-13 08:54:06.880149', '5', '小明', 1, '[{\"added\": {}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (138, '2018-05-13 08:54:17.161302', '4', '小花', 2, '[{\"changed\": {\"fields\": [\"name\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (139, '2018-05-13 08:54:36.470120', '6', '大明', 1, '[{\"added\": {}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (140, '2018-05-13 12:21:34.835284', '32', '小花', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (141, '2018-05-13 12:21:34.845104', '41', '小明', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (142, '2018-05-13 12:21:34.851701', '37', '小明', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (143, '2018-05-13 12:21:34.858104', '39', '大明', 3, '', 12, 1);
INSERT INTO `django_admin_log` VALUES (144, '2018-05-14 09:11:44.511414', '6', '大明', 2, '[]', 7, 1);
INSERT INTO `django_admin_log` VALUES (145, '2018-05-14 09:12:14.207083', '45', '大明', 2, '[]', 12, 1);
INSERT INTO `django_admin_log` VALUES (146, '2018-05-14 09:12:31.006348', '45', '大明', 2, '[{\"changed\": {\"fields\": [\"info\"]}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (147, '2018-05-14 09:22:40.602425', '6', '李林宇', 2, '[{\"changed\": {\"fields\": [\"department\"]}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (148, '2018-05-14 09:23:12.017546', '6', '李林宇', 2, '[]', 10, 1);
INSERT INTO `django_admin_log` VALUES (149, '2018-05-14 09:23:34.374296', '5', '丁进仁', 2, '[{\"changed\": {\"fields\": [\"department\"]}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (150, '2018-05-26 06:44:58.384228', '1', 'Profile object', 1, '[{\"added\": {}}]', 16, 2);
INSERT INTO `django_admin_log` VALUES (151, '2018-05-27 03:31:12.435688', '1', 'Profile object', 2, '[{\"changed\": {\"fields\": [\"avatar\"]}}]', 16, 2);
INSERT INTO `django_admin_log` VALUES (152, '2018-05-27 03:42:01.485766', '1', 'Profile object', 2, '[{\"changed\": {\"fields\": [\"avatar\"]}}]', 16, 2);
INSERT INTO `django_admin_log` VALUES (153, '2018-05-27 03:46:23.032183', '1', 'Profile object', 2, '[{\"changed\": {\"fields\": [\"avatar\"]}}]', 16, 2);
INSERT INTO `django_admin_log` VALUES (154, '2018-05-27 03:47:03.776018', '1', 'Profile object', 2, '[{\"changed\": {\"fields\": [\"avatar\"]}}]', 16, 2);
INSERT INTO `django_admin_log` VALUES (155, '2018-05-27 03:47:37.001004', '1', 'Profile object', 2, '[{\"changed\": {\"fields\": [\"avatar\"]}}]', 16, 2);
INSERT INTO `django_admin_log` VALUES (156, '2018-05-27 04:06:43.559960', '1', 'Profile object', 2, '[{\"changed\": {\"fields\": [\"avatar\"]}}]', 16, 2);
INSERT INTO `django_admin_log` VALUES (157, '2018-05-27 04:16:59.457260', '1', 'Profile object', 2, '[{\"changed\": {\"fields\": [\"avatar\"]}}]', 16, 2);
INSERT INTO `django_admin_log` VALUES (158, '2018-05-27 04:19:19.271866', '1', 'Profile object', 2, '[{\"changed\": {\"fields\": [\"avatar\"]}}]', 16, 2);
INSERT INTO `django_admin_log` VALUES (159, '2018-05-27 04:19:38.589208', '1', 'Profile object', 2, '[{\"changed\": {\"fields\": [\"avatar\"]}}]', 16, 2);
INSERT INTO `django_admin_log` VALUES (160, '2018-05-27 04:23:14.234454', '1', 'Profile object', 2, '[{\"changed\": {\"fields\": [\"avatar\"]}}]', 16, 2);

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 17 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');
INSERT INTO `django_content_type` VALUES (14, 'show', 'comment');
INSERT INTO `django_content_type` VALUES (8, 'show', 'department');
INSERT INTO `django_content_type` VALUES (9, 'show', 'event');
INSERT INTO `django_content_type` VALUES (15, 'show', 'headpicture');
INSERT INTO `django_content_type` VALUES (10, 'show', 'member');
INSERT INTO `django_content_type` VALUES (11, 'show', 'worksshow');
INSERT INTO `django_content_type` VALUES (16, 'tes', 'profile');
INSERT INTO `django_content_type` VALUES (7, 'user', 'fresher');
INSERT INTO `django_content_type` VALUES (12, 'user', 'statusdetails');
INSERT INTO `django_content_type` VALUES (13, 'user', 'statusinfo');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 38 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2018-05-05 18:32:46.688076');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2018-05-05 18:32:47.809848');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2018-05-05 18:32:48.122155');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2018-05-05 18:32:48.168278');
INSERT INTO `django_migrations` VALUES (5, 'contenttypes', '0002_remove_content_type_name', '2018-05-05 18:32:48.340920');
INSERT INTO `django_migrations` VALUES (6, 'auth', '0002_alter_permission_name_max_length', '2018-05-05 18:32:48.439671');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0003_alter_user_email_max_length', '2018-05-05 18:32:48.553121');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0004_alter_user_username_opts', '2018-05-05 18:32:48.569155');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0005_alter_user_last_login_null', '2018-05-05 18:32:48.654046');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0006_require_contenttypes_0002', '2018-05-05 18:32:48.660064');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0007_alter_validators_add_error_messages', '2018-05-05 18:32:48.674138');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0008_alter_user_username_max_length', '2018-05-05 18:32:48.884203');
INSERT INTO `django_migrations` VALUES (13, 'sessions', '0001_initial', '2018-05-05 18:34:24.186407');
INSERT INTO `django_migrations` VALUES (14, 'user', '0001_initial', '2018-05-05 18:34:34.752154');
INSERT INTO `django_migrations` VALUES (15, 'show', '0001_initial', '2018-05-05 18:34:38.722046');
INSERT INTO `django_migrations` VALUES (16, 'user', '0002_auto_20180506_0349', '2018-05-05 20:44:30.679280');
INSERT INTO `django_migrations` VALUES (18, 'user', '0003_auto_20180506_0444', '2018-05-05 21:48:34.810967');
INSERT INTO `django_migrations` VALUES (19, 'user', '0002_auto_20180506_1426', '2018-05-06 06:26:33.258562');
INSERT INTO `django_migrations` VALUES (20, 'user', '0003_auto_20180506_1625', '2018-05-06 08:25:12.293571');
INSERT INTO `django_migrations` VALUES (21, 'user', '0004_auto_20180509_1929', '2018-05-09 11:29:42.390493');
INSERT INTO `django_migrations` VALUES (22, 'user', '0005_auto_20180510_1542', '2018-05-10 07:43:05.079303');
INSERT INTO `django_migrations` VALUES (23, 'show', '0002_auto_20180510_1542', '2018-05-10 07:43:08.897251');
INSERT INTO `django_migrations` VALUES (24, 'user', '0006_auto_20180510_2240', '2018-05-10 14:42:24.806300');
INSERT INTO `django_migrations` VALUES (25, 'user', '0007_auto_20180510_2242', '2018-05-10 14:42:25.055636');
INSERT INTO `django_migrations` VALUES (26, 'show', '0003_auto_20180510_2240', '2018-05-10 14:42:30.499980');
INSERT INTO `django_migrations` VALUES (27, 'user', '0008_auto_20180510_2302', '2018-05-10 15:02:38.248959');
INSERT INTO `django_migrations` VALUES (28, 'user', '0009_auto_20180510_2305', '2018-05-10 15:05:51.200700');
INSERT INTO `django_migrations` VALUES (29, 'show', '0004_auto_20180511_1926', '2018-05-11 11:26:17.278348');
INSERT INTO `django_migrations` VALUES (30, 'user', '0010_auto_20180511_2146', '2018-05-11 13:47:03.019746');
INSERT INTO `django_migrations` VALUES (31, 'user', '0011_auto_20180511_2149', '2018-05-11 13:49:31.168574');
INSERT INTO `django_migrations` VALUES (32, 'user', '0012_auto_20180512_2202', '2018-05-12 14:02:29.060978');
INSERT INTO `django_migrations` VALUES (33, 'user', '0013_auto_20180512_2245', '2018-05-12 14:45:27.272933');
INSERT INTO `django_migrations` VALUES (34, 'show', '0005_auto_20180514_1707', '2018-05-14 09:07:38.884877');
INSERT INTO `django_migrations` VALUES (35, 'show', '0006_member_sex', '2018-05-14 09:19:24.752435');
INSERT INTO `django_migrations` VALUES (36, 'show', '0007_auto_20180516_1928', '2018-05-16 11:28:19.900506');
INSERT INTO `django_migrations` VALUES (37, 'tes', '0001_initial', '2018-05-26 06:39:20.306276');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('4efx310czpklhg8q5f0wfdd9d9hppemv', 'YTU5ZWRiMjY4OWE3ZDExYjg0ODMwOTk3ZjBkNDA0NDExYWE2YTllNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNjc3NGY1NDViNTExNWI5NmI3OWU4NGQxOWI0MWIzYmQwNTczZWY4In0=', '2018-05-26 02:06:02.508064');
INSERT INTO `django_session` VALUES ('et68eyvvea80bdkxq8yf0roahjlywxz8', 'MTQ1YjhjMjc1NTE3ZjYzZTkyMjg1ZTRiMjY4ZTgzNGRiZGZmMTA0Njp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyZThkODRmNjdhMjllOWJlMjgxZjdkOTU5ZTAxNzBkYzI2NWU5MWM4In0=', '2018-06-09 06:44:35.312441');
INSERT INTO `django_session` VALUES ('pglpanld7anofflvphqlaxr9j51kn5r8', 'YTU5ZWRiMjY4OWE3ZDExYjg0ODMwOTk3ZjBkNDA0NDExYWE2YTllNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNjc3NGY1NDViNTExNWI5NmI3OWU4NGQxOWI0MWIzYmQwNTczZWY4In0=', '2018-05-19 18:35:23.849541');
INSERT INTO `django_session` VALUES ('tm7v8kbl1tn4ayzasddg0f02cqdeyhn9', 'YTU5ZWRiMjY4OWE3ZDExYjg0ODMwOTk3ZjBkNDA0NDExYWE2YTllNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNjc3NGY1NDViNTExNWI5NmI3OWU4NGQxOWI0MWIzYmQwNTczZWY4In0=', '2018-05-19 19:40:20.696371');
INSERT INTO `django_session` VALUES ('udw7puxamjxbhqkune6s3sp7ipgktnj0', 'YTU5ZWRiMjY4OWE3ZDExYjg0ODMwOTk3ZjBkNDA0NDExYWE2YTllNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNjc3NGY1NDViNTExNWI5NmI3OWU4NGQxOWI0MWIzYmQwNTczZWY4In0=', '2020-05-25 14:27:01.492707');
INSERT INTO `django_session` VALUES ('z6o8zq8y5mclyq29qpvxv1qebfpuc5b9', 'YTU5ZWRiMjY4OWE3ZDExYjg0ODMwOTk3ZjBkNDA0NDExYWE2YTllNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNjc3NGY1NDViNTExNWI5NmI3OWU4NGQxOWI0MWIzYmQwNTczZWY4In0=', '2018-06-09 03:42:50.196291');

-- ----------------------------
-- Table structure for show_comment
-- ----------------------------
DROP TABLE IF EXISTS `show_comment`;
CREATE TABLE `show_comment`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `createTime` datetime(6) NOT NULL,
  `head_id` int(11) DEFAULT NULL,
  `name` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `code` int(11) NOT NULL,
  `reply` longtext CHARACTER SET utf8 COLLATE utf8_general_ci,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `show_comment_head_id_1a087e20_fk_show_headpicture_id`(`head_id`) USING BTREE,
  CONSTRAINT `show_comment_head_id_1a087e20_fk_show_headpicture_id` FOREIGN KEY (`head_id`) REFERENCES `show_headpicture` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of show_comment
-- ----------------------------
INSERT INTO `show_comment` VALUES (1, '爱特重量担当', '2018-05-11 14:03:39.905418', 1, '哲哲', 0, NULL);

-- ----------------------------
-- Table structure for show_department
-- ----------------------------
DROP TABLE IF EXISTS `show_department`;
CREATE TABLE `show_department`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `pic` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `intro` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of show_department
-- ----------------------------
INSERT INTO `show_department` VALUES (1, '前端开发', 'show/department_pic/QQ截图20180506025137_ZgUm7lp.png', '爱特前端部门负责网站的界面开发。他们用html,css,javascript等语言进行前台页面的构 建与优化。他们不仅仅满足于网站结构与功能的实现，更致力于带给用户强烈的视觉冲击和良好的交互体验。“前');
INSERT INTO `show_department` VALUES (2, '程序开发', 'show/department_pic/QQ截图20180506025137.png', '爱特工作室程序部门主要负责网站的后台开发、数据库搭建以及数据处理。成员主要基于 .NET Framework 等平台进行开发，应用 C#、JAVA、Python 等编程语言进行网络编程，实现与SQL');
INSERT INTO `show_department` VALUES (3, 'UI设计', 'show/department_pic/QQ截图20180506025137_6xkhRg6.png', '爱特UI设计部门专注于界面设计。他们以Photoshop, Illustration, Axure, After Effects 等软件为工具，以美为追求，使界面更有格调、更有品味，使网站操作更简单方');
INSERT INTO `show_department` VALUES (4, 'APP开发', 'show/department_pic/QQ截图20180506025137_AlrlqK9.png', '爱特APP开发部门是第一个跳出了传统的网页开发的部门，负责安卓端应用程序的开发。他们遵循Material Design的设计模式，利用C++、JAVA等语言进行应用程序后台的开发与构建，并使程序流畅的');

-- ----------------------------
-- Table structure for show_event
-- ----------------------------
DROP TABLE IF EXISTS `show_event`;
CREATE TABLE `show_event`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `pic` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `year` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of show_event
-- ----------------------------
INSERT INTO `show_event` VALUES (1, 'Android Ap', 'show/department_pic/QQ截图20180506025137_7C78oKT.png', 'Android App开发部门正式成立', 2017);

-- ----------------------------
-- Table structure for show_headpicture
-- ----------------------------
DROP TABLE IF EXISTS `show_headpicture`;
CREATE TABLE `show_headpicture`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `pic` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of show_headpicture
-- ----------------------------
INSERT INTO `show_headpicture` VALUES (1, '啦啦啦', 'image/HeadPicture/谢哲勇.jpg');

-- ----------------------------
-- Table structure for show_member
-- ----------------------------
DROP TABLE IF EXISTS `show_member`;
CREATE TABLE `show_member`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `photo` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `intro` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `year` int(11) NOT NULL,
  `department_id` int(11) DEFAULT NULL,
  `sex` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `show_member_department_id_d440d176_fk_show_department_id`(`department_id`) USING BTREE,
  CONSTRAINT `show_member_department_id_d440d176_fk_show_department_id` FOREIGN KEY (`department_id`) REFERENCES `show_department` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of show_member
-- ----------------------------
INSERT INTO `show_member` VALUES (1, '谢哲勇', 'image/MemberPhoto/谢哲勇.jpg', '爱特重量担当', 2017, NULL, 0);
INSERT INTO `show_member` VALUES (2, '浦泽元', 'image/MemberPhoto/浦泽元.jpg', '阿普爱曼联', 2017, NULL, 0);
INSERT INTO `show_member` VALUES (3, '陈尊龙', 'image/MemberPhoto/陈尊龙.jpg', '啊,,龙!!!', 2017, NULL, 0);
INSERT INTO `show_member` VALUES (4, '陈开拓', 'image/MemberPhoto/陈开拓.jpg', '拓拓', 2017, NULL, 0);
INSERT INTO `show_member` VALUES (5, '丁进仁', 'image/MemberPhoto/丁进仁.jpg', '丁丁', 2017, 2, 0);
INSERT INTO `show_member` VALUES (6, '李林宇', 'image/MemberPhoto/李林宇.jpg', '前任经理', 2017, 4, 0);

-- ----------------------------
-- Table structure for show_worksshow
-- ----------------------------
DROP TABLE IF EXISTS `show_worksshow`;
CREATE TABLE `show_worksshow`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `pic` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `link` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of show_worksshow
-- ----------------------------
INSERT INTO `show_worksshow` VALUES (1, '海洋技术系网站', 'show/WorksShow_pic/QQ截图20180506025137.png', 'http://it.ouc.edu.cn/SeaProject/View/Home.aspx');

-- ----------------------------
-- Table structure for tes_profile
-- ----------------------------
DROP TABLE IF EXISTS `tes_profile`;
CREATE TABLE `tes_profile`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `avatar` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tes_profile
-- ----------------------------
INSERT INTO `tes_profile` VALUES (1, 'avatars/微信图片_20171120215458.jpg');

-- ----------------------------
-- Table structure for user_fresher
-- ----------------------------
DROP TABLE IF EXISTS `user_fresher`;
CREATE TABLE `user_fresher`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sex` tinyint(1) NOT NULL,
  `yearAndMajor` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `phone` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `selfIntro` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `status_id` int(11) DEFAULT NULL,
  `registerTime` datetime(6) NOT NULL,
  `userCode` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `wantDepartment_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `user_fresher_status_id_b4e91ba9`(`status_id`) USING BTREE,
  INDEX `user_fresher_wantDepartment_id_827b732f`(`wantDepartment_id`) USING BTREE,
  CONSTRAINT `user_fresher_wantDepartment_id_827b732f_fk_show_department_id` FOREIGN KEY (`wantDepartment_id`) REFERENCES `show_department` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_fresher
-- ----------------------------
INSERT INTO `user_fresher` VALUES (4, '小花', 0, '21', '983739298@qq.com', '1221', '12', 6, '2018-05-12 13:57:21.738513', '12', 1);
INSERT INTO `user_fresher` VALUES (5, '小明', 1, '2018啦啦啦', '987@po.com', '12343252135123', '523152135215123', 2, '2018-05-13 08:54:06.877169', '13252152', 3);
INSERT INTO `user_fresher` VALUES (6, '大明', 0, '123', '132@qq.com', '345', '5532453', 3, '2018-05-13 08:54:36.450143', '53245234', 3);

-- ----------------------------
-- Table structure for user_statusdetails
-- ----------------------------
DROP TABLE IF EXISTS `user_statusdetails`;
CREATE TABLE `user_statusdetails`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` int(11) NOT NULL,
  `time` datetime(6) NOT NULL,
  `hostID_id` int(11) NOT NULL,
  `info` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `isTail` tinyint(1) NOT NULL,
  `statu_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `user_statusdetails_hostID_id_62bff682_fk_user_fresher_id`(`hostID_id`) USING BTREE,
  INDEX `user_statusdetails_statu_id_f9ebc5b7_fk_user_statusinfo_code`(`statu_id`) USING BTREE,
  CONSTRAINT `user_statusdetails_hostID_id_62bff682_fk_user_fresher_id` FOREIGN KEY (`hostID_id`) REFERENCES `user_fresher` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `user_statusdetails_statu_id_f9ebc5b7_fk_user_statusinfo_code` FOREIGN KEY (`statu_id`) REFERENCES `user_statusinfo` (`code`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 46 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_statusdetails
-- ----------------------------
INSERT INTO `user_statusdetails` VALUES (45, 1, '2018-05-14 09:11:44.510389', 6, '', 1, 3);

-- ----------------------------
-- Table structure for user_statusinfo
-- ----------------------------
DROP TABLE IF EXISTS `user_statusinfo`;
CREATE TABLE `user_statusinfo`  (
  `code` int(11) NOT NULL,
  `info` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `emailText` longtext CHARACTER SET utf8 COLLATE utf8_general_ci,
  `nextStatus_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`code`) USING BTREE,
  UNIQUE INDEX `user_statusinfo_code_4281e7d8_uniq`(`code`) USING BTREE,
  INDEX `user_statusinfo_nextStatus_id_1d56067f_fk_user_statusinfo_code`(`nextStatus_id`) USING BTREE,
  CONSTRAINT `user_statusinfo_nextStatus_id_1d56067f_fk_user_statusinfo_code` FOREIGN KEY (`nextStatus_id`) REFERENCES `user_statusinfo` (`code`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_statusinfo
-- ----------------------------
INSERT INTO `user_statusinfo` VALUES (1, '面试', '你已经进入一轮面试,请于几月几日到哪里参加,谢谢', 2);
INSERT INTO `user_statusinfo` VALUES (2, '笔试', '笔试地点2131', 3);
INSERT INTO `user_statusinfo` VALUES (3, '退出', '啦啦啦', 1);
INSERT INTO `user_statusinfo` VALUES (6, '21', '1', NULL);

SET FOREIGN_KEY_CHECKS = 1;
