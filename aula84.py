produtos = [
    {
        "nome": "p1",
        "preco": 20
    },
    
    {   
        "nome": "p2",
        "preco": 15
    },
    
    {
        "nome": "p3",
        "preco": 200
    }
]


produtos.sort(key=lambda lista: lista["preco"])

print(**produtos, sep="\n")