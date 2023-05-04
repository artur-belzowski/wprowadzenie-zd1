import json
import requests
import pprint
from floor_price_ebisu import floor_price_ebisu

def wallet_ebisu(wallet):
    url = requests.get('https://api.ebisusbay.com/walletoverview?pageSize=1000&wallet='+wallet)
    nfts = []
    suma = 0
    for erc721 in url.json()['data']['erc721']:
        name = erc721['name']
        address = erc721['address'].strip()
        sztuk = int(erc721['balance'])
        a = floor_price_ebisu(address)
        print(f'NFT z kolekcji: {name} ilość posiadanych: {sztuk}szt. obecny floor price kolekcji to: {a}')
        if a is not None:
            result = sztuk * int(a)
            print(f' Wartość tej kolekcji to: {result}')
            suma += result
        else:
            print('Nie znaleziono wartości fp dla adresu', address)
        print(50 * '*')
        nft = {
            'name': name,
            'address': address,
            'sztuk': sztuk,
            'floor_price': a,
            'result': result if a is not None else None
        }
        nfts.append(nft)
        print(suma)
    with open('nft.json', 'w') as f:
        json.dump(nfts, f)

wallet_ebisu('0xF56575D199D49dD502D0e99b315B2eef6a181af9')