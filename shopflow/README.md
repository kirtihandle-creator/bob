# ShopFlow

A small inventory and order management system written in plain Java with no
third-party dependencies. It has three modules:

| Module     | What it is                                                     | Entry point                     |
|------------|----------------------------------------------------------------|---------------------------------|
| `common`   | Domain models, a tiny JSON parser/writer, validation helpers   | (library)                       |
| `backend`  | REST API on the JDK's built-in HTTP server, JSON file storage  | `com.shopflow.backend.Main`     |
| `frontend` | Swing desktop client that talks to the backend over HTTP       | `com.shopflow.frontend.Main`    |

Requires JDK 17 or newer and Python 3 (see the note below).

## Build

```powershell
powershell -ExecutionPolicy Bypass -File scripts\build.ps1
```

or on a POSIX shell:

```bash
bash scripts/build.sh
```

Compiled classes land in `out/<module>`.

## Run

Start the backend. On the very first start the user store is empty, so you
must supply a bootstrap administrator password. It is used once to create the
`admin` account and is never stored in plain text.

```powershell
powershell -ExecutionPolicy Bypass -File scripts\run-backend.ps1 -AdminPassword "ChangeMe123"
```

Afterwards start it without the password:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\run-backend.ps1
```

Then start the desktop client and sign in as `admin` with the password you chose:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\run-frontend.ps1
```

Demo categories, products, customers and orders are seeded when the catalog is
empty. Disable with `-Dshopflow.seed=false`.

## Configuration

| System property           | Environment variable       | Default                                      |
|---------------------------|----------------------------|----------------------------------------------|
| `shopflow.port`           | `SHOPFLOW_PORT`            | `8080`                                       |
| `shopflow.data`           | `SHOPFLOW_DATA`            | `data`                                       |
| `shopflow.seed`           | `SHOPFLOW_SEED`            | `true`                                       |
| `shopflow.adminUser`      | `SHOPFLOW_ADMIN_USER`      | `admin`                                      |
| `shopflow.adminPassword`  | `SHOPFLOW_ADMIN_PASSWORD`  | unset (required only when no users exist)    |
| `shopflow.tokenTtl`       | `SHOPFLOW_TOKEN_TTL`       | 8 hours, in milliseconds                     |
| `shopflow.python`         | `SHOPFLOW_PYTHON`          | `python`                                     |
| `shopflow.reportScript`   | `SHOPFLOW_REPORT_SCRIPT`   | `backend/src/.../service/report_service.py`  |
| `shopflow.url` (client)   | `SHOPFLOW_URL`             | `http://localhost:8080`                      |

## The one Python file

`backend/src/com/shopflow/backend/service/report_service.py` is the only
non-Java source in the project, and it is deliberately not standalone. The
Java `ReportService` runs it as a subprocess for every `/api/reports/*`
request and the desktop dashboard renders its output. Without a working
`python` on the PATH the dashboard tab reports an error while every other
screen keeps working.

## API overview

All endpoints except `POST /api/auth/login` and `GET /api/health` require an
`Authorization: Bearer <token>` header.

- `POST /api/auth/login`, `POST /api/auth/logout`, `GET /api/auth/me`, `POST /api/auth/password`
- `GET|POST /api/users`, `DELETE /api/users/{id}` (admin)
- `GET|POST /api/categories`, `GET|PUT|DELETE /api/categories/{id}`
- `GET|POST /api/products`, `GET|PUT|DELETE /api/products/{id}`, `POST /api/products/{id}/stock`
- `GET|POST /api/customers`, `GET|PUT|DELETE /api/customers/{id}`, `GET /api/customers/{id}/orders`
- `GET|POST /api/orders`, `GET|DELETE /api/orders/{id}`, `POST /api/orders/{id}/status`, `GET /api/orders/statuses`
- `GET /api/reports/summary`, `GET /api/reports/low-stock`, `GET /api/reports/health`

Data is stored as pretty-printed JSON arrays in the data directory, one file
per entity type, written atomically on every change.
