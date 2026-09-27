SELECT
    cidade,
    SUM(lucro) AS lucro_total
FROM raw
GROUP BY cidade
ORDER BY lucro_total DESC;