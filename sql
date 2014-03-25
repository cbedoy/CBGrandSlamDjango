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
    "year" date NOT NULL,
    "name" text NOT NULL,
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
    "wins" integer NOT NULL,
    "losts" integer NOT NULL,
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
COMMIT;
