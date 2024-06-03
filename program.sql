CREATE SCHEMA `video_admin` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci ;

CREATE TABLE `video_admin`.`user` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `password` VARCHAR(255) NOT NULL,
  `username` VARCHAR(255) NOT NULL,
  `phone` VARCHAR(20) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `gender` ENUM('M', 'W', 'U') NOT NULL DEFAULT 'U',
  `regdate` DATE NOT NULL,
  `level` TINYINT(4) UNSIGNED NOT NULL DEFAULT 0,
  `introduction` TEXT(255) NULL DEFAULT NULL,
  `is_admin` INT NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `phone_UNIQUE` (`phone` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

CREATE TABLE `video_admin`.`level` (
  `level` TINYINT(4) UNSIGNED NOT NULL,
  `video_quality` INT NOT NULL,
  `comment` INT NOT NULL,
  `danmu_level` INT NOT NULL,
  UNIQUE INDEX `level_UNIQUE` (`level` ASC) VISIBLE,
  PRIMARY KEY (`level`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

ALTER TABLE `video_admin`.`user` 
ADD INDEX `level_user_idx` (`level` ASC) VISIBLE;
;
ALTER TABLE `video_admin`.`user` 
ADD CONSTRAINT `level_user`
  FOREIGN KEY (`level`)
  REFERENCES `video_admin`.`level` (`level`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

CREATE TABLE `video_admin`.`work` (
  `id` INT NOT NULL AUTO_INCREMENT
  `title` VARCHAR(45) NOT NULL,
  `id_author` INT UNSIGNED NOT NULL,
  `introduction` TEXT(255) NULL,
  `id_category` INT UNSIGNED NOT NULL,
  `id_partition` INT UNSIGNED NOT NULL,
  `view_number` INT NOT NULL,
  `like_number` INT NOT NULL,
  `comment_number` INT NOT NULL,
  `upload_date` DATE NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE `video_admin`.`partition` (
  `id` INT UNSIGNED NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

ALTER TABLE `video_admin`.`partition` 
ADD COLUMN `introduction` TEXT(255) NULL AFTER `name`;

CREATE TABLE `video_admin`.`category` (
  `id` INT UNSIGNED NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `introduction` TEXT(255) NULL,
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

ALTER TABLE `video_admin`.`work` 
ADD INDEX `work_category_idx` (`id_category` ASC) VISIBLE;
;
ALTER TABLE `video_admin`.`work` 
ADD CONSTRAINT `work_partition`
  FOREIGN KEY (`id_partition`)
  REFERENCES `video_admin`.`partition` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `work_category`
  FOREIGN KEY (`id_category`)
  REFERENCES `video_admin`.`category` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
ALTER TABLE `video_admin`.`work` 
ADD INDEX `work_user_idx` (`id_author` ASC) VISIBLE;
;
ALTER TABLE `video_admin`.`work` 
ADD CONSTRAINT `work_user`
  FOREIGN KEY (`id_author`)
  REFERENCES `video_admin`.`user` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

CREATE TABLE `video_admin`.`comment` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `comment_person_id` INT UNSIGNED NOT NULL,
  `work_id` INT NOT NULL,
  `content` TEXT(255) NOT NULL,
  `date` DATE NOT NULL,
  INDEX `comment_workid_idx` (`work_id` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  CONSTRAINT `comment_person`
    FOREIGN KEY (`comment_person_id`)
    REFERENCES `video_admin`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `comment_workid`
    FOREIGN KEY (`work_id`)
    REFERENCES `video_admin`.`work` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


