# Running the client (if you want)
```bash
docker compose build client
docker compose run --rm client bash -c "cd client/ && pnpm install"
docker compose up client
```

# Running the server
```bash
docker compose up server --build
```

You need to migrate the server to have the database up to date
```bash
docker compose run --rm server flask db upgrade
```

Now check if the server is running on [http://localhost:7777](http://localhost:7777)

# Endpoints

## Vaults

```bash
curl -X GET http://127.0.0.1:7777/vaults
curl -X POST -H "Content-Type: application/json" -d '{"name": "Vault 1"}' http://127.0.0.1:7777/vaults
curl -X GET http://127.0.0.1:7777/vaults/1
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Vault"}' http://127.0.0.1:7777/vaults/1
curl -X DELETE http://127.0.0.1:7777/vaults/1
```

# Troubleshooting

If you need, you can destroy everything and start from scratch.
```bash
docker compose down -v
```
