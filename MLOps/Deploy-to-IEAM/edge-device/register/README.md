### Register edge device with `node policy`

```
hzn register --policy node-policy.json
```

#### Test
- `exec` into the client docker container (to be improved)
```
docker exec -it <client-docker-CONTAINER ID> bash
```

- Run this command to test the sentiment analysis 
```
python3 client.py "ok"
```
