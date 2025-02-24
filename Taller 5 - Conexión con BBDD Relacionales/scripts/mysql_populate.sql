CREATE DATABASE IF NOT EXISTS nter_python; 
USE nter_python;

DROP TABLE IF EXISTS orders;
CREATE TABLE IF NOT EXISTS orders (
  order_id INT PRIMARY KEY,
  client_id INT,
  status VARCHAR(30),
  last_updated TIMESTAMP
);

-- Insertamos solo algunos registros (menos que en SQLite)
INSERT INTO Orders (order_id, client_id, order_status, last_updated)
VALUES
(1, 100, 'Pendiente de pago', '2024-04-01 10:00:00'),
(2, 101, 'En proceso', '2024-04-02 11:30:00');
