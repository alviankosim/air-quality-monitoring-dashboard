CREATE TABLE air_quality.monitoring (
	id int(32) auto_increment NOT NULL,
	`data` varchar(100) NULL,
	created_date DATETIME DEFAULT CURRENT_TIMESTAMP NULL,
	CONSTRAINT monitoring_PK PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;
