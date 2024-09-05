-- Keep a log of any SQL queries you execute as you solve the mystery.

SELECT description FROM crime_scene_reports WHERE
   ...> day = 28 and month = 7 and year = 2023 and street LIKE "Humphrey Street"
   ...> ;

SELECT activity FROM bakery_security_logs WHERE day = 28 and month = 7 and year = 2023;

SELECT activity,hour,minute,license_plate FROM bakery_security_logs WHERE day = 28 a
nd month = 7 and year = 2023;

SELECT activity,hour,minute,license_plate FROM bakery_security_logs WHERE day = 28 a
nd month = 7 and year = 2023 and license_plate LIKE "13FNH73";

SELECT transcript FROM interviews WHERE year = 2023 and month = 7 and day = 28;

SELECT account_number, transaction_type, amount  FROM atm_transactions WHERE year = 2023 and month = 7 and day = 28 and atm_location LIKE "Leggett Street";

SELECT caller, receiver, duration FROM phone_calls WHERE year = 2023 and month = 7 a
nd day = 28;

SELECT caller, receiver, duration FROM phone_calls WHERE year = 2023 and month = 7 and day = 28 and duration <= 60;

SELECT DISTINCT name,phone_number,license_plate FROM people join phone_calls WHERE year = 2023 and month = 7 and day = 28 and duration <=60 and license_plate not NULL and phone_number not NULL ORDER BY name;

SELECT * FROM people WHERE license_plate LIKE "5P2BI95"
   ...> ;

SELECT * FROM people WHERE license_plate LIKE "94KL13X";

SELECT * FROM people WHERE license_plate LIKE "6P58WS2";

SELECT * FROM people WHERE license_plate LIKE "4328GD8";

SELECT * FROM people WHERE license_plate LIKE "G412CB7";

SELECT * FROM people WHERE license_plate LIKE "L93JTIZ";

SELECT * FROM people WHERE license_plate LIKE "322W7JE";

SELECT * FROM people WHERE license_plate LIKE "0NTHK55";

SELECT name,phone_number,license_plate FROM people WHERE phone_number LIKE "(996) 555-8899";

SELECT name,phone_number,license_plate FROM people WHERE phone_number LIKE "(892) 555-8872";

SELECT name,phone_number,license_plate FROM people WHERE phone_number LIKE "(375) 555-8161";

SELECT name,phone_number,license_plate FROM people WHERE phone_number LIKE "(725) 555-3243";

SELECT id FROM people WHERE name LIKE "SOFIA";

SELECT id FROM people WHERE name LIKE "KELSEY";

SELECT id FROM people WHERE name LIKE "DIANA";

SELECT id FROM people WHERE name LIKE "BRUCE";

SELECT account_number FROM bank_accounts WHERE person_id LIKE "398010";

SELECT account_number FROM bank_accounts WHERE person_id LIKE "560886";

SELECT account_number FROM bank_accounts WHERE person_id LIKE "514354";

SELECT account_number FROM bank_accounts WHERE person_id LIKE "686048";

SELECT * FROM airports WHERE city LIKE "fiftyville";

SELECT hour,minute FROM flights WHERE origin_airport_id LIKE "8";

SELECT hour,minute FROM flights WHERE origin_airport_id LIKE "8" ORDER BY hour,minute;

SELECT * FROM flights WHERE origin_airport_id LIKE "8" and hour < 10 ORDER BY hour,minute;

SELECT * FROM airports WHERE id LIKE "4";

SELECT * FROM passengers WHERE flight_id LIKE "36";

SELECT * FROM people WHERE name LIKE "BRUCE";

SELECT * FROM people WHERE name LIKE "DIANA";

SELECT phone_number FROM people WHERE name LIKE "BRUCE";

SELECT receiver FROM phone_calls WHERE caller LIKE "(367) 555-5533";

SELECT receiver FROM phone_calls WHERE caller LIKE "(367) 555-5533" and duration <60;

SELECT receiver FROM phone_calls WHERE caller LIKE "(367) 555-5533" and duration <60 and day = 28 and month = 7 and year = 2023;

SELECT * FROM people WHERE phone_number LIKE "(375) 555-8161";
