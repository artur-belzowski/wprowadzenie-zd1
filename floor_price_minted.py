import requests
# from body3 import body3
import pprint

# def floor_price_minted(address):
body3 = {
        "operationName": "getCollectionAssets",
        "variables": {
            "address": '0xa560c70220c32c81217cf993676d177d43d48349',
            "chain": "CRONOS",
            "first": 2,
            "filter": {
                "chain": "CRONOS",
                "listingType": None,
                "priceRange": None,
                "attributes": None,
                "rarityRange": None,
                "nameOrTokenId": None
            },
            "sort": "LOWEST_PRICE"
        },
        "query": "query getCollectionAssets($address: EvmAddress!, $chain: Blockchain!, $first: Int!, $sort: AssetSort!, $after: String, $filter: AssetFilterInput) {\n  collection(address: $address, chain: $chain) {\n    ...CollectionIdentifyFields\n    assets(first: $first, after: $after, filter: $filter, sort: $sort) {\n      totalCount\n      edges {\n        node {\n          ...AssetDetailFields\n          bids(first: 1) {\n            edges {\n              node {\n                ...OrderFields\n                __typename\n              }\n              cursor\n              __typename\n            }\n            pageInfo {\n              ...PageInfoFields\n              __typename\n            }\n            totalCount\n            __typename\n          }\n          __typename\n        }\n        cursor\n        __typename\n      }\n      pageInfo {\n        ...PageInfoFields\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment CollectionIdentifyFields on AssetCollection {\n  address\n  name\n  chain {\n    name\n    __typename\n  }\n  status\n  __typename\n}\n\nfragment AssetDetailFields on Asset {\n  name\n  tokenId\n  image {\n    url\n    __typename\n  }\n  animatedImage {\n    url\n    __typename\n  }\n  owner {\n    ...UserFields\n    __typename\n  }\n  ask {\n    ...OrderFields\n    __typename\n  }\n  collection {\n    ...CollectionIdentifyFields\n    __typename\n  }\n  rarityRank\n  __typename\n}\n\nfragment UserFields on UserAccount {\n  evmAddress\n  name\n  avatar {\n    url\n    __typename\n  }\n  nonce\n  __typename\n}\n\nfragment OrderFields on MakerOrder {\n  hash\n  chain\n  isOrderAsk\n  collection\n  tokenId\n  currency\n  strategy\n  startTime\n  endTime\n  minPercentageToAsk\n  nonce\n  price\n  amount\n  status\n  signer\n  encodedParams\n  paramTypes\n  signature\n  __typename\n}\n\nfragment PageInfoFields on PageInfo {\n  hasPreviousPage\n  hasNextPage\n  startCursor\n  endCursor\n  __typename\n}"
    }
resp = requests.post(url="https://api.minted.network/graphql", json=body3)
lin = resp.json()
ask = lin['data']['collection']['assets']['edges'][0]['node']['ask']

address_collection = ask['collection']
fp2 = int(ask['price']) /1000000000000000000
print(fp2)

# if address_collection == '0xa560c70220c32c81217cf993676d177d43d48349':
# print(lin['data']['collection']['assets']['edges'][0]['node']['ask']['collection']['price'])
# print(address_collection)

# print(lin)
# pprint.pprint(lin['data']['collection']['assets']['edges'][0]['node']['ask'])
#
# for nft in lin['data']['collection']['assets']['edges'][0]['node']['ask']:
    # nazwa2 = nft['collection']
# print(lin['data']['collection']['assets']['edges'][0]['node']['ask']['collection'])
    # if nazwa2 == '0xa560c70220c32c81217cf993676d177d43d48349':
    #     print(nazwa2)
        #     if nft['node']['floorPrice']['latestFloorPriceNative'] is not None:
        #         floor_price_minted = int(nft['node']['floorPrice']['latestFloorPriceNative']) / 1000000000000000000
        #     else:
        #         floor_price_minted = 0
            # return floor_price_minted
# floor_price_minted('0xa560c70220c32c81217cf993676d177d43d48349')



