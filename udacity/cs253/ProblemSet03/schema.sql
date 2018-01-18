drop table if exists entries;
create table entries (
	post_id integer primary key autoincrement,
	update_date date,
	post_subject text not null,
	post_content text not null
);