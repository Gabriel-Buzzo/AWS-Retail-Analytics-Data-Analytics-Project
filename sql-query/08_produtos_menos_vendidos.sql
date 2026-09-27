SELECT
    produto,
    SUM(quantidade) AS quantidade_vendida
FROM raw
GROUP BY produto
ORDER BY quantidade_vendida ASC;