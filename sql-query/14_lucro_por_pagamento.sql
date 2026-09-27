SELECT
    forma_pagamento,
    SUM(lucro) AS lucro_total
FROM raw
GROUP BY forma_pagamento
ORDER BY lucro_total DESC;