SELECT
    COUNT(*) AS total_vendas,
    SUM(quantidade) AS quantidade_produtos,
    SUM(valor_total) AS faturamento_total,
    SUM(custo_total) AS custo_total,
    SUM(lucro) AS lucro_total
FROM raw;