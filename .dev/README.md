# PyDictDatabase - Development

## select/update - speed

Time average with 1000 queries:

fetchone("SELECT timestamp FROM dataI2C WHERE id = 0x23") **0.00260 ms**

fetchall("SELECT timestamp FROM dataI2C WHERE id = 0x23") **0.00283 ms**

fetchall("SELECT group,timestamp,value FROM dataI2C WHERE id = 0x23") **0.00372 ms**

commit("UPDATE connections SET noFail_timestamp = 12345678 WHERE id = wlan") **0.00936 ms**

commit("UPDATE connections SET noFail_timestamp = 12345678,value = True WHERE id = wlan") **0.01143 ms**
