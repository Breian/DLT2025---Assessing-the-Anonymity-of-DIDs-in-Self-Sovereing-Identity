# Original list
data = [
    ('ENS: Old Registrar', 2612), ('BlockchainArtExchange: BAE Token', 1828), ('Enjin:  X Token', 1474), ('Axie Infinity: Axie Clock Auction', 957), ('0xd48c6a5c3046a29a57dad9b6453769c674b7d22f', 659), ('0xe60c3a67c51483f7b619ff6e47f5f2d14de7d7d4', 624), ('dYdX: Solo Margin', 617), ('Falcon Project: FNT Token', 559), ('Axie Infinity: Breeding Contract #1', 540), ('Uniswap: Universal Router', 538), ('Opium.Team: Match', 525), ('0xa32ff8ca08036337fabf50fa029812361cd176c8', 523), ('0x: Exchange Proxy', 492), ('BAE: BAEPAY Token', 409), ('Wrapped Ether', 364), ('0x2947f98c42597966a0ec25e92843c09ac17fbaa7', 325), ('MetaCartel: Treasury', 323), ('Small Love Potion: Old SLP Token', 317), ('Axie Infinity: Ronin Bridge', 300), ('0x30e0130141b3f113480a5941ca180ad8c5f98612', 280), ('Wrapped Origin Axie : WOA Token', 276), ('0xd29044ed00822f543ed79ba237006f3f8be31609', 272), ('OpenSea: Wyvern Exchange v1', 262), ('Async Art: ASYNC Token', 255), ('0x91351a04b3365808518d22db2884d3c288a4bbd1', 237), ('Blockchain Art Exchange: BAE Token', 227), ('DSProxy #145,543', 222), ('Async Art: ASYNC-V2 Token', 212), ('Opium.Team: Oracle Aggregator V1', 210), ('DSProxy #7,004', 202)
]

# Extract strings
strings_list = [item[0] for item in data]

# Print the new list
print(strings_list)