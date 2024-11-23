```bash
docker compose build client
docker compose run --rm client bash -c "cd client/ && pnpm install"
docker compose up client
```
