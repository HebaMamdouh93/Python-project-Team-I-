-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 19, 2018 at 09:19 PM
-- Server version: 5.7.21-0ubuntu0.16.04.1
-- PHP Version: 7.0.22-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `djangoBlogdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add category', 7, 'add_category'),
(20, 'Can change category', 7, 'change_category'),
(21, 'Can delete category', 7, 'delete_category'),
(22, 'Can add user cat', 8, 'add_usercat'),
(23, 'Can change user cat', 8, 'change_usercat'),
(24, 'Can delete user cat', 8, 'delete_usercat'),
(25, 'Can add post', 9, 'add_post'),
(26, 'Can change post', 9, 'change_post'),
(27, 'Can delete post', 9, 'delete_post'),
(28, 'Can add tag', 10, 'add_tag'),
(29, 'Can change tag', 10, 'change_tag'),
(30, 'Can delete tag', 10, 'delete_tag'),
(31, 'Can add post tag', 11, 'add_posttag'),
(32, 'Can change post tag', 11, 'change_posttag'),
(33, 'Can delete post tag', 11, 'delete_posttag'),
(34, 'Can add forbidden words', 12, 'add_forbiddenwords'),
(35, 'Can change forbidden words', 12, 'change_forbiddenwords'),
(36, 'Can delete forbidden words', 12, 'delete_forbiddenwords'),
(37, 'Can add comment', 13, 'add_comment'),
(38, 'Can change comment', 13, 'change_comment'),
(39, 'Can delete comment', 13, 'delete_comment'),
(40, 'Can add reply comment', 14, 'add_replycomment'),
(41, 'Can change reply comment', 14, 'change_replycomment'),
(42, 'Can delete reply comment', 14, 'delete_replycomment'),
(43, 'Can add post review', 15, 'add_postreview'),
(44, 'Can change post review', 15, 'change_postreview'),
(45, 'Can delete post review', 15, 'delete_postreview');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, '123', NULL, 1, 'Heba Mamdouh', '', '', 'hebamamdouh2016@gmail.com', 1, 1, '2018-02-03 00:00:00.000000'),
(2, '123', NULL, 0, 'Heba Akel', '', '', 'hebakel2016@gmail.com', 1, 1, '2018-02-04 00:00:00.000000'),
(3, '123', NULL, 0, 'Ahmed Ali', '', '', 'ahmedzaytoun2016@gmail.com', 1, 1, '2018-02-19 00:00:00.000000'),
(4, 'pbkdf2_sha256$20000$R2JcMpkahU7a$n/O3RccDazy/0od/LxTQi+rAdaA0bWz/Ys4JEA6MtEQ=', '2018-02-18 13:11:41.142078', 1, 'Ahmed', '', '', 'ahmedali93@gmail.com', 1, 1, '2018-02-15 16:57:32.679869'),
(5, 'pbkdf2_sha256$20000$4ZsoWeFuBLVG$/OiTo3TihVT+7JgtWDGP1MGLGa5ICXLb27LvdZTGsiM=', '2018-02-19 18:44:40.004264', 0, 'Heba', '', '', 'heba93@gmail.com', 0, 1, '2018-02-16 10:46:15.283638'),
(6, 'pbkdf2_sha256$20000$U0KUmY9rssqo$e/Z/HHZMG3eJ6dIGMdRIbhU7qwesbzr/DTiWJqaRiAM=', '2018-02-18 11:46:32.228249', 0, 'Asmaa', '', '', 'asmaa93@gmail.com', 0, 1, '2018-02-18 11:46:31.856532'),
(7, 'pbkdf2_sha256$20000$YmqMDsqzfldy$cIlnTDcYdE7TmwMUUESrFqAJvToNaFO8XUEMHRozr14=', '2018-02-18 11:50:25.192499', 0, 'AsmaaAli', '', '', 'asmaa2016@gmail.com', 0, 1, '2018-02-18 11:50:24.716218'),
(8, 'pbkdf2_sha256$20000$59gnoFm6tbns$rFIcpdzCbTH5QKNZ75qB0Gw55lTocMx4CMAaXXrmjxQ=', '2018-02-18 12:18:13.206407', 0, 'Ali', '', '', 'aliahmed93@gmail.com', 0, 0, '2018-02-18 12:18:12.840152'),
(9, 'pbkdf2_sha256$20000$PYyiaP8zFoLW$cllstCl1IUwLF0/3rrD4api8WQ8jFn+G9ccrR1eB39I=', '2018-02-18 21:44:21.312552', 0, 'Mohamed', '', '', 'logy.mamdouh93@gmail.com', 0, 1, '2018-02-18 21:44:20.988092');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'social_Blog', 'category'),
(13, 'social_Blog', 'comment'),
(12, 'social_Blog', 'forbiddenwords'),
(9, 'social_Blog', 'post'),
(15, 'social_Blog', 'postreview'),
(11, 'social_Blog', 'posttag'),
(14, 'social_Blog', 'replycomment'),
(10, 'social_Blog', 'tag'),
(8, 'social_Blog', 'usercat');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2018-02-14 16:40:08.520712'),
(2, 'auth', '0001_initial', '2018-02-14 16:40:15.946117'),
(3, 'admin', '0001_initial', '2018-02-14 16:40:18.015763'),
(4, 'contenttypes', '0002_remove_content_type_name', '2018-02-14 16:40:19.400246'),
(5, 'auth', '0002_alter_permission_name_max_length', '2018-02-14 16:40:19.514021'),
(6, 'auth', '0003_alter_user_email_max_length', '2018-02-14 16:40:19.615081'),
(7, 'auth', '0004_alter_user_username_opts', '2018-02-14 16:40:19.675923'),
(8, 'auth', '0005_alter_user_last_login_null', '2018-02-14 16:40:20.274561'),
(9, 'auth', '0006_require_contenttypes_0002', '2018-02-14 16:40:20.308215'),
(10, 'sessions', '0001_initial', '2018-02-14 16:40:20.835040'),
(11, 'social_Blog', '0001_initial', '2018-02-14 16:40:21.138037'),
(12, 'social_Blog', '0002_category', '2018-02-14 16:40:21.517635'),
(13, 'social_Blog', '0003_usercat', '2018-02-14 16:40:23.685361'),
(14, 'social_Blog', '0004_post', '2018-02-14 16:40:25.563089'),
(15, 'social_Blog', '0005_tag', '2018-02-14 16:40:25.967183'),
(16, 'social_Blog', '0006_posttag', '2018-02-14 16:40:27.767687'),
(17, 'social_Blog', '0007_forbiddenwords', '2018-02-14 16:40:28.036855'),
(18, 'social_Blog', '0008_auto_20180214_1515', '2018-02-14 16:40:30.765506'),
(19, 'social_Blog', '0009_auto_20180214_1608', '2018-02-14 16:40:36.507237');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `social_Blog_category`
--

CREATE TABLE `social_Blog_category` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `social_Blog_category`
--

INSERT INTO `social_Blog_category` (`id`, `name`) VALUES
(1, 'News'),
(2, 'Politics'),
(3, 'Sports'),
(4, 'Fashion');

-- --------------------------------------------------------

--
-- Table structure for table `social_Blog_comment`
--

CREATE TABLE `social_Blog_comment` (
  `id` int(11) NOT NULL,
  `commmentText` varchar(255) NOT NULL,
  `comTime` datetime(6) NOT NULL,
  `post_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `social_Blog_comment`
--

INSERT INTO `social_Blog_comment` (`id`, `commmentText`, `comTime`, `post_id`, `user_id`) VALUES
(1, 'nm nm', '2018-02-08 00:00:00.000000', 1, 1),
(2, 'mkm,', '2018-02-21 00:00:00.000000', 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `social_Blog_forbiddenwords`
--

CREATE TABLE `social_Blog_forbiddenwords` (
  `id` int(11) NOT NULL,
  `word` varchar(255) NOT NULL,
  `wordLen` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `social_Blog_post`
--

CREATE TABLE `social_Blog_post` (
  `id` int(11) NOT NULL,
  `text` varchar(255) NOT NULL,
  `img` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `likes` int(11) DEFAULT NULL,
  `unLikes` int(11) DEFAULT NULL,
  `cat_id` int(11) NOT NULL,
  `publish_date` datetime(6)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `social_Blog_post`
--

INSERT INTO `social_Blog_post` (`id`, `text`, `img`, `title`, `likes`, `unLikes`, `cat_id`, `publish_date`) VALUES
(1, 'ustralian Conservative\'s Senator Cory Bernardi discusses the moral implications of Deputy Prime Minister Barnaby Joyce\'s marriage breakdown and his relationship with a former staffer.', 'images/1.jpeg', 'Politician-staffer relations unreasonable: Bernardi', 0, 0, 2, '2018-02-26 06:15:11.000000'),
(2, 'ustralian Conservative\'s Senator Cory Bernardi discusses the moral implications of Deputy Prime Minister Barnaby Joyce\'s marriage breakdown and his relationship with a former staffer.', 'images/2.jpeg', 'Politician-staffer relations unreasonable: Bernardi', 0, 0, 3, '2018-02-28 09:11:08.149149'),
(3, 'ustralian Conservative\'s Senator Cory Bernardi discusses the moral implications of Deputy Prime Minister Barnaby Joyce\'s marriage breakdown and his relationship with a former staffer.', 'images/3.jpeg', 'Politician-staffer relations unreasonable: Bernardi heba', 0, 0, 1, NULL),
(4, 'ustralian Conservative\'s Senator Cory Bernardi discusses the moral implications of Deputy Prime Minister Barnaby Joyce\'s marriage breakdown and his relationship with a former staffer.', 'images/4.jpeg', 'Politician-staffer relations unreasonable: Bernardi', 0, 0, 1, '2018-02-09 02:11:07.000000'),
(5, 'ustralian Conservative\'s Senator Cory Bernardi discusses the moral implications of Deputy Prime Minister Barnaby Joyce\'s marriage breakdown and his relationship with a former staffer.', 'images/5.jpeg', 'Politician-staffer relations unreasonable: Bernardi', 0, 0, 4, '2018-02-12 05:09:09.103000'),
(6, 'lvlznvlnlzkncln', 'images/5.jpeg', 'Sport mohamed salah', 0, 0, 3, '2018-02-20 00:00:00.000000');

-- --------------------------------------------------------

--
-- Table structure for table `social_Blog_postreview`
--

CREATE TABLE `social_Blog_postreview` (
  `id` int(11) NOT NULL,
  `post_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `review` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `social_Blog_posttag`
--

CREATE TABLE `social_Blog_posttag` (
  `id` int(11) NOT NULL,
  `post_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `social_Blog_posttag`
--

INSERT INTO `social_Blog_posttag` (`id`, `post_id`, `tag_id`) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 1, 2),
(4, 5, 3),
(5, 6, 3);

-- --------------------------------------------------------

--
-- Table structure for table `social_Blog_replycomment`
--

CREATE TABLE `social_Blog_replycomment` (
  `id` int(11) NOT NULL,
  `replyText` varchar(255) NOT NULL,
  `repTime` datetime(6) NOT NULL,
  `comment_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `social_Blog_tag`
--

CREATE TABLE `social_Blog_tag` (
  `id` int(11) NOT NULL,
  `tagName` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `social_Blog_tag`
--

INSERT INTO `social_Blog_tag` (`id`, `tagName`) VALUES
(1, 'sport'),
(2, 'mohamedsalah'),
(3, 'fashion');

-- --------------------------------------------------------

--
-- Table structure for table `social_Blog_usercat`
--

CREATE TABLE `social_Blog_usercat` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `cat_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `social_Blog_usercat`
--

INSERT INTO `social_Blog_usercat` (`id`, `user_id`, `cat_id`) VALUES
(1, 2, 1),
(2, 3, 1),
(3, 2, 2),
(7, 4, 3),
(14, 4, 1),
(16, 9, 2),
(18, 9, 1),
(19, 9, 4);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  ADD KEY `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `content_type_id` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  ADD KEY `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `djang_content_type_id_697914295151027a_fk_django_content_type_id` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_de54fa62` (`expire_date`);

--
-- Indexes for table `social_Blog_category`
--
ALTER TABLE `social_Blog_category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `social_Blog_comment`
--
ALTER TABLE `social_Blog_comment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `social_Blog_comment_f3aa1999` (`post_id`),
  ADD KEY `social_Blog_comment_e8701ad4` (`user_id`);

--
-- Indexes for table `social_Blog_forbiddenwords`
--
ALTER TABLE `social_Blog_forbiddenwords`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `social_Blog_post`
--
ALTER TABLE `social_Blog_post`
  ADD PRIMARY KEY (`id`),
  ADD KEY `social_Blog_p_cat_id_3ba0148f424a2804_fk_social_Blog_category_id` (`cat_id`);

--
-- Indexes for table `social_Blog_postreview`
--
ALTER TABLE `social_Blog_postreview`
  ADD PRIMARY KEY (`id`),
  ADD KEY `social_Blog_post_post_id_13db92ebd1fabedb_fk_social_Blog_post_id` (`post_id`),
  ADD KEY `social_Blog_postreview_user_id_1d2b84b5134cc05c_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `social_Blog_posttag`
--
ALTER TABLE `social_Blog_posttag`
  ADD PRIMARY KEY (`id`),
  ADD KEY `social_Blog_post_post_id_34ff2d79cdfade0c_fk_social_Blog_post_id` (`post_id`),
  ADD KEY `social_Blog_postta_tag_id_28c1528df9d10805_fk_social_Blog_tag_id` (`tag_id`);

--
-- Indexes for table `social_Blog_replycomment`
--
ALTER TABLE `social_Blog_replycomment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `social_Blo_comment_id_1ca2465683cdc87a_fk_social_Blog_comment_id` (`comment_id`),
  ADD KEY `social_Blog_replycommen_user_id_461616b78a328e8f_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `social_Blog_tag`
--
ALTER TABLE `social_Blog_tag`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `social_Blog_usercat`
--
ALTER TABLE `social_Blog_usercat`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;
--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
--
-- AUTO_INCREMENT for table `social_Blog_category`
--
ALTER TABLE `social_Blog_category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `social_Blog_comment`
--
ALTER TABLE `social_Blog_comment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `social_Blog_forbiddenwords`
--
ALTER TABLE `social_Blog_forbiddenwords`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `social_Blog_post`
--
ALTER TABLE `social_Blog_post`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `social_Blog_postreview`
--
ALTER TABLE `social_Blog_postreview`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `social_Blog_posttag`
--
ALTER TABLE `social_Blog_posttag`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `social_Blog_replycomment`
--
ALTER TABLE `social_Blog_replycomment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `social_Blog_tag`
--
ALTER TABLE `social_Blog_tag`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `social_Blog_usercat`
--
ALTER TABLE `social_Blog_usercat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `social_Blog_comment`
--
ALTER TABLE `social_Blog_comment`
  ADD CONSTRAINT `social_Blog_comm_post_id_190aeee79714f2fb_fk_social_Blog_post_id` FOREIGN KEY (`post_id`) REFERENCES `social_Blog_post` (`id`),
  ADD CONSTRAINT `social_Blog_comment_user_id_43c5317dbd5e84a6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `social_Blog_post`
--
ALTER TABLE `social_Blog_post`
  ADD CONSTRAINT `social_Blog_p_cat_id_3ba0148f424a2804_fk_social_Blog_category_id` FOREIGN KEY (`cat_id`) REFERENCES `social_Blog_category` (`id`);

--
-- Constraints for table `social_Blog_postreview`
--
ALTER TABLE `social_Blog_postreview`
  ADD CONSTRAINT `social_Blog_post_post_id_13db92ebd1fabedb_fk_social_Blog_post_id` FOREIGN KEY (`post_id`) REFERENCES `social_Blog_post` (`id`),
  ADD CONSTRAINT `social_Blog_postreview_user_id_1d2b84b5134cc05c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `social_Blog_posttag`
--
ALTER TABLE `social_Blog_posttag`
  ADD CONSTRAINT `social_Blog_post_post_id_34ff2d79cdfade0c_fk_social_Blog_post_id` FOREIGN KEY (`post_id`) REFERENCES `social_Blog_post` (`id`),
  ADD CONSTRAINT `social_Blog_postta_tag_id_28c1528df9d10805_fk_social_Blog_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `social_Blog_tag` (`id`);

--
-- Constraints for table `social_Blog_replycomment`
--
ALTER TABLE `social_Blog_replycomment`
  ADD CONSTRAINT `social_Blo_comment_id_1ca2465683cdc87a_fk_social_Blog_comment_id` FOREIGN KEY (`comment_id`) REFERENCES `social_Blog_comment` (`id`),
  ADD CONSTRAINT `social_Blog_replycommen_user_id_461616b78a328e8f_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
