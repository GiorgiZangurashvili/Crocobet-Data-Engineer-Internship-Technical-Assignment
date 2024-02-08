-- TASK 1
SELECT g.name genre_name, SUM(i.unit_price * i.quantity) total_sales
FROM genre g
JOIN track t ON g.genre_id = t.genre_id
JOIN invoice_line i ON t.track_id = i.track_id
GROUP BY g.name
ORDER BY total_sales DESC
LIMIT 3;


-- TASK 2
SELECT e.first_name, e.last_name, COALESCE(SUM(i.total), 0) total_sales
FROM employee e
LEFT JOIN customer c ON e.employee_id = c.support_rep_id
LEFT JOIN invoice i ON c.customer_id = i.customer_id
GROUP BY e.employee_id
ORDER BY total_sales DESC;


-- TASK 3
-- used DISTINCT, because playlists table contains duplicates
SELECT DISTINCT p.name, COUNT(*) number_of_tracks
FROM playlist p
JOIN playlist_track pt ON p.playlist_id = pt.playlist_id
JOIN track t ON pt.track_id = t.track_id
GROUP BY p.playlist_id
ORDER BY number_of_tracks DESC
LIMIT 5;

-- TASK 4
SELECT c.first_name, c.last_name, COUNT(*) total_number_of_purchases
FROM customer c
JOIN invoice i ON c.customer_id = i.customer_id
GROUP BY c.customer_id
ORDER BY total_number_of_purchases DESC;