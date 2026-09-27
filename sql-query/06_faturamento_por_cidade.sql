SELECT
    cidade,
    SUM(valor_total) AS faturamento
FROM raw
GROUP BY cidade
ORDER BY faturamento DESC;