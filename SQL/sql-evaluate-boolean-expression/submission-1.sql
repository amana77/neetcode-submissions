SELECT e.left_operand, e.operator, e.right_operand,
    CASE
        WHEN e.operator='>' AND lv.value>rv.value THEN true
        WHEN e.operator='<' AND lv.value<rv.value THEN true
        WHEN e.operator='=' AND lv.value=rv.value THEN true
        ELSE false
    END AS value
FROM expressions as e
JOIN variables as lv
ON e.left_operand=lv.name
JOIN variables as rv
ON e.right_operand=rv.name;