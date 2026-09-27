SELECT
    categoria,
    SUM(quantidade) AS quantidade_vendida
FROM raw
GROUP BY categoria
ORDER BY quantidade_vendida DESC;