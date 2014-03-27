BEGIN;
CREATE TABLE "game_country" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(45) NOT NULL
)
;
CREATE TABLE "game_location" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(45) NOT NULL,
    "longitud" real NOT NULL,
    "latitud" real NOT NULL,
    "country_id" integer NOT NULL REFERENCES "game_country" ("id")
)
;
CREATE TABLE "game_tournament" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(45) NOT NULL,
    "year" integer NOT NULL,
    "description" text NOT NULL,
    "country_id" integer NOT NULL REFERENCES "game_country" ("id")
)
;
CREATE TABLE "game_referee" (
    "id" integer NOT NULL PRIMARY KEY,
    "firstName" varchar(45) NOT NULL,
    "lastName" varchar(45) NOT NULL,
    "time" varchar(45) NOT NULL
)
;
CREATE TABLE "game_trainer" (
    "id" integer NOT NULL PRIMARY KEY,
    "firstName" varchar(45) NOT NULL,
    "lastName" varchar(45) NOT NULL,
    "initialDate" date NOT NULL,
    "lastDate" date NOT NULL
)
;
CREATE TABLE "game_nationality" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(45) NOT NULL,
    "link" varchar(150) NOT NULL,
    "abreviature" varchar(3) NOT NULL
)
;
CREATE TABLE "game_player" (
    "id" integer NOT NULL PRIMARY KEY,
    "firstName" varchar(45) NOT NULL,
    "lastName" varchar(45) NOT NULL,
    "age" integer NOT NULL,
    "sex" varchar(10) NOT NULL,
    "height" real NOT NULL,
    "weight" real NOT NULL,
    "games" integer NOT NULL,
    "wins" integer NOT NULL,
    "lost" integer NOT NULL,
    "web" varchar(45),
    "facebook" varchar(45),
    "telephone" varchar(45),
    "nationality_id" integer NOT NULL REFERENCES "game_nationality" ("id"),
    "trainer_id" integer NOT NULL REFERENCES "game_trainer" ("id")
)
;
CREATE TABLE "game_modality" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(45) NOT NULL
)
;
CREATE TABLE "game_game" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(45) NOT NULL,
    "trainer_id" integer NOT NULL REFERENCES "game_trainer" ("id"),
    "referee_id" integer NOT NULL REFERENCES "game_referee" ("id"),
    "player_id" integer NOT NULL REFERENCES "game_player" ("id"),
    "tournament_id" integer NOT NULL REFERENCES "game_tournament" ("id")
)
;
CREATE TABLE "game_award" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(45) NOT NULL,
    "amount" real NOT NULL,
    "description" text NOT NULL,
    "tournament_id" integer NOT NULL REFERENCES "game_tournament" ("id"),
    "player_id" integer NOT NULL REFERENCES "game_player" ("id"),
    "trainer_id" integer NOT NULL REFERENCES "game_trainer" ("id")
)
;
CREATE TABLE "game_category" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(45) NOT NULL,
    "abreviature" varchar(3) NOT NULL
)
;
CREATE TABLE "game_doubleteam" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(45) NOT NULL,
    "facebook" varchar(45),
    "twitter" varchar(45),
    "playerA_id" integer NOT NULL REFERENCES "game_player" ("id"),
    "playerB_id" integer NOT NULL REFERENCES "game_player" ("id")
)
;
CREATE TABLE "game_singleteam" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(45) NOT NULL,
    "facebook" varchar(45),
    "twitter" varchar(45),
    "player_id" integer NOT NULL REFERENCES "game_player" ("id")
)
;
COMMIT;