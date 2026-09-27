SELECT
    categoria,
    SUM(lucro) AS lucro_total
FROM raw
GROUP BY categoria
ORDER BY lucro_total DESC;