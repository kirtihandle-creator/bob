# bob reviewer notes

## Architecture

This repository contains a Java shop-flow domain/common module organized around JSON infrastructure, domain models, and shared utilities under `shopflow/common/src/com/shopflow/common`. Domain entities implement `Identifiable`, serialize themselves to ordered JSON-friendly maps, and reconstruct via static `fromJson` methods. JSON parsing/writing is intentionally self-contained rather than delegated to an external library.

## Conventions

- Entities stored by repositories implement `Identifiable`, expose mutable string IDs, and provide `toJson()` plus static `fromJson(...)`; see `model/Product.java`, `model/Category.java`, and `model/Customer.java`.
- JSON field names and insertion order are explicit: models use `LinkedHashMap` and add fields in a stable order, e.g. `model/Order.java` and `model/User.java`.
- Deserialization is tolerant of loosely typed or missing input. Use `Identifiable.str`, `dbl`, `integer`, `lng`, `bool`, and `idOrNull` rather than direct casts; these helpers default missing values to empty strings, zero, false, or null (`model/Identifiable.java`).
- Collections are represented as `List<Object>` and nested maps. `Json.mapList`, `Json.nested`, and `Json.nestedList` provide the standard conversion/defaulting behavior (`json/Json.java`).
- Use `Json.stringify`/`prettify` and `Json.parse`/`object`/`array` as the facade; low-level parser/writer classes are implementation details (`json/Json.java`).
- Enum persistence uses enum names in JSON and lenient parsing on input: `Order.toJson()` writes `status.name()`, while `OrderStatus.parse` accepts names or display labels and falls back to `NEW` (`model/Order.java`, `model/OrderStatus.java`).
- Domain-derived values are generally calculated rather than trusted from JSON. For example, `Order.getTotal()` sums item totals and `OrderItem.getLineTotal()` calculates quantity × unit price (`model/Order.java`, `model/OrderItem.java`).
- Monetary display/persistence boundaries should use `Money.round`, `format`, `plain`, or `multiply`; rounding is `BigDecimal`/`HALF_UP` to two decimals (`util/Money.java`).
- Validation is fluent and accumulates all failures; callers can inspect `getErrors`/`getMessage` or call `throwIfInvalid` (`util/Validation.java`).
- Timestamps are epoch milliseconds and display/grouping uses the system default time zone (`util/Dates.java`).

## Intentional non-standard choices

- The JSON implementation is deliberately minimal and custom: parsed numbers become `Double`, objects preserve order with `LinkedHashMap`, and unsupported writer values fall back to quoted `String.valueOf(...)` (`json/JsonParser.java`, `json/JsonWriter.java`).
- `User.toJson()` is the full persistence representation and includes `passwordHash`; client-facing code must use `toPublicJson()` (`model/User.java`).
- Monetary calculations use `double` internally despite currency concerns; `Money` provides the agreed rounding boundary (`util/Money.java`).
- Missing/invalid model data is commonly normalized rather than rejected, including blank IDs becoming null and unknown order statuses becoming `NEW` (`model/Identifiable.java`, `model/OrderStatus.java`).

## Watch out for

- Do not serialize `User.toJson()` into frontend/API responses; it intentionally contains the password hash. Use `toPublicJson()` (`model/User.java`).
- Do not add persisted fields to `toJson()` without corresponding `fromJson()` handling, or vice versa; this breaks round trips across all models.
- Preserve order transition rules in `OrderStatus.allowedTransitions()`; bypassing `canTransitionTo` can permit cancellation or advancement from final states (`model/OrderStatus.java`).
- Do not treat `OrderItem.lineTotal`, `Order.total`, or similar derived fields as authoritative input; they are recalculated from quantity, price, and items.
- Be alert to parser edge cases when changing `JsonParser`: its recursive reader assumes valid structural delimiters and all numbers are parsed as `Double` (`json/JsonParser.java`).
