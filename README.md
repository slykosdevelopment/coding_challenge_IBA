# coding challenge IBA

## in folder data : 

python3 createDatabase.py

sudo docker build -t image_fastapi .

sudo docker run  -p 8000:8000 image_fastapi


## Sample  : 

### Get all signals sample link
http://localhost:8000/get_all_signals


### Get by id sample link
http://localhost:8000/get_by_id/ns=6;s=StarGateway:Shaco.Jinx.CU.AL_fOndt_KEPXQlFdrS

### Sample command to post a new signal (in terminal)
curl -X POST http://localhost:8000/create_new -H "Content-Type: application/json" -d '{"node_id":"ns=6;s=StarGateway:Shaco.Jinx.CU.AC_DKLsd_TUFqHJPgxl", "sampling_interval_ms":500, "deadband_value":88, "deadband_type":"ABSOLUTE", "active":1, "keywords":"PS, DS"}'

#### Before and after, verify its absence/presence via the link
http://localhost:8000/get_by_id/ns=6;s=StarGateway:Shaco.Jinx.CU.AC_DKLsd_TUFqHJPgxl