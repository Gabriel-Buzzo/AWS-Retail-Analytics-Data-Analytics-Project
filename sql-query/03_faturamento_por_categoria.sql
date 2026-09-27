SELECT
    categoria,
    SUM(valor_total) AS faturamento
FROM raw
GROUP BY categoria
ORDER BY faturamento DESC;