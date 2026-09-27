SELECT
    CASE
        WHEN valor_unitario < 500 THEN 'Até R$ 500'
        WHEN valor_unitario < 1000 THEN 'R$ 500 - R$ 999'
        WHEN valor_unitario < 2000 THEN 'R$ 1.000 - R$ 1.999'
        ELSE 'R$ 2.000 ou mais'
    END AS faixa_preco,
    SUM(quantidade) AS quantidade_vendida
FROM raw
GROUP BY
    CASE
        WHEN valor_unitario < 500 THEN 'Até R$ 500'
        WHEN valor_unitario < 1000 THEN 'R$ 500 - R$ 999'
        WHEN valor_unitario < 2000 THEN 'R$ 1.000 - R$ 1.999'
        ELSE 'R$ 2.000 ou mais'
    END
ORDER BY quantidade_vendida DESC;