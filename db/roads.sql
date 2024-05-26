CREATE TABLE `roads` (
  `id` int NOT NULL AUTO_INCREMENT,
  `coordinates` text NOT NULL,
  `snow_mm` int NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
);
