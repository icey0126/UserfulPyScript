bb = 'e0be661032d5f0b676f82095e4d67623628fe6d376363183aed373a60167af537b46abc2af53d97485591f5bd94b944a3f49d94897ea1f699d1cdc291f2d9d4a5c705f2cad89e938dbacaca15e10d8aeaed90236f0be2e954a8cf0bea6112e84'
print(len(bb))

print(','.join(bb[i:i+16] for i in range(0,len(bb),16)))