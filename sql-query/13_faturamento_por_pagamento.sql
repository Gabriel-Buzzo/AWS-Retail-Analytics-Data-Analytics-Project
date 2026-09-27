SELECT
    forma_pagamento,
    SUM(valor_total) AS faturamento
FROM raw
GROUP BY forma_pagamento
ORDER BY faturamento DESC;