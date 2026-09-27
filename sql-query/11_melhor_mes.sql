SELECT
    date_format(
        date_parse(data_venda, '%Y-%m-%d'),
        '%Y-%m'
    ) AS mes,
    SUM(valor_total) AS faturamento
FROM raw
GROUP BY
    date_format(
        date_parse(data_venda, '%Y-%m-%d'),
        '%Y-%m'
    )
ORDER BY faturamento DESC;