CREATE TABLE `requests` (
  `id` int NOT NULL AUTO_INCREMENT,
  `coordinates` text NOT NULL,
  `description` text,
  `size` int NOT NULL,
  `plug_id` int,
  `done_plug` bool DEFAULT FALSE,
  `done_client` bool DEFAULT FALSE,
  PRIMARY KEY (`id`)
);
