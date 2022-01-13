
CREATE TABLE `role` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO `role` VALUES (1,'teacher'),(2,'student');

DROP TABLE IF EXISTS `subject`;

CREATE TABLE `subject` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO `subject` VALUES (1,'data structures'),(2,'algorithms'),(3,'probability'),(4,'micro processor'),(5,'english');



DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `mobile` varchar(15) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO `user` VALUES (1,'amar','1111',NULL),(2,'rahul','2222',NULL),(3,'syed','3333',NULL),(4,'rakesh','4444',NULL),(5,'vinay','5555',NULL),(6,'sindhu','6666',NULL);

DROP TABLE IF EXISTS `user_role`;

CREATE TABLE `user_role` (
  `user_id` int NOT NULL,
  `role_id` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
);

INSERT INTO `user_role` VALUES (1,1,1),(2,2,2),(3,2,3),(4,1,4),(5,1,5),(5,2,6),(6,1,7),(6,2,8);


DROP TABLE IF EXISTS `user_role_subject`;

CREATE TABLE `user_role_subject` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_role_id` int DEFAULT NULL,
  `subject_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO `user_role_subject` VALUES (1,1,1),(2,1,2),(3,1,3),(4,2,1),(5,2,2),(6,2,3),(7,2,4),(8,2,5),(9,3,3),(10,3,4),(11,3,5),(18,4,1),(19,4,4),(20,5,5),(21,6,1),(22,7,5),(23,8,2),(24,8,3);

