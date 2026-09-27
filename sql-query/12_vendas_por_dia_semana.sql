SELECT
    date_format(
        date_parse(data_venda, '%Y-%m-%d'),
        '%W'
    ) AS dia_semana,
    SUM(quantidade) AS quantidade_vendida,
    SUM(valor_total) AS faturamento
FROM raw
GROUP BY
    date_format(
        date_parse(data_venda, '%Y-%m-%d'),
        '%W'
    )
ORDER BY quantidade_vendida DESC;