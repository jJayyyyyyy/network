drop table if exists posts;
drop table if exists artworks;

create table posts (
	post_id integer primary key autoincrement,
	update_date date not null,
	subject text not null,
	content text not null);

create table artworks (
	artwork_id integer primary key autoincrement,
	subject text not null,
	content text not null);
