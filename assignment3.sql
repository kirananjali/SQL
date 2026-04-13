USE sakila;
-- 1. display all customer details who have made more than 5 payments. (USING VIEW)
CREATE VIEW customer_payment_counts AS
SELECT customer_id, COUNT(*) AS payment_count
FROM payment
GROUP BY customer_id;

SELECT c.*
FROM customer c
JOIN customer_payment_counts v 
  ON c.customer_id = v.customer_id
WHERE v.payment_count > 5;
-- 2. Find the names of actors who have acted in more than 10 films. (USING TEMP TABLE)
CREATE TEMPORARY TABLE actor_film_counts AS
SELECT actor_id, COUNT(film_id) AS film_count
FROM film_actor
GROUP BY actor_id;

SELECT a.first_name, a.last_name
FROM actor a
JOIN actor_film_counts t 
  ON a.actor_id = t.actor_id
WHERE t.film_count > 10;
-- 3. Find the names of customers who never made a payment. (USING CTE)
WITH paid_customers AS (
    SELECT DISTINCT customer_id
    FROM payment
)
SELECT *
FROM customer
WHERE customer_id NOT IN (SELECT customer_id FROM paid_customers);
-- 4. List all films whose rental rate is higher than the average rental rate of all films. (USING CTE)
WITH avg_rate AS (
    SELECT AVG(rental_rate) AS avg_val
    FROM film
)
SELECT title, rental_rate
FROM film, avg_rate
WHERE film.rental_rate > avg_val;
-- 5. List the titles of films that were never rented. (USING CTE)
WITH rented_films AS (
    SELECT DISTINCT i.film_id
    FROM inventory i
    JOIN rental r ON i.inventory_id = r.inventory_id
)
SELECT title
FROM film
WHERE film_id NOT IN (SELECT film_id FROM rented_films);
-- SUBQUERIES
-- 6. Display the customers who rented films in the same month as customer with ID 5.
SELECT DISTINCT c.customer_id, c.first_name, c.last_name
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
WHERE MONTH(r.rental_date) IN (
    SELECT DISTINCT MONTH(rental_date)
    FROM rental
    WHERE customer_id = 5
);
-- 7. Find all staff members who handled a payment greater than the average payment amount.
SELECT DISTINCT s.staff_id, s.first_name, s.last_name
FROM staff s
JOIN payment p ON s.staff_id = p.staff_id
WHERE p.amount > (
    SELECT AVG(amount)
    FROM payment
);
-- 8. Show the title and rental duration of films whose rental duration is greater than the average.
SELECT title, rental_duration
FROM film
WHERE rental_duration > (
    SELECT AVG(rental_duration)
    FROM film
);
-- 9. Find all customers who have the same address as customer with ID 1.
SELECT first_name, last_name
FROM customer
WHERE address_id = (
    SELECT address_id
    FROM customer
    WHERE customer_id = 1
);
-- 10. List all payments that are greater than the average of all payments.
SELECT *
FROM payment
WHERE amount > (
    SELECT AVG(amount)
    FROM payment
);