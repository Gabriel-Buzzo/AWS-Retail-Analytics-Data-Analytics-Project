SELECT
    date_format(
        date_parse(data_venda, '%Y-%m-%d'),
        '%Y-%m'
    ) AS mes,
    SUM(quantidade) AS quantidade_vendida,
    SUM(valor_total) AS faturamento,
    SUM(lucro) AS lucro_total
FROM raw
GROUP BY
    date_format(
        date_parse(data_venda, '%Y-%m-%d'),
        '%Y-%m'
    )
ORDER BY mes;