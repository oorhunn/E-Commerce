aa = [{"photo_link": "ananbaban", "price": 50.0, "product_name": "ayakkabi",
       "register_date": "2021-07-11 10:33:31.596816", "size": "45"},
      {"photo_link": "babananan", "price": 100.0, "product_name": "tulum",
       "register_date": "2021-07-11 12:34:40.851205", "size": "XL"}]


new = {
    'aaData':
        [
            [
                aa[0]['price'],
                aa[0]['product_name']
            ]
        ]

}
i = 0
while i < len(aa):
    keys, values = zip(*aa[i].items())
    i = i + 1

print(values)




