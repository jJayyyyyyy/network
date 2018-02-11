drop table if exists posts;
drop table if exists artworks;
drop table if exists users;

create table posts (
	id integer primary key autoincrement,
	update_date date not null,
	subject text not null,
	content text not null);

create table artworks (
	id integer primary key autoincrement,
	subject text not null,
	content text not null);

create table users (
	id integer primary key autoincrement,
	username text not null unique,
	pw_hash text not null,
	email text);