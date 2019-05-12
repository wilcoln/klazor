BEGIN;
--
-- Create model ACategoryCourse
--
CREATE TABLE `a_category_course` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY);
--
-- Create model ACourseInstructor
--
CREATE TABLE `a_course_instructor` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY);
--
-- Create model ACourseResource
--
CREATE TABLE `a_course_resource` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY);
--
-- Create model ASchoolCourseItem
--
CREATE TABLE `a_school_course_item` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY);
--
-- Create model AWeekItem
--
CREATE TABLE `a_week_item` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY);
--
-- Create model Category
--
CREATE TABLE `category` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `title` varchar(20) NULL);
--
-- Create model Course
--
CREATE TABLE `course` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `title` varchar(50) NULL);
--
-- Create model Instructor
--
CREATE TABLE `instructor` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `title` varchar(20) NULL, `link` longtext NULL);
--
-- Create model Item
--
CREATE TABLE `item` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `title` varchar(50) NULL, `type` varchar(2) NULL, `content` longtext NULL, `status` varchar(9) NULL, `next` integer NULL, `prev` integer NULL);
--
-- Create model MoocCourse
--
CREATE TABLE `mooc_course` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `course_id` integer NOT NULL);
--
-- Create model Resource
--
CREATE TABLE `resource` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `title` varchar(60) NULL);
--
-- Create model School
--
CREATE TABLE `school` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `admissions_link` longtext NULL, `programs_link` longtext NULL);
--
-- Create model Week
--
CREATE TABLE `week` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `title` varchar(20) NULL, `mooc_course_id` integer NOT NULL);
--
-- Create model SchoolCourse
--
CREATE TABLE `school_course` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `year` smallint NULL, `semester` smallint NULL, `course_id` integer NOT NULL);
--
-- Create model Note
--
CREATE TABLE `note` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `content` longtext NULL, `item_id` integer NOT NULL);
--
-- Create model NonSchool
--
CREATE TABLE `non_school` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `instructor_id` integer NOT NULL);
--
-- Add field instructors to course
--
--
-- Add field resources to course
--
--
-- Add field item to aweekitem
--
ALTER TABLE `a_week_item` ADD COLUMN `item_id` integer NOT NULL;
--
-- Add field week to aweekitem
--
ALTER TABLE `a_week_item` ADD COLUMN `week_id` integer NOT NULL;
--
-- Add field item to aschoolcourseitem
--
ALTER TABLE `a_school_course_item` ADD COLUMN `item_id` integer NOT NULL;
--
-- Add field school_course to aschoolcourseitem
--
ALTER TABLE `a_school_course_item` ADD COLUMN `school_course_id` integer NOT NULL;
--
-- Add field course to acourseresource
--
ALTER TABLE `a_course_resource` ADD COLUMN `course_id` integer NOT NULL;
--
-- Add field resource to acourseresource
--
ALTER TABLE `a_course_resource` ADD COLUMN `resource_id` integer NOT NULL;
--
-- Add field course to acourseinstructor
--
ALTER TABLE `a_course_instructor` ADD COLUMN `course_id` integer NOT NULL;
--
-- Add field instructor to acourseinstructor
--
ALTER TABLE `a_course_instructor` ADD COLUMN `instructor_id` integer NOT NULL;
--
-- Add field category to acategorycourse
--
ALTER TABLE `a_category_course` ADD COLUMN `category_id` integer NOT NULL;
--
-- Add field course to acategorycourse
--
ALTER TABLE `a_category_course` ADD COLUMN `course_id` integer NOT NULL;
--
-- Alter unique_together for aweekitem (1 constraint(s))
--
ALTER TABLE `a_week_item` ADD CONSTRAINT `a_week_item_week_id_item_id_39c6e523_uniq` UNIQUE (`week_id`, `item_id`);
--
-- Alter unique_together for aschoolcourseitem (1 constraint(s))
--
ALTER TABLE `a_school_course_item` ADD CONSTRAINT `a_school_course_item_school_course_id_item_id_e299f9b3_uniq` UNIQUE (`school_course_id`, `item_id`);
--
-- Alter unique_together for acourseresource (1 constraint(s))
--
ALTER TABLE `a_course_resource` ADD CONSTRAINT `a_course_resource_resource_id_course_id_dd5a5b8f_uniq` UNIQUE (`resource_id`, `course_id`);
--
-- Alter unique_together for acourseinstructor (1 constraint(s))
--
ALTER TABLE `a_course_instructor` ADD CONSTRAINT `a_course_instructor_course_id_instructor_id_27c60302_uniq` UNIQUE (`course_id`, `instructor_id`);
--
-- Alter unique_together for acategorycourse (1 constraint(s))
--
ALTER TABLE `a_category_course` ADD CONSTRAINT `a_category_course_category_id_course_id_7c0cc4bf_uniq` UNIQUE (`category_id`, `course_id`);
ALTER TABLE `mooc_course` ADD CONSTRAINT `mooc_course_course_id_d420cf76_fk_course_id` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`);
ALTER TABLE `week` ADD CONSTRAINT `week_mooc_course_id_f801ff0e_fk_mooc_course_id` FOREIGN KEY (`mooc_course_id`) REFERENCES `mooc_course` (`id`);
ALTER TABLE `school_course` ADD CONSTRAINT `school_course_course_id_701ccafe_fk_course_id` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`);
ALTER TABLE `note` ADD CONSTRAINT `note_item_id_97a8dda5_fk_item_id` FOREIGN KEY (`item_id`) REFERENCES `item` (`id`);
ALTER TABLE `non_school` ADD CONSTRAINT `non_school_instructor_id_4522c059_fk_instructor_id` FOREIGN KEY (`instructor_id`) REFERENCES `instructor` (`id`);
ALTER TABLE `a_week_item` ADD CONSTRAINT `a_week_item_item_id_c8c34cd6_fk_item_id` FOREIGN KEY (`item_id`) REFERENCES `item` (`id`);
ALTER TABLE `a_week_item` ADD CONSTRAINT `a_week_item_week_id_682ac8e3_fk_week_id` FOREIGN KEY (`week_id`) REFERENCES `week` (`id`);
ALTER TABLE `a_school_course_item` ADD CONSTRAINT `a_school_course_item_item_id_e9cb3486_fk_item_id` FOREIGN KEY (`item_id`) REFERENCES `item` (`id`);
ALTER TABLE `a_school_course_item` ADD CONSTRAINT `a_school_course_item_school_course_id_a2084019_fk_school_co` FOREIGN KEY (`school_course_id`) REFERENCES `school_course` (`id`);
ALTER TABLE `a_course_resource` ADD CONSTRAINT `a_course_resource_course_id_785208a8_fk_course_id` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`);
ALTER TABLE `a_course_resource` ADD CONSTRAINT `a_course_resource_resource_id_53195114_fk_resource_id` FOREIGN KEY (`resource_id`) REFERENCES `resource` (`id`);
ALTER TABLE `a_course_instructor` ADD CONSTRAINT `a_course_instructor_course_id_dbeb3636_fk_course_id` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`);
ALTER TABLE `a_course_instructor` ADD CONSTRAINT `a_course_instructor_instructor_id_4113b847_fk_instructor_id` FOREIGN KEY (`instructor_id`) REFERENCES `instructor` (`id`);
ALTER TABLE `a_category_course` ADD CONSTRAINT `a_category_course_category_id_7005674b_fk_category_id` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`);
ALTER TABLE `a_category_course` ADD CONSTRAINT `a_category_course_course_id_af686970_fk_course_id` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`);
COMMIT;
