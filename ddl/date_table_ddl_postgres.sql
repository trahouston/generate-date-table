-- drop table if exists `dates`;
CREATE TABLE `dates` (
  `id` int(11) NOT NULL,
  `calendar_date` date NOT NULL,
  `calendar_day` int(11) NOT NULL,
  `calendar_month` int(11) NOT NULL,
  `calendar_year` int(11) NOT NULL,
  `calendar_mon_d_y` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `calendar_m_d_y` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `reporting_y_q_w` varchar(15) COLLATE utf8_unicode_ci NOT NULL DEFAULT '0000Q0W0',
  `reporting_y_w` varchar(15) COLLATE utf8_unicode_ci NOT NULL DEFAULT '0000W0',
  `reporting_y_w_d` varchar(15) NOT NULL,
  `day_of_week_number` int(11) NOT NULL,
  `day_of_week_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `day_of_week_short_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `day_of_week_abv_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `week_number` int(11) NOT NULL,
  `week_short_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `month_number` int(11) NOT NULL,
  `month_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `month_short_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `day_of_month_number` int(11) NOT NULL,
  `quarter_number` int(11) NOT NULL,
  `quarter_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `year_number` int(11) NOT NULL,
  `year_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `day_of_year_number` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
CREATE INDEX idx_dates_calendar_date ON dates USING btree (calendar_date);
CREATE INDEX idx_dates_calendar_year ON dates USING btree (calendar_year);