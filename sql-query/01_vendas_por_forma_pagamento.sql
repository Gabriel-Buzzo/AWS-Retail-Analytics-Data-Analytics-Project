SELECT
    forma_pagamento,
    COUNT(*) AS quantidade_vendas
FROM raw
GROUP BY forma_pagamento
ORDER BY quantidade_vendas DESC;