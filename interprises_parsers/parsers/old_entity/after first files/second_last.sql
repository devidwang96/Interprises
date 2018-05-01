CREATE TEMPORARY TABLE `old_entity_temp` (BIN VARCHAR(1000) NOT NULL PRIMARY KEY, stat_id VARCHAR(1000) DEFAULT NULL, name_ru VARCHAR(1000) DEFAULT NULL, name_kk VARCHAR(1000) DEFAULT NULL, register_date VARCHAR(1000) DEFAULT NULL, economic_activity_code VARCHAR(1000) DEFAULT NULL COMMENT 'ОКЭД', economic_activity_codes VARCHAR(1000) DEFAULT NULL COMMENT 'ОКЭД второстепенные', company_size_code VARCHAR(1000) DEFAULT NULL COMMENT 'КРП', territory_code VARCHAR(1000) DEFAULT NULL COMMENT 'КАТО',address VARCHAR(1000) DEFAULT NULL, CEO VARCHAR(1000)  DEFAULT NULL COMMENT 'Первый руководитель', active int(5) NOT NULL DEFAULT 0, resident int(5) NOT NULL DEFAULT 1 COMMENT 'Резиденство') DEFAULT CHARSET=utf8;
CREATE TABLE IF NOT EXISTS `legal_entity_history` (id int NOT NULL PRIMARY KEY AUTO_INCREMENT, BIN VARCHAR(1000) DEFAULT NULL, stat_id VARCHAR(1000) DEFAULT NULL, name_ru VARCHAR(1000) DEFAULT NULL, name_kk VARCHAR(1000) DEFAULT NULL, register_date VARCHAR(1000) DEFAULT NULL, economic_activity_code VARCHAR(1000) DEFAULT NULL COMMENT 'ОКЭД', economic_activity_codes VARCHAR(1000) DEFAULT NULL COMMENT 'ОКЭД второстепенные', company_size_code VARCHAR(1000) DEFAULT NULL COMMENT 'КРП', territory_code VARCHAR(1000) DEFAULT NULL COMMENT 'КАТО',address VARCHAR(1000) DEFAULT NULL, CEO VARCHAR(1000)  DEFAULT NULL COMMENT 'Первый руководитель', active int(5) NOT NULL DEFAULT 0,  resident int(5) NOT NULL DEFAULT 1 COMMENT 'Резиденство');
CREATE TEMPORARY TABLE `old_entity_history_temp` (BIN VARCHAR(1000) NOT NULL PRIMARY KEY, stat_id VARCHAR(1000) DEFAULT NULL, name_ru VARCHAR(1000) DEFAULT NULL, name_kk VARCHAR(1000) DEFAULT NULL, register_date VARCHAR(1000) DEFAULT NULL, economic_activity_code VARCHAR(1000) DEFAULT NULL COMMENT 'ОКЭД', economic_activity_codes VARCHAR(1000) DEFAULT NULL COMMENT 'ОКЭД второстепенные', company_size_code VARCHAR(1000) DEFAULT NULL COMMENT 'КРП', territory_code VARCHAR(1000) DEFAULT NULL COMMENT 'КАТО',address VARCHAR(1000) DEFAULT NULL, CEO VARCHAR(1000)  DEFAULT NULL COMMENT 'Первый руководитель', active int(5) NOT NULL DEFAULT 0, resident int(5) NOT NULL DEFAULT 1 COMMENT 'Резиденство') DEFAULT CHARSET=utf8;
CREATE TEMPORARY TABLE `final_temp` (BIN VARCHAR(1000) NOT NULL PRIMARY KEY, stat_id VARCHAR(1000) DEFAULT NULL, name_ru VARCHAR(1000) DEFAULT NULL, name_kk VARCHAR(1000) DEFAULT NULL, register_date VARCHAR(1000) DEFAULT NULL, economic_activity_code VARCHAR(1000) DEFAULT NULL COMMENT 'ОКЭД', economic_activity_codes VARCHAR(1000) DEFAULT NULL COMMENT 'ОКЭД второстепенные', company_size_code VARCHAR(1000) DEFAULT NULL COMMENT 'КРП', territory_code VARCHAR(1000) DEFAULT NULL COMMENT 'КАТО',address VARCHAR(1000) DEFAULT NULL, CEO VARCHAR(1000)  DEFAULT NULL COMMENT 'Первый руководитель', active int(5) NOT NULL DEFAULT 0, resident int(5) NOT NULL DEFAULT 1 COMMENT 'Резиденство', update_date VARCHAR(50) DEFAULT NULL) DEFAULT CHARSET=utf8;
-- CREATE INDEX idx_bin_history ON legal_entity_history (BIN);
LOAD DATA LOCAL INFILE 'C:\\Users\\1\\Desktop\\parsers\\history\\01.01.18\\csv\\legal_entity.csv' IGNORE INTO TABLE old_entity_temp FIELDS TERMINATED BY '\t' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '\\' LINES TERMINATED BY '\n' IGNORE 1 LINES (BIN, stat_id, name_ru, name_kk, register_date, economic_activity_code, economic_activity_codes, company_size_code, territory_code, address, CEO, active, resident);
INSERT INTO old_entity_history_temp (BIN, stat_id, name_ru, name_kk, register_date, economic_activity_code, economic_activity_codes, company_size_code, territory_code, address, CEO, active, resident) SELECT a.BIN, a.stat_id, a.name_ru, a.name_kk, a.register_date, a.economic_activity_code, a.economic_activity_codes, a.company_size_code, a.territory_code, a.address, a.CEO, a.active, a.resident FROM old_entity_temp a, legal_entity b WHERE a.BIN = b.BIN and ( a.CEO <> b.CEO or a.name_ru <> b.name_ru or a.address <> b.address or a.company_size_code <> b.company_size_code or a.economic_activity_code <> b.economic_activity_code);
INSERT INTO final_temp (BIN, stat_id, name_ru, name_kk, register_date, economic_activity_code, economic_activity_codes, company_size_code, territory_code, address, CEO, active, resident) SELECT a.BIN, a.stat_id, a.name_ru, a.name_kk, a.register_date, a.economic_activity_code, a.economic_activity_codes, a.company_size_code, a.territory_code, a.address, a.CEO, a.active, a.resident FROM old_entity_history_temp a, legal_entity_history b WHERE a.BIN = b.BIN and ( a.CEO <> b.CEO or a.name_ru <> b.name_ru or a.address <> b.address or a.company_size_code <> b.company_size_code);
INSERT INTO legal_entity_history (BIN, stat_id, name_ru, name_kk, register_date, economic_activity_code, economic_activity_codes, company_size_code, territory_code, address, CEO, active, resident, update_date) SELECT a.BIN, a.stat_id, a.name_ru, a.name_kk, a.register_date, a.economic_activity_code, a.economic_activity_codes, a.company_size_code, a.territory_code, a.address, a.CEO, a.active, a.resident, b.date FROM final_temp a, dates b;