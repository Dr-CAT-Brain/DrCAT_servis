def decode_label(patology_index):
    d = {0: "ВЖК",
         1: "ВМГ 1",
         2: "ВМГ 2",
         3: "ВМГ_ВЖК",
         4: "ВМГ_ВЖК_САК",
         5: "ВМГ_ВЖК_ишем",
         6: "ВМГ_ишемия",
         7: "САК",
         8: "САК_ВЖК",
         9: "САК_ВМГ",
         10: "СД",
         11: "ишемия",
         12: "опухоль",
         13: "эд_сд"}

    return d[patology_index]


def decode_label_detail(patology_index):
    d = {0: "Внутрижелудочковое кровоизлияние",
         1: "Внутримозговая гематома без возможности операции",
         2: "Внутримозговая гематома под операцию",
         3: "Внутримозговая гематома с вентикулярным компонентом",
         4: "Внутримозговое кромоизлияние с вентикулярным компонентом с субарахноидальным кровоизлиянием",
         5: "Внутримозговая гематома с вентикулярным компонентом и инфарктом мозга",
         6: "Внутримозговая гематома с ишемическим инсультом",
         7: "Субарахноидальное кровоизлияние",
         8: "Субарахноидальное кровоизлияние с вентикулярным компонентам",
         9: "Субарахноидальное кровоизлияние с внутримозговой гематомой",
         10: "Субдуральное кровоизлияние",
         11: "Ишемический инсульт",
         12: "Подозрение на опухоль",
         13: "Сочетание эпидурального и субдурального кровоизлияний"}
    return d[patology_index]