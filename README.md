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

## Credentials

```bash
curl -X GET http://127.0.0.1:7777/vaults/1/credentials
curl -X POST -H "Content-Type: application/json" -d '{
  "name": "Account for LoboGuaraGuardian",
  "username": "user123",
  "password": "securepassword",
  "tags": ["personal", "email"],
  "urls": ["personal.io"]
}' http://127.0.0.1:7777/vaults/1/credentials
curl -X GET http://127.0.0.1:7777/vaults/1/credentials/1
curl -X PUT -H "Content-Type: application/json" -d '{
    "name": "Updated Password Name",
    "username": "updated_username",
    "description": "Updated description",
    "tags": ["personal", "email", "updated"],
    "urls": ["https://loboguara.guardian", "https://app.loboguara.guardian"]
}' http://127.0.0.1:7777/vaults/1/credentials/1
curl -X DELETE http://127.0.0.1:7777/vaults/1/credentials/1
```


# Troubleshooting

If you need, you can destroy everything and start from scratch.
```bash
docker compose down -v
```

# Future steps

- [X] Add multiple tags to a credential
- [X] Add multiple websites to a credential
- [ ] Encrypt sensible data (password and otp)
- [ ] Add the user auth
- [ ] Support to import / export
- [ ] Add security layer at the export
