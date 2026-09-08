This file is a merged representation of a subset of the codebase, containing files not matching ignore patterns, combined into a single document by Repomix.
The content has been processed where content has been compressed (code blocks are separated by ⋮---- delimiter).

# File Summary

## Purpose
This file contains a packed representation of a subset of the repository's contents that is considered the most important context.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching these patterns are excluded: bundles/**/viz.html, **/*.png, LICENSE.md, CODE_OF_CONDUCT.md
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Content has been compressed - code blocks are separated by ⋮---- delimiter
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure
`````
bundles/
  acme_retail/
    attesters/
      index.md
      sql_equality.py
    computations/
      gross-margin-period.md
      index.md
      revenue-ytd.md
    metrics/
      gross-margin-legacy.md
      gross-margin.md
      index.md
      revenue.md
    policies/
      index.md
      margin-standard.md
      revenue-recognition.md
    skills/
      index.md
      run-on-bq.md
    tables/
      index.md
      orders.md
    index.md
    log.md
  crypto_bitcoin/
    datasets/
      crypto_bitcoin.md
      index.md
    references/
      joins/
        blocks___transactions.md
        index.md
        inputs___transactions.md
        outputs___transactions.md
      metrics/
        duplicate_transactions.md
        index.md
      index.md
    tables/
      blocks.md
      index.md
      inputs.md
      outputs.md
      transactions.md
    index.md
  ga4/
    datasets/
      ga4_obfuscated_sample_ecommerce.md
      index.md
    references/
      metrics/
        acquired_users.md
        frequently_active_users.md
        google_acquired_cohorts.md
        highly_active_users.md
        index.md
        n_day_active_users.md
        n_day_inactive_users.md
        purchasers.md
      index.md
    tables/
      events_.md
      index.md
    index.md
  stackoverflow/
    datasets/
      index.md
      stackoverflow.md
    references/
      joins/
        comments__posts.md
        index.md
        post_links__posts.md
        posts__votes.md
        posts_answers__posts_questions.md
      metrics/
        accepted_answer_rate.md
        bad_question_flag_ratio.md
        index.md
      content_licenses.md
      index.md
      post_types.md
      vote_types.md
    tables/
      badges.md
      comments.md
      index.md
      post_history.md
      post_links.md
      posts_answers.md
      posts_moderator_nomination.md
      posts_orphaned_tag_wiki.md
      posts_privilege_wiki.md
      posts_questions.md
      posts_tag_wiki_excerpt.md
      posts_tag_wiki.md
      posts_wiki_placeholder.md
      stackoverflow_posts.md
      tags.md
      users.md
      votes.md
    index.md
connectors/
  gcp-knowledge-catalog.md
samples/
  crypto_bitcoin/
    README.md
    seeds.txt
  ga4_merch_store/
    README.md
    seeds.txt
  stackoverflow/
    README.md
    seeds.txt
src/
  reference_agent/
    bundle/
      __init__.py
      document.py
      index.py
      paths.py
      synthesizer.py
    prompts/
      reference_instruction.md
      web_ingestion_instruction.md
    sources/
      __init__.py
      base.py
      bigquery.py
    tools/
      __init__.py
      bundle_tools.py
      context.py
      source_tools.py
      web_tools.py
    viewer/
      static/
        viz.css
        viz.js
      templates/
        viz.html
      __init__.py
      generator.py
    web/
      __init__.py
      fetcher.py
    __init__.py
    __main__.py
    agent.py
    cli.py
    runner.py
tests/
  __init__.py
  test_bigquery_source.py
  test_bundle_tools.py
  test_document.py
  test_index.py
  test_viewer.py
  test_web_fetcher.py
  test_web_tools.py
.gitignore
CONTRIBUTING.md
pyproject.toml
README.md
SPEC.md
`````

# Files

## File: bundles/acme_retail/attesters/index.md
`````markdown
# Attester

* [sql_equality.py](sql_equality.py) - Canonicalizes SQL and verifies BigQuery receipts against the sanctioned computation.
`````

## File: bundles/acme_retail/attesters/sql_equality.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
⋮----
"""Deterministic attester for Attested Computations with runtime: bigquery.

Verifies two things about a receipt produced by skills/run-on-bq.md:

  1. Provenance: the SQL that actually ran (`receipt.executed_sql`) equals the
     computation body of the concept (or the file at `computation:`) after
     normalizing whitespace, casing of keywords, and comment stripping.
     Named bind variables (@name) are compared symbolically; their values are
     not inspected here (the executor is trusted to bind).

  2. Fidelity: the value the caller displayed to the user (`claimed_value`)
     equals the first cell of `receipt.result`.

Returns a verdict dict:
  { "ok": bool, "reason": str | None, "details": { ... } }

Never uses an LLM. Never makes network calls. Safe to run consumer-side.
"""
⋮----
# ---- normalization helpers ---------------------------------------------------
⋮----
_COMMENT_LINE = re.compile(r"--[^\n]*")
_COMMENT_BLOCK = re.compile(r"/\*.*?\*/", flags=re.DOTALL)
_WHITESPACE = re.compile(r"\s+")
_KEYWORDS = frozenset({
⋮----
def _canonicalize(sql: str) -> str
⋮----
"""Strip comments, collapse whitespace, uppercase keywords."""
s = _COMMENT_BLOCK.sub(" ", sql)
s = _COMMENT_LINE.sub(" ", s)
s = _WHITESPACE.sub(" ", s).strip()
# Uppercase only known SQL keywords; leave identifiers alone.
def _upper_kw(match: re.Match[str]) -> str
⋮----
w = match.group(0)
⋮----
s = re.sub(r"[A-Za-z_][A-Za-z_0-9]*", _upper_kw, s)
⋮----
# ---- entrypoint --------------------------------------------------------------
⋮----
"""Verify a BigQuery receipt against a sanctioned computation.

    Args:
      sanctioned_sql: the SQL from the concept's `# Computation` fence or its
                      `computation:` file.
      receipt:        the dict returned by skills/run-on-bq.md,
                      expected to carry `executed_sql` and `result`.
      claimed_value:  the value the caller is about to display.

    Returns:
      A verdict dict. Callers MUST refuse to display `claimed_value` when
      verdict["ok"] is False.
    """
executed = receipt.get("executed_sql")
⋮----
can_sanctioned = _canonicalize(sanctioned_sql)
can_executed = _canonicalize(executed)
⋮----
result = receipt.get("result")
⋮----
# `result` may be a scalar (single cell) or a row-shaped list.
first_cell = result[0] if isinstance(result, list) else result
`````

## File: bundles/acme_retail/computations/gross-margin-period.md
`````markdown
---
type: Attested Computation
title: Gross margin for a period
description: Sanctioned SQL that produces the gross-margin figure for a period, per Acme's FY2026 Cost Allocation Standard (full COGS = product + fulfillment + shipping + payment fees).
tags: [finance, margin, attested]
runtime: bigquery
parameters:
  - { name: period_start, type: date, required: true }
  - { name: period_end, type: date, required: true }
executor:
  resource: skills/run-on-bq.md
  receipt: [job_id, executed_sql, result]
attester:
  resource: attesters/sql_equality.py
generated: { by: reference_agent/gemini-2.5-pro, at: 2026-06-30T14:00:00Z }
verified:
  - { by: human:jsmith@acme, at: 2026-07-01T09:00:00Z }
status: stable
stale_after: 2026-12-31T00:00:00Z
sources:
  - id: margin-standard
    resource: policies/margin-standard.md
    title: Cost Allocation & Margin Standard (FY2026)
    author: human:jsmith@acme
    last_modified: 2026-06-15T00:00:00Z
  - id: revenue-policy
    resource: policies/revenue-recognition.md
    title: Revenue Recognition Policy (FY2026)
    author: human:jsmith@acme
    last_modified: 2026-06-15T00:00:00Z
---

# Computation

```sql
WITH recognized_orders AS (
  SELECT
    o.order_id,
    CASE
      WHEN o.currency = 'USD' THEN o.net_amount
      ELSE o.net_amount * fx.rate_to_usd
    END AS revenue_usd
  FROM `acme.sales.orders` AS o
  LEFT JOIN `acme.finance.fx_daily_rates` AS fx
    ON fx.currency = o.currency
    AND fx.rate_date = DATE(o.order_ts)
  WHERE o.order_status = 'delivered'
    AND DATE_DIFF(CURRENT_DATE(), DATE(o.order_ts), DAY) >= 30
    AND DATE(o.order_ts) BETWEEN @period_start AND @period_end
),
cogs_full AS (
  SELECT
    ol.order_id,
    SUM(ol.quantity * p.cost) AS product_cost,
    SUM(fc.allocated_cost) AS fulfillment_cost,
    SUM(sc.shipping_cost) AS shipping_cost,
    SUM(pf.fee_amount) AS payment_fee
  FROM `acme.sales.order_lines` AS ol
  JOIN `acme.catalog.products` AS p ON p.product_id = ol.product_id
  LEFT JOIN `acme.logistics.fulfillment_cost` AS fc ON fc.order_id = ol.order_id
  LEFT JOIN `acme.logistics.shipment_cost` AS sc ON sc.order_id = ol.order_id
  LEFT JOIN `acme.finance.payment_fees` AS pf ON pf.order_id = ol.order_id
  GROUP BY ol.order_id
)
SELECT
  SUM(r.revenue_usd) - SUM(
    COALESCE(c.product_cost, 0)
    + COALESCE(c.fulfillment_cost, 0)
    + COALESCE(c.shipping_cost, 0)
    + COALESCE(c.payment_fee, 0)
  ) AS gross_margin_usd
FROM recognized_orders AS r
LEFT JOIN cogs_full AS c USING (order_id)
```

# Notes on the COGS composition

Every one of the four COGS components is required per the FY2026 Cost Allocation Standard. [^margin-standard] A receipt whose executed SQL drops any of the four LEFT JOINs on `cogs_full` will fail attestation, because canonicalized-SQL equality includes the join graph.

The revenue side uses the same recognition rules as [`computations/revenue-ytd.md`](./revenue-ytd.md), by policy.

# Freshness

`stale_after: 2026-12-31T00:00:00Z` mirrors the cost-allocation standard's annual review. The standard is expected to remain stable through the FY, but a consumer running this after 2027-01-01 MUST re-verify against the FY2027 standard before serving.

[^margin-standard]: Cost Allocation & Margin Standard (FY2026)
[^revenue-policy]: Revenue Recognition Policy (FY2026)
`````

## File: bundles/acme_retail/computations/index.md
`````markdown
# Attested Computation

* [Revenue for a fiscal year](revenue-ytd.md) - Sanctioned SQL for annual revenue, bigquery runtime.
* [Gross margin for a period](gross-margin-period.md) - Sanctioned SQL for gross margin, bigquery runtime.
`````

## File: bundles/acme_retail/computations/revenue-ytd.md
`````markdown
---
type: Attested Computation
title: Revenue for a fiscal year
description: Sanctioned SQL that produces the recognized-revenue figure for a given fiscal year, per Acme's FY2026 Revenue Recognition Policy.
tags: [finance, revenue, attested]
runtime: bigquery
parameters:
  - { name: year, type: integer, required: true }
executor:
  resource: skills/run-on-bq.md
  receipt: [job_id, executed_sql, result]
attester:
  resource: attesters/sql_equality.py
generated: { by: reference_agent/gemini-2.5-pro, at: 2026-06-30T14:00:00Z }
verified:
  - { by: human:jsmith@acme, at: 2026-07-01T09:00:00Z }
status: stable
stale_after: 2026-12-31T00:00:00Z
sources:
  - id: revenue-policy
    resource: policies/revenue-recognition.md
    title: Revenue Recognition Policy (FY2026)
    author: human:jsmith@acme
    last_modified: 2026-06-15T00:00:00Z
  - id: orders-table
    resource: tables/orders.md
    title: Customer Orders (BigQuery table)
    author: team:data-platform
    last_modified: 2026-07-01T00:00:00Z
---

# Computation

```sql
SELECT
  SUM(
    CASE
      WHEN o.currency = 'USD' THEN o.net_amount
      ELSE o.net_amount * fx.rate_to_usd
    END
  ) AS revenue_usd
FROM `acme.sales.orders` AS o
LEFT JOIN `acme.finance.fx_daily_rates` AS fx
  ON fx.currency = o.currency
  AND fx.rate_date = DATE(o.order_ts)
WHERE o.order_status = 'delivered'
  AND DATE_DIFF(CURRENT_DATE(), DATE(o.order_ts), DAY) >= 30
  AND EXTRACT(YEAR FROM o.order_ts) = @year
```

This computation implements the four rules of the FY2026 Revenue Recognition Policy: [^revenue-policy]

1. **Recognition trigger:** `order_status = 'delivered'` AND the 30-day return window has closed.
2. **Recognized amount:** `net_amount` (excludes shipping and tax).
3. **Currency:** non-USD orders convert at the `order_ts` daily rate.
4. **Fiscal year:** calendar year from `order_ts`.

# What the attester checks

`attesters/sql_equality.py` receives the receipt returned by `skills/run-on-bq.md` and verifies two things:

1. **Provenance:** `receipt.executed_sql`, canonicalized (whitespace, comment stripping, keyword casing), equals the SQL above canonicalized the same way. Any rewrite (a swapped table, an added filter, a dropped JOIN) fails the check.
2. **Fidelity:** the value the caller is about to display equals `receipt.result[0]`.

A run whose SQL does not match is treated as unattested; the consumer MUST refuse to display the value.

# Freshness

`stale_after: 2026-12-31T00:00:00Z` mirrors the revenue-recognition policy's annual review cycle. On 2027-01-01, a consumer running this computation SHOULD flag the result for re-verification before serving it, per the memory-aware consumer contract.

[^revenue-policy]: Revenue Recognition Policy (FY2026)
`````

## File: bundles/acme_retail/metrics/gross-margin-legacy.md
`````markdown
---
type: Metric
title: Gross Margin (legacy, pre-FY2026)
description: Retired gross-margin definition that included only product cost. Preserved for historical query reproducibility. Do not use for new analyses.
tags: [finance, margin, deprecated]
generated: { by: human:jsmith@acme, at: 2024-01-15T10:00:00Z }
verified:
  - { by: human:jsmith@acme, at: 2024-01-15T10:00:00Z }
status: deprecated
---

# Deprecated

**This metric is retired.** The current gross-margin definition is [`metrics/gross-margin.md`](./gross-margin.md), which implements the FY2026 Cost Allocation Standard (product cost + inbound fulfillment + outbound shipping + payment fees).

This concept is preserved so historical reports written before 2026-02-01 remain reproducible. Do not reference it for new work.

# Legacy definition (for reproducibility only)

Under the pre-FY2026 definition, gross margin was:

```
gross-margin-legacy(period) = revenue(period) - SUM(products.cost * order_lines.quantity)  over orders recognized in period
```

That is, COGS was product cost only; fulfillment, shipping, and payment fees were booked to operating expenses rather than COGS. Finance concluded in Q4 2025 that this understated the operational cost of goods and made the number unreconcilable to the general ledger.

# Why no attested computation

There is no `Attested Computation` for this metric. When it was retired, its SQL was deleted from the sanctioned set. Anyone re-running historical reports must reconstruct the SQL from this narrative and clearly label the result as legacy.
`````

## File: bundles/acme_retail/metrics/gross-margin.md
`````markdown
---
type: Metric
title: Gross Margin
description: Gross margin for a period, per Acme's FY2026 Cost Allocation Standard (product cost + inbound fulfillment + outbound shipping + payment fees).
tags: [finance, margin, headline-metric]
generated: { by: reference_agent/gemini-2.5-pro, at: 2026-06-30T14:00:00Z }
verified:
  - { by: human:jsmith@acme, at: 2026-07-01T09:00:00Z }
status: stable
stale_after: 2026-12-31T00:00:00Z
not:
  - term: "revenue minus product cost only"
    why: "that is the pre-FY2026 definition (see gross-margin-legacy). It excluded fulfillment, shipping, and payment fees, and could not be reconciled to the general ledger."
    instead: "revenue minus full COGS (product cost + inbound fulfillment + outbound shipping + payment fees)"
sources:
  - id: margin-standard
    resource: policies/margin-standard.md
    title: Cost Allocation & Margin Standard (FY2026)
    author: human:jsmith@acme
    last_modified: 2026-06-15T00:00:00Z
  - id: revenue-policy
    resource: policies/revenue-recognition.md
    title: Revenue Recognition Policy (FY2026)
    author: human:jsmith@acme
    last_modified: 2026-06-15T00:00:00Z
---

# Definition

**Not:** revenue minus product cost only (that was the pre-2026 formula; see [`gross-margin-legacy`](./gross-margin-legacy.md)).

Gross margin for a period equals recognized [Revenue](./revenue.md) minus **full COGS**, where full COGS is the sum of product cost, inbound fulfillment cost, outbound shipping cost, and payment processing fees. [^margin-standard]

```
gross_margin(period) = revenue(period) - cogs_full(period)
```

The sanctioned computation is [`computations/gross-margin-period.md`](../computations/gross-margin-period.md). Consumers MUST run and attest that computation.

# What changed in FY2026

Prior to 2026-02-01, Acme's gross-margin definition included only product cost, excluding fulfillment, shipping, and payment fees. That legacy definition is preserved in [`metrics/gross-margin-legacy.md`](./gross-margin-legacy.md) as `status: deprecated` for historical query reproducibility.

The switch reduced reported gross margin by roughly 4-6 percentage points depending on category. It also brought the number in line with the general ledger, closing a long-standing reconciliation gap.

# Trust and freshness

- **Verified:** VP Finance sign-off on 2026-07-01, against the FY2026 margin standard.
- **Stale after 2026-12-31:** the cost-allocation standard is reviewed annually. Consumers must re-verify against the FY2027 standard before serving.

[^margin-standard]: Cost Allocation & Margin Standard (FY2026)
[^revenue-policy]: Revenue Recognition Policy (FY2026)
`````

## File: bundles/acme_retail/metrics/index.md
`````markdown
# Metric

* [Revenue](revenue.md) - Recognized revenue per Acme's FY2026 policy.
* [Gross Margin](gross-margin.md) - Gross margin per Acme's FY2026 Cost Allocation Standard.
* [Gross Margin (legacy, pre-FY2026)](gross-margin-legacy.md) - Deprecated pre-2026 formula, kept for historical reproducibility.
`````

## File: bundles/acme_retail/metrics/revenue.md
`````markdown
---
type: Metric
title: Revenue
description: Recognized revenue for a period, per Acme's FY2026 revenue-recognition policy. Backed by an Attested Computation.
tags: [finance, revenue, headline-metric]
generated: { by: reference_agent/gemini-2.5-pro, at: 2026-06-30T14:00:00Z }
verified:
  - { by: human:jsmith@acme, at: 2026-07-01T09:00:00Z }
status: stable
stale_after: 2026-12-31T00:00:00Z
sources:
  - id: revenue-policy
    resource: policies/revenue-recognition.md
    title: Revenue Recognition Policy (FY2026)
    author: human:jsmith@acme
    last_modified: 2026-06-15T00:00:00Z
---

# Definition

Revenue for a fiscal year is the sum of `net_amount` over orders that (a) reached `order_status = 'delivered'`, (b) completed the 30-day return window, and (c) fall in the fiscal year by `order_ts`. Multi-currency orders are converted to USD at the `order_ts` daily reference rate. [^revenue-policy]

The sanctioned computation is [`computations/revenue-ytd.md`](../computations/revenue-ytd.md). Consumers MUST run and attest that computation rather than composing their own SUM. The attester rejects any receipt whose executed SQL does not match the sanctioned form.

# Reporting cuts

- **By fiscal year:** the sanctioned computation takes `year` as its sole parameter.
- **By channel or category:** these are approved narrations, not new metrics. Join the receipt's row-level result to `orders.channel` or to `order_lines` × `products.category` client-side. Do NOT rewrite the sanctioned SQL.

# Trust and freshness

- **Verified:** VP Finance sign-off on 2026-07-01, against the FY2026 policy.
- **Stale after 2026-12-31:** Finance re-issues the revenue recognition policy each January. Consumers of this concept after 2027-01-01 MUST re-verify the definition against the new policy before serving.

[^revenue-policy]: Revenue Recognition Policy (FY2026)
`````

## File: bundles/acme_retail/policies/index.md
`````markdown
# Policy

* [Revenue Recognition Policy (FY2026)](revenue-recognition.md) - When a customer order is recognized as revenue.
* [Cost Allocation & Margin Standard (FY2026)](margin-standard.md) - COGS composition and the standard gross-margin formula.
`````

## File: bundles/acme_retail/policies/margin-standard.md
`````markdown
---
type: Policy
title: Acme Retail — Cost Allocation & Margin Standard (FY2026)
description: Finance policy defining COGS composition and the standard gross-margin formula. Introduced FY2026 (superseded a legacy definition that excluded fulfillment/shipping).
resource: https://wiki.acme.internal/finance/margin-standard
tags: [finance, policy, margin, cogs]
generated: { by: human:jsmith@acme, at: 2026-02-01T10:00:00Z }
verified:
  - { by: human:jsmith@acme, at: 2026-06-15T09:00:00Z }
status: stable
stale_after: 2026-12-31T00:00:00Z
---

# Acme Retail Cost Allocation & Margin Standard — FY2026

**Owner:** VP Finance (jsmith@acme)
**Effective:** 2026-02-01
**Supersedes:** the pre-2026 margin definition (see `metrics/gross-margin-legacy.md`)

## COGS composition

FY2026 COGS for a completed order is the sum of:

1. **Product cost** — from `products.cost` at time of order (locked at order creation)
2. **Inbound fulfillment cost** — allocated per-unit from monthly warehouse aggregates
3. **Outbound shipping cost** — carrier-billed actuals from `logistics.shipment_cost`
4. **Payment processing fees** — Stripe fees from `finance.payment_fees`

The pre-2026 definition included only (1). Adding (2) — (4) reduces reported gross margin by ~4-6 percentage points but produces a number Finance can reconcile to the GL.

## Gross margin formula

For a period P:

```
gross_margin(P) = SUM(net_amount) - SUM(cogs_full)   over orders recognized in P
```

Where `cogs_full` is the sum of the four components above.

## Reporting granularity

The standard supports gross margin at three levels: portfolio, category, and SKU. Category and SKU cuts require joining `orders` to `products` on `product_id`.

## What this policy authorizes

Any Attested Computation whose `sources` cites this policy MUST use all four COGS components. The legacy formula (product-cost-only) is preserved in `metrics/gross-margin-legacy.md` for historical query reproducibility; do not use it for new analyses.

# Cited by

- [`metrics/gross-margin`](/metrics/gross-margin.md) — current gross-margin metric implements this standard
- [`metrics/gross-margin-legacy`](/metrics/gross-margin-legacy.md) — deprecated metric, superseded by the definition this standard authorizes
- [`computations/gross-margin-period`](/computations/gross-margin-period.md) — sanctioned SQL implements the four COGS components defined here
`````

## File: bundles/acme_retail/policies/revenue-recognition.md
`````markdown
---
type: Policy
title: Acme Retail — Revenue Recognition Policy (FY2026)
description: Finance policy defining when a customer order is recognized as revenue. Reviewed annually.
resource: https://wiki.acme.internal/finance/revenue-recognition
tags: [finance, policy, revenue]
generated: { by: human:jsmith@acme, at: 2026-01-05T10:00:00Z }
verified:
  - { by: human:jsmith@acme, at: 2026-06-15T09:00:00Z }
status: stable
stale_after: 2026-12-31T00:00:00Z
---

# Acme Retail Revenue Recognition Policy — FY2026

**Owner:** VP Finance (jsmith@acme)
**Effective:** 2026-01-01
**Next scheduled review:** 2026-12-31

## Recognition trigger

Revenue is recognized when a customer order reaches `order_status = 'delivered'` **and** the return window has closed (delivered date + 30 days). Orders in earlier statuses are backlog, not revenue.

## Recognized amount

The recognized amount for an order equals `net_amount = gross_amount - discount_amount`. Shipping and tax are excluded from revenue per US GAAP (they are pass-through liabilities).

## Currency

Multi-currency orders are converted at the daily reference rate published in `finance.fx_daily_rates`, using the `order_ts` date. All reporting is in USD.

## Refunds and cancellations

Refunds and post-recognition cancellations are booked as contra-revenue in the period of the refund, not by retroactive adjustment to the original recognition period.

## Fiscal year

Acme Retail operates on the US calendar year (Jan 1 – Dec 31). All fiscal-year metrics use `fiscal_year = EXTRACT(YEAR FROM order_ts)`.

## What this policy authorizes

Any Attested Computation whose `sources` cites this policy MUST implement the four rules above. Deviations require a policy addendum reviewed by Finance.

# Cited by

- [`tables/orders`](/tables/orders.md) — `order_status`, `order_ts`, and `net_amount` columns implement the recognition rules
- [`metrics/revenue`](/metrics/revenue.md) — the recognized-revenue definition derives from this policy
- [`metrics/gross-margin`](/metrics/gross-margin.md) — the revenue side of gross margin follows this policy
- [`computations/revenue-ytd`](/computations/revenue-ytd.md) — the sanctioned SQL implements all four rules
- [`computations/gross-margin-period`](/computations/gross-margin-period.md) — revenue leg uses these recognition rules
`````

## File: bundles/acme_retail/skills/index.md
`````markdown
# Skill

* [Run an Attested Computation on BigQuery](run-on-bq.md) - Executor for Attested Computations with runtime: bigquery.
`````

## File: bundles/acme_retail/skills/run-on-bq.md
`````markdown
---
type: Skill
title: Run an Attested Computation on BigQuery
description: "Executor skill for `Attested Computation` concepts with `runtime: bigquery`. Binds declared parameters, submits the job, and returns a receipt the attester will verify."
tags: [skill, executor, bigquery]
generated: { by: human:kliu@acme, at: 2026-06-30T14:00:00Z }
status: stable
---

# Skill: run on BigQuery

## When to use

The `executor.resource` field of an `Attested Computation` points here when the computation's `runtime` is `bigquery`.

## Preconditions

- Caller has a service account with `bigquery.jobs.create` on the concept's `resource` project.
- Caller has read access on every table referenced by the computation's `# Computation` fence (or the file at `computation:`).
- The concept declares its `parameters:` list. Every required parameter has been supplied a value by the caller.

## Steps

1. **Load the computation.** Read the `# Computation` fence from the concept body, or the file at `computation:` if the field is set. The result is a SQL string containing `@name`-style bind variables for each declared parameter.
2. **Bind parameters.** Pass the caller-supplied values as BigQuery [named query parameters](https://cloud.google.com/bigquery/docs/parameterized-queries). Do NOT string-interpolate; the attester will reject a receipt whose `executed_sql` shows literal substitution.
3. **Submit the job.** Use `jobs.query` (or `jobs.insert` with a `Query` configuration). Set `useLegacySql: false`. Set the job's `labels` to include `okf_concept: <bundle-relative-path>` for auditability.
4. **Wait for completion.** Poll `jobs.get` until `status.state = 'DONE'`. If `status.errorResult` is present, return the receipt with `result: null` and `error: <errorResult>` so the attester can distinguish "sanctioned SQL that failed at runtime" from "the executor ran the wrong SQL."
5. **Assemble the receipt.** Return exactly the fields declared in `executor.receipt`. For this skill:

    ```json
    {
      "job_id": "bq://<project>/us/<jobId>",
      "executed_sql": "<queryConfig.query with parameters shown as @name>",
      "result": "<the first result row's cell values, in declared select-order>"
    }
    ```

6. **Never modify the computation.** If the caller-supplied parameters cannot be bound (missing required, wrong type), refuse and return an error receipt. Do NOT rewrite the SQL to work around missing parameters.

## Post-conditions

The receipt is handed to the concept's `attester.resource`. Do not display the value to the user until the attester returns `verdict: ok`.
`````

## File: bundles/acme_retail/tables/index.md
`````markdown
# BigQuery Table

* [Customer Orders](orders.md) - One row per completed customer order across web, mobile, and marketplace channels.
`````

## File: bundles/acme_retail/tables/orders.md
`````markdown
---
type: BigQuery Table
title: Customer Orders
description: One row per completed customer order across web, mobile, and marketplace channels. The grain is the order, not the line item; per-line product detail lives in `order_lines`.
resource: https://console.cloud.google.com/bigquery?p=acme&d=sales&t=orders
tags: [sales, orders, revenue]
generated: { by: reference_agent/gemini-2.5-pro, at: 2026-06-30T14:00:00Z }
verified:
  - { by: human:kliu@acme, at: 2026-07-01T16:00:00Z }
status: stable
stale_after: 2026-12-31T00:00:00Z
sources:
  - id: warehouse-schema
    resource: https://wiki.acme.internal/data/warehouse/schemas/sales
    title: Acme Retail warehouse schema — sales dataset
    author: team:data-platform
    usage_count: 1240
    last_modified: 2026-06-15T00:00:00Z
  - id: revenue-policy
    resource: policies/revenue-recognition.md
    title: Revenue Recognition Policy (FY2026)
    author: human:jsmith@acme
    last_modified: 2026-06-15T00:00:00Z
usage_window: { from: 2026-04-01T00:00:00Z, to: 2026-06-30T00:00:00Z }
---

# Schema

| Column | Type | Description |
|---|---|---|
| `order_id` | STRING | Globally unique order id. Generated at order creation. [^warehouse-schema] |
| `customer_id` | STRING | FK into `customers`. Never null for completed orders. [^warehouse-schema] |
| `order_ts` | TIMESTAMP | Order placement time in UTC. This is the timestamp used for fiscal-year assignment. [^revenue-policy] |
| `order_status` | STRING | One of `pending`, `paid`, `shipped`, `delivered`, `cancelled`, `refunded`. Revenue is recognized only when `order_status = 'delivered'` and the 30-day return window has closed. [^revenue-policy] |
| `gross_amount` | NUMERIC(18,4) | Pre-discount subtotal, in `currency`. Excludes tax and shipping. [^warehouse-schema] |
| `discount_amount` | NUMERIC(18,4) | Total discounts applied (promo codes, loyalty credits, price adjustments). [^warehouse-schema] |
| `net_amount` | NUMERIC(18,4) | `gross_amount - discount_amount`. This is the recognized-revenue amount per policy. [^revenue-policy] |
| `shipping_amount` | NUMERIC(18,4) | Carrier charge billed to the customer. Excluded from revenue (pass-through liability). [^revenue-policy] |
| `tax_amount` | NUMERIC(18,4) | Sales tax collected. Excluded from revenue (pass-through liability). [^revenue-policy] |
| `currency` | STRING | ISO 4217 currency code. Non-USD orders convert via `finance.fx_daily_rates` on `order_ts` date. [^revenue-policy] |
| `channel` | STRING | Order origin: `web`, `mobile`, `marketplace`. Marketplace orders (Amazon, eBay) are net-settled and recognized on marketplace payout, not on `order_status = 'delivered'`. |

# Notes for consumers

- The grain assumption trips up new analysts: `SUM(net_amount) GROUP BY order_id` is a no-op because there is exactly one row per order. For per-SKU revenue, join `order_lines`.
- The `refunded` status is terminal in this table; the refund event itself lives in `finance.refunds`, keyed on `order_id`.

[^warehouse-schema]: Acme Retail warehouse schema — sales dataset
[^revenue-policy]: Revenue Recognition Policy (FY2026)
`````

## File: bundles/acme_retail/index.md
`````markdown
# Subdirectories

* [tables](tables/index.md) - BigQuery tables the bundle grounds against.
* [metrics](metrics/index.md) - Business definitions of Acme Retail's headline numbers.
* [computations](computations/index.md) - Sanctioned SQL as Attested Computations for each metric.
* [policies](policies/index.md) - Source-of-truth Finance policy documents.
* [skills](skills/index.md) - Executor instructions for running Attested Computations.
* [attesters](attesters/index.md) - Deterministic verification code for computation receipts.
`````

## File: bundles/acme_retail/log.md
`````markdown
---
type: Log
title: Acme Retail bundle history
---

# Bundle history

## 2026-07-01

- **Verified** the full bundle for OKF v0.2 conformance. `human:kliu@acme` reviewed all `verified` and `sources` entries.

## 2026-06-30

- **Re-generated** `metrics/revenue.md`, `computations/revenue-ytd.md`, and `policies/revenue-recognition.md` after Finance published the FY2026 revenue recognition policy addendum. Updated `stale_after` on both revenue concepts to `2026-12-31T00:00:00Z`.

## 2026-04-15

- **Deprecated** the legacy gross-margin definition. Original file moved to `metrics/gross-margin-legacy.md` with `status: deprecated`. New definition at `metrics/gross-margin.md` implements the FY2026 Cost Allocation Standard (includes fulfillment and shipping costs in COGS).

## 2026-02-10

- **Bundle bootstrapped** by `reference_agent/gemini-2.5-pro` from the BigQuery `INFORMATION_SCHEMA` and a 90-day sample of `region-us.INFORMATION_SCHEMA.JOBS_BY_PROJECT`. Initial trust tier: machine-confirmed across the board; finance-critical concepts flagged for human review.
`````

## File: bundles/crypto_bitcoin/datasets/crypto_bitcoin.md
`````markdown
---
type: BigQuery Dataset
resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/crypto_bitcoin
title: Bitcoin Blockchain Dataset
description: A public Google BigQuery dataset containing the complete transaction
  ledger and block history of the Bitcoin blockchain.
tags:
- bitcoin
- blockchain
- crypto
- public-data
generated:
  by: reference_agent/gemini-3.5-flash
  at: '2026-07-10T23:14:11+00:00'
sources:
- title: BigQuery Dataset Metadata - crypto_bitcoin
  resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/crypto_bitcoin
  id: bq-crypto-bitcoin-meta
---

The `crypto_bitcoin` dataset is a public Google BigQuery dataset containing the entire blockchain transaction history for Bitcoin. It is updated continuously and provides a highly structured, queryable format of block and transaction data from the genesis block onwards.

The dataset contains four primary tables:
- [blocks](../tables/blocks.md) representing Bitcoin blocks, including hashes, sizes, transaction counts, and block rewards.
- [transactions](../tables/transactions.md) containing top-level transaction details such as inputs/outputs totals, fees, and cryptographic signatures.
- [inputs](../tables/inputs.md) containing the transaction inputs (spending previous outputs) representing the source of funds.
- [outputs](../tables/outputs.md) containing the transaction outputs representing the destinations of funds (addresses and values).

This dataset is widely used for blockchain forensics, macroeconomic analysis of transaction volumes, wallet balance tracking, and research into mining activities.

# Schema

As a BigQuery Dataset, `crypto_bitcoin` acts as a namespace and container for the following tables:

| Table ID | Description |
| :--- | :--- |
| **[blocks](../tables/blocks.md)** | Blocks containing transactions that have been validated and written to the ledger. |
| **[transactions](../tables/transactions.md)** | Individual ledger entries where value is transferred between participants. |
| **[inputs](../tables/inputs.md)** | References to UTXOs (Unspent Transaction Outputs) being spent in transactions. |
| **[outputs](../tables/outputs.md)** | Outputs created by transactions that become new UTXOs. |

# Common query patterns

### 1. Count of blocks and average transaction count per block by month
This query calculates the monthly volume of blocks and the average number of transactions included per block.

```sql
SELECT
  TIMESTAMP_TRUNC(timestamp, MONTH) AS month,
  COUNT(1) AS total_blocks,
  AVG(transaction_count) AS avg_transactions_per_block
FROM
  `bigquery-public-data.crypto_bitcoin.blocks`
GROUP BY
  month
ORDER BY
  month DESC
LIMIT 12;
```

### 2. Transaction fee statistics (in Satoshis) over the last 30 days
This query explores transaction fee distributions across recent transactions.

```sql
SELECT
  MIN(fee) AS min_fee,
  MAX(fee) AS max_fee,
  AVG(fee) AS avg_fee,
  APPROX_QUANTILES(fee, 2)[OFFSET(1)] AS median_fee
FROM
  `bigquery-public-data.crypto_bitcoin.transactions`
WHERE
  block_timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY);
```
`````

## File: bundles/crypto_bitcoin/datasets/index.md
`````markdown
# BigQuery Dataset

* [Bitcoin Blockchain Dataset](crypto_bitcoin.md) - A public Google BigQuery dataset containing the complete transaction ledger and block history of the Bitcoin blockchain.
`````

## File: bundles/crypto_bitcoin/references/joins/blocks___transactions.md
`````markdown
---
type: Reference
resource: https://github.com/blockchain-etl/bitcoin-etl
title: Blocks to Transactions Join Path
description: Join relationship linking blocks to their corresponding transactions
  by block height / block number.
tags:
- join
- bitcoin
generated:
  by: reference_agent/gemini-3.5-flash
  at: '2026-07-10T23:15:51+00:00'
sources:
- id: bitcoin-etl
  resource: https://github.com/blockchain-etl/bitcoin-etl
  title: Bitcoin ETL Parser
---

This join path represents the link between a block and all the transactions included in that block. This is useful for analyzing block density, mining fee shares, and validating transaction confirmation times relative to block production.

```sql
SELECT
  b.number AS block_height,
  b.hash AS block_hash,
  b.timestamp AS block_timestamp,
  t.hash AS transaction_hash,
  t.fee AS transaction_fee
FROM
  `bigquery-public-data.crypto_bitcoin.blocks` AS b
JOIN
  `bigquery-public-data.crypto_bitcoin.transactions` AS t
ON
  b.number = t.block_number;
```
`````

## File: bundles/crypto_bitcoin/references/joins/index.md
`````markdown
# Reference

* [Blocks to Transactions Join Path](blocks___transactions.md) - Join relationship linking blocks to their corresponding transactions by block height / block number.
* [Transactions to Inputs Join Path](inputs___transactions.md) - Join path between transactions and inputs to trace fund consumption details.
* [Transactions to Outputs Join Path](outputs___transactions.md) - Join path between transactions and outputs to audit target recipient distribution.
`````

## File: bundles/crypto_bitcoin/references/joins/inputs___transactions.md
`````markdown
---
type: Reference
resource: https://github.com/blockchain-etl/bitcoin-etl
title: Transactions to Inputs Join Path
description: Join path between transactions and inputs to trace fund consumption details.
tags:
- join
- bitcoin
generated:
  by: reference_agent/gemini-3.5-flash
  at: '2026-07-10T23:15:56+00:00'
sources:
- id: bitcoin-etl
  title: Bitcoin ETL Parser
  resource: https://github.com/blockchain-etl/bitcoin-etl
---

This join path connects transactions to their inputs. In the Unspent Transaction Output (UTXO) database structure, joining the main `transactions` table with the flat `inputs` table lets analysts audit the historical origin of funds being consumed in a transaction.

```sql
SELECT
  t.hash AS transaction_hash,
  t.block_timestamp AS transaction_timestamp,
  i.index AS input_index,
  i.spent_transaction_hash,
  i.spent_output_index,
  i.value AS input_value_satoshis
FROM
  `bigquery-public-data.crypto_bitcoin.transactions` AS t
JOIN
  `bigquery-public-data.crypto_bitcoin.inputs` AS i
ON
  t.hash = i.transaction_hash;
```
`````

## File: bundles/crypto_bitcoin/references/joins/outputs___transactions.md
`````markdown
---
type: Reference
resource: https://github.com/blockchain-etl/bitcoin-etl
title: Transactions to Outputs Join Path
description: Join path between transactions and outputs to audit target recipient
  distribution.
tags:
- join
- bitcoin
generated:
  by: reference_agent/gemini-3.5-flash
  at: '2026-07-10T23:15:59+00:00'
sources:
- title: Bitcoin ETL Parser
  resource: https://github.com/blockchain-etl/bitcoin-etl
  id: bitcoin-etl
---

This join path relates a transaction to its generated outputs. Joining `transactions` with `outputs` is useful for tracking how funds are distributed (split or forwarded) from a parent transaction into target addresses.

```sql
SELECT
  t.hash AS transaction_hash,
  t.block_timestamp AS transaction_timestamp,
  o.index AS output_index,
  o.addresses,
  o.value AS output_value_satoshis
FROM
  `bigquery-public-data.crypto_bitcoin.transactions` AS t
JOIN
  `bigquery-public-data.crypto_bitcoin.outputs` AS o
ON
  t.hash = o.transaction_hash;
```
`````

## File: bundles/crypto_bitcoin/references/metrics/duplicate_transactions.md
`````markdown
---
type: Reference
resource: https://cloud.google.com/blog/topics/public-datasets/bitcoin-in-bigquery-blockchain-analytics-on-public-data
title: Duplicate Transactions Metric
description: An anomaly detection metric to find historical duplicate transactions
  across different blocks.
tags:
- metric
- anomaly-detection
- bitcoin
generated:
  by: reference_agent/gemini-3.5-flash
  at: '2026-07-10T23:15:47+00:00'
sources:
- id: gcp-blog
  title: 'Bitcoin in BigQuery: blockchain analytics on public data'
  resource: https://cloud.google.com/blog/topics/public-datasets/bitcoin-in-bigquery-blockchain-analytics-on-public-data
---

The anomaly query pattern identifies transactions that appear in multiple blocks. Historically, in the Bitcoin blockchain, transactions could be duplicated due to a behavior in the original BerkeleyDB database engine that allowed non-unique keys. This was later addressed by implementing Bitcoin Improvement Proposal [BIP-0030](https://github.com/bitcoin/bips/blob/master/bip-0030.mediawiki) and transitioning to LevelDB.

### standardSQL
```sql
SELECT
  transaction_id,
  COUNT(transaction_id) AS dup_transaction_count
FROM (
  SELECT
    hash AS transaction_id
  FROM
    `bigquery-public-data.crypto_bitcoin.transactions`
)
GROUP BY
  transaction_id
HAVING
  dup_transaction_count > 1;
```
`````

## File: bundles/crypto_bitcoin/references/metrics/index.md
`````markdown
# Reference

* [Duplicate Transactions Metric](duplicate_transactions.md) - An anomaly detection metric to find historical duplicate transactions across different blocks.
`````

## File: bundles/crypto_bitcoin/references/index.md
`````markdown
# Subdirectories

* [joins](joins/index.md) - This directory contains join paths linking blocks to transactions and transactions to their corresponding inputs and outputs to trace transaction details.
* [metrics](metrics/index.md) - An anomaly detection metric to find historical duplicate transactions across different blocks.
`````

## File: bundles/crypto_bitcoin/tables/blocks.md
`````markdown
---
type: BigQuery Table
resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/crypto_bitcoin/tables/blocks
title: Bitcoin Blocks Table
description: All blocks from the Bitcoin blockchain, including block headers, transaction
  counts, sizes, and timestamps.
tags:
- bitcoin
- blockchain
- crypto
generated:
  by: reference_agent/gemini-3.5-flash
  at: '2026-07-10T23:16:06+00:00'
sources:
- resource: https://github.com/blockchain-etl/bitcoin-etl
  title: Bitcoin ETL Export Tool
  id: bitcoin-etl
- id: bip-141
  resource: https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki
  title: BIP-141 Segregated Witness (Consensus layer)
---

The `blocks` table contains structured records for every block in the Bitcoin blockchain [^bitcoin-etl]. Each row in this table represents a single block, captured with detailed block header attributes such as hash, size, transaction count, nonce, difficulty bits, and the Merkle root of all transactions contained within that block.

The dataset is continually exported from live nodes and represents a complete historical index of Bitcoin blocks starting from the genesis block in January 2009. The table is partitioned by month using the `timestamp_month` column to optimize query performance and lower data scanning costs when filtering blocks by date.

The table can be joined with [transactions](transactions.md) to drill down into individual payments or to aggregate block-level statistics like total transaction fees, transaction densities, and witness data weights.

# Schema

| Field Name | Type | Mode | Description |
| :--- | :--- | :--- | :--- |
| **hash** | STRING | REQUIRED | Unique block hash that identifies the block. |
| **size** | INTEGER | NULLABLE | Total size of the block data in bytes. |
| **stripped_size** | INTEGER | NULLABLE | The size of block data in bytes excluding witness data. |
| **weight** | INTEGER | NULLABLE | Three times the base size plus the total size as defined in BIP-141 [^bip-141]. |
| **number** | INTEGER | REQUIRED | The sequential height of the block. |
| **version** | INTEGER | NULLABLE | Protocol version specified in the block header. |
| **merkle_root** | STRING | NULLABLE | The root node of a Merkle tree, where leaves are transaction hashes. |
| **timestamp** | TIMESTAMP | REQUIRED | Block creation timestamp specified in the block header. |
| **timestamp_month** | DATE | REQUIRED | Month of the block creation timestamp (used as the partitioning key). |
| **nonce** | STRING | NULLABLE | Difficulty solution specified in the block header. |
| **bits** | STRING | NULLABLE | Difficulty threshold specified in the block header. |
| **coinbase_param** | STRING | NULLABLE | Data specified in the coinbase transaction of this block. |
| **transaction_count** | INTEGER | NULLABLE | Number of transactions included in this block. |

# Common query patterns

### 1. Daily block counts and average transactions per block
Find out how many blocks are mined each day and the average number of transactions per block for a specific month.

```sql
SELECT
  DATE(timestamp) AS block_date,
  COUNT(1) AS blocks_mined,
  AVG(transaction_count) AS avg_transactions_per_block,
  SUM(transaction_count) AS total_transactions
FROM
  `bigquery-public-data.crypto_bitcoin.blocks`
WHERE
  timestamp_month = '2023-10-01'
GROUP BY
  block_date
ORDER BY
  block_date ASC;
```

### 2. Retrieve details for a specific block height
Lookup a single block's metadata and structure using its height number.

```sql
SELECT
  number,
  hash,
  timestamp,
  size,
  transaction_count,
  version,
  coinbase_param
FROM
  `bigquery-public-data.crypto_bitcoin.blocks`
WHERE
  number = 800000;
```

### 3. Calculate monthly average block size and weight
Analyze the adoption and impact of SegWit over time by analyzing the trends in block size, stripped size, and SegWit weight [^bip-141].

```sql
SELECT
  timestamp_month,
  COUNT(1) AS blocks_mined,
  AVG(size) AS avg_block_size_bytes,
  AVG(stripped_size) AS avg_stripped_size_bytes,
  AVG(weight) AS avg_weight
FROM
  `bigquery-public-data.crypto_bitcoin.blocks`
WHERE
  timestamp_month >= '2020-01-01'
GROUP BY
  timestamp_month
ORDER BY
  timestamp_month DESC;
```

# Joins

- [transactions](../references/joins/blocks___transactions.md) — Connects blocks to all included transactions to trace block validation times, miner fee revenue, or transaction densities.

[^bitcoin-etl]: https://github.com/blockchain-etl/bitcoin-etl
[^bip-141]: https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki
`````

## File: bundles/crypto_bitcoin/tables/index.md
`````markdown
# BigQuery Table

* [Bitcoin Blocks Table](blocks.md) - All blocks from the Bitcoin blockchain, including block headers, transaction counts, sizes, and timestamps.
* [Bitcoin Outputs Table](outputs.md) - Outputs from all Bitcoin transactions, including script details and values in Satoshis.
* [Bitcoin Transaction Inputs](inputs.md) - Bitcoin transaction inputs detailing UTXOs spent.
* [Bitcoin Transactions Table](transactions.md) - All Bitcoin transactions containing inputs, outputs, block metadata, and fee structures.
`````

## File: bundles/crypto_bitcoin/tables/inputs.md
`````markdown
---
type: BigQuery Table
resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/crypto_bitcoin/tables/inputs
title: Bitcoin Transaction Inputs
description: Bitcoin transaction inputs detailing UTXOs spent.
tags:
- bitcoin
- crypto
- blockchain
- utxo
- inputs
generated:
  by: reference_agent/gemini-3.5-flash
  at: '2026-07-10T23:16:22+00:00'
sources:
- resource: https://github.com/blockchain-etl/bitcoin-etl
  title: Bitcoin ETL GitHub Repository
  id: bitcoin-etl
---

The `inputs` table contains details of all transaction inputs (UTXOs spent) on the Bitcoin blockchain. Each row represents a single input that was consumed to fund a transaction[^bitcoin-etl]. Because Bitcoin uses an Unspent Transaction Output (UTXO) model, every transaction consumes existing outputs (which become "inputs" in the new transaction) and creates new outputs[^bitcoin-etl].

This table is particularly useful for tracking the flow of funds, analyzing spending behavior, and tracing transaction lineage. By linking the `spent_transaction_hash` and `spent_output_index` of an input back to the [outputs](outputs.md) table, analysts can fully reconstruct the transaction graph.

Data is exported from the blockchain using the open-source [bitcoin-etl](https://github.com/blockchain-etl/bitcoin-etl) tool[^bitcoin-etl] and is housed in the [crypto_bitcoin](../datasets/crypto_bitcoin.md) dataset.

# Schema

| Field Name | Type | Mode | Description |
| :--- | :--- | :--- | :--- |
| **transaction_hash** | STRING | NULLABLE | Hash of the transaction containing this input |
| **block_hash** | STRING | NULLABLE | Hash of the block containing this transaction |
| **block_number** | INTEGER | NULLABLE | Height of the block containing this transaction |
| **block_timestamp** | TIMESTAMP | NULLABLE | Timestamp of the block containing this transaction |
| **index** | INTEGER | NULLABLE | 0-based index of this input within the transaction |
| **spent_transaction_hash** | STRING | NULLABLE | Hash of the transaction containing the output spent by this input |
| **spent_output_index** | INTEGER | NULLABLE | Index of the output spent by this input in the original transaction |
| **script_asm** | STRING | NULLABLE | Symbolic representation of the input's script (scriptSig) |
| **script_hex** | STRING | NULLABLE | Hexadecimal representation of the input's script (scriptSig) |
| **sequence** | INTEGER | NULLABLE | Transaction input sequence number |
| **required_signatures** | INTEGER | NULLABLE | Number of signatures required to spend (if applicable) |
| **type** | STRING | NULLABLE | Type of script (e.g., `witness_v1_taproot`, `pubkeyhash`) |
| **addresses** | STRING | REPEATED | List of addresses associated with this input |
| **value** | NUMERIC | NULLABLE | Value of the spent output in Satoshis |

# Common query patterns

### 1. Identify the largest transaction inputs in a given period
This query retrieves the largest inputs consumed on a specific day, demonstrating how to find massive UTXO consolidations or large-value transfers.

```sql
SELECT
  block_timestamp,
  transaction_hash,
  value / 100000000 AS value_btc,
  addresses
FROM `bigquery-public-data.crypto_bitcoin.inputs`
WHERE block_timestamp >= '2024-04-17 00:00:00 UTC'
  AND block_timestamp < '2024-04-18 00:00:00 UTC'
ORDER BY value DESC
LIMIT 10;
```

### 2. Track input types over time
Analyze the adoption of modern Bitcoin script types (like Taproot) by counting inputs grouped by their transaction script type.

```sql
SELECT
  DATE(block_timestamp) AS block_date,
  type,
  COUNT(1) AS input_count,
  SUM(value) / 100000000 AS total_value_btc
FROM `bigquery-public-data.crypto_bitcoin.inputs`
WHERE block_timestamp >= '2024-01-01 00:00:00 UTC'
GROUP BY block_date, type
ORDER BY block_date DESC, input_count DESC;
```

### 3. Trace provenance by joining inputs and outputs
To find where funds spent in a transaction came from, you can join the inputs table to the outputs table using the spent transaction keys.

```sql
SELECT
  inp.transaction_hash AS spending_tx,
  inp.block_timestamp AS spend_time,
  out.transaction_hash AS source_tx,
  out.block_timestamp AS source_time,
  inp.value / 100000000 AS value_btc
FROM `bigquery-public-data.crypto_bitcoin.inputs` AS inp
JOIN `bigquery-public-data.crypto_bitcoin.outputs` AS out
  ON inp.spent_transaction_hash = out.transaction_hash
  AND inp.spent_output_index = out.index
WHERE inp.block_timestamp >= '2024-04-17 00:00:00 UTC'
  AND inp.block_timestamp < '2024-04-17 01:00:00 UTC'
LIMIT 10;
```

# Joins

- [transactions](../references/joins/inputs___transactions.md) — Connects this spent input to the parent transaction record which spent it.

[^bitcoin-etl]: https://github.com/blockchain-etl/bitcoin-etl
`````

## File: bundles/crypto_bitcoin/tables/outputs.md
`````markdown
---
type: BigQuery Table
resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/crypto_bitcoin/tables/outputs
title: Bitcoin Outputs Table
description: Outputs from all Bitcoin transactions, including script details and values
  in Satoshis.
tags:
- bitcoin
- blockchain
- crypto
- utxo
generated:
  by: reference_agent/gemini-3.5-flash
  at: '2026-07-10T23:16:28+00:00'
sources:
- id: bitcoin-etl
  resource: https://github.com/blockchain-etl/bitcoin-etl
  title: Bitcoin ETL Export Tool
- title: BigQuery Bitcoin Outputs Table Metadata
  resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/crypto_bitcoin/tables/outputs
  id: outputs-table
---

The `outputs` table contains structured data representing all transaction outputs (also known as UTXOs or Unspent Transaction Outputs before they are spent) in the Bitcoin blockchain. Each row represents a single output generated by a transaction, which specifies an amount of satoshis (value) and the cryptographic conditions (locking script) required to spend it.

Data is extracted and exported from the blockchain ledger using the open-source `bitcoin-etl` tool[^bitcoin-etl]. This table belongs to the [crypto_bitcoin](../datasets/crypto_bitcoin.md) dataset and can be joined with sibling tables such as [transactions](transactions.md) and [inputs](inputs.md) to reconstruct full transaction lineages and trace the movement of funds across the network.

### Grain and Interpretation

The table grain is **one row per transaction output**, uniquely identified by the combination of `transaction_hash` and output `index`. The `value` field represents the output amount in Satoshis (where 1 BTC = 100,000,000 Satoshis), represented as a high-precision `NUMERIC` type.

# Schema

| Field Name | Type | Mode | Description |
|---|---|---|---|
| `transaction_hash` | STRING | NULLABLE | Hash of the transaction containing this output. |
| `block_hash` | STRING | NULLABLE | Hash of the block containing this transaction. |
| `block_number` | INTEGER | NULLABLE | The block number/height. |
| `block_timestamp` | TIMESTAMP | NULLABLE | Timestamp of when the block was mined. |
| `index` | INTEGER | NULLABLE | The zero-based index of the output within the transaction. |
| `script_asm` | STRING | NULLABLE | Symbolic representation (Assembly) of the locking script. |
| `script_hex` | STRING | NULLABLE | Hexadecimal representation of the locking script. |
| `required_signatures` | INTEGER | NULLABLE | Number of signatures required to spend this output (typically 1 for common addresses). |
| `type` | STRING | NULLABLE | Type of the script (e.g., `pubkeyhash`, `scripthash`). |
| `addresses` | STRING | REPEATED | List of Bitcoin addresses associated with this output (normally contains a single address). |
| `value` | NUMERIC | NULLABLE | The value of the output in Satoshis (1 BTC = 100,000,000 Satoshis). |

# Common query patterns

### 1. Calculate the total value of transaction outputs generated on a specific day
The following query aggregates the output values for a given day to find the total volume minted, converting Satoshis to Bitcoin (BTC).

```sql
SELECT
  DATE(block_timestamp) AS date,
  SUM(value) / 100000000.0 AS total_btc_volume,
  COUNT(1) AS output_count
FROM `bigquery-public-data.crypto_bitcoin.outputs`
WHERE block_timestamp >= '2023-01-01 00:00:00 UTC'
  AND block_timestamp < '2023-01-02 00:00:00 UTC'
GROUP BY 1;
```

### 2. Find the largest transaction outputs for a given block
This query lists the highest-value outputs in block number 301641, along with the receiving addresses.

```sql
SELECT
  transaction_hash,
  `index`,
  addresses,
  value / 100000000.0 AS btc_value,
  type
FROM `bigquery-public-data.crypto_bitcoin.outputs`
WHERE block_number = 301641
ORDER BY value DESC
LIMIT 5;
```

### 3. Analyze output types over a specific time range
This query identifies the popularity of different script locking types (such as `pubkeyhash` or `scripthash`) over a weekly timeframe.

```sql
SELECT
  type,
  COUNT(1) AS output_count,
  SUM(value) / 100000000.0 AS total_btc
FROM `bigquery-public-data.crypto_bitcoin.outputs`
WHERE block_timestamp >= '2023-06-01 00:00:00 UTC'
  AND block_timestamp < '2023-06-08 00:00:00 UTC'
GROUP BY type
ORDER BY output_count DESC;
```

# Joins

- [transactions](../references/joins/outputs___transactions.md) — Connects this output back to the parent transaction record that created it.

[^bitcoin-etl]: Blockchain ETL Bitcoin Extractor: https://github.com/blockchain-etl/bitcoin-etl
`````

## File: bundles/crypto_bitcoin/tables/transactions.md
`````markdown
---
type: BigQuery Table
resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/crypto_bitcoin/tables/transactions
title: Bitcoin Transactions Table
description: All Bitcoin transactions containing inputs, outputs, block metadata,
  and fee structures.
tags:
- bitcoin
- crypto
- blockchain
- transactions
generated:
  by: reference_agent/gemini-3.5-flash
  at: '2026-07-10T23:16:14+00:00'
sources:
- title: Bitcoin ETL Parser
  resource: https://github.com/blockchain-etl/bitcoin-etl
  id: bitcoin-etl
- resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/crypto_bitcoin/tables/transactions
  id: bq-metadata
  title: BigQuery transactions Table Schema
- resource: https://cloud.google.com/blog/topics/public-datasets/bitcoin-in-bigquery-blockchain-analytics-on-public-data
  id: gcp-blog
  title: 'Bitcoin in BigQuery: blockchain analytics on public data'
---

This table contains all Bitcoin transactions since the genesis block in January 2009. The data is exported from the Bitcoin blockchain using the open-source `bitcoin-etl` utility.[^bitcoin-etl] The grain of this table is one row per transaction.

Each transaction contains structural data such as its hash, size, coinbase indicator, block metadata (like block number, hash, and timestamp), fees, and nested records representing its spending inputs and resulting outputs. To perform cost-effective queries, the table is partitioned on the `block_timestamp_month` column.

This table links directly to several sibling tables in the [crypto_bitcoin](../datasets/crypto_bitcoin.md) dataset, such as [blocks](blocks.md). While inputs and outputs are nested as repeated records here, they are also flattened into dedicated sibling tables: [inputs](inputs.md) and [outputs](outputs.md).

# Schema

| Field Name | Type | Mode | Description |
|---|---|---|---|
| **hash** | STRING | REQUIRED | The unique SHA-256 hash of this transaction |
| **size** | INTEGER | NULLABLE | The size of this transaction in bytes |
| **virtual_size** | INTEGER | NULLABLE | The virtual transaction size (differs from size for SegWit/witness transactions) |
| **version** | INTEGER | NULLABLE | Protocol version specified in the block which contained this transaction |
| **lock_time** | INTEGER | NULLABLE | Earliest time/block height that miners can include the transaction |
| **block_hash** | STRING | REQUIRED | Hash of the block which contains this transaction |
| **block_number** | INTEGER | REQUIRED | Number of the block which contains this transaction |
| **block_timestamp** | TIMESTAMP | REQUIRED | Timestamp of the block which contains this transaction |
| **block_timestamp_month** | DATE | REQUIRED | Partitioning column; month of the block which contains this transaction |
| **input_count** | INTEGER | NULLABLE | The number of inputs in the transaction |
| **output_count** | INTEGER | NULLABLE | The number of outputs in the transaction |
| **input_value** | NUMERIC | NULLABLE | Total value of inputs in the transaction |
| **output_value** | NUMERIC | NULLABLE | Total value of outputs in the transaction |
| **is_coinbase** | BOOLEAN | NULLABLE | True if this transaction is a coinbase transaction (mined block reward) |
| **fee** | NUMERIC | NULLABLE | The transaction fee paid to miners (input_value - output_value) |
| **inputs** | RECORD | REPEATED | Nested array of transaction inputs |
| *inputs.***index** | INTEGER | REQUIRED | 0-indexed number of an input within a transaction |
| *inputs.***spent_transaction_hash** | STRING | NULLABLE | The hash of the transaction containing the output that this input spends |
| *inputs.***spent_output_index** | INTEGER | NULLABLE | The index of the output this input spends |
| *inputs.***script_asm** | STRING | NULLABLE | Symbolic representation of the script signature |
| *inputs.***script_hex** | STRING | NULLABLE | Hexadecimal representation of the script signature |
| *inputs.***sequence** | INTEGER | NULLABLE | Sequence number for locktime modifications |
| *inputs.***required_signatures** | INTEGER | NULLABLE | The number of signatures required to authorize the spent output |
| *inputs.***type** | STRING | NULLABLE | The address type of the spent output (e.g. pubkeyhash, scripthash) |
| *inputs.***addresses** | STRING | REPEATED | Array of addresses which own the spent output |
| *inputs.***value** | NUMERIC | NULLABLE | The value in base currency (satoshis) attached to the spent output |
| **outputs** | RECORD | REPEATED | Nested array of transaction outputs |
| *outputs.***index** | INTEGER | REQUIRED | 0-indexed number of the output used to reference this specific output later |
| *outputs.***script_asm** | STRING | NULLABLE | Symbolic representation of the script pubkey |
| *outputs.***script_hex** | STRING | NULLABLE | Hexadecimal representation of the script pubkey |
| *outputs.***required_signatures** | INTEGER | NULLABLE | The number of signatures required to authorize spending of this output |
| *outputs.***type** | STRING | NULLABLE | The address type of the output |
| *outputs.***addresses** | STRING | REPEATED | Array of addresses which own this output |
| *outputs.***value** | NUMERIC | NULLABLE | The value in base currency (satoshis) attached to this output |

# Common query patterns

### 1. Calculate average transaction fees and size over a month
The following query aggregates daily transaction volumes, average fees, and average sizes for a specific partitioned month.

```sql
SELECT
  DATE(block_timestamp) AS transaction_date,
  COUNT(1) AS transaction_count,
  AVG(fee) AS avg_fee_satoshis,
  AVG(size) AS avg_size_bytes
FROM
  `bigquery-public-data.crypto_bitcoin.transactions`
WHERE
  block_timestamp_month = '2023-10-01'
GROUP BY
  transaction_date
ORDER BY
  transaction_date;
```

### 2. Identify the highest-value transactions in a given month
This query retrieves the largest transactions by output value, excluding coinbase transactions (block rewards).

```sql
SELECT
  hash,
  block_number,
  block_timestamp,
  output_count,
  output_value
FROM
  `bigquery-public-data.crypto_bitcoin.transactions`
WHERE
  block_timestamp_month = '2023-10-01'
  AND is_coinbase = FALSE
ORDER BY
  output_value DESC
LIMIT 10;
```

### 3. Analyze output types and values (unnesting repeated records)
To analyze the distribution of different Bitcoin address types (such as `scripthash` or `witness_v0_keyhash`), you must unnest the `outputs` repeated record.

```sql
SELECT
  out.type AS address_type,
  COUNT(1) AS output_count,
  SUM(out.value) AS total_value
FROM
  `bigquery-public-data.crypto_bitcoin.transactions`,
  UNNEST(outputs) AS out
WHERE
  block_timestamp_month = '2023-10-01'
GROUP BY
  address_type
ORDER BY
  total_value DESC;
```

# Metrics

- [Duplicate transactions across blocks](../references/metrics/duplicate_transactions.md) — An anomaly detection query to spot old duplicate transaction IDs prior to the BIP-0030 implementation.

# Joins

- [blocks](../references/joins/blocks___transactions.md) — Links block metadata to find which block mined this transaction.
- [inputs](../references/joins/inputs___transactions.md) — Links a transaction to its UTXO spending sources.
- [outputs](../references/joins/outputs___transactions.md) — Links a transaction to its output receipts.

[^bitcoin-etl]: Blockchain ETL on GitHub: https://github.com/blockchain-etl/bitcoin-etl
`````

## File: bundles/crypto_bitcoin/index.md
`````markdown
# Subdirectories

* [datasets](datasets/index.md) - A public Google BigQuery dataset containing the complete transaction ledger and block history of the Bitcoin blockchain.
* [references](references/index.md) - The references directory contains join paths for tracing transaction details and an anomaly detection metric for identifying historical duplicate transactions across blocks.
* [tables](tables/index.md) - This directory contains tables documenting Bitcoin blockchain data, including blocks, transactions, and transaction inputs and outputs.
`````

## File: bundles/ga4/datasets/ga4_obfuscated_sample_ecommerce.md
`````markdown
---
type: BigQuery Dataset
resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/ga4_obfuscated_sample_ecommerce
title: GA4 Obfuscated Sample Ecommerce Dataset
description: Obfuscated Google Analytics 4 dataset emulating a web ecommerce implementation
  of the Google Merchandise Store.
tags:
- ga4
- ecommerce
- obfuscated
- analytics
- sample-data
generated:
  by: reference_agent/gemini-3.5-flash
  at: '2026-07-10T21:14:56+00:00'
sources:
- title: BigQuery Dataset Metadata for ga4_obfuscated_sample_ecommerce
  id: ga4-metadata
  resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/ga4_obfuscated_sample_ecommerce
- resource: https://developers.google.com/analytics/bigquery/web-ecommerce-demo-dataset
  title: Google Analytics 4 eCommerce Demo Dataset Documentation
  id: ga4-demo-docs
---

The `ga4_obfuscated_sample_ecommerce` dataset is an obfuscated, publicly accessible export of Google Analytics 4 (GA4) event data representing a real-world web ecommerce implementation (specifically, from the Google Merchandise Store)[^ga4-demo-docs]. It spans three months of historical activity from November 1, 2020, to January 1, 2021[^ga4-demo-docs], and is designed to allow developers, analysts, and students to experiment with high-volume, granular GA4 event data in BigQuery without provisioning a proprietary dataset.

This dataset contains a single sharded table family, [events_](../tables/events_.md), which holds daily export tables containing individual session interactions, user properties, and ecommerce transaction details. Analysts can leverage this dataset to learn how to query GA4 nested schemas, build user acquisition models, reconstruct user journeys, and analyze purchase funnels.

# Schema

As a BigQuery Dataset, this resource acts as a namespace containing tables and does not have a flat column schema of its own. It hosts the following tables:

*   [events_](../tables/events_.md): A partitioned, sharded table containing daily Google Analytics 4 event export records.

# Common query patterns

### 1. Count total events and distinct users across the entire dataset

This query demonstrates how to query over all sharded tables in the dataset using a wildcard suffix pattern.

```sql
SELECT
  COUNT(*) AS total_events,
  COUNT(DISTINCT user_pseudo_id) AS total_users
FROM
  `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
```

### 2. Locate tables and confirm data availability

This query retrieves metadata about the individual tables contained within the dataset namespace.

```sql
SELECT
  table_id,
  creation_time,
  row_count,
  size_bytes
FROM
  `bigquery-public-data.ga4_obfuscated_sample_ecommerce.__TABLES__`
ORDER BY
  table_id DESC
```

[^ga4-demo-docs]: [Google Analytics 4 eCommerce Demo Dataset documentation](https://developers.google.com/analytics/bigquery/web-ecommerce-demo-dataset)
`````

## File: bundles/ga4/datasets/index.md
`````markdown
# BigQuery Dataset

* [GA4 Obfuscated Sample Ecommerce Dataset](ga4_obfuscated_sample_ecommerce.md) - Obfuscated Google Analytics 4 dataset emulating a web ecommerce implementation of the Google Merchandise Store.
`````

## File: bundles/ga4/references/metrics/acquired_users.md
`````markdown
---
type: Reference
resource: https://support.google.com/analytics/answer/9037342
title: Acquired Users Metric
description: Builds an audience of users acquired via a specific Source, Medium, and
  Campaign name.
tags:
- metric
- audience
- ga4
- acquired-users
generated:
  by: reference_agent/gemini-3.5-flash
  at: '2026-07-10T21:16:35+00:00'
sources:
- title: Sample queries for audiences based on BigQuery data - Analytics Help
  resource: https://support.google.com/analytics/answer/9037342
  id: sample_queries
---

Builds an audience of Acquired Users, defined as users who were acquired via a specific marketing campaign source, medium, and name.

# Schema
This reference describes a query pattern and does not map to a single database schema.

# Common query patterns

```sql
/**
 * Builds an audience of Acquired Users.
 *
 * Acquired Users = users who were acquired via some Source/Medium/Campaign.
 */

SELECT
  COUNT(DISTINCT user_id) AS acquired_users_count
FROM
  `YOUR_TABLE.events_*`
WHERE
  traffic_source.source = 'google'
  AND traffic_source.medium = 'cpc'
  AND traffic_source.name = 'VTA-Test-Android'
  AND _TABLE_SUFFIX BETWEEN '20180521' AND '20240131';
```
[^sample_queries]

[^sample_queries]: [Google Analytics Help: Sample queries for audiences based on BigQuery data](https://support.google.com/analytics/answer/9037342)
`````

## File: bundles/ga4/references/metrics/frequently_active_users.md
`````markdown
---
type: Reference
resource: https://support.google.com/analytics/answer/9037342
title: Frequently Active Users Metric
description: Builds an audience of users active on at least N of the last M days.
tags:
- metric
- audience
- ga4
- frequent-actives
generated:
  by: reference_agent/gemini-3.5-flash
  at: '2026-07-10T21:16:25+00:00'
sources:
- title: Sample queries for audiences based on BigQuery data - Analytics Help
  id: sample_queries
  resource: https://support.google.com/analytics/answer/9037342
---

Builds an audience of Frequently Active Users, defined as users who have logged at least one event with the event parameter `engagement_time_msec > 0` on N of the last M days, where M > N (for example, on at least 4 of the last 10 days).

# Schema
This reference describes a query pattern and does not map to a single database schema.

# Common query patterns

```sql
/**
 * Builds an audience of Frequently Active Users.
 *
 * Frequently Active Users = users who have logged at least one
 * event with event param engagement_time_msec > 0 on N of
 * the last M days where M > N.
 */

SELECT
  COUNT(DISTINCT user_id) AS frequent_active_users_count
FROM
  (
    SELECT
      user_id,
      COUNT(DISTINCT event_date)
    FROM
      `YOUR_TABLE.events_*` AS T
    CROSS JOIN
      T.event_params
    WHERE
      event_params.key = 'engagement_time_msec' AND event_params.value.int_value > 0
      -- User engagement in the last M = 10 days.
      AND event_timestamp >
          UNIX_MICROS(TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 10 DAY))
      AND _TABLE_SUFFIX BETWEEN '20180521' AND '20240131'
    GROUP BY 1
    -- Having engaged in at least N = 4 days.
    HAVING COUNT(event_date) >= 4
  );
```
[^sample_queries]

[^sample_queries]: [Google Analytics Help: Sample queries for audiences based on BigQuery data](https://support.google.com/analytics/answer/9037342)
`````

## File: bundles/ga4/references/metrics/google_acquired_cohorts.md
`````markdown
---
type: Reference
resource: https://support.google.com/analytics/answer/9037342
title: Google Acquired Cohorts Metric
description: Builds an audience of users acquired in a specific time-window cohort
  filtered by Google campaign source.
tags:
- metric
- audience
- ga4
- cohorts
generated:
  by: reference_agent/gemini-3.5-flash
  at: '2026-07-10T21:16:43+00:00'
sources:
- title: Sample queries for audiences based on BigQuery data - Analytics Help
  resource: https://support.google.com/analytics/answer/9037342
  id: sample_queries
---

Builds an audience composed of users acquired last week through Google campaigns (cohorts with specific campaign filters).

# Schema
This reference describes a query pattern and does not map to a single database schema.

# Common query patterns

```sql
/**
 * Builds an audience composed of users acquired last week
 * through Google campaigns, i.e., cohorts with filters.
 *
 * Cohort is defined as users acquired last week, i.e. between 7 - 14
 * days ago. The cohort filter is for users acquired through a direct
 * campaign.
 */

SELECT
  COUNT(DISTINCT user_id) AS users_acquired_through_google_count
FROM
  `YOUR_TABLE.events_*`
WHERE
  event_name = 'first_open'
  -- Cohort: opened app 1-2 weeks ago. One week of cohort, aka. weekly.
  AND event_timestamp >
      UNIX_MICROS(TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 14 DAY))
  AND event_timestamp <
      UNIX_MICROS(TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 7 DAY))
  -- Cohort filter: users acquired through 'google' source.
  AND traffic_source.source = 'google'
  AND _TABLE_SUFFIX BETWEEN '20180501' AND '20240131';
```
[^sample_queries]

[^sample_queries]: [Google Analytics Help: Sample queries for audiences based on BigQuery data](https://support.google.com/analytics/answer/9037342)
`````

## File: bundles/ga4/references/metrics/highly_active_users.md
`````markdown
---
type: Reference
resource: https://support.google.com/analytics/answer/9037342
title: Highly Active Users Metric
description: Builds an audience of users active for more than N minutes in the last
  M days.
tags:
- metric
- audience
- ga4
- high-actives
generated:
  by: reference_agent/gemini-3.5-flash
  at: '2026-07-10T21:16:29+00:00'
sources:
- title: Sample queries for audiences based on BigQuery data - Analytics Help
  resource: https://support.google.com/analytics/answer/9037342
  id: sample_queries
---

Builds an audience of Highly Active Users, defined as users who have been active/engaged for more than N minutes in the last M days, where M > N (for example, more than 0.1 minutes in the last 10 days).

# Schema
This reference describes a query pattern and does not map to a single database schema.

# Common query patterns

```sql
/**
 * Builds an audience of Highly Active Users.
 *
 * Highly Active Users = users who have been active for more than N minutes
 * in the last M days where M > N.
*/

SELECT
  COUNT(DISTINCT user_id) AS high_active_users_count
FROM
  (
    SELECT
      user_id,
      event_params.key,
      SUM(event_params.value.int_value)
    FROM
      `YOUR_TABLE.events_*` AS T
    CROSS JOIN
      T.event_params
    WHERE
      -- User engagement in the last M = 10 days.
      event_timestamp >
          UNIX_MICROS(TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 10 DAY))
      AND event_params.key = 'engagement_time_msec'
      AND _TABLE_SUFFIX BETWEEN '20180521' AND '20240131'
    GROUP BY 1, 2
    HAVING
      -- Having engaged for more than N = 0.1 minutes.
      SUM(event_params.value.int_value) > 0.1 * 60 * 1000000
  );
```
[^sample_queries]

[^sample_queries]: [Google Analytics Help: Sample queries for audiences based on BigQuery data](https://support.google.com/analytics/answer/9037342)
`````

## File: bundles/ga4/references/metrics/index.md
`````markdown
# Reference

* [Acquired Users Metric](acquired_users.md) - Builds an audience of users acquired via a specific Source, Medium, and Campaign name.
* [Frequently Active Users Metric](frequently_active_users.md) - Builds an audience of users active on at least N of the last M days.
* [Google Acquired Cohorts Metric](google_acquired_cohorts.md) - Builds an audience of users acquired in a specific time-window cohort filtered by Google campaign source.
* [Highly Active Users Metric](highly_active_users.md) - Builds an audience of users active for more than N minutes in the last M days.
* [N-Day Active Users Metric](n_day_active_users.md) - Builds an audience of users active in the last N days based on engagement_time_msec.
* [N-Day Inactive Users Metric](n_day_inactive_users.md) - Builds an audience of users active in the last M days who have not been active in the last N days.
* [Purchasers Audience Metric](purchasers.md) - Computes the count or list of users who have completed a purchase or in-app purchase.
`````

## File: bundles/ga4/references/metrics/n_day_active_users.md
`````markdown
---
type: Reference
resource: https://support.google.com/analytics/answer/9037342
title: N-Day Active Users Metric
description: Builds an audience of users active in the last N days based on engagement_time_msec.
tags:
- metric
- audience
- ga4
- active-users
generated:
  by: reference_agent/gemini-3.5-flash
  at: '2026-07-10T21:16:16+00:00'
sources:
- title: Sample queries for audiences based on BigQuery data - Analytics Help
  resource: https://support.google.com/analytics/answer/9037342
  id: sample_queries
---

Builds an audience of N-Day Active Users, defined as users who have logged at least one event with the event parameter `engagement_time_msec > 0` in the last N days.

# Schema
This reference describes a query pattern and does not map to a single database schema.

# Common query patterns

```sql
/**
 * Builds an audience of N-Day Active Users.
 *
 * N-day active users = users who have logged at least one event with event param
 * engagement_time_msec > 0 in the last N days.
*/

SELECT
  COUNT(DISTINCT user_id) AS n_day_active_users_count
FROM
  `YOUR_TABLE.events_*` AS T
    CROSS JOIN
      T.event_params
WHERE
  event_params.key = 'engagement_time_msec' AND event_params.value.int_value > 0
  -- Pick events in the last N = 20 days.
  AND event_timestamp >
      UNIX_MICROS(TIMESTAMP_SUB(CURRENT_TIMESTAMP, INTERVAL 20 DAY))
  AND _TABLE_SUFFIX BETWEEN '20180521' AND '20240131';
```
[^sample_queries]

[^sample_queries]: [Google Analytics Help: Sample queries for audiences based on BigQuery data](https://support.google.com/analytics/answer/9037342)
`````

## File: bundles/ga4/references/metrics/n_day_inactive_users.md
`````markdown
---
type: Reference
resource: https://support.google.com/analytics/answer/9037342
title: N-Day Inactive Users Metric
description: Builds an audience of users active in the last M days who have not been
  active in the last N days.
tags:
- metric
- audience
- ga4
- inactive-users
generated:
  by: reference_agent/gemini-3.5-flash
  at: '2026-07-10T21:16:21+00:00'
sources:
- title: Sample queries for audiences based on BigQuery data - Analytics Help
  id: sample_queries
  resource: https://support.google.com/analytics/answer/9037342
---

Builds an audience of N-Day Inactive Users. Inactive users are defined as those active in the last M days (e.g. 7 days) who have NOT logged any event with event parameter `engagement_time_msec > 0` in the last N days (e.g. 2 days), where M > N.

# Schema
This reference describes a query pattern and does not map to a single database schema.

# Common query patterns

```sql
/**
 * Builds an audience of N-Day Inactive Users.
 *
 * N-Day inactive users = users in the last M days who have not logged one  
 * event with event param engagement_time_msec > 0 in the last N days
 *  where M > N.
 */

SELECT
  COUNT(DISTINCT MDaysUsers.user_id) AS n_day_inactive_users_count
FROM
  (
    SELECT
      user_id
    FROM
      `YOUR_TABLE.events_*` AS T
    CROSS JOIN
      T.event_params
    WHERE
      event_params.key = 'engagement_time_msec' AND event_params.value.int_value > 0
      /* Has engaged in last M = 7 days */
      AND event_timestamp >
          UNIX_MICROS(TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 7 DAY))
      AND _TABLE_SUFFIX BETWEEN '20180521' AND '20240131'
  ) AS MDaysUsers
LEFT JOIN
  (
    SELECT
      user_id
    FROM
      `YOUR_TABLE.events_*` AS T
    CROSS JOIN
      T.event_params
    WHERE
      event_params.key = 'engagement_time_msec' AND event_params.value.int_value > 0
      /* Has engaged in last N = 2 days */
      AND event_timestamp >
          UNIX_MICROS(TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 2 DAY))
      AND _TABLE_SUFFIX BETWEEN '20180521' AND '20240131'
  ) AS NDaysUsers
  ON MDaysUsers.user_id = NDaysUsers.user_id
WHERE
  NDaysUsers.user_id IS NULL;
```
[^sample_queries]

[^sample_queries]: [Google Analytics Help: Sample queries for audiences based on BigQuery data](https://support.google.com/analytics/answer/9037342)
`````

## File: bundles/ga4/references/metrics/purchasers.md
`````markdown
---
type: Reference
resource: https://support.google.com/analytics/answer/9037342
title: Purchasers Audience Metric
description: Computes the count or list of users who have completed a purchase or
  in-app purchase.
tags:
- metric
- audience
- ga4
- purchasers
generated:
  by: reference_agent/gemini-3.5-flash
  at: '2026-07-10T21:16:12+00:00'
sources:
- id: sample_queries
  title: Sample queries for audiences based on BigQuery data - Analytics Help
  resource: https://support.google.com/analytics/answer/9037342
---

Computes the audience of purchasers, defined as users who have logged either `in_app_purchase` or `purchase`.

# Schema
This reference describes a query pattern and does not map to a single database schema.

# Common query patterns

```sql
/**
 * Computes the audience of purchasers.
 *
 * Purchasers = users who have logged either in_app_purchase or
 * purchase.
 */

SELECT
  COUNT(DISTINCT user_id) AS purchasers_count
FROM
  `YOUR_TABLE.events_*`
WHERE
  event_name IN ('in_app_purchase', 'purchase')
  AND _TABLE_SUFFIX BETWEEN '20180501' AND '20240131';
```
[^sample_queries]

[^sample_queries]: [Google Analytics Help: Sample queries for audiences based on BigQuery data](https://support.google.com/analytics/answer/9037342)
`````

## File: bundles/ga4/references/index.md
`````markdown
# Subdirectories

* [metrics](metrics/index.md) - This directory contains sql queries and schemas to define and build various user audience metrics based on acquisition sources, activity levels, and purchasing behavior.
`````

## File: bundles/ga4/tables/events_.md
`````markdown
---
type: BigQuery Table
resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/ga4_obfuscated_sample_ecommerce/tables/events_*
title: GA4 Events Export
description: Google Analytics 4 event-level daily sharded export tables containing
  user interaction logs.
tags:
- analytics
- e-commerce
- ga4
- sharded-tables
generated:
  by: reference_agent/gemini-3.5-flash
  at: '2026-07-10T21:15:20+00:00'
sources:
- title: 'Google Analytics Help: BigQuery Export Schema'
  id: ga4-export-docs
  resource: https://support.google.com/analytics/answer/7029846
- title: BigQuery Table Metadata
  id: metadata
  resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/ga4_obfuscated_sample_ecommerce/tables/events_*
- title: Sample queries for audiences based on BigQuery data - Analytics Help
  resource: https://support.google.com/analytics/answer/9037342
  id: sample_queries
---

The `events_` table family contains obfuscated Google Analytics 4 (GA4) event-level export data from the Google Merchandise Store.[^ga4-export-docs] It is structured as a series of daily sharded tables, starting from `events_20201101` through `events_20210131`.[^metadata] Each row represents a single event (e.g., `page_view`, `scroll`, `session_start`, `view_item`, `purchase`) triggered by a user's interaction with the online storefront.

The data is useful for behavioral analysis, funnel conversion mapping, and e-commerce tracking. Key user attributes such as geographic location, device platform, and acquisition traffic source are nested within top-level records. Additionally, parameters associated with specific events or products are stored in repeated record fields (`event_params` and `items`), requiring flatting or unnesting operations during querying.

# Schema

Below is the flattened schema representation for the sharded daily events table.

| Field Name | Type | Mode | Description |
| :--- | :--- | :--- | :--- |
| **event_date** | STRING | NULLABLE | The date on which the event was logged (formatted as `YYYYMMDD`). |
| **event_timestamp** | INTEGER | NULLABLE | The POSIX timestamp (in microseconds) when the event was registered. |
| **event_name** | STRING | NULLABLE | The name of the event (e.g., `page_view`, `purchase`, `session_start`). |
| **event_params** | RECORD | REPEATED | Key-value parameters associated with the event. |
| *event_params.key* | STRING | NULLABLE | The name of the parameter. |
| *event_params.value* | RECORD | NULLABLE | The value of the parameter, nested by data type. |
| *event_params.value.string_value* | STRING | NULLABLE | Parameter value if it is a string. |
| *event_params.value.int_value* | INTEGER | NULLABLE | Parameter value if it is an integer. |
| *event_params.value.float_value* | FLOAT | NULLABLE | Parameter value if it is a float. |
| *event_params.value.double_value* | FLOAT | NULLABLE | Parameter value if it is a double. |
| **event_previous_timestamp** | INTEGER | NULLABLE | The timestamp of the previous event (in microseconds). |
| **event_value_in_usd** | FLOAT | NULLABLE | The monetary value of the event, converted to USD. |
| **event_bundle_sequence_id** | INTEGER | NULLABLE | The sequence ID of the upload bundle. |
| **event_server_timestamp_offset** | INTEGER | NULLABLE | Difference between server time and device logging time. |
| **user_id** | STRING | NULLABLE | The unique identifier of the user (when signed in). |
| **user_pseudo_id** | STRING | NULLABLE | The pseudonymous consumer device identifier (e.g. GA client ID). |
| **privacy_info** | RECORD | NULLABLE | Consent and privacy settings. |
| *privacy_info.analytics_storage* | INTEGER | NULLABLE | Status of analytics storage consent. |
| *privacy_info.ads_storage* | INTEGER | NULLABLE | Status of ads storage consent. |
| *privacy_info.uses_transient_token* | STRING | NULLABLE | Whether a transient token is used. |
| **user_properties** | RECORD | REPEATED | Custom user properties. |
| *user_properties.key* | INTEGER | NULLABLE | Property name/key. |
| *user_properties.value* | RECORD | NULLABLE | Nested custom value and update timestamp. |
| **user_first_touch_timestamp** | INTEGER | NULLABLE | The time (in microseconds) when the user first interacted with the site. |
| **user_ltv** | RECORD | NULLABLE | User lifetime value details. |
| *user_ltv.revenue* | FLOAT | NULLABLE | Total revenue attributed to the user over time. |
| *user_ltv.currency* | STRING | NULLABLE | The currency of the lifetime revenue value. |
| **device** | RECORD | NULLABLE | Device information of the visitor. |
| *device.category* | STRING | NULLABLE | Device category (e.g., `mobile`, `desktop`, `tablet`). |
| *device.mobile_brand_name* | STRING | NULLABLE | Mobile device brand name (e.g., `Apple`, `Samsung`). |
| *device.mobile_model_name* | STRING | NULLABLE | Mobile model name. |
| *device.mobile_marketing_name* | STRING | NULLABLE | Device marketing name. |
| *device.operating_system* | STRING | NULLABLE | Operating system name (e.g., `iOS`, `Android`, `Web`). |
| *device.operating_system_version* | STRING | NULLABLE | OS version. |
| *device.language* | STRING | NULLABLE | Browser/device language code. |
| *device.web_info.browser* | STRING | NULLABLE | Web browser name. |
| *device.web_info.browser_version* | STRING | NULLABLE | Web browser version. |
| **geo** | RECORD | NULLABLE | Geographical information derived from IP addresses. |
| *geo.continent* | STRING | NULLABLE | Continent name. |
| *geo.sub_continent* | STRING | NULLABLE | Sub-continent name. |
| *geo.country* | STRING | NULLABLE | Country name. |
| *geo.region* | STRING | NULLABLE | Region or state name. |
| *geo.city* | STRING | NULLABLE | City name. |
| *geo.metro* | STRING | NULLABLE | Metro area name. |
| **app_info** | RECORD | NULLABLE | Application specific information. |
| **traffic_source** | RECORD | NULLABLE | User acquisition source. |
| *traffic_source.medium* | STRING | NULLABLE | The medium (e.g., `organic`, `referral`, `cpc`). |
| *traffic_source.name* | STRING | NULLABLE | The campaign name. |
| *traffic_source.source* | STRING | NULLABLE | The source (e.g., `google`, `direct`). |
| **stream_id** | INTEGER | NULLABLE | Data stream ID. |
| **platform** | STRING | NULLABLE | The collection platform (e.g., `WEB`, `IOS`, `ANDROID`). |
| **event_dimensions** | RECORD | NULLABLE | Event-level metadata dimensions. |
| *event_dimensions.hostname* | STRING | NULLABLE | Target hostname where the event occurred. |
| **ecommerce** | RECORD | NULLABLE | Order level transaction details. |
| *ecommerce.total_item_quantity* | INTEGER | NULLABLE | Total items in the transaction. |
| *ecommerce.purchase_revenue_in_usd* | FLOAT | NULLABLE | Revenue of the transaction converted to USD. |
| *ecommerce.transaction_id* | STRING | NULLABLE | Transaction identifier. |
| **items** | RECORD | REPEATED | Product-level attributes for the items involved in the event. |
| *items.item_id* | STRING | NULLABLE | Product ID or SKU. |
| *items.item_name* | STRING | NULLABLE | Name of the product. |
| *items.item_brand* | STRING | NULLABLE | Brand of the product. |
| *items.price_in_usd* | FLOAT | NULLABLE | Unit price in USD. |
| *items.quantity* | INTEGER | NULLABLE | Quantity of items. |

# Common query patterns

### 1. Count events and active users by event name
This query counts the total events logged and counts distinct users (`user_pseudo_id`) for each event type over the full range of tables.

```sql
SELECT
  event_name,
  COUNT(1) AS event_count,
  COUNT(DISTINCT user_pseudo_id) AS unique_users
FROM
  `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20201101' AND '20210131'
GROUP BY
  1
ORDER BY
  event_count DESC;
```

### 2. Extract nested page_location from event_params
Since `event_params` is a repeated record (ARRAY), you must unnest it or filter using a subquery to extract a specific parameter like `page_location` for page views.

```sql
SELECT
  event_date,
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'page_location') AS page_path,
  COUNT(1) AS page_views
FROM
  `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
WHERE
  event_name = 'page_view'
  AND _TABLE_SUFFIX BETWEEN '20210101' AND '20210115'
GROUP BY
  1, 2
ORDER BY
  page_views DESC;
```

### 3. Compute top selling products from items array
To analyze product sales, we unnest the repeated `items` record structure on purchase events and aggregate quantities.

```sql
SELECT
  item.item_id,
  item.item_name,
  SUM(item.quantity) AS units_sold,
  ROUND(SUM(item.item_revenue_in_usd), 2) AS total_revenue_usd
FROM
  `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`,
  UNNEST(items) AS item
WHERE
  event_name = 'purchase'
  AND _TABLE_SUFFIX BETWEEN '20201101' AND '20210131'
GROUP BY
  1, 2
ORDER BY
  total_revenue_usd DESC
LIMIT 10;
```

# Metrics
The following predefined and custom audience cohort metrics can be derived from the events log table:
* [Purchasers](../references/metrics/purchasers.md) — Users who have logged either `in_app_purchase` or `purchase`.
* [N-Day Active Users](../references/metrics/n_day_active_users.md) — Users who have logged at least one event with `engagement_time_msec > 0` in the last N days.
* [N-Day Inactive Users](../references/metrics/n_day_inactive_users.md) — Active users from the last M days who have not logged any event with `engagement_time_msec > 0` in the last N days (M > N).
* [Frequently Active Users](../references/metrics/frequently_active_users.md) — Users who have logged at least one event with `engagement_time_msec > 0` on N of the last M days.
* [Highly Active Users](../references/metrics/highly_active_users.md) — Users who have been active/engaged for more than N minutes in the last M days.
* [Acquired Users](../references/metrics/acquired_users.md) — Users acquired via a specific campaign source, medium, and name.
* [Google Acquired Cohorts](../references/metrics/google_acquired_cohorts.md) — Users acquired in a specific weekly cohort filtered by Google campaign source.

[^ga4-export-docs]: [Google Analytics Help: BigQuery Export Schema](https://support.google.com/analytics/answer/7029846)
[^metadata]: Source dataset `ga4_obfuscated_sample_ecommerce` table list metadata.
`````

## File: bundles/ga4/tables/index.md
`````markdown
# BigQuery Table

* [GA4 Events Export](events_.md) - Google Analytics 4 event-level daily sharded export tables containing user interaction logs.
`````

## File: bundles/ga4/index.md
`````markdown
# Subdirectories

* [datasets](datasets/index.md) - Obfuscated Google Analytics 4 dataset emulating a web ecommerce implementation of the Google Merchandise Store.
* [references](references/index.md) - This directory contains sql queries and schemas to define and build various user audience metrics based on acquisition sources, activity levels, and purchasing behavior.
* [tables](tables/index.md) - Google Analytics 4 event-level daily sharded export tables containing user interaction logs.
`````

## File: bundles/stackoverflow/datasets/index.md
`````markdown
# BigQuery Dataset

* [Stack Overflow Public Dataset](stackoverflow.md) - This dataset contains a public archive of Stack Overflow data, including posts, users, and tags. It was last updated on 2022-11-25 and is no longer actively updated.
`````

## File: bundles/stackoverflow/datasets/stackoverflow.md
`````markdown
---
type: BigQuery Dataset
resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow
title: Stack Overflow Public Dataset
description: This dataset contains a public archive of Stack Overflow data, including
  posts, users, and tags. It was last updated on 2022-11-25 and is no longer actively
  updated.
tags: Stack Overflow, Q&A, developer, programming, public dataset
generated:
  by: reference_agent/gemini-2.5-flash
  at: '2026-07-10T22:46:36+00:00'
sources:
- title: Stack Overflow Public Dataset
  resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow
  id: stackoverflow-dataset-resource
---

The `stackoverflow` dataset, hosted in BigQuery's public data program, provides a comprehensive archive of Stack Overflow's community-generated content. It includes information on questions, answers, comments, users, badges, and tags, offering a rich resource for analyzing developer activity, programming trends, and community dynamics. The data was last updated on 2022-11-25 and is no longer actively updated by its original source. It is located in the `US` multi-region.

# Schema
This dataset contains the following tables:

*   [`badges`](../tables/badges.md): Information about badges awarded to users.
*   [`comments`](../tables/comments.md): User-submitted comments on posts.
*   [`post_history`](../tables/post_history.md): Historical revisions and events for posts.
*   [`post_links`](../tables/post_links.md): Links between posts.
*   [`posts_answers`](../tables/posts_answers.md): Answers to questions.
*   [`posts_moderator_nomination`](../tables/posts_moderator_nomination.md): Posts related to moderator nominations.
*   [`posts_orphaned_tag_wiki`](../tables/posts_orphaned_tag_wiki.md): Orphaned tag wiki posts.
*   [`posts_privilege_wiki`](../tables/posts_privilege_wiki.md): Privilege wiki posts.
*   [`posts_questions`](../tables/posts_questions.md): User-submitted questions.
*   [`posts_tag_wiki`](../tables/posts_tag_wiki.md): Tag wiki entries.
*   [`posts_tag_wiki_excerpt`](../tables/posts_tag_wiki_excerpt.md): Excerpts from tag wiki entries.
*   [`posts_wiki_placeholder`](../tables/posts_wiki_placeholder.md): Placeholder posts for wiki content.
*   [`stackoverflow_posts`](../tables/stackoverflow_posts.md): A consolidated view of all posts (questions and answers).
*   [`tags`](../tables/tags.md): Information about tags used on Stack Overflow.
*   [`users`](../tables/users.md): User profiles and statistics.
*   [`votes`](../tables/votes.md): Records of votes on posts.

# Common query patterns
To explore the tables within this dataset:

```sql
SELECT table_name
FROM `bigquery-public-data.stackoverflow.INFORMATION_SCHEMA.TABLES`
WHERE table_schema = 'stackoverflow';
```

To query the number of questions posted in a specific year:

```sql
SELECT
  EXTRACT(YEAR FROM creation_date) AS year,
  COUNT(*) AS num_questions
FROM `bigquery-public-data.stackoverflow.posts_questions`
GROUP BY 1
ORDER BY 1 DESC
LIMIT 100;
```
`````

## File: bundles/stackoverflow/references/joins/comments__posts.md
`````markdown
---
type: Reference
resource: https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede
title: Comments ↔ Posts Join
description: Join path between the comments and posts tables.
tags:
- join
- comments
- posts
generated:
  by: reference_agent/gemini-3.5-flash
  at: '2026-07-10T23:02:52+00:00'
sources:
- resource: https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede
  id: meta_schema_doc
  title: Database schema documentation for the public data dump and SEDE
---

# comments ↔ posts

Join relationship between the comments and posts (or answers/questions) tables.

```sql
ON comments.post_id = posts.id
```

## Usage

Use this join path to associate comment content and comment scores directly with the parent post, answer, or question. Useful for calculating comment engagement per post or finding comment threads.

[^1]: Verified from [Database Schema Documentation](https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede) on Meta Stack Exchange.
`````

## File: bundles/stackoverflow/references/joins/index.md
`````markdown
# Reference

* [Comments ↔ Posts Join](comments__posts.md) - Join path between the comments and posts tables.
* [Post Links ↔ Posts Join](post_links__posts.md) - Join path between the post_links and posts tables.
* [Posts Answers ↔ Posts Questions Join](posts_answers__posts_questions.md) - Join path between posts_answers and posts_questions tables.
* [Posts ↔ Votes Join](posts__votes.md) - Join path between the votes and posts tables.
`````

## File: bundles/stackoverflow/references/joins/post_links__posts.md
`````markdown
---
type: Reference
resource: https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede
title: Post Links ↔ Posts Join
description: Join path between the post_links and posts tables.
tags:
- join
- posts
- links
generated:
  by: reference_agent/gemini-3.5-flash
  at: '2026-07-10T23:03:01+00:00'
sources:
- title: Database schema documentation for the public data dump and SEDE
  id: meta_schema_doc
  resource: https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede
---

# post_links ↔ posts

Join relationship between the post links table and target/source posts.

```sql
ON post_links.post_id = posts.id
```

## Usage

Use this join path to resolve metadata for the source post (`post_id`) or targets (`related_post_id`) in a link/duplicate relationship.

[^1]: Verified from [Database Schema Documentation](https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede) on Meta Stack Exchange.
`````

## File: bundles/stackoverflow/references/joins/posts__votes.md
`````markdown
---
type: Reference
resource: https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede
title: Posts ↔ Votes Join
description: Join path between the votes and posts tables.
tags:
- join
- posts
- votes
generated:
  by: reference_agent/gemini-3.5-flash
  at: '2026-07-10T23:02:55+00:00'
sources:
- resource: https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede
  id: meta_schema_doc
  title: Database schema documentation for the public data dump and SEDE
---

# posts ↔ votes

Join relationship between the votes table and the posts tables.

```sql
ON votes.post_id = posts.id
```

## Usage

Use this join path to associate individual votes, flags, and favorites with their target posts (questions, answers, or moderator nominations).

[^1]: Verified from [Database Schema Documentation](https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede) on Meta Stack Exchange.
`````

## File: bundles/stackoverflow/references/joins/posts_answers__posts_questions.md
`````markdown
---
type: Reference
resource: https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede
title: Posts Answers ↔ Posts Questions Join
description: Join path between posts_answers and posts_questions tables.
tags:
- join
- posts
- answers
- questions
generated:
  by: reference_agent/gemini-3.5-flash
  at: '2026-07-10T23:03:04+00:00'
sources:
- id: meta_schema_doc
  title: Database schema documentation for the public data dump and SEDE
  resource: https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede
---

# posts_answers ↔ posts_questions

Join relationship between Stack Overflow questions and their answers.

```sql
ON posts_answers.parent_id = posts_questions.id
```

## Usage

Use this join path to correlate answers directly back to their parent questions to aggregate answer counts, verify metrics like Accepted Answer rate, or compare question/answer scores.

[^1]: Verified from [Database Schema Documentation](https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede) on Meta Stack Exchange.
`````

## File: bundles/stackoverflow/references/metrics/accepted_answer_rate.md
`````markdown
---
type: Reference
resource: https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede
title: Accepted Answer Rate
description: The proportion of questions that have an accepted answer.
tags:
- metric
- posts
- community
generated:
  by: reference_agent/gemini-3.5-flash
  at: '2026-07-10T23:02:48+00:00'
sources:
- resource: https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede
  id: meta_schema_doc
  title: Database schema documentation for the public data dump and SEDE
---

# accepted_answer_rate

The accepted answer rate measures the proportion of questions that have a resolved and accepted answer. It is a core community-health KPI indicating question resolution efficiency.

## Formula

```sql
SAFE_DIVIDE(
  COUNT(AcceptedAnswerId),
  COUNT(Id)
)
```

[^1]: Formulas sourced and derived from the `posts_questions` and `stackoverflow_posts` schema documented in [Database Schema Documentation](https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede).
`````

## File: bundles/stackoverflow/references/metrics/bad_question_flag_ratio.md
`````markdown
---
type: Reference
resource: https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede
title: Bad Question Flag Ratio
description: Calculates the ratio of spam and offensive flags (VoteTypeId 4 and 12)
  to overall votes/flags.
tags:
- metric
- votes
- moderation
generated:
  by: reference_agent/gemini-3.5-flash
  at: '2026-07-10T23:02:44+00:00'
sources:
- id: meta_schema_doc
  resource: https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede
  title: Database schema documentation for the public data dump and SEDE
---

# bad_question_flag_ratio

The bad question flag ratio measures the proportion of total flags cast on questions that are categorized as spam or offensive flags. This metric is a useful signal for tracking spam attack waves or highly inappropriate content trends.

## Formula

```sql
SAFE_DIVIDE(
  COUNTIF(VoteTypeId IN (4, 12)),
  COUNT(Id)
)
```

[^1]: Formulas sourced and derived from the `VoteTypeId` categories (4 = Offensive, 12 = Spam) documented in [Database Schema Documentation](https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede).
`````

## File: bundles/stackoverflow/references/metrics/index.md
`````markdown
# Reference

* [Accepted Answer Rate](accepted_answer_rate.md) - The proportion of questions that have an accepted answer.
* [Bad Question Flag Ratio](bad_question_flag_ratio.md) - Calculates the ratio of spam and offensive flags (VoteTypeId 4 and 12) to overall votes/flags.
`````

## File: bundles/stackoverflow/references/content_licenses.md
`````markdown
---
type: Reference
resource: https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede
title: Creative Commons Content Licenses Reference
description: Lookup table defining user-contributed content licensing rules and dates
  on the Stack Exchange network.
tags:
- license
- legal
- meta
generated:
  by: reference_agent/gemini-3.5-flash
  at: '2026-07-10T23:02:40+00:00'
sources:
- resource: https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede
  id: meta_schema_doc
  title: Database schema documentation for the public data dump and SEDE
---

# Creative Commons Content Licenses

Lookup table defining Stack Overflow user content licensing over time based on the `ContentLicense` attribute.

## Content License Lookups

| ContentLicense Value | Date Start | Date End | License Link |
| --- | --- | --- | --- |
| **CC BY-SA 4.0** | 2018-05-02 | *present* | [Creative Commons BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |
| **CC BY-SA 3.0** | 2011-04-08 | 2018-05-01 | [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) |
| **CC BY-SA 2.5** | *inception* | 2011-04-07 | [Creative Commons BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/) |

[^1]: Verified from [Database Schema Documentation](https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede) on Meta Stack Exchange.
`````

## File: bundles/stackoverflow/references/index.md
`````markdown
# Reference

* [Creative Commons Content Licenses Reference](content_licenses.md) - Lookup table defining user-contributed content licensing rules and dates on the Stack Exchange network.
* [Post Types Reference](post_types.md) - Enum lookup values for the PostTypeId column in Stack Overflow posts tables.
* [Vote Types Reference](vote_types.md) - Enum lookup values for the VoteTypeId column in the Stack Overflow votes table.

# Subdirectories

* [joins](joins/index.md) - This directory contains join paths between posts and related tables including comments, post links, votes, and answers and questions.
* [metrics](metrics/index.md) - This directory contains documentation and definitions for the accepted answer rate and bad question flag ratio metrics.
`````

## File: bundles/stackoverflow/references/post_types.md
`````markdown
---
type: Reference
resource: https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede
title: Post Types Reference
description: Enum lookup values for the PostTypeId column in Stack Overflow posts
  tables.
tags:
- lookup
- enum
- posts
generated:
  by: reference_agent/gemini-3.5-flash
  at: '2026-07-10T23:02:30+00:00'
sources:
- resource: https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede
  title: Database schema documentation for the public data dump and SEDE
  id: meta_schema_doc
- id: meta_post_types
  title: Meaning of Values for PostTypeId in data explorer or in data-dump
  resource: https://meta.stackexchange.com/questions/99265/meaning-of-values-for-posttypeid-in-data-explorer-or-in-data-dump
---

# Post Types Reference

A lookup catalog defining the meaning of the `PostTypeId` attribute used in the primary `posts_answers`, `posts_questions`, `posts_moderator_nomination`, `posts_orphaned_tag_wiki`, `posts_privilege_wiki`, `posts_tag_wiki`, `posts_tag_wiki_excerpt`, `posts_wiki_placeholder`, and `stackoverflow_posts` tables.

## Lookup Catalog

| PostTypeId | Name | Description |
|---|---|---|
| 1 | Question | A user-submitted question. |
| 2 | Answer | A user-submitted answer to a question. |
| 3 | Orphaned tag wiki | Tag wikis for tags that have since been deleted. |
| 4 | Tag wiki excerpt | Short intro/excerpt text for a tag. |
| 5 | Tag wiki | Full body text detailing a tag's usage guidelines. |
| 6 | Moderator nomination | Moderator candidate nomination posts. |
| 7 | Wiki placeholder | Auxiliary site content (e.g. Help Center intro, election description, tour intro). |
| 8 | Privilege wiki | Privilege description pages. |
| 9 | Article | Article post type. |
| 10 | HelpArticle | Help Center articles. |
| 12 | Collection | Content collections. |
| 13 | ModeratorQuestionnaireResponse | Candidate answers to moderator questionnaires. |
| 14 | Announcement | Site announcements. |
| 15 | CollectiveDiscussion | Stack Overflow Collectives discussion threads. |
| 17 | CollectiveCollection | Stack Overflow Collectives collections. |

[^1]: Verified from [Database Schema Documentation](https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede) and [PostTypeId Meanings](https://meta.stackexchange.com/questions/99265/meaning-of-values-for-posttypeid-in-data-explorer-or-in-data-dump) on Meta Stack Exchange.
`````

## File: bundles/stackoverflow/references/vote_types.md
`````markdown
---
type: Reference
resource: https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede
title: Vote Types Reference
description: Enum lookup values for the VoteTypeId column in the Stack Overflow votes
  table.
tags:
- lookup
- enum
- votes
generated:
  by: reference_agent/gemini-3.5-flash
  at: '2026-07-10T23:02:36+00:00'
sources:
- id: meta_schema_doc
  resource: https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede
  title: Database schema documentation for the public data dump and SEDE
- title: List of Vote type IDs
  resource: https://meta.stackexchange.com/questions/171176/list-of-vote-type-ids
  id: meta_vote_types
---

# Vote Types Reference

A lookup catalog defining the meaning of the `VoteTypeId` attribute in the `votes` table.

## Lookup Catalog

| VoteTypeId | Name | Description |
|---|---|---|
| -1 | InformModerator | Flag raised to bring a moderator's attention to a post. |
| 0 | UndoMod | Undo a moderation action or vote. |
| 1 | AcceptedByOriginator | Question owner accepted an answer. |
| 2 | UpMod | Question/Answer upvote. |
| 3 | DownMod | Question/Answer downvote. |
| 4 | Offensive | Flagged as offensive or abusive. |
| 5 | Favorite | Bookmark (now deprecated and replaced by Saves). |
| 6 | Close | Vote to close a question. (No longer populated here; close votes reside in PostHistory). |
| 7 | Reopen | Vote to reopen a question. |
| 8 | BountyStart | User started a bounty on a question. |
| 9 | BountyClose | Bounty closed/awarded on a question. |
| 10 | Deletion | Vote to delete a post. |
| 11 | Undeletion | Vote to undelete a post. |
| 12 | Spam | Flagged as spam. |
| 15 | ModeratorReview | A moderator reviewed a flagged post. |
| 16 | ApproveEditSuggestion | Vote to approve a suggested edit. |
| 17-28 | Teams Reactions | Reactions (e.g. celebrate, smile, heart) implemented in Stack Overflow for Teams. |
| 29 | Outdated | Answer flagged as outdated. |
| 30 | NotOutdated | Vote asserting an answer is not outdated. |
| 31 | PreVote | Pre-vote action. |
| 32 | CollectiveDiscussionUpvote | Upvote on a Collectives discussion. |
| 33 | CollectiveDiscussionDownvote | Downvote on a Collectives discussion (deprecated). |
| 35 | privateAiAnswerCorrect | Vote stating AI answer is correct (experiment). |
| 36 | privateAiAnswerIncorrect | Vote stating AI answer is incorrect (experiment). |
| 37 | privateAiAnswerPartiallyCorrect | Vote stating AI answer is partially correct. |

[^1]: Verified from [Database Schema Documentation](https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede) and [List of Vote type IDs](https://meta.stackexchange.com/questions/171176/list-of-vote-type-ids) on Meta Stack Exchange.
`````

## File: bundles/stackoverflow/tables/badges.md
`````markdown
---
type: BigQuery Table
resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/badges
title: Badges
description: This table contains information about badges awarded to users on Stack
  Overflow.
tags:
- stackoverflow
- badges
- gamification
generated:
  by: reference_agent/gemini-2.5-flash
  at: '2026-07-10T22:59:00+00:00'
sources:
- resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/badges
  title: Stack Overflow Badges Table
  id: badges-table
---

The `badges` table tracks all badges awarded to users on the Stack Overflow platform. Each row represents a single badge instance awarded to a specific user at a specific time. The table includes details such as the badge's name, the user who received it, and whether it's a tag-based badge. This data can be used to analyze user engagement, recognize top contributors, and understand the gamification aspects of the platform.

# Schema
- `id`: INTEGER, Unique identifier for the badge award.
- `name`: STRING, Name of the awarded badge (e.g., "Great Answer", "Electorate").
- `date`: TIMESTAMP, The date and time the badge was awarded.
- `user_id`: INTEGER, The ID of the user who received the badge. Links to the [users](../tables/users.md) table.
- `class`: INTEGER, The class or tier of the badge (e.g., 1 for gold, 2 for silver, 3 for bronze).
- `tag_based`: BOOLEAN, Indicates whether the badge is associated with a specific tag.

# Common query patterns
1. **Count the number of badges awarded per user:**
   ```sql
   SELECT
     user_id,
     count(id) AS badge_count
   FROM
     `bigquery-public-data.stackoverflow.badges`
   GROUP BY
     user_id
   ORDER BY
     badge_count DESC
   LIMIT 10;
   ```
2. **Find the most frequently awarded badges:**
   ```sql
   SELECT
     name,
     count(id) AS award_count
   FROM
     `bigquery-public-data.stackoverflow.badges`
   GROUP BY
     name
   ORDER BY
     award_count DESC
   LIMIT 10;
   ```
3. **Get all gold badges awarded to a specific user:**
   ```sql
   SELECT
     t2.display_name,
     t1.name,
     t1.date
   FROM
     `bigquery-public-data.stackoverflow.badges` AS t1
   JOIN
     `bigquery-public-data.stackoverflow.users` AS t2
   ON
     t1.user_id = t2.id
   WHERE
     t1.class = 1 -- Assuming class 1 is Gold
     AND t2.display_name = 'Jon Skeet'
   ORDER BY
     t1.date DESC;
   ```
`````

## File: bundles/stackoverflow/tables/comments.md
`````markdown
---
type: BigQuery Table
resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/comments
title: Comments
description: Contains all comments made on posts within the Stack Overflow dataset.
tags:
- comments
- stackoverflow
- user activity
generated:
  by: reference_agent/gemini-2.5-flash
  at: '2026-07-10T22:47:09+00:00'
sources:
- id: stackoverflow-comments
  resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/comments
  title: Stack Overflow Comments Table
---

The `comments` table within the [Stack Overflow dataset](../datasets/stackoverflow.md) contains a record of all comments posted on questions and answers by users. Each row represents a single comment, providing details such as the comment's text, its creation date, the associated post, and the user who made the comment. This table can be joined with the [posts_questions](posts_questions.md) or [posts_answers](posts_answers.md) tables on `post_id` to retrieve the content being commented on, and with the [users](users.md) table on `user_id` to get more information about the commenter. The data spans from September 2008 onwards.

# Schema

- `id`: Unique identifier for the comment.
- `text`: The content of the comment.
- `creation_date`: Timestamp when the comment was created.
- `post_id`: The ID of the post (question or answer) the comment belongs to.
- `user_id`: The ID of the user who made the comment.
- `user_display_name`: The display name of the user who made the comment (may be NULL if user is anonymous or deleted).
- `score`: The score or upvotes received by the comment.

# Common query patterns

1.  **Retrieve all comments for a specific post:**
    ```sql
    SELECT
      id,
      text,
      creation_date,
      user_display_name,
      score
    FROM
      `bigquery-public-data.stackoverflow.comments`
    WHERE
      post_id = 47885
    ORDER BY
      creation_date DESC
    LIMIT 100;
    ```

2.  **Count comments per user:**
    ```sql
    SELECT
      user_display_name,
      COUNT(id) AS total_comments
    FROM
      `bigquery-public-data.stackoverflow.comments`
    WHERE
      user_display_name IS NOT NULL
    GROUP BY
      user_display_name
    ORDER BY
      total_comments DESC
    LIMIT 10;
    ```

3.  **Find comments on questions containing a specific keyword:**
    ```sql
    SELECT
      c.id,
      c.text AS comment_text,
      q.title AS question_title,
      q.body AS question_body,
      c.creation_date
    FROM
      `bigquery-public-data.stackoverflow.comments` AS c
    JOIN
      `bigquery-public-data.stackoverflow.posts_questions` AS q
    ON
      c.post_id = q.id
    WHERE
      q.title LIKE '%python%'
    ORDER BY
      c.creation_date DESC
    LIMIT 10;
    ```
`````

## File: bundles/stackoverflow/tables/index.md
`````markdown
# BigQuery Table

* [Badges](badges.md) - This table contains information about badges awarded to users on Stack Overflow.
* [Comments](comments.md) - Contains all comments made on posts within the Stack Overflow dataset.
* [Orphaned Tag Wiki Posts](posts_orphaned_tag_wiki.md) - Posts that serve as wiki entries for tags that no longer exist or are orphaned.
* [Post History](post_history.md) - Records the history of all changes and events related to posts on Stack Overflow.
* [Post Links](post_links.md) - Contains information about links between posts on Stack Overflow.
* [Posts Answers](posts_answers.md) - Contains Stack Overflow answers, including their content, scores, and associated metadata.
* [Posts Moderator Nomination](posts_moderator_nomination.md) - Contains posts related to moderator nominations on the Stack Overflow platform.
* [Posts Tag Wiki](posts_tag_wiki.md) - Detailed wiki entries associated with tags used on Stack Overflow, providing comprehensive information beyond the basic tag descriptions.
* [Posts Tag Wiki Excerpt](posts_tag_wiki_excerpt.md) - This table contains excerpt posts from the Stack Overflow tag wikis.
* [Stack Overflow Posts (Deprecated)](stackoverflow_posts.md) - A deprecated table containing Stack Overflow posts. Use the posts_answers or posts_questions tables instead.
* [Stack Overflow Posts Questions](posts_questions.md) - Contains all question posts from Stack Overflow.
* [Stack Overflow Posts Wiki Placeholder](posts_wiki_placeholder.md) - Placeholder table for various Wiki-style posts within the Stack Overflow dataset.
* [Stack Overflow Privilege Wiki Posts](posts_privilege_wiki.md) - Contains information about Stack Overflow's privilege wiki posts, detailing user capabilities and their requirements.
* [Stack Overflow Users](users.md) - Contains information about registered users on the Stack Overflow platform.
* [Stack Overflow Votes](votes.md) - Records all votes cast on Stack Overflow posts.
* [Tags](tags.md) - Contains information about tags used on Stack Overflow, including their names and usage counts.
`````

## File: bundles/stackoverflow/tables/post_history.md
`````markdown
---
type: BigQuery Table
resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/post_history
title: Post History
description: Records the history of all changes and events related to posts on Stack
  Overflow.
tags:
- stackoverflow
- posts
- history
- changes
- events
generated:
  by: reference_agent/gemini-2.5-flash
  at: '2026-07-10T22:47:32+00:00'
sources:
- id: post-history-resource
  resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/post_history
  title: Post History BigQuery Table
---

The `post_history` table in the [stackoverflow](../datasets/stackoverflow.md) dataset records a detailed history of all changes and events associated with posts on Stack Overflow. Each row represents a specific historical event or revision made to a post, including initial creation, edits, rollbacks, and changes in status. This table is crucial for auditing post evolution and understanding how content changes over time. Records date back to October 2016, with a total of over 150 million entries.

# Schema

- `id`: Unique identifier for each post history entry.
- `creation_date`: Timestamp when this history entry was created.
- `post_id`: The ID of the post to which this history entry belongs. This links to the `id` field in the [posts_questions](../tables/posts_questions.md) and [posts_answers](../tables/posts_answers.md) tables.
- `post_history_type_id`: An integer ID representing the type of history event (e.g., initial title, body edit, tag edit). Specific meanings for these IDs are typically found in a separate lookup table.
- `revision_guid`: A unique GUID used to group related history entries that constitute a single revision.
- `user_id`: The ID of the user who performed this action. This links to the `id` field in the [users](../tables/users.md) table.
- `text`: The content associated with this history entry. Its meaning depends on `post_history_type_id` (e.g., new title, new body content, old tags).
- `comment`: An optional comment provided by the user for this change.

# Common query patterns

**Retrieve all history entries for a specific post:**
```sql
SELECT
  id,
  creation_date,
  post_id,
  post_history_type_id,
  revision_guid,
  user_id,
  text,
  comment
FROM
  `bigquery-public-data.stackoverflow.post_history`
WHERE
  post_id = 12345 -- Replace with a specific post ID
ORDER BY
  creation_date DESC;
```

**Find the most recent edits made by a specific user:**
```sql
SELECT
  ph.creation_date,
  ph.post_id,
  ph.text,
  ph.comment,
  pq.title AS post_title
FROM
  `bigquery-public-data.stackoverflow.post_history` AS ph
JOIN
  `bigquery-public-data.stackoverflow.posts_questions` AS pq ON ph.post_id = pq.id
WHERE
  ph.user_id = 67890 -- Replace with an actual user ID
  AND ph.post_history_type_id IN (2, 5) -- Example: assuming 2 and 5 represent body/title edits
ORDER BY
  ph.creation_date DESC
LIMIT 10;
```

**Count distinct types of history events for a given post:**
```sql
SELECT
  post_history_type_id,
  COUNT(*) AS event_count
FROM
  `bigquery-public-data.stackoverflow.post_history`
WHERE
  post_id = 12345 -- Replace with a specific post ID
GROUP BY
  post_history_type_id
ORDER BY
  event_count DESC;
```
`````

## File: bundles/stackoverflow/tables/post_links.md
`````markdown
---
type: BigQuery Table
resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/post_links
title: Post Links
description: Contains information about links between posts on Stack Overflow.
tags:
- stackoverflow
- posts
- links
- cross-references
generated:
  by: reference_agent/gemini-2.5-flash
  at: '2026-07-10T22:47:44+00:00'
sources:
- id: post_links_table
  resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/post_links
---

The `post_links` table stores information about how posts on Stack Overflow are linked to each other. Each row represents a single link between two posts, indicating a relationship such as a duplicate question, a related question, or a wiki link. This table is crucial for understanding the interconnectedness of content within the Stack Overflow platform.

The grain of this table is one row per link between two posts.

# Schema

- `id`: Unique identifier for the post link.
- `creation_date`: The date and time when the link was created.
- `link_type_id`: Identifier for the type of link (e.g., duplicate, related).
- `post_id`: The ID of the primary post in the link. This typically refers to a post in the [posts_questions](posts_questions.md) or [posts_answers](posts_answers.md) tables.
- `related_post_id`: The ID of the related post in the link, also referring to a post in the [posts_questions](posts_questions.md) or [posts_answers](posts_answers.md) tables.

# Common query patterns

```sql
SELECT
  pl.id,
  pl.creation_date,
  pl.link_type_id,
  p1.title AS post_title,
  p2.title AS related_post_title
FROM
  `bigquery-public-data.stackoverflow.post_links` AS pl
JOIN
  `bigquery-public-data.stackoverflow.posts_questions` AS p1
  ON pl.post_id = p1.id
JOIN
  `bigquery-public-data.stackoverflow.posts_questions` AS p2
  ON pl.related_post_id = p2.id
WHERE
  pl.link_type_id = 3 -- Example: LinkType = "Related"
LIMIT 100;
```

```sql
SELECT
  link_type_id,
  COUNT(*)
FROM
  `bigquery-public-data.stackoverflow.post_links`
GROUP BY
  link_type_id
ORDER BY
  COUNT(*) DESC;
```
`````

## File: bundles/stackoverflow/tables/posts_answers.md
`````markdown
---
type: BigQuery Table
resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/posts_answers
title: Posts Answers
description: Contains Stack Overflow answers, including their content, scores, and
  associated metadata.
tags: stackoverflow, answers, posts, Q&A
generated:
  by: reference_agent/gemini-2.5-flash
  at: '2026-07-10T22:48:04+00:00'
sources:
- title: Stack Overflow Posts Answers Table
  id: stackoverflow-posts_answers
  resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/posts_answers
---

The `posts_answers` table in the `bigquery-public-data.stackoverflow` dataset contains all answers submitted by users on the Stack Overflow platform. Each row in this table represents a single answer to a question. Key information includes the answer's `body` (content), `creation_date`, `score`, and `owner_user_id`. Answers are linked to their corresponding questions via the `parent_id` field, which references the `id` from the [posts_questions](posts_questions.md) table. This table is useful for analyzing answer quality, user contributions, and trends in responses over time.

# Schema

- id: INTEGER (Unique ID of the answer)
- title: STRING (Title of the post. Typically NULL for answers, as the title belongs to the question)
- body: STRING (The HTML content of the answer)
- accepted_answer_id: STRING (ID of the accepted answer for the parent question. Typically NULL for answers themselves)
- answer_count: STRING (Number of answers for the parent question. Typically NULL for answers)
- comment_count: INTEGER (Number of comments on this specific answer)
- community_owned_date: TIMESTAMP (Date when the answer became community-owned)
- creation_date: TIMESTAMP (UTC timestamp when the answer was posted)
- favorite_count: STRING (Number of times the parent question was favorited. Typically NULL for answers)
- last_activity_date: TIMESTAMP (UTC timestamp of the last activity on this answer)
- last_edit_date: TIMESTAMP (UTC timestamp of the last edit to this answer)
- last_editor_display_name: STRING (Display name of the user who last edited the answer)
- last_editor_user_id: INTEGER (User ID of the user who last edited the answer)
- owner_display_name: STRING (Display name of the user who posted the answer)
- owner_user_id: INTEGER (User ID of the user who posted the answer)
- parent_id: INTEGER (The ID of the question this answer belongs to. Links to `id` in the [posts_questions](posts_questions.md) table.)
- post_type_id: INTEGER (The type of post; `2` for answers.)
- score: INTEGER (The current score of the answer, based on upvotes and downvotes)
- tags: STRING (Tags associated with the parent question. Typically NULL for answers)
- view_count: STRING (View count of the parent question. Typically NULL for answers)

# Common query patterns

```sql
SELECT
  id,
  body,
  score,
  creation_date
FROM
  `bigquery-public-data.stackoverflow.posts_answers`
ORDER BY
  score DESC
LIMIT 10
```

```sql
SELECT
  owner_user_id,
  count(id) AS answer_count
FROM
  `bigquery-public-data.stackoverflow.posts_answers`
WHERE
  owner_user_id IS NOT NULL
GROUP BY
  owner_user_id
ORDER BY
  answer_count DESC
LIMIT 5
```

```sql
SELECT
  id,
  body,
  score,
  owner_display_name
FROM
  `bigquery-public-data.stackoverflow.posts_answers`
WHERE
  parent_id = 12345
ORDER BY
  score DESC
```
`````

## File: bundles/stackoverflow/tables/posts_moderator_nomination.md
`````markdown
---
type: BigQuery Table
resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/posts_moderator_nomination
title: Posts Moderator Nomination
description: Contains posts related to moderator nominations on the Stack Overflow
  platform.
tags: stackoverflow, posts, moderator, nomination
generated:
  by: reference_agent/gemini-2.5-flash
  at: '2026-07-10T22:48:22+00:00'
sources:
- title: 'BigQuery Table: posts_moderator_nomination'
  id: posts-moderator-nomination-table
  resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/posts_moderator_nomination
---

This table stores posts that represent moderator nominations within the Stack Overflow community. Each row corresponds to a single nomination post, typically detailing why an individual should be considered for a moderator role. These posts are characterized by `post_type_id = 6`. The table includes information such as the post's content (`body`), creation date, and the user who owns the post.

# Schema

- `id` (INTEGER): Unique identifier for the post.
- `title` (STRING): The title of the post.
- `body` (STRING): The main content of the moderator nomination post.
- `accepted_answer_id` (STRING)
- `answer_count` (STRING)
- `comment_count` (INTEGER): The number of comments on the post.
- `community_owned_date` (TIMESTAMP)
- `creation_date` (TIMESTAMP): The date and time the post was created.
- `favorite_count` (STRING)
- `last_activity_date` (TIMESTAMP)
- `last_edit_date` (TIMESTAMP)
- `last_editor_display_name` (STRING)
- `last_editor_user_id` (INTEGER)
- `owner_display_name` (STRING)
- `owner_user_id` (INTEGER): The ID of the user who owns the post.
- `parent_id` (STRING)
- `post_type_id` (INTEGER): Indicates the type of post; `6` for moderator nominations.
- `score` (INTEGER): The score of the post.
- `tags` (STRING): Tags associated with the post.
- `view_count` (STRING)

# Common query patterns

```sql
SELECT
  id,
  creation_date,
  owner_user_id,
  body
FROM
  `bigquery-public-data.stackoverflow.posts_moderator_nomination`
WHERE
  creation_date >= '2020-01-01'
LIMIT 100;
```
`````

## File: bundles/stackoverflow/tables/posts_orphaned_tag_wiki.md
`````markdown
---
type: BigQuery Table
resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/posts_orphaned_tag_wiki
title: Orphaned Tag Wiki Posts
description: Posts that serve as wiki entries for tags that no longer exist or are
  orphaned.
tags:
- stackoverflow
- posts
- wiki
- tags
- orphaned
generated:
  by: reference_agent/gemini-2.5-flash
  at: '2026-07-10T22:48:39+00:00'
sources:
- id: posts-orphaned-tag-wiki-resource
  resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/posts_orphaned_tag_wiki
---

This table contains posts that are considered "tag wiki" entries for tags that have become orphaned or no longer exist on Stack Overflow. These posts typically provide an explanation or definition for a specific tag. The table `posts_orphaned_tag_wiki` is part of the larger [stackoverflow dataset](../datasets/stackoverflow.md).

# Schema
The schema contains fields related to the post itself, such as content, dates, and ownership information.
- `id`: Unique identifier for the post.
- `title`: The title of the post.
- `body`: The main content of the post, often in Markdown format.
- `accepted_answer_id`: (STRING) ID of the accepted answer (if applicable).
- `answer_count`: (STRING) Number of answers for the post.
- `comment_count`: Number of comments on the post.
- `community_owned_date`: Timestamp when the post became community-owned.
- `creation_date`: Timestamp when the post was created.
- `favorite_count`: (STRING) Number of times the post has been favorited.
- `last_activity_date`: Timestamp of the last activity on the post.
- `last_edit_date`: Timestamp of the last edit to the post.
- `last_editor_display_name`: Display name of the last editor.
- `last_editor_user_id`: User ID of the last editor.
- `owner_display_name`: Display name of the post owner.
- `owner_user_id`: User ID of the post owner.
- `parent_id`: (STRING) ID of the parent post (for answers or comments).
- `post_type_id`: Type of post (e.g., 1 for question, 2 for answer, 3 for tag wiki entry).
- `score`: The score of the post.
- `tags`: (STRING) Tags associated with the post (usually NULL for tag wikis themselves, as they describe the tag).
- `view_count`: (STRING) Number of views for the post.

# Common query patterns

```sql
-- Select all orphaned tag wiki posts
SELECT
    id,
    title,
    creation_date
FROM
    `bigquery-public-data.stackoverflow.posts_orphaned_tag_wiki`
LIMIT 100;
```

```sql
-- Find the body content of a specific orphaned tag wiki post
SELECT
    body
FROM
    `bigquery-public-data.stackoverflow.posts_orphaned_tag_wiki`
WHERE
    id = 4164933;
```
`````

## File: bundles/stackoverflow/tables/posts_privilege_wiki.md
`````markdown
---
type: BigQuery Table
resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/posts_privilege_wiki
title: Stack Overflow Privilege Wiki Posts
description: Contains information about Stack Overflow's privilege wiki posts, detailing
  user capabilities and their requirements.
tags:
- stackoverflow
- wiki
- privilege
- posts
generated:
  by: reference_agent/gemini-2.5-flash
  at: '2026-07-10T22:49:00+00:00'
sources:
- resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/posts_privilege_wiki
  id: posts-privilege-wiki-resource
  title: Stack Overflow posts_privilege_wiki Table
---

This table, part of the [Stack Overflow dataset](../datasets/stackoverflow.md), contains specific posts from the Stack Overflow platform that describe various user privileges. These "privilege wiki" posts detail the capabilities users gain at different reputation levels, such as the ability to edit questions and answers or retag questions without peer review. Each entry in this table represents a single privilege explanation, providing a comprehensive description of the privilege and its implications.

The `posts_privilege_wiki` table is characterized by `post_type_id` equal to `8`, indicating its nature as a wiki post specifically for privileges. It allows users to understand the mechanics of reputation and privileges on the platform.

# Schema

- id: INTEGER
- title: STRING
- body: STRING
    The full HTML content of the privilege wiki post, describing the privilege in detail.
- accepted_answer_id: STRING
- answer_count: STRING
- comment_count: INTEGER
- community_owned_date: STRING
- creation_date: TIMESTAMP
    The date and time when the privilege wiki post was originally created.
- favorite_count: STRING
- last_activity_date: TIMESTAMP
- last_edit_date: TIMESTAMP
    The date and time when the privilege wiki post was last edited.
- last_editor_display_name: STRING
- last_editor_user_id: INTEGER
- owner_display_name: STRING
- owner_user_id: INTEGER
    The ID of the user who owns or created the privilege wiki post.
- parent_id: STRING
- post_type_id: INTEGER
    Always `8` for privilege wiki posts.
- score: INTEGER
- tags: STRING
- view_count: STRING

# Common query patterns

```sql
-- Retrieve all privilege wiki posts
SELECT
    id,
    title,
    body,
    creation_date
  FROM
    `bigquery-public-data.stackoverflow.posts_privilege_wiki`
  WHERE
    post_type_id = 8
  LIMIT 100;
```

```sql
-- Find privilege wiki posts mentioning "edit" in their body
SELECT
    id,
    title,
    creation_date
  FROM
    `bigquery-public-data.stackoverflow.posts_privilege_wiki`
  WHERE
    post_type_id = 8 AND CONTAINS_SUBSTR(body, 'edit');
```

```sql
-- Count the number of privilege wiki posts
SELECT
    COUNT(id) AS privilege_wiki_post_count
  FROM
    `bigquery-public-data.stackoverflow.posts_privilege_wiki`
  WHERE
    post_type_id = 8;
```
`````

## File: bundles/stackoverflow/tables/posts_questions.md
`````markdown
---
type: BigQuery Table
resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/posts_questions
title: Stack Overflow Posts Questions
description: Contains all question posts from Stack Overflow.
tags: stackoverflow, posts, questions
generated:
  at: '2026-07-10T22:49:19+00:00'
  by: reference_agent/gemini-2.5-flash
sources:
- id: stackoverflow-posts-questions
  resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/posts_questions
  title: Stack Overflow Posts Questions Table
- id: meta_schema_doc
  resource: https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede
  title: Database schema documentation for the public data dump and SEDE
---

This table contains all question posts from Stack Overflow, including their content, metadata, and various counts related to activity and user engagement. Each row represents a unique question post. This table can be joined with other tables like [posts_answers](posts_answers.md) to link questions to their corresponding answers, or with [users](users.md) to get more information about the question's owner.

For a detailed catalog of the `post_type_id` column values, see the [Post Types Reference](../references/post_types.md). For details on post licensing, see the [Creative Commons Content Licenses Reference](../references/content_licenses.md). [^1]

# Schema

- `id`: INTEGER, Unique identifier for the post.
- `title`: STRING, The title of the question.
- `body`: STRING, The main content of the question.
- `accepted_answer_id`: INTEGER, The ID of the accepted answer, if any.
- `answer_count`: INTEGER, Number of answers for the question.
- `comment_count`: INTEGER, Number of comments on the question.
- `community_owned_date`: TIMESTAMP, Date when the question became community owned.
- `creation_date`: TIMESTAMP, Date and time when the question was created.
- `favorite_count`: INTEGER, Number of times the question has been favorited.
- `last_activity_date`: TIMESTAMP, Date and time of the last activity on the question.
- `last_edit_date`: TIMESTAMP, Date and time of the last edit to the question.
- `last_editor_display_name`: STRING, Display name of the last editor.
- `last_editor_user_id`: INTEGER, User ID of the last editor.
- `owner_display_name`: STRING, Display name of the question's owner.
- `owner_user_id`: INTEGER, User ID of the question's owner (links to [users](users.md)).
- `parent_id`: STRING, Parent ID (not typically used for questions).
- `post_type_id`: INTEGER, Type of post (1 for question). See [Post Types Reference](../references/post_types.md). [^1]
- `score`: INTEGER, The score of the question.
- `tags`: STRING, Tags associated with the question, separated by '|'.
- `view_count`: INTEGER, Number of times the question has been viewed.

# Common query patterns

```sql
SELECT
    id,
    title,
    view_count
FROM
    `bigquery-public-data.stackoverflow.posts_questions`
ORDER BY
    view_count DESC
LIMIT 10;
```

```sql
SELECT
    p.title,
    p.score,
    u.display_name AS owner_name
FROM
    `bigquery-public-data.stackoverflow.posts_questions` AS p
JOIN
    `bigquery-public-data.stackoverflow.users` AS u
ON
    p.owner_user_id = u.id
WHERE
    p.creation_date BETWEEN '2022-01-01' AND '2022-01-31'
ORDER BY
    p.score DESC
LIMIT 5;
```

```sql
SELECT
    EXTRACT(DATE FROM creation_date) AS question_date,
    COUNT(id) AS number_of_questions
FROM
    `bigquery-public-data.stackoverflow.posts_questions`
GROUP BY
    question_date
ORDER BY
    question_date DESC;
```

# Metrics

- [Accepted Answer Rate](../references/metrics/accepted_answer_rate.md) — Calculates the proportion of questions having an accepted answer. [^1]

# Joins

- [posts_answers](../references/joins/posts_answers__posts_questions.md) — join on `id` ↔ `parent_id` to attach answers to questions. [^1]
- [comments](../references/joins/comments__posts.md) — join on `id` ↔ `post_id` to correlate comments with questions. [^1]
- [votes](../references/joins/posts__votes.md) — join on `id` ↔ `post_id` to find votes/flags on questions. [^1]
- [post_links](../references/joins/post_links__posts.md) — join on `id` ↔ `post_id` to discover duplicate and related question links. [^1]

[^1]: Sourced from [Database Schema Documentation](https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede) on Meta Stack Exchange.
`````

## File: bundles/stackoverflow/tables/posts_tag_wiki_excerpt.md
`````markdown
---
type: BigQuery Table
resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/posts_tag_wiki_excerpt
title: Posts Tag Wiki Excerpt
description: This table contains excerpt posts from the Stack Overflow tag wikis.
tags:
- stackoverflow
- tag wiki
- posts
- excerpt
generated:
  by: reference_agent/gemini-2.5-flash
  at: '2026-07-10T22:49:51+00:00'
sources:
- id: posts-tag-wiki-excerpt-resource
  resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/posts_tag_wiki_excerpt
  title: 'BigQuery Table: posts_tag_wiki_excerpt'
---

This table contains excerpt posts from the Stack Overflow tag wikis. Each row represents a summary or excerpt of a tag wiki, providing a brief description of a particular tag. This can be useful for understanding the purpose and context of various tags used on the Stack Overflow platform without needing to read the full tag wiki.

# Schema

- `id`: INTEGER, Unique identifier for the tag wiki excerpt post.
- `title`: STRING, Title of the tag wiki excerpt.
- `body`: STRING, The main content or body of the tag wiki excerpt.
- `accepted_answer_id`: STRING, ID of the accepted answer (if applicable, though unlikely for tag wiki excerpts).
- `answer_count`: STRING, Number of answers (if applicable).
- `comment_count`: INTEGER, Number of comments on the post.
- `community_owned_date`: TIMESTAMP, Date when the post became community-owned.
- `creation_date`: TIMESTAMP, Date when the post was created.
- `favorite_count`: STRING, Number of times the post has been favorited.
- `last_activity_date`: TIMESTAMP, Date of the last activity on the post.
- `last_edit_date`: TIMESTAMP, Date of the last edit to the post.
- `last_editor_display_name`: STRING, Display name of the last editor.
- `last_editor_user_id`: INTEGER, User ID of the last editor.
- `owner_display_name`: STRING, Display name of the post owner.
- `owner_user_id`: INTEGER, User ID of the post owner.
- `parent_id`: STRING, ID of the parent post (if applicable).
- `post_type_id`: INTEGER, Type of the post (e.g., 5 for Tag Wiki Excerpt).
- `score`: INTEGER, Score of the post.
- `tags`: STRING, Tags associated with the post (e.g., `<python><sql>`).
- `view_count`: STRING, Number of times the post has been viewed.

# Common query patterns

```sql
SELECT
    id,
    title,
    body
  FROM
    `bigquery-public-data.stackoverflow.posts_tag_wiki_excerpt`
  WHERE
    creation_date BETWEEN '2020-01-01' AND '2020-12-31'
  LIMIT 100;
```
```sql
SELECT
    t.tag_name,
    p.title AS excerpt_title,
    p.body AS excerpt_body
  FROM
    `bigquery-public-data.stackoverflow.posts_tag_wiki_excerpt` AS p
    JOIN `bigquery-public-data.stackoverflow.tags` AS t ON CONCAT('<', t.tag_name, '>') = p.tags
  WHERE
    t.tag_name = 'python'
  LIMIT 1;
```
`````

## File: bundles/stackoverflow/tables/posts_tag_wiki.md
`````markdown
---
type: BigQuery Table
resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/posts_tag_wiki
title: Posts Tag Wiki
description: Detailed wiki entries associated with tags used on Stack Overflow, providing
  comprehensive information beyond the basic tag descriptions.
tags:
- stackoverflow
- posts
- tags
- wiki
generated:
  by: reference_agent/gemini-2.5-flash
  at: '2026-07-10T22:49:37+00:00'
sources:
- resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/posts_tag_wiki
  title: 'BigQuery Table: posts_tag_wiki'
  id: bq-table
---

The `posts_tag_wiki` table in the [stackoverflow](../datasets/stackoverflow.md) dataset contains comprehensive wiki entries for tags used across the Stack Overflow platform. Unlike the brief descriptions found in the [tags](tags.md) table or the [posts_tag_wiki_excerpt](posts_tag_wiki_excerpt.md), this table provides full-length content for each tag's wiki, often including extensive explanations, usage guidelines, and examples. Each row represents a single tag wiki entry, identified by its unique `id`.

# Schema

- `id`: Unique identifier for the tag wiki entry.
- `title`: The title of the wiki entry (often NULL in this table, implying the tag itself is the title).
- `body`: The main content of the tag wiki, typically in HTML format.
- `accepted_answer_id`: ID of the accepted answer (if applicable).
- `answer_count`: Number of answers.
- `comment_count`: Number of comments.
- `community_owned_date`: Date when the post became community-owned.
- `creation_date`: Timestamp when the tag wiki entry was created.
- `favorite_count`: Number of times the post has been favorited.
- `last_activity_date`: Timestamp of the last activity on the post.
- `last_edit_date`: Timestamp of the last edit.
- `last_editor_display_name`: Display name of the last editor.
- `last_editor_user_id`: User ID of the last editor.
- `owner_display_name`: Display name of the owner.
- `owner_user_id`: User ID of the owner.
- `parent_id`: ID of the parent post (if applicable).
- `post_type_id`: Type of the post (e.g., 5 for Wiki entry).
- `score`: The score of the post.
- `tags`: Tags associated with the entry (often NULL in this table as it *is* a tag wiki).
- `view_count`: Number of views.

# Common query patterns

```sql
SELECT
    id,
    creation_date,
    body
  FROM
    `bigquery-public-data.stackoverflow.posts_tag_wiki`
  WHERE
    id = 5046395;
```

```sql
SELECT
    id,
    creation_date,
    last_edit_date,
    LENGTH(body) AS body_length
  FROM
    `bigquery-public-data.stackoverflow.posts_tag_wiki`
  WHERE
    creation_date > '2020-01-01 00:00:00 UTC'
  ORDER BY
    creation_date DESC
  LIMIT 10;
```

```sql
SELECT
    id,
    SUBSTR(body, 1, 100) AS body_preview
  FROM
    `bigquery-public-data.stackoverflow.posts_tag_wiki`
  WHERE
    LOWER(body) LIKE '%example code%';
```
`````

## File: bundles/stackoverflow/tables/posts_wiki_placeholder.md
`````markdown
---
type: BigQuery Table
resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/posts_wiki_placeholder
title: Stack Overflow Posts Wiki Placeholder
description: Placeholder table for various Wiki-style posts within the Stack Overflow
  dataset.
tags: stackoverflow, posts, wiki, placeholder, community
generated:
  by: reference_agent/gemini-2.5-flash
  at: '2026-07-10T22:59:18+00:00'
sources:
- resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/posts_wiki_placeholder
  title: 'BigQuery Public Data: Stack Overflow posts_wiki_placeholder table'
  id: stackoverflow-table
---

This table, `posts_wiki_placeholder`, serves as a repository for various Wiki-style posts found within the broader [Stack Overflow dataset](../datasets/stackoverflow.md). These posts often contain community-contributed information, guidelines, or meta-discussions rather than direct questions and answers. The content is typically informational, covering topics such as site elections, help center articles, and definitions of what constitutes a valid programming problem. Each row represents a single Wiki post, identified by a unique `id`.

# Schema
The table contains the following fields:

- `id`: Unique identifier for the post.
- `title`: Title of the post.
- `body`: The main content of the Wiki post, often containing rich text and markdown.
- `accepted_answer_id`: (NULLABLE)
- `answer_count`: (NULLABLE)
- `comment_count`: Number of comments on the post.
- `community_owned_date`: (NULLABLE)
- `creation_date`: Timestamp when the post was created.
- `favorite_count`: (NULLABLE)
- `last_activity_date`: Timestamp of the last activity on the post (e.g., edit, comment).
- `last_edit_date`: Timestamp of the last edit to the post.
- `last_editor_display_name`: Display name of the last user who edited the post.
- `last_editor_user_id`: User ID of the last user who edited the post.
- `owner_display_name`: Display name of the post's owner.
- `owner_user_id`: User ID of the post's owner. Often -1 for community-owned posts.
- `parent_id`: (NULLABLE)
- `post_type_id`: Type of the post. For this table, it consistently appears to be `7`, indicating Wiki posts.
- `score`: Score of the post, reflecting community upvotes/downvotes.
- `tags`: (NULLABLE) Tags associated with the post.
- `view_count`: (NULLABLE) Number of times the post has been viewed.

# Common query patterns

To retrieve the body content of a specific Wiki post:
```sql
SELECT
    id,
    title,
    body
  FROM
    `bigquery-public-data.stackoverflow.posts_wiki_placeholder`
  WHERE id = 8041931
```

To find the most recent Wiki posts by creation date:
```sql
SELECT
    id,
    title,
    creation_date
  FROM
    `bigquery-public-data.stackoverflow.posts_wiki_placeholder`
  ORDER BY
    creation_date DESC
  LIMIT 5
```

To count the total number of Wiki posts:
```sql
SELECT
    COUNT(DISTINCT id) AS total_wiki_posts
  FROM
    `bigquery-public-data.stackoverflow.posts_wiki_placeholder`
```
`````

## File: bundles/stackoverflow/tables/stackoverflow_posts.md
`````markdown
---
type: BigQuery Table
resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/stackoverflow_posts
title: Stack Overflow Posts (Deprecated)
description: A deprecated table containing Stack Overflow posts. Use the posts_answers
  or posts_questions tables instead.
tags: stackoverflow, posts, deprecated
status: deprecated
generated:
  by: reference_agent/gemini-2.5-flash
  at: '2026-07-10T22:50:28+00:00'
sources:
- title: Deprecated Stack Overflow Posts Table
  id: stackoverflow-posts-table
  resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/stackoverflow_posts
---

This table, `stackoverflow_posts`, contains a comprehensive collection of posts from Stack Overflow. Each row represents a single post, which can be a question, an answer, or another type of post. Key information includes the post's title, body, creation date, score, and associated tags.

**WARNING:** This table is **deprecated** and should not be used for new development or analysis. For up-to-date and more specialized data, please use the individual post type tables, specifically [posts_questions](posts_questions.md) for questions and [posts_answers](posts_answers.md) for answers.

# Schema
The `stackoverflow_posts` table contains the following fields:

*   `id`: `INTEGER` (REQUIRED) - Unique identifier for the post.
*   `title`: `STRING` - The title of the post (e.g., for questions).
*   `body`: `STRING` - The main content of the post.
*   `accepted_answer_id`: `INTEGER` - The ID of the accepted answer, if applicable.
*   `answer_count`: `INTEGER` - Number of answers to a question.
*   `comment_count`: `INTEGER` - Number of comments on the post.
*   `community_owned_date`: `TIMESTAMP` - Date when the post became community owned.
*   `creation_date`: `TIMESTAMP` - Date and time the post was created.
*   `favorite_count`: `INTEGER` - Number of times the post has been favorited.
*   `last_activity_date`: `TIMESTAMP` - Last date of activity on the post.
*   `last_edit_date`: `TIMESTAMP` - Last date the post was edited.
*   `last_editor_display_name`: `STRING` - Display name of the last editor.
*   `last_editor_user_id`: `INTEGER` - User ID of the last editor.
*   `owner_display_name`: `STRING` - Display name of the post owner.
*   `owner_user_id`: `INTEGER` - User ID of the post owner.
*   `parent_id`: `INTEGER` - For answers, the ID of the question it answers.
*   `post_type_id`: `INTEGER` - Type of the post (e.g., 1 for Question, 2 for Answer).
*   `score`: `INTEGER` - The current score of the post.
*   `tags`: `STRING` - Tags associated with the post, typically for questions (e.g., `<python><django>`).
*   `view_count`: `INTEGER` - Number of times the post has been viewed.

# Common query patterns

```sql
-- DANGER: This table is deprecated. Do not use for new queries.
-- Example of selecting basic post information (for historical context only).
SELECT
    id,
    title,
    creation_date,
    score,
    tags
FROM
    `bigquery-public-data.stackoverflow.stackoverflow_posts`
WHERE
    creation_date BETWEEN '2016-01-01' AND '2016-01-31'
LIMIT 100;
```
`````

## File: bundles/stackoverflow/tables/tags.md
`````markdown
---
type: BigQuery Table
resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/tags
title: Tags
description: Contains information about tags used on Stack Overflow, including their
  names and usage counts.
tags:
- stackoverflow
- tags
- metadata
generated:
  by: reference_agent/gemini-2.5-flash
  at: '2026-07-10T22:50:47+00:00'
sources:
- resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/tags
  title: Stack Overflow Tags BigQuery Table
  id: stackoverflow-tags-table
- id: stackoverflow-website
  resource: https://stackoverflow.com/
  title: Stack Overflow Website
---

The `tags` table in the [stackoverflow](../datasets/stackoverflow.md) dataset provides a comprehensive list of all tags used across Stack Overflow, along with their associated metadata. Each row represents a unique tag, detailing its identifier, name, the number of times it has been used, and references to its excerpt and wiki posts. This table is essential for understanding the categorization of questions and answers within the Stack Overflow community.

# Schema

- `id`: Unique identifier for the tag. (INTEGER)
- `tag_name`: The name of the tag (e.g., 'python', 'java', 'c#'). (STRING)
- `count`: The total number of times this tag has been used. (INTEGER)
- `excerpt_post_id`: The ID of the post containing the tag's excerpt description. This can be joined with [posts_tag_wiki_excerpt](posts_tag_wiki_excerpt.md) or [posts_tag_wiki](posts_tag_wiki.md) tables. (INTEGER)
- `wiki_post_id`: The ID of the post containing the tag's full wiki description. This can be joined with [posts_tag_wiki](posts_tag_wiki.md) table. (INTEGER)

# Common query patterns

```sql
-- Retrieve the top 10 most used tags
SELECT
    tag_name,
    count
  FROM
    `bigquery-public-data.stackoverflow.tags`
  ORDER BY
    count DESC
  LIMIT 10;
```

```sql
-- Find details for a specific tag
SELECT
    id,
    tag_name,
    count,
    excerpt_post_id,
    wiki_post_id
  FROM
    `bigquery-public-data.stackoverflow.tags`
  WHERE
    tag_name = 'python';
```

```sql
-- Count total unique tags
SELECT
    COUNT(DISTINCT tag_name) AS total_unique_tags
  FROM
    `bigquery-public-data.stackoverflow.tags`;
```
`````

## File: bundles/stackoverflow/tables/users.md
`````markdown
---
type: BigQuery Table
resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/users
title: Stack Overflow Users
description: Contains information about registered users on the Stack Overflow platform.
tags: stackoverflow, users, community, reputation
generated:
  by: reference_agent/gemini-2.5-flash
  at: '2026-07-10T22:51:02+00:00'
sources:
- resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/users
  title: 'BigQuery Table: users'
  id: bq-table-users
---

The `users` table in the [stackoverflow](../datasets/stackoverflow.md) dataset provides a comprehensive profile for each registered user on the Stack Overflow platform. Each row in this table represents a unique user, capturing details such as their display name, reputation score, activity dates, and biographical information. This table is essential for analyzing user behavior, community engagement, and overall platform dynamics.

# Schema

- `id`: Unique identifier for the user.
- `display_name`: The public display name chosen by the user.
- `about_me`: A short biography provided by the user.
- `age`: User's age (as a string, if provided).
- `creation_date`: Timestamp when the user account was created.
- `last_access_date`: Timestamp of the user's last activity or login.
- `location`: The geographical location provided by the user.
- `reputation`: The user's reputation score.
- `up_votes`: Total number of upvotes received by the user.
- `down_votes`: Total number of downvotes received by the user.
- `views`: Number of times the user's profile has been viewed.
- `profile_image_url`: URL to the user's profile picture.
- `website_url`: URL to the user's personal website.

# Common query patterns

```sql
-- Get the top 10 users by reputation
SELECT
    display_name,
    reputation,
    location
FROM
    `bigquery-public-data.stackoverflow.users`
ORDER BY
    reputation DESC
LIMIT 10;
```

```sql
-- Find users who joined in 2020 and have a high number of upvotes
SELECT
    id,
    display_name,
    creation_date,
    up_votes
FROM
    `bigquery-public-data.stackoverflow.users`
WHERE
    EXTRACT(YEAR FROM creation_date) = 2020
    AND up_votes > 1000
ORDER BY
    up_votes DESC
LIMIT 5;
```

```sql
-- Count users by location (top 5 locations)
SELECT
    location,
    COUNT(id) AS user_count
FROM
    `bigquery-public-data.stackoverflow.users`
WHERE
    location IS NOT NULL AND location != ''
GROUP BY
    location
ORDER BY
    user_count DESC
LIMIT 5;
```
`````

## File: bundles/stackoverflow/tables/votes.md
`````markdown
---
type: BigQuery Table
resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/votes
title: Stack Overflow Votes
description: Records all votes cast on Stack Overflow posts.
tags: Stack Overflow, votes, posts, community
generated:
  by: reference_agent/gemini-2.5-flash
  at: '2026-07-10T22:51:18+00:00'
sources:
- resource: https://bigquery.googleapis.com/v2/projects/bigquery-public-data/datasets/stackoverflow/tables/votes
  title: 'BigQuery Table: votes'
  id: bq-table
- title: Database schema documentation for the public data dump and SEDE
  resource: https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede
  id: meta_schema_doc
---

This table contains all individual votes cast on posts within the Stack Overflow community. Each row represents a single vote, linking it to the specific post and capturing the type of vote and when it occurred. The `vote_type_id` column can be joined with a dimension table to decode the meaning of the vote (e.g., upvote, downvote, favorite).

For a detailed catalog of the `vote_type_id` column values, see the [Vote Types Reference](../references/vote_types.md). [^1]

# Schema

*   `id`: Unique identifier for the vote.
*   `creation_date`: The date and time when the vote was cast. (Note: Time information is truncated to `00:00:00` for privacy). [^1]
*   `post_id`: The identifier of the post that received the vote. This can be joined with the `id` column in tables such as [posts_questions](posts_questions.md) or [posts_answers](posts_answers.md) to get details about the voted post.
*   `vote_type_id`: The type of vote cast (e.g., upvote, downvote, favorite). See [Vote Types Reference](../references/vote_types.md). [^1]

# Common query patterns

To count the total number of upvotes for a specific post:
```sql
SELECT
    count(*) AS upvotes
  FROM
    `bigquery-public-data.stackoverflow.votes`
  WHERE
    post_id = 12345 -- Replace with an actual post ID
    AND vote_type_id = 2 -- Assuming '2' represents an upvote
```

To find the top 10 most voted posts by total votes:
```sql
SELECT
    post_id,
    count(*) AS total_votes
  FROM
    `bigquery-public-data.stackoverflow.votes`
  GROUP BY
    post_id
  ORDER BY
    total_votes DESC
  LIMIT 10
```

To see the distribution of vote types:
```sql
SELECT
    vote_type_id,
    count(*) AS vote_count
  FROM
    `bigquery-public-data.stackoverflow.votes`
  GROUP BY
    vote_type_id
  ORDER BY
    vote_count DESC
```

# Metrics

- [Bad Question Flag Ratio](../references/metrics/bad_question_flag_ratio.md) — Calculates the ratio of spam and offensive flags on questions. [^1]

# Joins

- [posts](../references/joins/posts__votes.md) — join on `post_id` ↔ `id` to associate vote actions with questions, answers, and other post types. [^1]

[^1]: Sourced from [Database Schema Documentation](https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede) on Meta Stack Exchange.
`````

## File: bundles/stackoverflow/index.md
`````markdown
# Subdirectories

* [datasets](datasets/index.md) - This dataset contains a public archive of Stack Overflow data, including posts, users, and tags. It was last updated on 2022-11-25 and is no longer actively updated.
* [references](references/index.md) - This directory contains documentation, join paths, and enum lookup tables referencing licenses, post types, vote types, and metrics for Stack Overflow data.
* [tables](tables/index.md) - This directory contains tables storing Stack Overflow data, including posts, users, tags, comments, votes, badges, and post history.
`````

## File: connectors/gcp-knowledge-catalog.md
`````markdown
# Publishing an OKF bundle to Google Cloud Knowledge Catalog

Push an OKF bundle into a [Knowledge Catalog][kc] EntryGroup and pull it back as
clean OKF, using **`kcmd`** from [`toolbox/mdcode`][mdcode].

Read [Limitations](#limitations) first.

[kc]: https://docs.cloud.google.com/dataplex/docs/catalog-overview
[mdcode]: https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/toolbox/mdcode
[demo]: https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/toolbox/mdcode/demo/okf

## Prerequisites

A GCP project with the Dataplex API enabled, `gcloud`, and [Bun](https://bun.sh).

```bash
gcloud auth application-default login
gcloud config set project <your-project-id>
gcloud config set compute/region us-central1
```

Set both. `kcmd` reads project and location from `gcloud config`; there is no
flag and no environment variable.

Build the CLI:

```bash
git clone https://github.com/GoogleCloudPlatform/knowledge-catalog
cd knowledge-catalog/toolbox/mdcode
npm install && npm run build      # produces dist/kcmd
```

## 1. Run the demo

Confirms the environment before you change anything.

```bash
cd demo/okf
bun setup.ts && bun push.ts && bun pull.ts
git diff --exit-code catalog/     # should be empty
bun cleanup.ts
```

## 2. Copy the connector

Copy everything in [`demo/okf`][demo] except `catalog/` into your own directory,
then edit:

- `entryGroup` in `setup.ts` and `cleanup.ts` — hardcoded to `okf_ga4`.
- `path.resolve(root, '../../dist/kcmd')` in `push.ts` and `pull.ts`, if your
  directory is not two levels below `toolbox/mdcode`. Those two also
  `import * as kcmd from 'kcmd'`, so keep that module resolvable.

Add `.staging/` and `catalog.yaml` to `.gitignore`.

## 3. Set up the catalog side

Creates the EntryGroup, the custom `okf` aspect type, and `catalog.yaml`.
Re-running is safe.

```bash
bun setup.ts
```

## 4. Add your bundle

```bash
cp -R /path/to/bundle/. catalog/
```

## 5. Push

```bash
bun push.ts
```

## 6. Verify the round-trip

```bash
bun pull.ts
git diff catalog/                 # first pull: YAML normalization
git add catalog/ && bun pull.ts
git diff --exit-code catalog/     # now clean
```

The first pull rewrites every frontmatter block into `kcmd`'s YAML style —
sequences indented, timestamps unquoted, mapping keys reordered, lines
rewrapped at a different width. No values change. Commit that normalization
once and later pulls are byte-identical, which is what makes `--exit-code`
worth running. The demo skips this only because its `catalog/` was generated
by a pull already.

Two content diffs are also expected and are not translation loss:

- Directories without an `index.md` gain one — `kcmd` synthesizes an `index`
  entry for every directory.
- A document with `resource:` and no `title:` comes back with `title:` set to
  the resource URI.

Any other diff is a key the translation doesn't carry. See
[Limitations](#limitations).

## 7. Clean up

Deletes the EntryGroup. The `okf` aspect type is left in place — it is scoped
to the project, not to your EntryGroup, so every OKF bundle in the project
shares one. `cleanup.ts` prints the command to remove it once nothing else
needs it.

```bash
bun cleanup.ts
```

## Limitations

- **Seven frontmatter keys are carried**, plus the markdown body. `title`,
  `description` and `tags` become native entry fields, `resource` becomes
  `catalogEntry.resource.name`, and `type`, `generated` and `sources` go on the
  `okf` aspect. To carry more, add fields to `okf-aspect.json` and `okf.ts`,
  keeping existing `index` values stable.
- **Only `.md` files are carried.** Anything else in the bundle — images, HTML,
  CSV — is ignored in both directions: never pushed, and left alone on pull.
- **Cross-links resolve to nothing.** Relative paths (§6.1) are stored verbatim.
  Don't rewrite them in your source — the relative form is what renders on
  GitHub.
- **Tags become entry labels set to `"true"`**, and only labels with that exact
  value are read back as tags. Dataplex caps label keys at 128 characters.
- **Renames orphan catalog state, deletes leave entries behind**, and there is
  no merge story. Treat git as authoritative: push on merge, don't pull into a
  tracked bundle.
- **No entry-level access control.** Anyone with a basic role on the project can
  read and bulk-export the EntryGroup — `roles/viewer` is a strict superset of
  `roles/dataplex.catalogViewer` and adds `entryGroups.export`. Not public by
  default, but check what your bundle discloses before pushing.
- **Scale is untested** beyond the 14-file demo. Push is per-file, and Dataplex
  enforces quotas.
`````

## File: samples/crypto_bitcoin/README.md
`````markdown
# Bitcoin public dataset sample

Runs the reference agent against the public
`bigquery-public-data.crypto_bitcoin` dataset (blocks, transactions,
inputs, outputs — produced by the open-source `bitcoin-etl` pipeline)
and seeds the web pass with the canonical schema source and the
foundational Google Cloud blockchain-on-BigQuery announcement.

This sample contrasts with GA4 (single denormalized events table) and
Stack Overflow (many independent entities) by exercising a **small set
of tightly related fact tables** where each row in `transactions`
references rows in `blocks`, `inputs`, and `outputs`. Good for seeing
how the agent surfaces cross-table foreign-key relationships in prose.

## Prerequisites

- Install the agent (from the repo root):
  ```
  python3.13 -m venv .venv
  .venv/bin/pip install --index-url https://pypi.org/simple/ -e .[dev]
  ```
- BigQuery access:
  ```
  gcloud auth application-default login
  gcloud config set project <your-billing-project>
  ```
  Public datasets are readable, but the caller's project is billed for
  query bytes. The `crypto_bitcoin` tables are very large
  (`transactions` is ~hundreds of GB) — keep `--web-max-pages` modest
  while iterating and prefer `--concept` for smoke runs.
- Gemini credentials — either `GEMINI_API_KEY` (AI Studio) **or** Vertex
  AI (`GOOGLE_GENAI_USE_VERTEXAI=true`, `GOOGLE_CLOUD_PROJECT=<id>`,
  `GOOGLE_CLOUD_LOCATION=<region>`).

## Run

```
.venv/bin/python -m reference_agent enrich \
    --source bq \
    --dataset bigquery-public-data.crypto_bitcoin \
    --web-seed-file samples/crypto_bitcoin/seeds.txt \
    --out ./bundles/crypto_bitcoin
```

To iterate on a single concept, add `--concept tables/transactions`.
To skip the web pass, add `--no-web`. To raise or lower the web budget,
use `--web-max-pages N` (default 100).

## What you get

A bundle under `./bundles/crypto_bitcoin/` with one OKF doc per BQ
concept (dataset + each table), augmented and cross-linked with
reference docs minted from the seeded blockchain-etl and Google Cloud
pages, plus an auto-generated `index.md` at each directory level.
`````

## File: samples/crypto_bitcoin/seeds.txt
`````
# Seed URLs for the Bitcoin public BigQuery dataset
# (bigquery-public-data.crypto_bitcoin).
#
# The BQ dataset is produced by the open-source bitcoin-etl pipeline and
# mirrors its schema (blocks, transactions, inputs, outputs).
#
# Each non-comment line is one URL. The web-ingestion agent crawls outward
# from these by following links it judges relevant; same-domain by default.

# Canonical schema source — the bitcoin-etl repo's README documents the
# blocks / transactions / transaction_input / transaction_output schemas
# that map directly onto the crypto_bitcoin tables.
https://github.com/blockchain-etl/bitcoin-etl

# Foundational Google Cloud blog post on blockchain analytics in BigQuery.
# Note: it predates the crypto_bitcoin dataset name and references the
# older bitcoin_blockchain dataset, but provides authoritative context
# and links to newer material.
https://cloud.google.com/blog/products/gcp/bitcoin-in-bigquery-blockchain-analytics-on-public-data
`````

## File: samples/ga4_merch_store/README.md
`````markdown
# GA4 Google Merchandise Store sample

Runs the reference agent against the public
`bigquery-public-data.ga4_obfuscated_sample_ecommerce` dataset (a GA4 export
from the Google Merchandise Store) and seeds the web pass with canonical GA4
BigQuery Export documentation URLs.

## Prerequisites

- Install the agent (from the repo root):
  ```
  python3.13 -m venv .venv
  .venv/bin/pip install --index-url https://pypi.org/simple/ -e .[dev]
  ```
- BigQuery access:
  ```
  gcloud auth application-default login
  gcloud config set project <your-billing-project>
  ```
  Public datasets are readable, but the caller's project is billed for
  query bytes.
- Gemini credentials — either `GEMINI_API_KEY` (AI Studio) **or** Vertex
  AI (`GOOGLE_GENAI_USE_VERTEXAI=true`, `GOOGLE_CLOUD_PROJECT=<id>`,
  `GOOGLE_CLOUD_LOCATION=<region>`).

## Run

```
.venv/bin/python -m reference_agent enrich \
    --source bq \
    --dataset bigquery-public-data.ga4_obfuscated_sample_ecommerce \
    --web-seed-file samples/ga4_merch_store/seeds.txt \
    --out ./bundles/ga4
```

To iterate on a single concept, add `--concept tables/events_`. To skip
the web pass, add `--no-web`. To raise or lower the web budget, use
`--web-max-pages N` (default 100).

## What you get

A bundle under `./bundles/ga4/` with one OKF doc per BQ
concept (dataset + tables), optionally augmented and cross-linked with
reference docs minted from the seeded GA4 documentation pages, plus an
auto-generated `index.md` at each directory level.
`````

## File: samples/ga4_merch_store/seeds.txt
`````
# Seed URLs for the GA4 Google Merchandise Store anchor dataset
# (bigquery-public-data.ga4_obfuscated_sample_ecommerce).
#
# Each non-comment line is one URL. The web-ingestion agent crawls outward
# from these by following links it judges relevant; same-domain by default.

# GA4 BigQuery Export — schema reference (events, items, params, user)
https://support.google.com/analytics/answer/7029846

# GA4 BigQuery Export — sample / cookbook queries (audiences, metrics)
https://support.google.com/analytics/answer/9037342
`````

## File: samples/stackoverflow/README.md
`````markdown
# Stack Overflow public dataset sample

Runs the reference agent against the public
`bigquery-public-data.stackoverflow` dataset (a mirror of the Stack
Exchange Data Dump for Stack Overflow — `posts_questions`,
`posts_answers`, `users`, `votes`, `comments`, `badges`, `tags`,
`post_history`, `post_links`, ...) and seeds the web pass with the
canonical schema references maintained by the Stack Exchange community.

This sample contrasts with the GA4 sample by exercising **multi-concept
enrichment**: a single schema-docs page typically describes several tables
(`posts_questions` + `posts_answers` + `users`), so the web agent often
updates more than one concept per fetched page.

## Prerequisites

- Install the agent (from the repo root):
  ```
  python3.13 -m venv .venv
  .venv/bin/pip install --index-url https://pypi.org/simple/ -e .[dev]
  ```
- BigQuery access:
  ```
  gcloud auth application-default login
  gcloud config set project <your-billing-project>
  ```
  Public datasets are readable, but the caller's project is billed for
  query bytes. The `stackoverflow` tables are large — keep
  `--web-max-pages` modest while iterating.
- Gemini credentials — either `GEMINI_API_KEY` (AI Studio) **or** Vertex
  AI (`GOOGLE_GENAI_USE_VERTEXAI=true`, `GOOGLE_CLOUD_PROJECT=<id>`,
  `GOOGLE_CLOUD_LOCATION=<region>`).

## Run

```
.venv/bin/python -m reference_agent enrich \
    --source bq \
    --dataset bigquery-public-data.stackoverflow \
    --web-seed-file samples/stackoverflow/seeds.txt \
    --out ./bundles/stackoverflow
```

To iterate on a single concept, add `--concept tables/posts_questions`.
To skip the web pass, add `--no-web`. To raise or lower the web budget,
use `--web-max-pages N` (default 100).

## What you get

A bundle under `./bundles/stackoverflow/` with one OKF doc per BQ concept
(dataset + each table), augmented and cross-linked with reference docs
minted from the seeded Stack Exchange schema pages, plus an
auto-generated `index.md` at each directory level.
`````

## File: samples/stackoverflow/seeds.txt
`````
# Seed URLs for the Stack Overflow public BigQuery dataset
# (bigquery-public-data.stackoverflow).
#
# The BQ dataset mirrors the Stack Exchange Data Dump schema (Posts, Users,
# Votes, Comments, Badges, Tags, PostHistory, PostLinks, ...). These seeds
# point at the canonical schema references the community maintains.
#
# Each non-comment line is one URL. The web-ingestion agent crawls outward
# from these by following links it judges relevant; same-domain by default.

# Canonical schema documentation for the Stack Exchange Data Dump / SEDE
# (covers Posts, Users, Votes, Comments, Badges, Tags, etc.)
https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede

# Stack Exchange Data Explorer help — table descriptions and example queries
https://data.stackexchange.com/help

# Internet Archive page for the Stack Exchange data dump (upstream source
# of the BigQuery export; includes README with field semantics)
https://archive.org/details/stackexchange
`````

## File: src/reference_agent/bundle/__init__.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
⋮----
__all__ = [
`````

## File: src/reference_agent/bundle/document.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
⋮----
# OKF v0.2 §11: `type` is the only always-required frontmatter key.
REQUIRED_FRONTMATTER_KEYS = ("type",)
⋮----
_FRONTMATTER_DELIM = "---"
⋮----
class _Loader(yaml.SafeLoader)
⋮----
"""SafeLoader that leaves timestamps as the text the author wrote.

    PyYAML implements YAML 1.1, whose implicit resolvers turn a value like
    `2026-06-30T14:00:00Z` into a `datetime`. Dumping it back yields
    `2026-06-30 14:00:00+00:00`, so a parse/serialize round-trip silently
    rewrites the author's frontmatter. Dropping the resolver keeps every
    value a string, matching the YAML 1.2 core schema.
    """
⋮----
class OKFDocumentError(ValueError)
⋮----
@dataclass
class OKFDocument
⋮----
frontmatter: dict[str, Any] = field(default_factory=dict)
body: str = ""
⋮----
@classmethod
    def parse(cls, text: str) -> "OKFDocument"
⋮----
lines = text.splitlines()
⋮----
end_idx = None
⋮----
end_idx = i
⋮----
fm_text = "\n".join(lines[1:end_idx])
⋮----
fm = yaml.load(fm_text, Loader=_Loader) or {}
⋮----
body = "\n".join(lines[end_idx + 1:])
⋮----
body = body[1:]
⋮----
def serialize(self) -> str
⋮----
fm_text = yaml.safe_dump(
body = self.body if self.body.endswith("\n") else self.body + "\n"
⋮----
def validate(self) -> None
⋮----
missing = [k for k in REQUIRED_FRONTMATTER_KEYS if not self.frontmatter.get(k)]
⋮----
def normalize_verified(frontmatter: dict[str, Any]) -> list[dict[str, Any]]
⋮----
"""Return the `verified` events as a list (OKF v0.2 §5.2).

    A single verifier MAY be written as one `{ by, at }` mapping without the
    list dash; consumers MUST treat a bare mapping as a one-element list.
    """
verified = frontmatter.get("verified")
⋮----
def trust_tier(frontmatter: dict[str, Any]) -> str
⋮----
"""Derive a concept's trust tier from `verified` (OKF v0.2 §5.3).

    - No `verified` key ⇒ "unverified".
    - `verified` by non-`human:` actors only ⇒ "machine-confirmed".
    - `verified` by a `human:<id>` actor ⇒ "human-reviewed".
    """
events = normalize_verified(frontmatter)
⋮----
by = str(event.get("by") or "")
⋮----
def is_stale(frontmatter: dict[str, Any], now: datetime | None = None) -> bool
⋮----
"""Whether a concept is stale per `stale_after` (OKF v0.2 §5.5).

    A concept is stale when `now >= stale_after`. Returns False when
    `stale_after` is absent, or is not an ISO 8601 datetime with an explicit
    UTC offset: a date-only `2026-12-31` names a different instant in every
    timezone, so it is ignored rather than guessed at.
    """
raw = str(frontmatter.get("stale_after") or "")
⋮----
stale_after = datetime.fromisoformat(raw)
`````

## File: src/reference_agent/bundle/index.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
⋮----
_INDEX_FILE = "index.md"
_FALLBACK_MODEL = "gemini-flash-latest"
⋮----
def _load_doc(path: Path) -> OKFDocument | None
⋮----
def _build_index_text(entries: list[tuple[str, str, str, str]]) -> str
⋮----
# entries: (type, title, relative_link, description)
grouped: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
⋮----
sections: list[str] = []
⋮----
lines = [f"# {typ}", ""]
⋮----
suffix = f" - {desc}" if desc else ""
⋮----
def _directories_to_index(bundle_root: Path) -> list[Path]
⋮----
dirs: set[Path] = set()
⋮----
cur = md.parent
⋮----
cur = cur.parent
⋮----
bundle_root = Path(bundle_root)
written: list[Path] = []
⋮----
directories = sorted(
⋮----
dir_descriptions: dict[Path, str] = {}
⋮----
entries: list[tuple[str, str, str, str]] = []
⋮----
doc = _load_doc(child)
⋮----
fm = doc.frontmatter
title = str(fm.get("title") or child.stem)
desc = str(fm.get("description") or "")
typ = str(fm.get("type") or "")
⋮----
desc = dir_descriptions.get(child, "")
⋮----
index_path = directory / _INDEX_FILE
⋮----
pairs = [(title, desc) for _, title, _, desc in entries]
⋮----
rel = str(directory.relative_to(bundle_root))
`````

## File: src/reference_agent/bundle/paths.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
⋮----
_SEGMENT_RE = re.compile(r"[A-Za-z0-9_][A-Za-z0-9_.\-]*")
⋮----
def _validate_segment(seg: str) -> None
⋮----
def concept_id_to_path(bundle_root: Path, concept_id: tuple[str, ...]) -> Path
⋮----
def path_to_concept_id(bundle_root: Path, path: Path) -> tuple[str, ...]
⋮----
rel = path.relative_to(bundle_root).with_suffix("")
⋮----
def parse_concept_id(s: str) -> tuple[str, ...]
⋮----
parts = tuple(p for p in s.split("/") if p)
`````

## File: src/reference_agent/bundle/synthesizer.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
⋮----
log = logging.getLogger(__name__)
⋮----
_PROMPT_TEMPLATE = """\
⋮----
def _fallback(children: list[tuple[str, str]]) -> str
⋮----
titles = ", ".join(t for t, _ in children if t) or "no titled entries"
⋮----
contents = "\n".join(
prompt = _PROMPT_TEMPLATE.format(rel_path=rel_path, contents=contents)
⋮----
client = genai.Client()
response = client.models.generate_content(model=model, contents=prompt)
text = (getattr(response, "text", None) or "").strip()
`````

## File: src/reference_agent/prompts/reference_instruction.md
`````markdown
You are a reference agent that produces **Open Knowledge Format (OKF v0.2)**
documents from raw source metadata. Each invocation enriches exactly **one**
concept and finishes by calling `write_concept_doc` exactly once.

## Workflow

1. Call `read_existing_doc(concept_id)` to see whether a prior document exists.
   If it does, use it as a starting point and refine rather than rewrite.
2. Call `read_concept_raw(concept_id)` to get structured metadata (schema,
   partitioning, etc.).
3. Optionally call `sample_rows(concept_id, n=3)` if the metadata is sparse
   and a small data sample would help you describe the concept.
4. Call `list_concepts()` to learn what other concepts exist in the bundle.
   Use the result to weave cross-links into your prose (see "Cross-linking").
5. Compose an OKF document and call `write_concept_doc(concept_id, frontmatter,
   body)` exactly once, passing the frontmatter and body as the tool's
   arguments. Do **not** print the document, the frontmatter, or the body in
   your reply — the only way to persist a concept is the `write_concept_doc`
   call. Do not call any tools after that.

## Frontmatter (YAML)

Only `type` is strictly required; the rest are strongly recommended.

- `type` (required): the concept type, exactly as returned in the concept ref
  (e.g. `BigQuery Table`, `BigQuery Dataset`).
- `title`: a short human-readable display name.
- `description`: **one sentence** explaining what this concept is. This is
  used verbatim in auto-generated `index.md` files, so keep it tight and
  informative.
- `resource` (recommended when applicable): the URI of the underlying asset.
- `tags` (recommended): a comma-separated list or YAML list of useful search
  tags inferred from the metadata.
- `status` (optional): `draft` | `stable` | `deprecated`. Defaults to `stable`
  when omitted, so you only need to set it for a draft or deprecated concept.
- `generated`: leave unset and the tool will record
  `generated: {by: reference_agent/<model>, at: <current UTC time>}` for you.
  Only supply a `{by, at}` mapping yourself if you need to override it. Actors
  follow the convention `<producer>/<version>` for tools,
  `human:<id>` for people, and `process:<id>` for automated processes.
- `sources` (recommended): where the content derives from — see "Sources and
  attribution" below. Provenance lives here, **not** in a `# Citations` body
  section.

## Body sections

In this order:

1. A short prose description (1–3 paragraphs) of what this concept is, what it
   represents, and how it is typically used. For tables, describe the grain
   (one row per X), the time range, and any obfuscation or sampling caveats.
2. `# Schema` — a flattened, readable summary of fields. For nested RECORD
   fields, indent or table-format their sub-fields. Skip mode/type when they
   are obvious. Highlight repeated records explicitly.
3. `# Common query patterns` — 1 to 3 short SQL snippets, fenced as
   ```` ```sql ```` blocks, illustrating realistic usage of this asset.

Do **not** add a `# Citations` section; provenance now lives in the `sources`
frontmatter (see below).

## Sources and attribution

Record the materials this concept derives from in the `sources` frontmatter
list (OKF v0.2 §5.1). Each entry is a mapping with a required `resource` (the
URI), a stable `id` key, and a human-readable `title`. Include this concept's
own `resource` value as a `sources` entry (when present), followed by any URLs
that informed the description. Do not invent URLs; record only sources you
actually know.

To attribute a specific claim in the body, end the sentence with a markdown
footnote whose label matches a `sources[].id` (e.g. a sentence ending in
`[^ga4-export-docs]`, with a matching `[^ga4-export-docs]: GA4 BigQuery Export
schema` footnote definition later in the body).

## Cross-linking

When your prose naturally references another concept by name — a sibling
table, the parent dataset, a reference doc — link to it using a path
**relative to the current document's directory**, so the link resolves
correctly when the bundle is browsed as plain files (e.g. on GitHub).
The list of available targets comes from `list_concepts()` (workflow
step 4). Examples, written from a doc at `tables/<this_table>.md`:

- Sibling table: `[users](users.md)`
- Parent dataset from a table: `[dataset](../datasets/<slug>.md)`
- Reference doc: `[event parameters](../references/event_parameters.md)`

Rules:

- Use file-relative paths only. Never start a link with `/` (that breaks
  GitHub rendering), and don't use bare filenames that aren't actual
  siblings.
- Only link to ids returned by `list_concepts()`. Do not invent link targets.
- One link per concept mention per section is enough. Do not over-link.
- Do not link from headers, fenced code blocks, or schema field-name listings.
- Do not link the current doc to itself.

## Style

- Be concrete. Prefer concrete examples and concrete field names over generic
  hand-waving.
- Do not invent fields, partitions, or shard counts that are not in the raw
  metadata.
- Do not include preamble, apologies, or reasoning narration in the document
  body. The body must be valid markdown that a human or downstream agent can
  consume directly.
`````

## File: src/reference_agent/prompts/web_ingestion_instruction.md
`````markdown
You are a web-ingestion agent that augments an existing **Open Knowledge
Format (OKF)** bundle with information from web pages. You drive your own
crawl: starting from a list of seed URLs, you decide which links are worth
following and what to do with each page you fetch.

## Inputs

The user message contains:
- A list of **seed URLs** to start from.
- A **max-pages budget** (a hard cap enforced by the `fetch_url` tool; you
  cannot exceed it).
- Optionally, a list of **allowed hosts**. By default only the hosts of the
  seed URLs are allowed.

## Workflow

1. Call `list_concepts()` once at the start to learn what concepts the
   bundle already has. You will route web findings against these.
2. For each seed URL, call `fetch_url(url)`. The result includes the page's
   markdown content and `links` — its outbound URLs.
3. From those links, pick the ones that look like they lead to
   **authoritative documentation** on topics related to the existing
   concepts. A seed is usually an index or schema-reference page, so its
   most valuable outbound links are to **sample-query / cookbook pages,
   metric-definition pages, and field/enum reference pages** — follow
   those; they are what produce `references/metrics/` and
   `references/joins/` docs. Skip nav links, site footers, login pages,
   "About us", marketing pages, cookie/privacy notices, and anything
   obviously tangential. Call `fetch_url` on each selected link. Their
   results in turn contain more links, which you can also follow —
   recursively, with your judgment as the filter. Do not stop after one
   page: keep crawling relevant in-domain links until you have covered the
   material or hit the page budget.
4. For **each page you fetch**, decide one of:
   - **Enrich existing concept(s)**. If the page describes a topic that an
     existing concept doc covers (e.g. a schema reference for a specific
     table), call `read_existing_doc(concept_id)` to read the current doc,
     then call `write_concept_doc(concept_id, frontmatter, body)` with the
     **augmented** doc. Augmentation is strict (see "Augmentation rules"
     below) — you must preserve the existing structure verbatim and add
     content within or alongside it. You may update multiple concepts from
     a single page.
   - **Mint a new reference concept** — only if the page meets all four
     of:
     1. **Topic shape**: it defines something *referenceable by name*
        from a primary concept doc. Allowed kinds: a business entity
        definition, a metric definition, an enum or status-code
        reference, a field/parameter glossary, a pricing/billing note,
        a units/timezone/identifier convention.
     2. **Not bundle-level meta**: it is NOT an overview, introduction,
        "getting started", quickstart, tutorial, walkthrough, release
        notes, changelog, roadmap, FAQ, or product landing page. If the
        page title or URL slug contains any of `overview`, `intro`,
        `getting-started`, `quickstart`, `tutorial`, `walkthrough`,
        `release-notes`, `changelog`, `roadmap`, `faq` — skip.
     3. **Citation test**: you can plausibly write a sentence in a
        primary concept doc of the form
        `See the [X reference](/references/x.md) for ...` where X is a
        concrete noun (an entity, a metric, an enum, a field set). If
        the best sentence you can write is "See the overview for
        context", it fails this test.
     4. **Reuse test**: at least two existing concepts would benefit
        from citing it, OR one existing concept needs it as
        load-bearing background that doesn't fit in its own doc.

     If all four hold: pick an id under `references/` (e.g.
     `references/event_parameters`), set `type: Reference`, set
     `resource` to this page's URL, call `write_concept_doc`, and
     cross-link from each related primary doc with a markdown link
     written **relative to the linking doc's directory**, e.g. from a
     `tables/<slug>.md` doc:
     `[Event parameters reference](../references/event_parameters.md)`.

     When in doubt, **skip**. A bundle with zero `references/` docs is
     fine; a bundle full of `references/overview` and
     `references/getting_started` is noise.
   - **Skip**. If the page is irrelevant, low-signal, or already covered,
     do nothing. Move on.
5. Stop when:
   - `fetch_url` returns `"max_pages reached"` — your budget is spent.
   - You have actually fetched the seed pages **and** followed their
     high-value links (sample-query/cookbook, metric, and reference pages)
     until further in-domain fetches would have genuine diminishing
     returns. Fetching only the seed page and stopping is **not** done —
     seeds are indexes; the value is one or two hops out.
   Before you stop, **verify no reference you minted is orphaned**: every
   `references/metrics/<slug>.md` and `references/joins/<a>__<b>.md` you
   wrote this session must be linked from at least one primary table doc's
   `# Metrics` / `# Joins` section. If any is still uncited, go back and
   augment the contributing table doc(s) now — do not end the session with
   orphan references.

## Frontmatter conventions

When you write a doc — primary or reference — frontmatter must include at
minimum `type`. Strongly include `title` and `description` (one sentence; used
in `index.md`). Leave `generated` unset; the tool fills
`generated: {by: reference_agent/<model>, at: <now>}`. Record provenance in the
`sources` frontmatter list (each entry `{id, resource, title}`), never in a
`# Citations` body section. For reference docs:

- `type`: `Reference`
- `resource`: the canonical source URL (the page you ingested)
- `tags`: a YAML list inferred from the page topic
- `sources`: at least an entry for the page you ingested

## Augmentation rules

When you call `write_concept_doc` for a concept that **already has an
on-disk doc** (i.e. `read_existing_doc` returned non-null), the call is
an *augmentation*, not a rewrite. Treat the existing doc as the source of
truth and fold the web page into it. These rules are non-negotiable:

1. **Frontmatter — pass the complete dict, with existing values preserved:**
   `write_concept_doc` does a full replacement, not a patch — the
   `frontmatter` argument **must include every key** the existing doc had
   (`type`, `title`, `description`, `resource`, `tags`, etc.). Omitting a
   key drops it. The augmentation rule is about which *values* you keep,
   not which *keys* you send. Specifically:
   - Copy `type` verbatim from the existing frontmatter into your new dict.
   - Copy `title` verbatim. The web page's `<title>` is **not** the
     concept's title.
   - Copy `resource` verbatim. For a `BigQuery Table` doc the `resource`
     is the BigQuery REST URI; it must stay that. The web page URL goes
     in the `sources` list, never in `resource`.
   - For `tags`, pass the union of existing tags plus any new ones
     (merge, don't replace).
   - For `sources`, pass the union of existing entries plus any new ones
     (merge, don't replace) — the tool refuses a write that shrinks the
     list. Add an entry for the page you ingested.
   - Leave `generated` unset (omit the key) so the tool refreshes it.
     This is the *only* key you may legitimately drop.
   - You may refine `description` if the web page surfaces a more
     accurate one-sentence summary; otherwise copy it verbatim.

2. **Body — every `#` heading in the existing body must appear in your
   new body**, in the same order, with the same wording. You may:
   - extend the prose under each heading,
   - add new bullets to existing lists (e.g. add fields to `# Schema`,
     not replace the list),
   - add new sub-sections (`##`) under existing top-level headings,
   - add brand-new top-level headings **after** the existing ones,
   - add the web page as a new `sources` frontmatter entry.
   You may not:
   - drop or rename any existing `#` heading,
   - replace the body wholesale with a topical rewrite of the web page,
   - shrink or rewrite the `# Schema` section for a `BigQuery Table` doc
     — the BQ pass populated it from real schema metadata; keep every
     field listing.

3. **If you cannot honor rule 2** because the web page is a fundamentally
   different topic (a query cookbook, a release notes page, a generic
   tutorial), do **not** call `write_concept_doc` for the existing
   concept. Either mint a `references/<slug>` doc and cross-link from the
   primary doc's prose, or skip the page.

4. **A rejected write did not happen — fix it and retry, do not give up.**
   When `write_concept_doc` returns an `error` (for example, the schema
   guard reporting that your `# Schema` is missing fields the BQ pass
   populated, or the `sources` guard reporting a shrunken list), the doc
   was **not** written. Do not abandon the concept and do not move on as
   if it succeeded. Re-call `read_existing_doc(concept_id)`, copy the
   **entire** existing `# Schema` (every field) and every existing
   `sources` entry verbatim into your new call, add only your new content
   on top, and call `write_concept_doc` again. A `BigQuery Table` schema
   from the BQ pass is authoritative and complete — never shrink or
   summarize it; augment field descriptions inline while keeping every
   field. If after re-reading you still cannot add value without dropping
   existing content, mint a `references/<slug>` doc instead and skip the
   augmentation.

## Required extractions: metrics, dimensions, join paths

When a fetched page contains any of the following content types, you
**must** capture them in the appropriate doc — these are the
highest-signal artifacts a web page can contribute and they are easy to
lose in a topical paraphrase. For each, the destination and required
shape are non-negotiable:

- **Aggregate metrics** (e.g. *daily active users*, *conversion rate*,
  *revenue per user*, *retention curve*). Capture the metric's name, a
  one-line definition, and the **concrete SQL expression** (e.g.
  `COUNT(DISTINCT user_pseudo_id)`) — paraphrase is not enough.
  - **Step 1 — mint the reference**: one `references/metrics/<slug>.md`
    file *per metric* (e.g. `references/metrics/daily_active_users.md`).
    The reference doc owns the SQL. Frontmatter: `type: Reference`, `tags:
    [metric]`, `resource` set to the page URL, a `sources` entry for the
    page, plus the standard `title`/`description`. Body: one-sentence
    definition, then a fenced SQL block with the formula.
  - **Step 2 — cite it back (MANDATORY, not optional)**: a minted metric
    reference is **incomplete until a primary table doc links to it**. An
    orphan `references/metrics/<slug>.md` that no table cites is a bug, not
    a deliverable. Immediately after Step 1, for **each** contributing
    table: call `read_existing_doc(<table_id>)`, then
    `write_concept_doc(<table_id>, ...)` with a `# Metrics` top-level
    section (added **after** the existing headings, per the augmentation
    rules) containing one bullet per metric, using a link **relative to
    the table doc's directory** — from `tables/events_.md` that is
    `- [Daily active users](../references/metrics/daily_active_users.md) — DISTINCT user_pseudo_id per day.`
    (never an absolute `/references/...` path). Do **not** duplicate the
    SQL in the table doc; the reference owns it.
  - This augmentation **will** trip the `# Schema` guard if you drop
    fields — that is expected. Do not give up: follow augmentation rule 4
    (copy the entire existing `# Schema` and every `sources` entry
    verbatim, append your `# Metrics` section, retry). A metric reference
    you minted but never linked is worse than not minting it.
  - If the metric spans multiple tables, link it from every
    contributing table's `# Metrics` section.

- **Dimensions** (groupable / filterable attributes used in `GROUP BY`
  or `WHERE`, e.g. `event_name`, `device.category`, `traffic_source.medium`).
  Capture the column path, allowed values if enumerated, and a short
  semantic description.
  - **Destination**: the primary concept doc of the table that **owns
    the column**. Extend `# Schema` with the semantic description
    inline, OR add a `# Dimensions` sub-section listing dimension column
    paths and what each is good for.
  - For shared enum values that recur across tables (e.g. event-name
    catalogs), mint `references/<slug>.md` and cite from each table.

- **Join paths** (foreign-key relationships, recommended joins between
  tables in this bundle, e.g. *`events_.user_pseudo_id` ↔
  `users.user_pseudo_id`*). Capture the two sides and the **concrete
  `ON` clause**.
  - **Destination**: one `references/joins/<a>__<b>.md` file *per
    pair*, with the two table names sorted alphabetically and joined by
    a double underscore (e.g. `references/joins/events___users.md` for
    the `events_` ↔ `users` pair). One canonical file per pair,
    regardless of which side you came from. Frontmatter:
    `type: Reference`, `tags: [join]`, `resource` set to the page URL, a
    `sources` entry for the page, plus the standard
    `title`/`description`. Body: the `ON` clause as a fenced SQL block,
    then one sentence on when to use this join.
  - **Cite it back (MANDATORY)**: as with metrics, a minted join
    reference is incomplete until **both** sides link to it. After writing
    `references/joins/<a>__<b>.md`, augment **each** side's primary doc
    (`read_existing_doc` then `write_concept_doc`) with a `# Joins`
    top-level section containing a one-line link written **relative to
    that doc's directory** — from `tables/events_.md` that is
    `- [users](../references/joins/events___users.md) — join on user_pseudo_id to attach user attributes to events.`
    (never an absolute `/references/...` path). If the augmentation trips
    the `# Schema` guard, follow augmentation rule 4 and retry; do not
    abandon the back-link.
  - Do not invent join paths. Only capture joins explicitly named in
    documentation or example queries on the fetched page.

**These structured extractions bypass the four-gate reference test
above.** The gates exist to keep prose pages from becoming junk
references; metrics and joins are inherently concept-shaped and
inherently reusable, so they go straight into `references/metrics/` and
`references/joins/` without gate-checking. The four gates still apply
to *all other* `references/` mints.

If a page surfaces several of these at once (a typical "data model"
or "schema reference" page), make **multiple** `write_concept_doc`
calls — one per affected concept — rather than dumping everything into
one doc.

## Style and integrity

- Record in `sources` **only** URLs you actually fetched (or URLs already
  present in the doc you're refining). Do not invent URLs.
- Be concrete. Use concrete field names, concrete enum values, concrete
  example queries.
- Do not include preamble, apologies, or reasoning narration in document
  bodies. Bodies must be valid markdown ready for direct consumption.
- End your session with one short sentence summarizing what you did: how
  many pages you fetched, how many docs you updated, how many references
  you minted.
`````

## File: src/reference_agent/sources/__init__.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
⋮----
__all__ = ["ConceptRef", "Source"]
`````

## File: src/reference_agent/sources/base.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
⋮----
@dataclass(frozen=True)
class ConceptRef
⋮----
id: tuple[str, ...]
type: str
resource: str | None = None
hint: dict[str, Any] = field(default_factory=dict)
⋮----
@property
    def id_str(self) -> str
⋮----
class Source(ABC)
⋮----
name: str = ""
⋮----
@abstractmethod
    def list_concepts(self) -> list[ConceptRef]
⋮----
@abstractmethod
    def read_concept(self, ref: ConceptRef) -> dict[str, Any]
⋮----
def sample_rows(self, ref: ConceptRef, n: int = 5) -> list[dict[str, Any]] | None
⋮----
def find(self, concept_id: tuple[str, ...]) -> ConceptRef | None
`````

## File: src/reference_agent/sources/bigquery.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
⋮----
_SHARD_SUFFIX_RE = re.compile(r"^(?P<prefix>.+?_)(?P<shard>\d{6,8})$")
⋮----
def _schema_to_dict(fields: list[bigquery.SchemaField]) -> list[dict[str, Any]]
⋮----
out: list[dict[str, Any]] = []
⋮----
entry: dict[str, Any] = {
⋮----
class BigQuerySource(Source)
⋮----
name = "bigquery"
⋮----
def __init__(self, dataset: str, billing_project: str | None = None)
⋮----
def _dataset_resource_uri(self) -> str
⋮----
def _table_resource_uri(self, table_id: str) -> str
⋮----
def list_concepts(self) -> list[ConceptRef]
⋮----
concepts: list[ConceptRef] = []
⋮----
families: dict[str, list[str]] = {}
singletons: list[str] = []
⋮----
m = _SHARD_SUFFIX_RE.match(tbl.table_id)
⋮----
family_concept_id = ("tables", prefix)
shards_sorted = sorted(shards)
⋮----
def _representative_table_id(self, ref: ConceptRef) -> str
⋮----
def read_concept(self, ref: ConceptRef) -> dict[str, Any]
⋮----
ds = self.client.get_dataset(self._dataset_ref)
⋮----
table_id = self._representative_table_id(ref)
tbl = self.client.get_table(self._dataset_ref.table(table_id))
data: dict[str, Any] = {
⋮----
rp = tbl.range_partitioning
⋮----
table_ref = self._dataset_ref.table(table_id)
⋮----
tbl = self.client.get_table(table_ref)
⋮----
table_type = (getattr(tbl, "table_type", None) or "TABLE").upper()
⋮----
row_iter = self.client.list_rows(table_ref, max_results=n)
⋮----
# VIEW / MATERIALIZED_VIEW / EXTERNAL / SNAPSHOT — the
# tabledata.list REST endpoint refuses non-base-tables, so
# fall back to a small query that materializes the rows.
sql = (
row_iter = self.client.query(sql).result()
`````

## File: src/reference_agent/tools/__init__.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
`````

## File: src/reference_agent/tools/bundle_tools.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
⋮----
_PREFERRED_KEY_ORDER = (
⋮----
_FIELD_NAME_RE = re.compile(r"`([A-Za-z_][A-Za-z0-9_.]*)`")
⋮----
def _section_content_lines(body: str, heading: str) -> list[str]
⋮----
"""Return non-blank lines under a top-level `# heading` section."""
in_section = False
out: list[str] = []
⋮----
stripped = line.strip()
⋮----
in_section = stripped == heading
⋮----
def _schema_field_names(body: str) -> set[str]
⋮----
names: set[str] = set()
⋮----
def _sources_count(frontmatter: dict[str, Any]) -> int
⋮----
sources = frontmatter.get("sources")
⋮----
if sources:  # a bare mapping counts as one entry
⋮----
def _reorder_frontmatter(fm: dict[str, Any]) -> dict[str, Any]
⋮----
ordered: dict[str, Any] = {}
⋮----
def read_existing_doc(concept_id: str) -> dict[str, Any] | None
⋮----
"""Return the existing OKF document for this concept, if one is already on
    disk.

    Use this before writing to refine prior content instead of overwriting
    blindly. Returns null when no document exists yet. When a document exists,
    returns {'frontmatter': <object>, 'body': <markdown string>}.
    """
ctx = get_context()
cid = parse_concept_id(concept_id)
path = concept_id_to_path(ctx.bundle_root, cid)
⋮----
doc = OKFDocument.parse(path.read_text(encoding="utf-8"))
⋮----
"""Write (or overwrite) the OKF markdown document for this concept.

    `frontmatter` must include at minimum `type` (OKF v0.2 §11). `title`,
    `description`, `resource`, and `tags` are strongly recommended when
    applicable. `generated` is filled in automatically: leave it unset and the
    tool records `generated: {by: reference_agent/<model>, at: <now>}`, or
    provide your own `{by, at}` mapping. Provenance goes in the `sources`
    frontmatter family (not a `# Citations` body section); attribute individual
    body claims with markdown footnotes keyed to `sources[].id`. The `body`
    should contain the prose description plus `# Schema` and
    `# Common query patterns` sections per the OKF convention.

    Returns {'path': <relative path written>, 'bytes': <int>}.
    """
⋮----
fm = dict(frontmatter)
generated = fm.get("generated")
⋮----
generated = {}
⋮----
generated = dict(generated)
⋮----
fm = _reorder_frontmatter(fm)
⋮----
doc = OKFDocument(frontmatter=fm, body=body or "")
⋮----
# Augmentation guard: during the web pass, refuse writes that shrink
# an existing BigQuery Table doc's # Schema field set or its `sources`
# frontmatter list. The BQ pass populates these from real metadata; the
# web pass must augment, not replace.
⋮----
existing = OKFDocument.parse(path.read_text(encoding="utf-8"))
⋮----
existing = None
⋮----
old_fields = _schema_field_names(existing.body)
new_fields = _schema_field_names(body or "")
missing = sorted(old_fields - new_fields)
⋮----
shown = ", ".join(f"`{m}`" for m in missing[:10])
truncated = " (and more)" if len(missing) > 10 else ""
⋮----
old_sources = _sources_count(existing.frontmatter)
new_sources = _sources_count(fm)
⋮----
text = doc.serialize()
`````

## File: src/reference_agent/tools/context.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
⋮----
@dataclass
class ToolContext
⋮----
source: Source
bundle_root: Path
model: str = ""
⋮----
@dataclass
class WebState
⋮----
allowed_hosts: set[str]
max_pages: int
allowed_path_prefixes: tuple[str, ...] = ()
denied_path_substrings: tuple[str, ...] = ()
max_depth: int = 2
visited: set[str] = field(default_factory=set)
fetched_count: int = 0
url_depth: dict[str, int] = field(default_factory=dict)
⋮----
_ctx: ToolContext | None = None
_web: WebState | None = None
⋮----
def set_context(source: Source, bundle_root: Path, model: str = "") -> None
⋮----
_ctx = ToolContext(source=source, bundle_root=Path(bundle_root), model=model)
⋮----
def get_context() -> ToolContext
⋮----
_web = WebState(
⋮----
def get_web_state() -> WebState
⋮----
def clear_web_state() -> None
⋮----
_web = None
⋮----
def is_web_pass() -> bool
⋮----
"""True while the runner is executing the web-ingestion pass."""
`````

## File: src/reference_agent/tools/source_tools.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
⋮----
def _ref_to_dict(ref) -> dict[str, Any]
⋮----
def list_concepts() -> list[dict[str, Any]]
⋮----
"""List every concept the active source advertises.

    Returns a list of objects with fields: `id` (slash-joined path used as the
    concept_id in other tools), `type` (OKF type, e.g. 'BigQuery Table'),
    `resource` (canonical URI of the underlying asset, if any), and `hint`
    (source-specific extra info such as wildcard flags or shard counts).
    """
src = get_context().source
⋮----
def read_concept_raw(concept_id: str) -> dict[str, Any]
⋮----
"""Fetch raw structured metadata for a single concept from its source.

    `concept_id` is the slash-joined id returned by `list_concepts` (e.g.
    'tables/events_'). For BigQuery tables this includes schema (with nested
    RECORD fields), partitioning, clustering, row counts, and timestamps.
    """
⋮----
cid = parse_concept_id(concept_id)
ref = src.find(cid)
⋮----
def sample_rows(concept_id: str, n: int = 5) -> dict[str, Any]
⋮----
"""Pull a small sample of rows from the underlying asset, if supported.

    Returns an object with `rows` (a list of stringified row dicts; empty if
    sampling is unsupported or fails) and `note` (a short human-readable
    explanation when rows could not be sampled).
    """
⋮----
rows = src.sample_rows(ref, n=n)
⋮----
coerced = [{k: str(v) for k, v in row.items()} for row in rows]
`````

## File: src/reference_agent/tools/web_tools.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
⋮----
def fetch_url(url: str) -> dict[str, Any]
⋮----
"""Fetch a single web page and return its content as markdown plus its
    outbound links.

    The session-wide crawl budget (`max_pages`), the allowed-hosts filter,
    optional URL path-prefix allow-list, denied-substring blocklist, and a
    hop-depth cap measured from the seed URLs are all enforced inside this
    tool. When a fetch is rejected the return value contains an `error`
    field instead of page content. Treat that as a signal to stop or pick a
    different URL; do not retry the same URL.

    Successful return shape:
      {"url", "title", "markdown", "links",
       "fetched_count", "max_pages_budget", "depth", "max_depth"}

    Rejected return shape:
      {"error": "<reason>", "url": url,
       "fetched_count", "max_pages_budget"}
    """
state = get_web_state()
parsed = urlparse(url)
⋮----
def _reject(reason: str) -> dict[str, Any]
⋮----
path = parsed.path or "/"
⋮----
depth = state.url_depth.get(url)
⋮----
# Unknown URL — treat as the agent typing it in directly, which is
# only allowed for the initial seeds (already pre-registered at
# depth 0). Anything else means the agent invented a URL not
# surfaced via a parent page; reject so we don't lose depth tracking.
⋮----
page = fetch_and_parse(url)
⋮----
child_depth = depth + 1
`````

## File: src/reference_agent/viewer/static/viz.css
`````css
/*
 * Copyright 2026 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
⋮----
* { box-sizing: border-box; }
body {
header {
.title strong { font-size: 16px; margin-right: 8px; }
.muted { color: #64748b; font-size: 12px; }
.controls { display: flex; gap: 8px; }
.controls input, .controls select, .controls button {
.controls input { width: 220px; }
.controls button { cursor: pointer; background: #f1f5f9; }
.controls button:hover { background: #e2e8f0; }
⋮----
main {
#graph {
#detail {
#detail-empty {
⋮----
.detail-header { margin-bottom: 12px; }
.detail-header h1 {
.type-chip {
dl.frontmatter {
dl.frontmatter dt {
dl.frontmatter dd { margin: 0; }
dl.frontmatter a { color: #2563eb; word-break: break-all; }
⋮----
.tag {
⋮----
.badges {
.badge {
.badge.status-stable { background: #ecfdf5; color: #047857; border-color: #a7f3d0; }
.badge.status-draft { background: #fefce8; color: #a16207; border-color: #fde68a; }
.badge.status-deprecated { background: #f1f5f9; color: #64748b; border-color: #cbd5e1; text-decoration: line-through; }
.badge.trust-unverified { background: #f1f5f9; color: #64748b; border-color: #cbd5e1; }
.badge.trust-machine-confirmed { background: #eff6ff; color: #1d4ed8; border-color: #bfdbfe; }
.badge.trust-human-reviewed { background: #f5f3ff; color: #6d28d9; border-color: #ddd6fe; }
.badge.stale { background: #fef2f2; color: #b91c1c; border-color: #fecaca; }
.badge.fresh { background: #ecfdf5; color: #047857; border-color: #a7f3d0; }
⋮----
.sources-list { padding-left: 18px; margin: 0; }
.sources-list li { margin: 1px 0; }
⋮----
hr { border: none; border-top: 1px solid #e2e8f0; margin: 14px 0; }
⋮----
#detail-body { font-size: 13px; line-height: 1.55; }
#detail-body h1 {
#detail-body h2 { font-size: 14px; margin: 14px 0 4px; }
#detail-body h3 { font-size: 13px; margin: 12px 0 4px; }
#detail-body p { margin: 6px 0; }
#detail-body code {
#detail-body pre {
#detail-body pre code { background: transparent; color: inherit; padding: 0; }
#detail-body ul, #detail-body ol { padding-left: 22px; margin: 6px 0; }
#detail-body li { margin: 2px 0; }
#detail-body table { border-collapse: collapse; margin: 8px 0; }
#detail-body th, #detail-body td {
#detail-body a.internal { color: #2563eb; cursor: pointer; }
#detail-body a.external { color: #2563eb; }
⋮----
#detail-backlinks { margin-top: 18px; }
#detail-backlinks h2 { font-size: 13px; color: #64748b; margin-bottom: 6px; }
#detail-backlinks ul { padding-left: 18px; }
#detail-backlinks a { color: #2563eb; cursor: pointer; }
`````

## File: src/reference_agent/viewer/static/viz.js
`````javascript
// Copyright 2026 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
⋮----
// Populate type filter
⋮----
// Build reverse-link index for backlinks
⋮----
// Look up node label/type by id
⋮----
function clearSelection()
⋮----
function showDetail(conceptId)
⋮----
// v0.2 signal badges: status, trust tier, staleness.
⋮----
function makeBadge(text, cls)
⋮----
function formatActorEvent(event)
⋮----
function rewriteInternalLinks(root)
⋮----
// Auto-show the first node (a dataset if available, else first concept)
`````

## File: src/reference_agent/viewer/templates/viz.html
`````html
<!DOCTYPE html>
<!--
  Copyright 2026 Google LLC

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
<html lang="en">
<head>
<meta charset="utf-8">
<title>OKF Bundle Viewer</title>
<script src="https://cdn.jsdelivr.net/npm/cytoscape@3.28.1/dist/cytoscape.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/marked@12.0.0/marked.min.js"></script>
<style>
/*__VIZ_CSS__*/
</style>
</head>
<body>
<header>
  <div class="title">
    <strong id="bundle-name"></strong>
    <span class="muted">OKF bundle</span>
  </div>
  <div class="controls">
    <input id="search" type="search" placeholder="Search title / id / tag">
    <select id="filter-type">
      <option value="">All types</option>
    </select>
    <select id="layout">
      <option value="cose">cose (force)</option>
      <option value="concentric">concentric</option>
      <option value="breadthfirst">breadth-first</option>
      <option value="circle">circle</option>
      <option value="grid">grid</option>
    </select>
    <button id="reset">Reset view</button>
  </div>
</header>

<main>
  <section id="graph"></section>
  <section id="detail">
    <div id="detail-empty" class="muted">Click a node to see its details.</div>
    <article id="detail-content" hidden>
      <header class="detail-header">
        <span class="type-chip" id="detail-type"></span>
        <h1 id="detail-title"></h1>
        <div class="muted" id="detail-id"></div>
      </header>
      <div class="badges" id="detail-badges"></div>
      <dl class="frontmatter">
        <dt>Description</dt><dd id="detail-description"></dd>
        <dt>Resource</dt><dd id="detail-resource"></dd>
        <dt>Tags</dt><dd id="detail-tags"></dd>
        <dt>Generated</dt><dd id="detail-generated"></dd>
        <dt>Verified</dt><dd id="detail-verified"></dd>
        <dt>Sources</dt><dd id="detail-sources"></dd>
      </dl>
      <hr>
      <div id="detail-body"></div>
      <section id="detail-backlinks" hidden>
        <h2>Cited by</h2>
        <ul id="backlinks-list"></ul>
      </section>
    </article>
  </section>
</main>

<script>
window.BUNDLE_NAME = __BUNDLE_NAME__;
window.BUNDLE = __BUNDLE_DATA__;
</script>
<script>
/*__VIZ_JS__*/
</script>
</body>
</html>
`````

## File: src/reference_agent/viewer/__init__.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
⋮----
__all__ = ["generate_visualization"]
`````

## File: src/reference_agent/viewer/generator.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
⋮----
_INDEX_NAME = "index.md"
_LINK_RE = re.compile(r"\]\(([^)\s]+\.md)(?:#[A-Za-z0-9_\-]*)?\)")
_TYPE_PALETTE = {
_DEFAULT_NODE_COLOR = "#94a3b8"
⋮----
@dataclass
class Concept
⋮----
id: str
type: str
title: str
description: str
resource: str
tags: list[str]
body: str
status: str = "stable"
generated: dict[str, Any] = field(default_factory=dict)
verified: list[dict[str, Any]] = field(default_factory=list)
stale_after: str = ""
sources: list[dict[str, Any]] = field(default_factory=list)
trust_tier: str = "unverified"
stale: bool = False
links_to: list[str] = field(default_factory=list)
⋮----
def to_node(self) -> dict[str, Any]
⋮----
color = _TYPE_PALETTE.get(self.type, _DEFAULT_NODE_COLOR)
⋮----
def _extract_links(body: str, doc_dir: Path, bundle_root: Path) -> list[str]
⋮----
out: list[str] = []
seen: set[str] = set()
bundle_root_resolved = bundle_root.resolve()
⋮----
target = m.group(1)
⋮----
resolved = (doc_dir / target).resolve().relative_to(bundle_root_resolved)
⋮----
rel = resolved.as_posix()
⋮----
rel = rel[:-3]
⋮----
def _walk_concepts(bundle_root: Path) -> list[Concept]
⋮----
concepts: list[Concept] = []
⋮----
rel = md_path.relative_to(bundle_root).with_suffix("")
concept_id = "/".join(rel.parts)
⋮----
doc = OKFDocument.parse(md_path.read_text(encoding="utf-8"))
⋮----
fm = doc.frontmatter or {}
tags = fm.get("tags") or []
⋮----
tags = [str(tags)]
generated = fm.get("generated") if isinstance(fm.get("generated"), dict) else {}
sources = fm.get("sources")
⋮----
sources = [sources]
⋮----
sources = []
concept = Concept(
⋮----
def _build_graph(concepts: list[Concept]) -> dict[str, Any]
⋮----
ids = {c.id for c in concepts}
nodes = [c.to_node() for c in concepts]
edges: list[dict[str, Any]] = []
seen_edges: set[tuple[str, str]] = set()
⋮----
key = (c.id, target)
⋮----
bodies = {c.id: c.body for c in concepts}
types = sorted({c.type for c in concepts})
⋮----
def _load_template() -> str
⋮----
template_path = Path(__file__).parent / "templates" / "viz.html"
⋮----
def _load_asset(name: str) -> str
⋮----
asset_path = Path(__file__).parent / "static" / name
⋮----
"""Walk a bundle and write a single self-contained HTML visualization.

    Returns counts: {'concepts': N, 'edges': M, 'bytes': K}.
    """
bundle_root = Path(bundle_root)
out_path = Path(out_path)
⋮----
concepts = _walk_concepts(bundle_root)
graph = _build_graph(concepts)
template = _load_template()
css = _load_asset("viz.css")
js = _load_asset("viz.js")
name = bundle_name or bundle_root.resolve().name
⋮----
html = (
`````

## File: src/reference_agent/web/__init__.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
`````

## File: src/reference_agent/web/fetcher.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
⋮----
_USER_AGENT = "okf-reference-agent/0.1 (+https://github.com/amirhormati/open-knowledge-format)"
_MAX_MARKDOWN_BYTES = 40 * 1024
⋮----
_TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)
_HREF_RE = re.compile(r"""href\s*=\s*["']([^"'#\s]+)["']""", re.IGNORECASE)
⋮----
class FetchError(Exception)
⋮----
@dataclass(frozen=True)
class Page
⋮----
url: str
title: str | None
markdown: str
links: list[str]
⋮----
def _extract_title(html: str) -> str | None
⋮----
m = _TITLE_RE.search(html)
⋮----
raw = re.sub(r"\s+", " ", m.group(1)).strip()
⋮----
def _extract_links(html: str, base_url: str) -> list[str]
⋮----
seen: set[str] = set()
out: list[str] = []
⋮----
href = match.group(1).strip()
⋮----
scheme = urlparse(href).scheme.lower()
⋮----
def _truncate(text: str, max_bytes: int) -> str
⋮----
encoded = text.encode("utf-8", errors="replace")
⋮----
def fetch_and_parse(url: str, *, timeout: float = 10.0) -> Page
⋮----
req = Request(url, headers={"User-Agent": _USER_AGENT, "Accept": "text/html,*/*;q=0.5"})
⋮----
content_type = resp.headers.get("Content-Type", "")
final_url = resp.geturl() or url
body_bytes = resp.read()
⋮----
charset = "utf-8"
⋮----
charset = content_type.lower().split("charset=", 1)[1].split(";", 1)[0].strip() or "utf-8"
⋮----
html = body_bytes.decode(charset, errors="replace")
⋮----
html = body_bytes.decode("utf-8", errors="replace")
⋮----
title = _extract_title(html)
links = _extract_links(html, final_url)
markdown = markdownify(html, heading_style="ATX")
markdown = _truncate(markdown, _MAX_MARKDOWN_BYTES)
`````

## File: src/reference_agent/__init__.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
⋮----
__version__ = "0.1.0"
`````

## File: src/reference_agent/__main__.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
`````

## File: src/reference_agent/agent.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
⋮----
DEFAULT_MODEL = "gemini-flash-latest"
⋮----
def _load_prompt(filename: str) -> str
⋮----
def build_bq_agent(model: str = DEFAULT_MODEL) -> Agent
⋮----
def build_web_agent(model: str = DEFAULT_MODEL) -> Agent
`````

## File: src/reference_agent/cli.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
⋮----
_SOURCES = ("bq",)
⋮----
def _build_source(name: str, args: argparse.Namespace)
⋮----
def _parse_seed_file(path: Path) -> list[str]
⋮----
urls: list[str] = []
text = path.read_text(encoding="utf-8")
⋮----
line = raw.split("#", 1)[0].strip()
⋮----
def _collect_seeds(args: argparse.Namespace) -> list[str]
⋮----
seeds: list[str] = []
⋮----
def _dedup_preserve_order(items: list[str]) -> list[str]
⋮----
seen: set[str] = set()
out: list[str] = []
⋮----
def _parser() -> argparse.ArgumentParser
⋮----
p = argparse.ArgumentParser(prog="reference-agent")
sub = p.add_subparsers(dest="command", required=True)
⋮----
enrich = sub.add_parser(
⋮----
viz = sub.add_parser(
⋮----
def main(argv: list[str] | None = None) -> int
⋮----
args = _parser().parse_args(argv)
⋮----
# Quiet chatty third-party loggers regardless of mode.
⋮----
out = args.out or (args.bundle / "viz.html")
stats = generate_visualization(args.bundle, out, bundle_name=args.name)
⋮----
source = _build_source(args.source, args)
seeds = _collect_seeds(args)
allowed_hosts: set[str] | None = None
⋮----
allowed_hosts = {urlparse(s).netloc for s in seeds if urlparse(s).netloc}
⋮----
runner = ReferenceRunner(
only = (
n = runner.enrich_all(only=only)
web_note = f"; web pass used {len(seeds)} seed(s)" if seeds else "; web pass skipped"
`````

## File: src/reference_agent/runner.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
⋮----
log = logging.getLogger(__name__)
⋮----
_BQ_APP_NAME = "reference_agent_bq"
_WEB_APP_NAME = "reference_agent_web"
_USER_ID = "enricher"
⋮----
_COMPACT_STR_LIMIT = 120
_COMPACT_TEXT_LIMIT = 200
⋮----
def _summarize_value(value: Any, limit: int) -> str
⋮----
def _compact_args(args: dict[str, Any] | None) -> str
⋮----
parts = [
⋮----
def _compact_response(value: Any) -> str
⋮----
# Surface useful scalar fields verbatim, summarize others.
bits = []
⋮----
def _compact_text(text: str) -> str
⋮----
one_line = " · ".join(s.strip() for s in text.splitlines() if s.strip())
⋮----
def _full_json(value: Any) -> str
⋮----
def _log_event_parts(event, prefix: str, *, verbose: bool) -> str | None
⋮----
last_text: str | None = None
⋮----
fc = getattr(part, "function_call", None)
fr = getattr(part, "function_response", None)
text = getattr(part, "text", None)
⋮----
response = getattr(fr, "response", None)
⋮----
stripped = text.strip()
⋮----
last_text = text
⋮----
def _build_bq_user_message(ref: ConceptRef) -> types.Content
⋮----
text = (
⋮----
seed_lines = "\n".join(f"- {s}" for s in seeds)
allowed_lines = ", ".join(sorted(allowed_hosts)) or "(any)"
prefixes = ", ".join(allowed_path_prefixes) or "(any path)"
denied = ", ".join(denied_path_substrings) or "(none)"
⋮----
class ReferenceRunner
⋮----
def enrich_concept(self, ref: ConceptRef) -> None
⋮----
session_id = f"enrich-{uuid.uuid4().hex[:12]}"
⋮----
message = _build_bq_user_message(ref)
⋮----
def run_web_pass(self) -> None
⋮----
session_id = f"web-{uuid.uuid4().hex[:12]}"
⋮----
message = _build_web_user_message(
⋮----
def enrich_all(self, only: list[tuple[str, ...]] | None = None) -> int
⋮----
concepts = self.source.list_concepts()
⋮----
wanted = set(only)
concepts = [c for c in concepts if c.id in wanted]
missing = wanted - {c.id for c in concepts}
⋮----
count = 0
`````

## File: tests/__init__.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
`````

## File: tests/test_bigquery_source.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
⋮----
def _table_ref(table_id: str) -> SimpleNamespace
⋮----
def _build_mock_client(table_ids, table_objects_by_id)
⋮----
client = MagicMock()
⋮----
def get_table(table_ref)
⋮----
@patch("reference_agent.sources.bigquery.bigquery.Client")
def test_wildcard_sharded_tables_collapse_to_one_concept(client_cls)
⋮----
table_ids = [
table_objects = {
⋮----
src = BigQuerySource(dataset="proj.dset")
concepts = src.list_concepts()
ids = [c.id for c in concepts]
⋮----
family = next(c for c in concepts if c.id == ("tables", "events_"))
⋮----
@patch("reference_agent.sources.bigquery.bigquery.Client")
def test_sample_rows_uses_list_rows_for_table(client_cls)
⋮----
client = _build_mock_client(["users"], table_objects)
⋮----
ref = next(c for c in src.list_concepts() if c.id == ("tables", "users"))
rows = src.sample_rows(ref, n=3)
⋮----
@patch("reference_agent.sources.bigquery.bigquery.Client")
def test_sample_rows_falls_back_to_query_for_view(client_cls)
⋮----
client = _build_mock_client(["user_summary"], table_objects)
query_job = MagicMock()
⋮----
ref = next(c for c in src.list_concepts() if c.id == ("tables", "user_summary"))
rows = src.sample_rows(ref, n=4)
⋮----
sql = client.query.call_args.args[0]
⋮----
@patch("reference_agent.sources.bigquery.bigquery.Client")
def test_read_concept_returns_schema_and_partitioning(client_cls)
⋮----
table_ids = ["events_20210103"]
inner = [
schema = [
time_part = SimpleNamespace(type_="DAY", field=None, expiration_ms=None)
⋮----
family = next(c for c in src.list_concepts() if c.id == ("tables", "events_"))
⋮----
data = src.read_concept(family)
⋮----
nested = data["schema"][1]
`````

## File: tests/test_bundle_tools.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
⋮----
@pytest.fixture(autouse=True)
def _cleanup()
⋮----
def _set_ctx(tmp_path: Path) -> None
⋮----
src = MagicMock()
⋮----
def _good_frontmatter(**overrides)
⋮----
fm = {
⋮----
def _bq_body(fields: list[str]) -> str
⋮----
schema_lines = "\n".join(f"- `{f}` STRING: desc" for f in fields)
⋮----
def _sources(*ids: str) -> list[dict[str, str]]
⋮----
def test_write_succeeds_when_no_existing_doc(tmp_path)
⋮----
result = write_concept_doc(
⋮----
def test_generated_is_auto_filled(tmp_path)
⋮----
doc = OKFDocument.parse((tmp_path / "tables" / "users.md").read_text(encoding="utf-8"))
⋮----
generated = doc.frontmatter["generated"]
⋮----
def test_generated_by_and_at_are_preserved_when_supplied(tmp_path)
⋮----
def test_web_pass_rejects_schema_shrinkage(tmp_path)
⋮----
# Simulate the BQ pass having already written the doc.
⋮----
# Now enter the web pass.
⋮----
def test_web_pass_rejects_sources_shrinkage(tmp_path)
⋮----
def test_web_pass_allows_augmentation_with_new_section(tmp_path)
⋮----
augmented = (
⋮----
def test_bq_pass_can_shrink_schema_when_no_web_state(tmp_path)
⋮----
# Initial doc with three fields.
⋮----
# BQ pass re-runs (no web state) and the table evolved — legacy_col gone.
⋮----
def test_web_pass_skips_guard_for_non_bigquery_table_types(tmp_path)
⋮----
# An existing reference doc with two backtick-quoted things and two sources.
ref_body = "Prose.\n\n# Definition\nUses `field_a` and `field_b`.\n"
⋮----
# Drop both backticked identifiers and shrink sources — guard should not
# fire because the existing doc is not type=BigQuery Table.
`````

## File: tests/test_document.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
⋮----
def test_roundtrip_preserves_frontmatter_and_body()
⋮----
src = (
doc = OKFDocument.parse(src)
⋮----
serialized = doc.serialize()
reparsed = OKFDocument.parse(serialized)
⋮----
def test_parse_no_frontmatter_treats_all_as_body()
⋮----
src = "# Hello\n\nNo frontmatter here.\n"
⋮----
def test_unterminated_frontmatter_raises()
⋮----
src = "---\ntype: X\nstill in frontmatter\n"
⋮----
def test_validate_rejects_missing_type()
⋮----
doc = OKFDocument(frontmatter={"title": "Y"})
⋮----
def test_validate_accepts_type_only()
⋮----
# OKF v0.2 §11: `type` is the only always-required key.
⋮----
def test_normalize_verified_treats_bare_mapping_as_list()
⋮----
fm = {"verified": {"by": "human:ahormati", "at": "2026-06-25T09:00:00Z"}}
⋮----
def test_trust_tier()
⋮----
# A bare mapping is treated as a one-element list.
⋮----
def test_is_stale()
⋮----
ref = datetime(2026, 9, 23, 12, 0, tzinfo=timezone.utc)
⋮----
# A date-only value is ignored rather than read as midnight in whichever
# zone the consumer happens to run in.
`````

## File: tests/test_index.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
⋮----
def _stub_synth(rel: str, children: list[tuple[str, str]], *, model: str) -> str
⋮----
def _write_doc(path: Path, type_: str, title: str, description: str) -> None
⋮----
doc = OKFDocument(
⋮----
def test_regenerate_groups_by_type_and_links_relative(tmp_path: Path)
⋮----
root = tmp_path / "bundle"
⋮----
written = regenerate_indexes(root, model="stub", synthesize=_stub_synth)
written_names = {p.parent.name for p in written}
⋮----
tables_index = (root / "tables" / "index.md").read_text(encoding="utf-8")
⋮----
root_index = (root / "index.md").read_text(encoding="utf-8")
⋮----
def test_regenerate_skips_empty_directories(tmp_path: Path)
⋮----
def test_regenerate_single_child_reuses_description(tmp_path: Path)
⋮----
call_count = 0
⋮----
def counting_synth(rel: str, children, *, model: str) -> str
`````

## File: tests/test_viewer.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
⋮----
def _write(path: Path, body: str) -> None
⋮----
def _make_bundle(root: Path) -> None
⋮----
# An auto-generated index that should NOT appear as a concept node.
⋮----
def _extract_bundle_data(html: str) -> dict
⋮----
m = re.search(r"window\.BUNDLE\s*=\s*(\{.*?\});", html, re.DOTALL)
⋮----
def test_generate_visualization_writes_html(tmp_path: Path)
⋮----
bundle = tmp_path / "bundle"
⋮----
out = tmp_path / "viz.html"
stats = generate_visualization(bundle, out, bundle_name="My Bundle")
⋮----
html = out.read_text(encoding="utf-8")
⋮----
def test_index_md_is_not_a_concept(tmp_path: Path)
⋮----
data = _extract_bundle_data(out.read_text(encoding="utf-8"))
ids = {n["data"]["id"] for n in data["nodes"]}
⋮----
def test_cross_links_become_edges(tmp_path: Path)
⋮----
pairs = {(e["data"]["source"], e["data"]["target"]) for e in data["edges"]}
⋮----
def test_missing_link_targets_are_skipped(tmp_path: Path)
⋮----
def test_node_colors_match_palette(tmp_path: Path)
⋮----
by_id = {n["data"]["id"]: n["data"] for n in data["nodes"]}
⋮----
def test_v02_signals_appear_in_graph_payload(tmp_path: Path)
⋮----
users = {n["data"]["id"]: n["data"] for n in data["nodes"]}["tables/users"]
⋮----
# Both a process and a human attestation → human-reviewed tier.
⋮----
# stale_after is in the past → stale.
⋮----
def test_raises_when_bundle_missing(tmp_path: Path)
`````

## File: tests/test_web_fetcher.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
⋮----
def _mock_response(body: bytes, content_type: str = "text/html; charset=utf-8", url: str = "https://example.com/page")
⋮----
resp = MagicMock()
⋮----
def test_fetch_and_parse_extracts_title_links_markdown()
⋮----
html = b"""
⋮----
page = fetch_and_parse("https://example.com/page")
⋮----
def test_fetch_and_parse_rejects_non_html()
⋮----
def test_fetch_and_parse_truncates_large_pages()
⋮----
big_text = "<p>" + ("x" * 200_000) + "</p>"
html = f"<html><head><title>big</title></head><body>{big_text}</body></html>".encode()
⋮----
page = fetch_and_parse("https://example.com/big")
⋮----
def test_fetch_and_parse_wraps_network_errors()
`````

## File: tests/test_web_tools.py
`````python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
⋮----
#      http://www.apache.org/licenses/LICENSE-2.0
⋮----
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
⋮----
@pytest.fixture(autouse=True)
def _cleanup()
⋮----
def _set_state(**overrides)
⋮----
defaults = dict(
⋮----
def _page(url: str, links: list[str] | None = None) -> Page
⋮----
def test_seed_fetch_succeeds_and_records_link_depth()
⋮----
result = fetch_url("https://docs.example.com/docs/intro")
⋮----
# The followed link is now reachable at depth 1.
⋮----
def test_allowed_path_prefix_rejects_off_path_urls()
⋮----
result = fetch_url("https://docs.example.com/blog/post")
⋮----
def test_denied_path_substring_rejects()
⋮----
result = fetch_url("https://docs.example.com/login")
⋮----
def test_max_depth_caps_recursion()
⋮----
# depth 0 (seed): ok
r0 = fetch_url("https://docs.example.com/a")
⋮----
# depth 1: ok (== max_depth)
r1 = fetch_url("https://docs.example.com/b")
⋮----
# depth 2: rejected (> max_depth=1)
r2 = fetch_url("https://docs.example.com/c")
⋮----
def test_unregistered_url_rejected()
⋮----
# Agent invents a URL that was never returned as a link.
result = fetch_url("https://docs.example.com/docs/random")
`````

## File: .gitignore
`````
.venv/
__pycache__/
*.pyc
*.pyo
.pytest_cache/
.mypy_cache/
*.egg-info/
build/
dist/
.DS_Store
.env
.claude/
`````

## File: CONTRIBUTING.md
`````markdown
# Contributing

Thanks for your interest in contributing to the Open Knowledge Format (OKF)!

Contributions generally fall into two categories, and they are reviewed
differently:

- **The format itself** ([`SPEC.md`](SPEC.md)) — OKF aims to be a universal,
  vendor-neutral format, so spec changes are held to a higher bar. Open an
  issue describing the problem and the proposed change before sending a pull
  request, so the design can be discussed first.
- **The reference agent, viewer, samples, and bundles** — proof-of-concept
  tooling that demonstrates producing and consuming OKF. Ordinary pull
  requests are welcome.

To get started contributing:

1. Sign a Contributor License Agreement (see details below).
1. Fork the repo, develop and test your code changes.
1. Ensure that your code adheres to the existing style.
1. Ensure that your code has an appropriate set of unit tests which all pass.
1. Ensure that all tests pass by running `.venv/bin/pytest` (see
   [README.md](README.md) for environment setup).
1. Submit a pull request.

## Contributor License Agreement

Contributions to this project must be accompanied by a Contributor License
Agreement. You (or your employer) retain the copyright to your contribution;
this simply gives us permission to use and redistribute your contributions as
part of the project. Head over to <https://cla.developers.google.com/> to see
your current agreements on file or to sign a new one.

You generally only need to submit a CLA once, so if you've already submitted one
(even if it was for a different project), you probably don't need to do it
again.

## Code reviews

All submissions, including submissions by project members, require review. We
use GitHub pull requests for this purpose. Consult
[GitHub Help](https://help.github.com/articles/about-pull-requests/) for more
information on using pull requests.
`````

## File: pyproject.toml
`````toml
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "reference-agent"
version = "0.1.0"
description = "Reference agent that produces Open Knowledge Format bundles"
requires-python = ">=3.11"
dependencies = [
    "google-adk>=2.0",
    "google-cloud-bigquery>=3.20",
    "pyyaml>=6.0",
    "pydantic>=2.0",
    "markdownify>=0.11",
]

[project.optional-dependencies]
dev = ["pytest>=7.0"]

[project.scripts]
reference-agent = "reference_agent.cli:main"

[tool.setuptools.packages.find]
where = ["src"]

[tool.setuptools.package-data]
reference_agent = ["prompts/*.md", "viewer/templates/*.html", "viewer/static/*"]

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]
`````

## File: README.md
`````markdown
# Open Knowledge Format (OKF)

### 📖 [Read the Open Knowledge Format v0.2 specification → SPEC.md](SPEC.md)

> **This repository is primarily about the [Open Knowledge Format
> (OKF)](SPEC.md).**
>
> OKF is a **universal, vendor-neutral format** for representing knowledge
> as plain markdown files with YAML frontmatter. It is **not tied to any
> particular agent, framework, model provider, or serving system**. The
> goal is simple:
>
> - **Anyone can produce** OKF — humans authoring by hand, agents built on
>   any framework (Google ADK, LangChain, custom), export pipelines from
>   existing catalogs (Dataplex, Unity Catalog, Collibra, …), or scripts
>   walking a database.
> - **Anyone can serve and consume** OKF — a static file server, a
>   knowledge-management UI (Obsidian, Notion, MkDocs), an LLM loading
>   files into context, a search index, or a graph viewer like the one
>   bundled in this repo.
>
> The agent below is a **proof of concept** demonstrating *one* way to
> produce OKF bundles automatically. The format itself is the
> contribution; this agent and the visualizer exist to make the format
> tangible at both ends — production and consumption.
>
> **See OKF in practice** — three ready-to-browse bundles produced by this
> agent, checked into [`bundles/`](bundles/):
>
> - [`bundles/ga4/`](bundles/ga4/) — GA4 e-commerce dataset
>   ([viz.html](bundles/ga4/viz.html))
> - [`bundles/stackoverflow/`](bundles/stackoverflow/) — Stack Overflow
>   public dataset ([viz.html](bundles/stackoverflow/viz.html))
> - [`bundles/crypto_bitcoin/`](bundles/crypto_bitcoin/) — Bitcoin
>   blocks/transactions ([viz.html](bundles/crypto_bitcoin/viz.html))
> - [`bundles/acme_retail/`](bundles/acme_retail/) — Acme Retail
>   ([viz.html](bundles/acme_retail/viz.html))

## Why OKF?

OKF represents catalog knowledge as plain markdown files with YAML
frontmatter, organized in a directory hierarchy. That choice unlocks a few
properties that are hard to get from a service-owned metadata store:

- **Human- and agent-readable.** No SDK or query language stands between a
  reader and the content. An engineer can `cat` a concept; an LLM can ingest
  it verbatim into context.
- **Version-controllable out of the box.** Bundles live in git. Pull
  requests, line-by-line diffs, blame, and review workflows just work —
  knowledge curation becomes a normal software-engineering activity.
- **Portable and lock-in free.** A bundle is a directory. Ship it as a
  tarball, host it in any repo, mount it from any filesystem, or sync it to
  any system that speaks files. No proprietary API stands between you and
  your metadata.
- **Mixes structured and unstructured data deliberately.** Use frontmatter
  for the few fields you want to query, filter, or index on (`type`,
  `resource`, `tags`, `generated`, `status`); use the markdown body for the
  prose, schemas, and example queries that LLMs and humans actually read.
- **Trust, provenance, and freshness are first-class.** v0.2 puts queryable
  signals in frontmatter — where a concept came from (`sources` with per-source
  credibility signals), who produced and confirmed it (`generated`, `verified`,
  from which consumers derive a trust tier), and whether it is still current
  (`status`, `stale_after`) — so an agent-maintained corpus stays trustable
  without any bespoke runtime.
- **Minimally opinionated, freely extensible.** A small set of required
  keys ensures interoperability, but bundles can carry arbitrary extra
  frontmatter keys and arbitrary body sections without breaking
  consumers.
- **Composes with existing tooling.** Many knowledge tools — Notion,
  Obsidian, MkDocs, Hugo, Jekyll — already speak markdown plus YAML
  frontmatter, so bundles can be browsed, edited, or rendered without
  custom UI.
- **Progressive disclosure built in.** Auto-generated `index.md` files
  let an agent or human navigate the hierarchy one level at a time
  instead of loading the entire bundle into context.
- **Graph-shaped, not just tree-shaped.** Concepts link to each other via
  normal markdown links, expressing relationships richer than the
  parent/child implied by the directory layout.

The net effect is that reference agents, consumption agents, and humans
collaborate on the same artifacts in the same way they already collaborate
on source code.

## Install

```
python3.13 -m venv .venv
.venv/bin/pip install --index-url https://pypi.org/simple/ -e .[dev]
```

## Credentials

- BigQuery: `gcloud auth application-default login` plus a project for billing
  (`gcloud config set project <id>`). Public datasets are readable, but the
  caller's project is billed for query bytes.
- Gemini: set `GEMINI_API_KEY` (AI Studio) **or** use Vertex AI by setting
  `GOOGLE_GENAI_USE_VERTEXAI=true`, `GOOGLE_CLOUD_PROJECT=<id>`, and
  `GOOGLE_CLOUD_LOCATION=<region>`.

## How the reference agent works

The reference agent runs in two passes. The **BQ pass** writes one OKF
doc per concept the source advertises, using BigQuery metadata alone.
The **web pass** then runs the LLM as its own crawler: it receives a
list of seed URLs (provided via `--web-seed` or `--web-seed-file`),
fetches the seeds via the `fetch_url` tool, and decides which outbound
links are worth following based on whether they look like authoritative
documentation for the existing concepts. For each page it fetches, the
agent chooses to (a) enrich one or more existing concept docs, (b) mint
a standalone `references/<slug>` doc, or (c) skip. A hard
`--web-max-pages` cap and a same-domain allowed-hosts filter
(configurable via `--web-allowed-host`) are enforced inside the tool,
so the agent cannot overrun. Use `--no-web` to skip the web pass.

## Run

Minimum invocation — point at a BigQuery dataset and a bundle output
directory. Seeds for the web pass are explicit; omit them (or pass
`--no-web`) to run BQ-only:

```
.venv/bin/python -m reference_agent enrich \
    --source bq \
    --dataset <project>.<dataset> \
    --web-seed-file <path/to/seeds.txt> \
    --out ./bundles/<name>
```

Iterate on a single concept by adding `--concept <type>/<name>` (e.g.
`--concept tables/events_`); repeatable.

## Samples

Each sample pairs a **recipe** (`samples/<name>/`, with the seed URLs and
exact `enrich` command) with the **produced bundle** (`bundles/<name>/`)
that the recipe generated. Open the recipe to reproduce; open the bundle
to browse the result directly.

- **GA4 Google Merchandise Store** — public e-commerce dataset, seeded
  with canonical GA4 BigQuery Export documentation URLs.
  · [recipe](samples/ga4_merch_store/README.md)
  · [bundle](bundles/ga4/)
  · [viz.html](bundles/ga4/viz.html)
- **Stack Overflow** — public dataset (mirror of the Stack Exchange Data
  Dump), seeded with the community's canonical schema references.
  Exercises multi-concept enrichment from cross-cutting docs pages.
  · [recipe](samples/stackoverflow/README.md)
  · [bundle](bundles/stackoverflow/)
  · [viz.html](bundles/stackoverflow/viz.html)
- **Bitcoin (crypto)** — public dataset (blocks, transactions, inputs,
  outputs) from the `bitcoin-etl` pipeline. Exercises cross-table
  foreign-key relationships in prose.
  · [recipe](samples/crypto_bitcoin/README.md)
  · [bundle](bundles/crypto_bitcoin/)
  · [viz.html](bundles/crypto_bitcoin/viz.html)

## Visualize

The `visualize` subcommand renders any OKF bundle as a **self-contained
interactive HTML file** — one file, no backend, no install on the
viewing side. Open it in any modern browser, share it as an artifact,
host it on a static file server, or commit it next to the bundle (as
this repo does).

The viewer is itself a proof-of-concept *consumer* of OKF, mirroring
the way the reference agent is a proof-of-concept *producer*. OKF
bundles can be consumed by anything that reads markdown; this is just
one shape.

### What it shows

- A **force-directed graph** of every concept in the bundle, with
  colored nodes by type (datasets, tables, references, …) and directed
  edges drawn from each cross-link in the markdown bodies.
- A **detail panel** for the selected concept showing its frontmatter
  (description, resource link, tags) and its rendered markdown body —
  with internal `[…](/path/to/concept.md)` links rewired to navigate
  within the viewer instead of following the path.
- A **"Cited by" backlinks** list under each concept (computed from the
  reverse of the link graph).
- A **search box** (matches title, concept id, and tags), a **type
  filter**, and switchable graph layouts (cose / concentric /
  breadth-first / circle / grid).

### Generate

```
.venv/bin/python -m reference_agent visualize --bundle ./bundles/<name>
```

That writes `bundles/<name>/viz.html`. Flags:

| Flag           | Default                | Description                                 |
|----------------|------------------------|---------------------------------------------|
| `--bundle`     | *(required)*           | Bundle root directory.                      |
| `--out`        | `<bundle>/viz.html`    | Output HTML path.                           |
| `--name`       | bundle directory name  | Display name shown in the viewer header.    |

Example, writing the output somewhere else and overriding the header:

```
.venv/bin/python -m reference_agent visualize \
    --bundle ./bundles/crypto_bitcoin \
    --out /tmp/btc.html \
    --name "Bitcoin OKF"
```

### How it's built

The HTML embeds the bundle as a JSON blob and uses
[Cytoscape.js](https://js.cytoscape.org/) for the graph and
[marked](https://marked.js.org/) for in-browser markdown rendering,
both loaded from a CDN. No data leaves the page; the bundle is parsed
once at generation time and serialized into the file.

## Tests

```
.venv/bin/pytest
```
`````

## File: SPEC.md
`````markdown
# Open Knowledge Format (OKF)

**Version 0.2**

OKF is an open, human- and agent-friendly format for representing
*knowledge*: the metadata, context, and curated insight that surrounds
data and systems. It is designed to be authored by people, generated by
agents, exchanged across organizations, and consumed by both.

The format is intentionally minimal: a directory of markdown files with
YAML frontmatter. There is no schema registry, no central authority, and
no required tooling. If you can `cat` a file, you can read OKF; if you
can `git clone` a repo, you can ship it.

This document is self-contained: it specifies everything needed to
produce and consume OKF v0.2. A summary of what changed from v0.1 is in
§13.

---

## 1. Motivation

The space of knowledge representation for AI agents is evolving quickly,
and many incompatible conventions are emerging. OKF takes the position
that knowledge is best represented in commonly accessible, established
formats that are:

- **Readable** by humans without tooling.
- **Parseable** by agents without bespoke SDKs.
- **Diffable** in version control.
- **Portable** across tools, organizations, and time.

Increasingly, a knowledge corpus is not authored once and then read: it
is **continuously written and maintained by agents**. When most concepts
are machine-generated, a consumer needs answers that a plain
markdown-plus-frontmatter convention does not make first-class:

1. What was this created from, and how was it verified? (**provenance**)
2. How much should I trust it? (**trust**)
3. Is it still true? (**freshness**)
4. Is it the current version? (**lifecycle**)
5. Was this number produced the way we said it must be? (**attestation**)

OKF v0.2 makes provenance, trust, lifecycle, and attestation first-class
while keeping the format minimally opinionated. The format is minimally
opinionated. It standardizes only the small set of structural conventions
needed to make a knowledge corpus self-describing — anything beyond that
is left to the producer.

### Goals

1. Define a universal format that **producers** (people, agents, export
   pipelines) can write into.
2. Inform how **consumers** (agents, UIs, search indexes, deterministic
   code) should read and traverse it.
3. Facilitate **exchange** of knowledge across systems and organizations.
4. Standardize the small set of frontmatter fields that make an
   agent-maintained corpus **trustable**, without prescribing any runtime.

### Non-goals

- Defining a fixed taxonomy of concept types.
- Prescribing storage, serving, or query infrastructure.
- Replacing domain-specific schemas (Avro, Protobuf, OpenAPI, and so on).
  OKF *references* them; it does not subsume them.
- Specifying a packaging or invocation standard for the code an executor
  or attester points at. OKF fixes the interface, not the packaging.

---

## 2. Terminology

- **Knowledge Bundle** (or **bundle**): A self-contained, hierarchical
  collection of knowledge documents. The unit of distribution.
- **Concept**: A single unit of knowledge within a bundle, represented as
  one markdown document. It may describe a tangible asset (a table, an
  API), an abstract idea (a metric, a business process), or anything in
  between.
- **Concept ID**: The path of the concept's file within the bundle, with
  the `.md` suffix removed.
- **Frontmatter**: A YAML metadata block delimited by `---` at the top of
  a markdown file.
- **Body**: Everything in the file after the frontmatter.
- **Link**: A standard markdown link from one concept to another, used to
  express relationships beyond the implicit parent/child hierarchy.
- **Source**: A material a concept derives from, external or internal to
  the bundle, recorded in the `sources` frontmatter field.
- **Provenance**: The set of sources a concept derives from.
- **Credibility signal**: An objective, per-source fact (`author`,
  `usage_count`, `last_modified`) used to infer trust; OKF records the
  signals, not a verdict (see §5.1).
- **Actor**: A string identifying who or what performed an action, using
  the convention `<producer>/<version>` for agents, `human:<id>` for
  people, and `process:<id>` for automated processes (see §7).
- **Trust tier**: A level derived from a concept's `verified` field:
  unverified, machine-confirmed, or human-reviewed (see §5.3).
- **Attested Computation**: A concept (`type: Attested Computation`)
  carrying a sanctioned way to compute a value, so a consumer can confirm
  the value was produced by running it (see §10).
- **Executor**: Run instructions or code that executes a computation and
  returns a receipt (see §10.2).
- **Receipt**: The evidence a run returns, shaped by `executor.receipt`; a
  runtime artifact, not stored in the bundle (see §10).
- **Attester**: Deterministic (no-LLM) code that inspects a receipt and
  returns a verdict (see §10.2).

---

## 3. Bundle structure

A bundle is a directory tree of markdown files. The directory structure
is independent of the domain: producers organize concepts however makes
sense for the knowledge being captured.

```
path/to/bundle/
  index.md                      # Optional. Directory listing for progressive disclosure.
  log.md                        # Optional. Chronological history of updates.
  <concept>.md                  # A concept at the bundle root.
  <subdirectory>/               # Subdirectories organize concepts into groups.
    index.md
    <concept>.md
    <subdirectory>/
      ...
```

A bundle MAY be distributed as:

- A git repository (recommended, since it provides history, attribution,
  and diffs).
- A tarball or zip archive of the directory.
- A subdirectory within a larger repository.

### 3.1 Reserved filenames

The following filenames have defined meaning at any level of the
hierarchy and MUST NOT be used for concept documents:

| Filename   | Purpose                          |
|------------|----------------------------------|
| `index.md` | Directory listing. See §8.       |
| `log.md`   | Update history. See §9.          |

All other `.md` files are concept documents.

Tags remain a first-class concept through the `tags` frontmatter field
(§4.1). OKF does not specify a separate file format for aggregating
documents by tag; a consumer that wants a tag-browsing view can
synthesize one at consumption time by scanning frontmatter.

---

## 4. Concept documents

Every concept is a UTF-8 markdown file with two parts:

1. A **YAML frontmatter block**, delimited by `---` on its own line at the
   start of the file and a closing `---` on its own line.
2. A **markdown body**, containing free-form content.

### 4.1 Frontmatter

```yaml
---
type: <Type name>                  # REQUIRED
title: <Optional display name>
description: <Optional one-line summary>
resource: <Optional canonical URI for the underlying asset>
tags: [<tag>, <tag>, ...]          # Optional
# ... trust, lifecycle, provenance, and computation families (see §5, §10)
# ... other producer-defined key/value pairs
---
```

**Required:**

- `type`: A short string identifying the kind of concept. Consumers use it
  for routing, filtering, and presentation. Example values:
  `BigQuery Table`, `BigQuery Dataset`, `API Endpoint`, `Metric`,
  `Playbook`, `Reference`, `Attested Computation`.

  Type values are **not** registered centrally. Producers SHOULD pick
  values that are descriptive and self-explanatory; consumers MUST
  tolerate unknown types gracefully, typically by treating them as generic
  concepts.

`type` is the only always-required key; a concept carrying just `type` is
fully conformant (§11).

**Recommended:**

- `title`: Human-readable display name. If omitted, consumers MAY derive a
  title from the filename.
- `description`: A single sentence summarizing the concept. Used by
  `index.md` generators, search snippets, and previews.
- `resource`: A URI that uniquely identifies the underlying asset the
  concept describes. Absent for concepts that describe abstract ideas
  rather than physical resources.
- `tags`: A YAML list of short strings for cross-cutting categorization.

The optional **provenance**, **trust**, and **lifecycle** families (§5) and
the **computation** fields for Attested Computation concepts (§10) may also
appear.

**Extensions:** Producers MAY include any additional keys. Consumers
SHOULD preserve unknown keys when round-tripping and MUST NOT reject
documents with unrecognized fields.

### 4.2 Body

The body is standard markdown. Producers SHOULD favor structural markdown
(headings, lists, tables, fenced code blocks) over freeform prose, since
structure aids both human reading and agent retrieval.

There are no required body sections. The following headings have
**conventional** meaning and SHOULD be used when applicable:

| Heading         | Purpose                                                |
|-----------------|--------------------------------------------------------|
| `# Schema`      | Structured description of an asset's columns/fields.   |
| `# Examples`    | Concrete usage examples, often as fenced code blocks.  |
| `# Computation` | The sanctioned computation of an Attested Computation. See §10. |

Per-claim attribution to external sources uses markdown footnotes keyed to
`sources` entries rather than a body citations list (§5.1).

### 4.3 Example: a concept bound to a resource

```markdown
---
type: BigQuery Table
title: Customer Orders
description: One row per completed customer order across all channels.
resource: https://console.cloud.google.com/bigquery?p=acme&d=sales&t=orders
tags: [sales, orders, revenue]
generated: { by: reference_agent/gemini-2.5-pro, at: 2026-05-28T14:30:00Z }
---

# Schema

| Column        | Type      | Description                              |
|---------------|-----------|------------------------------------------|
| `order_id`    | STRING    | Globally unique order identifier.        |
| `customer_id` | STRING    | Foreign key into [customers](/tables/customers.md). |
| `total_usd`   | NUMERIC   | Order total in US dollars.               |
| `placed_at`   | TIMESTAMP | When the customer submitted the order.   |

# Joins

Joined with [customers](/tables/customers.md) on `customer_id`.
```

### 4.4 Example: a concept not bound to a resource

```markdown
---
type: Playbook
title: "Incident response: data freshness alert"
description: Steps to triage a freshness alert on the orders pipeline.
tags: [oncall, incident]
generated: { by: human:ahormati, at: 2026-04-12T09:00:00Z }
---

# Trigger

A freshness alert fires when `orders` lags more than 30 minutes behind its
expected SLA. See the [orders table](/tables/orders.md).

# Steps

1. Check the [ingestion job dashboard](https://example.com/dash).
2. ...
```

---

## 5. Provenance, trust, and lifecycle

These frontmatter families make "where did this come from," "how much
should I trust it," and "is it still current" answerable from frontmatter.
All are optional. Their absence carries meaning: an unverified concept is
distinguishable from a verified one, but is never rejected (§11).

Every timestamp-valued key in OKF is an ISO 8601 datetime with an explicit
UTC offset, for example `2026-06-30T14:00:00Z`.

### 5.1 Provenance: `sources`

`sources` records the materials a concept derives from, external or
internal to the bundle.

```yaml
sources:
  - id: ga4-schema
    resource: https://developers.google.com/analytics/bigquery/export-schema
    title: GA4 BigQuery Export schema
    author: team:ga4-docs
    usage_count: 5000
    last_modified: 2026-05-30T00:00:00Z
usage_window: { from: 2026-06-01T00:00:00Z, to: 2026-06-30T00:00:00Z }
```

Each `sources` entry:

- `resource`: REQUIRED within an entry. Names either a concrete artifact a
  consumer can follow (an absolute URL, a bundle-relative path, or a path
  into a `references/` subdirectory, §6) or a population or scope descriptor
  it cannot (for example `all queries in BigQuery project X`).
- `id`: Optional. A stable key used to attribute individual claims (see
  below). SHOULD be present when the body cites the source.
- `title`: Optional. Human-readable label for the source.
- The optional credibility signals `author`, `usage_count`, and
  `last_modified`, described next.

**Source credibility signals.** OKF records objective, per-source signals
so a consumer can judge how much to trust a concept by judging the sources
it was extracted from. It does not store a credibility score: a score is
subjective, unportable across consumers, and goes stale. Credibility is
*inferred* from the signals, the same way trust tiers are (§5.3), not
stored. Each signal is optional and lives on a `sources` entry:

- `author`: Who or what produced the source, in the actor convention (§7).
  An authority signal.
- `usage_count`: How often `resource` was exercised (dashboard views, query
  executions, page reads) over `usage_window`. An adoption and liveness
  signal. For a single artifact it is that artifact's own exercise count;
  for a scope descriptor it is the number of exercises within the scope that
  touch the concept.
- `last_modified`: When the source itself last changed. A recency signal,
  distinct from `generated.at` (§5.2), which records when the concept was
  written.
- `usage_window`: Written once as a sibling of `sources`, it frames every
  `usage_count` with a `{ from, to }` datetime range. A single entry MAY
  carry its own `usage_window` to override the shared one.

`usage_count` is a coarse signal. It is comparable at the
alive-versus-dead and order-of-magnitude level, and against a source's own
history over time, but not as a precise cross-kind ranking: a scheduled
query's executions and a human's deliberate dashboard views do not carry
equal weight. Consumers SHOULD read it as liveness and trend, not as a
score.

Lineage is expressed through links, not a dedicated field. When a
`resource` points at another OKF concept, the derivation edge already
exists in the bundle graph (§6), so a consumer MAY recurse into that
source's own `sources` and let credibility propagate. External leaf sources
carry only their intrinsic signals. Deeper lineage (an explicit external
`derived_from`, or data lineage) is out of scope for v0.2.

**Per-claim attribution.** To attribute a specific claim, use a markdown
footnote whose label is a `sources[].id`:

```markdown
The `events_` table is sharded daily as `events_YYYYMMDD`.[^ga4-schema]

[^ga4-schema]: GA4 BigQuery Export schema
```

The footnote label is the join key into `sources`; consumers resolve
attribution through the matching entry, not by parsing the footnote prose.
Labels are keyed rather than positional (`sources[0]`) because agents
constantly rewrite these documents: a positional index misattributes
silently the moment the list is reordered, whereas a stable `id` survives
reordering.

### 5.2 Trust: `generated` and `verified`

`generated` records how the current content was produced. `verified`
records who or what has confirmed the content against its sources or
`resource`. They are kept distinct because who *wrote* a concept need not
be who *confirmed* it.

```yaml
generated: { by: reference_agent/gemini-2.5-pro, at: 2026-06-20T22:53:05Z }
```

- `generated.by`: REQUIRED within `generated`. An actor (§7).
- `generated.at`: An ISO 8601 datetime marking the content's last
  meaningful change. Consumers use it to tell a recent edit from a stale
  fact.

```yaml
verified:
  - { by: human:ahormati, at: 2026-06-25T09:00:00Z }
  - { by: process:finance-nightly, at: 2026-06-26T02:00:00Z }
```

- `verified`: A list of verification events, each with `by` (an actor) and
  `at` (an ISO 8601 datetime). Multiple entries capture independent
  checks, for example a human sign-off plus a nightly process. "How
  recently" is the latest `at`.
- `verified` is independent of `generated.at`: content can change without
  re-confirmation, and facts can be re-confirmed without regeneration.
- A single verifier MAY be written as one `{ by, at }` mapping without the
  list dash. Consumers MUST treat a bare mapping as a one-element list:

```yaml
verified: { by: human:ahormati, at: 2026-06-25T09:00:00Z }
```

### 5.3 Trust tiers

Consumers derive a trust tier from `verified`, lowest to highest:

- No `verified` key ⇒ **unverified**.
- `verified` by non-`human:` actors only ⇒ **machine-confirmed**.
- `verified` by a `human:<id>` actor ⇒ **human-reviewed**.

A concept with no trust frontmatter is still consumable; consumers MUST
NOT reject it (§11). Trust tiers are advisory signals, not access control.

### 5.4 Lifecycle: `status`

```yaml
status: stable        # draft | stable | deprecated
```

- `draft`: not yet reviewed; possibly incomplete.
- `stable`: default; ready for consumption.
- `deprecated`: kept for links and history; no longer current.

Absent `status` ⇒ `stable`.

### 5.5 Lifecycle: `stale_after`

```yaml
stale_after: 2026-09-23T00:00:00Z   # content is stale on/after this instant
```

Optional. An absolute instant. A concept is stale when
`now >= stale_after`. An absolute instant, not a relative TTL, keeps the
staleness decision a plain comparison with no reference to when the
concept was read.

---

## 6. Cross-linking and paths

### 6.1 Links between concepts

Concepts MAY link to other concepts using standard markdown links. Two
forms are supported:

- **Absolute (bundle-relative):** begins with `/`, interpreted relative to
  the bundle root. This is the **recommended** form because it is stable
  when documents are moved within their subdirectory.

  ```markdown
  See the [customers table](/tables/customers.md) for the join key.
  ```

- **Relative:** a standard markdown relative path.

  ```markdown
  See the [neighboring concept](./other.md).
  ```

A link from concept A to concept B asserts a *relationship*. The specific
kind (parent/child, references, joins-with, depends-on) is conveyed by the
surrounding prose, not by the link itself. Consumers that build a graph
view typically treat all links as directed edges of an untyped
relationship.

Consumers MUST tolerate broken links: a link whose target does not exist
in the bundle is not malformed; it may simply represent not-yet-written
knowledge.

### 6.2 Path-valued fields

Several fields name a path or URI: `resource`, `sources[].resource`,
`computation`, `executor.resource`, and `attester.resource` (§10). A
`sources[].resource` may instead be a scope descriptor (§5.1), in which
case it is not a path. Each path-valued field accepts:

- an absolute URL (for example `https://...`),
- a bundle-relative path beginning with `/`, or
- a relative path (for example `../computations/revenue.md`).

### 6.3 The `references/` convention

A `references/` subdirectory conventionally mirrors external material, run
instructions, or code as first-class concepts within the bundle. Sources,
executors, and attesters commonly point into it (for example
`references/attesters/revenue.py`). It is a naming convention, not a
requirement.

---

## 7. Actor convention

Fields that record an identity (`generated.by`, `verified[].by`) use a
single actor convention:

- `<producer>/<version>` for agents and tools, for example
  `reference_agent/gemini-2.5-pro`.
- `human:<id>` for a person, for example `human:ahormati`.
- `process:<id>` for an automated process, for example
  `process:finance-nightly`.

Consumers that classify trust (§5.3) key off the `human:` prefix, so
producers MUST use it for hand-authored or human-confirmed content.

---

## 8. Index files

An `index.md` file MAY appear in any directory, including the bundle root.
It enumerates the directory's contents to support **progressive
disclosure**: letting a human or agent see what is available before
opening individual documents.

Index files contain no frontmatter, with one exception: a bundle-root
`index.md` MAY carry an `okf_version` key (§12). The body uses one or more
sections, each grouping concepts under a heading:

```markdown
# Section / Group Heading

* [Title 1](relative-url-1) - short description of item 1
* [Title 2](relative-url-2) - short description of item 2

# Another Section

* [Subdirectory](subdir/) - short description of the subdirectory
```

Entries SHOULD include the description from the linked concept's
frontmatter. Producers MAY generate `index.md` automatically; consumers
MAY synthesize one on the fly when none is present.

---

## 9. Log files

A `log.md` file MAY appear at any level of the hierarchy to record the
history of changes to that scope. The format is a flat list of
date-grouped entries, newest first:

```markdown
# Directory Update Log

## 2026-05-22
* **Update**: Added a BigQuery table reference for [Customer Metrics](/tables/customer-metrics.md).
* **Creation**: Established the [Dataplex Playbook](/playbooks/dataplex.md).

## 2026-05-15
* **Initialization**: Created foundational directory structure.
```

Date headings MUST use ISO 8601 `YYYY-MM-DD` form. Log entries are prose;
the leading bold word (`**Update**`, `**Creation**`, `**Deprecation**`) is
a convention, not a requirement.

---

## 10. Attested computations concept

An Attested Computation concept carries not just what a value *means* but a
sanctioned way to *compute* it, so a consumer can confirm the agent ran the
blessed computation instead of improvising its own. Provenance (§5.1)
answers "where did this claim come from"; attestation answers "was this
number produced the way we said it must be." OKF records the computation
and the means to check it; it does not execute anything itself.

### 10.1 A computation is its own concept

A sanctioned computation is a standalone concept of
`type: Attested Computation`. A concept that needs the value (a `Metric`, a
`BigQuery Table`) links to it with a normal markdown link (§6). Three
properties motivate the standalone concept:

- **`runtime` defines what `parameters` mean.** A parameter is a SQL bind
  variable, a dbt var, or a Python argument depending on the runtime.
  Keeping `runtime` and `parameters` in one frontmatter makes the binding
  semantics self-evident.
- **One computation, many consumers.** The same computation can back a
  metric, a dashboard concept, and a report; as a concept it is referenced
  once and reused.
- **Trust state is per computation.** `verified`, `stale_after`, and a
  single `attester` describe one thing. Revenue, profit, and margin each
  verify and attest independently, which is three concepts, not three
  entries in one frontmatter.

### 10.2 Contract fields

The contract is the concept's top-level frontmatter. In addition to the
provenance, trust, and lifecycle families (§5), an Attested Computation
concept carries:

- `runtime`: REQUIRED for this type. The single field that says how to run
  the computation, and so how the executor and attester interpret it and
  what `parameters` mean. Example values: `bigquery`, `postgres`, `dbt`,
  `python`, `Looker`.
- `parameters`: A list of the typed, named holes the agent may fill. Each
  entry: `{ name, type, required }`. Binding semantics follow `runtime`.
- `computation`: Optional. A path (§6.2) to a file holding the
  computation, used instead of an inline body fence (see §10.3). Absent ⇒
  the body `# Computation` fence is the computation.
- `executor`: How the computation is run. `resource` names run
  instructions or code; a runner (an agent, or deterministic consumer
  code) follows it. `receipt` declares the fields a run must return, the
  evidence the attester inspects (for example a BigQuery `job_id` and the
  SQL the job actually executed).
- `attester`: The deterministic check. `resource` names code (no LLM) that
  takes a receipt and returns a verdict. It is meant to run consumer-side.

What sits behind a `resource` (a Skill, a script, a container) is a
packaging choice; OKF fixes the interface, not the packaging (§1).

```markdown
---
type: Attested Computation
title: Revenue for fiscal year
description: Recognized revenue for a fiscal year, per Finance's definition.
status: stable
runtime: bigquery
parameters:
  - { name: year, type: integer, required: true }
executor:
  resource: references/skills/run-on-bq.md
  receipt: [job_id, executed_sql, result]
attester:
  resource: references/attesters/revenue.py
generated: { by: reference_agent/gemini-2.5-pro, at: 2026-06-20T22:53:05Z }
verified: { by: human:ahormati, at: 2026-06-25T09:00:00Z }
stale_after: 2026-09-23T00:00:00Z
sources:
  - id: rev-policy
    resource: https://wiki.acme/finance/revenue-recognition
    title: Revenue recognition policy
---

# Computation

    SELECT SUM(amount) AS revenue
    FROM finance.recognized_revenue
    WHERE fiscal_year = @year

The computation binds only the declared `parameters`, per the recognition
policy.[^rev-policy]

[^rev-policy]: Revenue recognition policy
```

### 10.3 The computation

Provide the computation in one of two ways:

- **Inline:** a single fenced code block in the body under `# Computation`.
  Best for a short computation reviewed alongside the contract.
- **File:** set `computation` to a path (§6.2) and omit the body fence.
  Best for a long or generated computation, or one already kept as a real
  file shared with non-OKF tooling.

```yaml
runtime: bigquery
computation: references/computations/lib/revenue.sql
parameters:
  - { name: year, type: integer, required: true }
```

The agent MAY only supply *values* for the declared `parameters`; it MUST
NOT author or edit the computation. Binding `computation` with the
parameter values into the executable artifact is the consumer's job, and
the attester independently re-derives that same binding to compare against
what actually ran. Because the comparison is on the expanded, compiled
artifact the receipt carries (`executed_sql`, `compiled_sql`), a rewritten
query, a swapped computation file, or a mutated dependency fails the check.
A typed, parameter-only surface is what makes "did the sanctioned thing
run" a mechanical comparison rather than a judgement call.

### 10.4 Concepts that use a computation

A document is rarely a single computation. An income-statement overview
that discusses revenue, profit, and margin stays one readable concept and
links to one Attested Computation per figure:

```markdown
---
type: Metric
title: Revenue
description: Recognized revenue for a fiscal year.
tags: [finance, revenue]
status: stable
generated: { by: reference_agent/gemini-2.5-pro, at: 2026-06-20T22:53:05Z }
---

# Definition

Recognized revenue sums `amount` over rows booked to the fiscal year,
computed by [the revenue computation](../computations/revenue.md).
```

Because each computation is its own concept, revenue can be fresh while
profit is past its `stale_after`, and each attests on its own run.
Co-locating them is a directory choice (a `computations/` folder with an
`index.md`), not a frontmatter one.

### 10.5 How a consumer uses it (informative)

This subsection is informative, not normative. The runtime artifacts below
are **not** stored in the bundle.

1. **Discover** via `type: Attested Computation`, a frontmatter signal
   liftable into `index.md`; a consumer reaches one directly or by
   following a link from a concept that uses it.
2. **Load** the contract from frontmatter and the computation from the
   body (or the file named by `computation`).
3. **Parameterize**: the agent supplies values for the declared parameters.
4. **Execute**: the executor runs the bound computation and returns a
   receipt shaped by `executor.receipt`.
5. **Attest**: the consumer runs the attester over the receipt. It
   confirms provenance (the computation that ran equals `computation` bound
   with the claimed parameters, not agent-authored SQL) and fidelity (the
   displayed value matches the receipt's authoritative source, re-read by
   job id rather than taken from the agent's text).
6. **Gate**: refuse to display a failing attestation; warn or refuse when
   `now >= stale_after`. On success, surface the verdict (for example a
   link to the job log) so trust is visible.

### 10.6 Verification versus attestation

`verified` (§5.2) and attestation are distinct, and both exist:

- `verified` confirms the *definition* still matches policy. It is
  doc-level, slow, and recorded in the bundle.
- Attestation confirms a single *run* produced the value the sanctioned
  way. It is per-call, runtime, and not stored in the bundle.

A concept with a stale definition can still attest cleanly, and a
freshly-verified definition still requires attestation on each run, which
is why both are needed.

---

## 11. Conformance

A bundle is **conformant** with OKF v0.2 if:

1. Every non-reserved `.md` file in the tree contains a parseable YAML
   frontmatter block.
2. Every frontmatter block contains a non-empty `type` field.
3. Every reserved filename (`index.md`, `log.md`) follows the structure in
   §8 and §9 respectively when present.

When the trust, lifecycle, provenance, or computation families are
present, producers SHOULD follow §5 through §10, and consumers:

- MUST treat a bare `verified` mapping as a one-element list (§5.2).
- MUST NOT reject a concept for missing any optional family (§5.3).
- SHOULD derive trust tiers and staleness only from the fields specified
  here, and SHOULD surface, not silently drop, a failing attestation
  (§10.5).

Consumers SHOULD treat all other constraints as soft guidance. In
particular, consumers MUST NOT reject a bundle because of:

- Missing optional frontmatter fields.
- Unknown `type` values.
- Unknown additional frontmatter keys.
- Broken cross-links.
- Missing `index.md` files.

---

## 12. Versioning

This document specifies OKF version **0.2**. Revisions are versioned as
`<major>.<minor>`:

- A **minor** version bump introduces backward-compatible additions (new
  optional fields, new conventional section headings).
- A **major** version bump may make breaking changes (renaming required
  fields, changing reserved filenames).

Bundles MAY declare the version they target with `okf_version: "0.2"` in a
bundle-root `index.md` frontmatter block (the only place frontmatter is
permitted in an `index.md`). Consumers that do not understand the declared
version SHOULD attempt best-effort consumption rather than refusing the
bundle.

### Considered and deferred

The following are intentionally left to a future revision:

- The full runtime protocol: receipt and verdict wire formats, and the
  attestation lifecycle around a run.
- The attester ABI, portability, and sandboxing, likely bundled with
  future work on serving and Skills.
- Attestation caching.
- Semantic-layer templates (Looker, dbt) where the attester comparison
  shifts from SQL equality to model-and-binding equality.

---

## 13. Changes from v0.1

v0.2 supersedes OKF v0.1 and is a minor version bump under §12, except for
two deliberate breaking changes called out below because they rename or
retire v0.1 fields. A v0.1 bundle is consumable by a v0.2 consumer under
the fallbacks noted here.

### 13.1 Breaking changes

- **`timestamp` is superseded by `generated.at`.** A concept's last
  content change is now recorded as `generated: { by, at }` (§5.2).
  Consumers MAY fall back to a legacy `timestamp` when `generated` is
  absent.
- **The body `# Citations` list is superseded by `sources`.** Provenance
  moves to frontmatter (§5.1). Consumers SHOULD read `sources` and MAY
  still parse a legacy `# Citations` body list for v0.1 documents.

### 13.2 Additive changes

All of the following are additive: new optional keys, one new concept
type, and one new conventional heading. Their absence yields a plain v0.1
concept.

- New frontmatter families: `sources` with its per-source credibility
  signals (`author`, `usage_count`, `last_modified`) and the `usage_window`
  sibling; `generated`, `verified`; `status`, `stale_after` (§5).
- New concept type `Attested Computation` and its computation keys
  `runtime`, `parameters`, `computation`, `executor`, `attester` (§10).
- New conventional body heading `# Computation` (§4.2).
- The actor convention for `generated.by` and `verified[].by` (§7).

Everything else (bundle structure, reserved filenames, the required
`type`, recommended `title`/`description`/`resource`/`tags`, cross-linking,
index files, log files, permissive conformance) is carried forward
unchanged.

---

## Appendix A: Worked example, an income statement

One bundle exercising every family, shown as a v0.1 to v0.2 migration of an
income statement with two figures, revenue and gross profit.

### v0.1 form

A single doc: both figures in one concept, the SQL in prose an agent can
read, ignore, or rewrite, citations a flat list, and the only timestamp is
`timestamp`.

```markdown
---
type: Metric
title: Income statement (fiscal year)
description: Headline income-statement figures for a fiscal year.
tags: [finance, income-statement]
timestamp: '2026-05-28T22:53:05+00:00'
---

# Definition
The income statement reports revenue and gross profit for a fiscal year.

# Revenue
Recognized revenue sums `amount` over rows booked to the fiscal year:

    SELECT SUM(amount) AS revenue
    FROM finance.recognized_revenue
    WHERE fiscal_year = <year>

# Gross profit
Gross profit by segment, per the cost-allocation standard:

    SELECT gross_profit FROM fct_income_statement
    WHERE fiscal_year = <year> AND segment = <segment>

# Citations
- https://wiki.acme/finance/fpa-handbook
- https://wiki.acme/finance/revenue-recognition
- https://wiki.acme/finance/cost-allocation
```

### v0.2 form

The two figures split into attested computations linked from a narrative
concept. Every family is populated, and the two computations sit in
deliberately different states so one consumer reaches two verdicts.

```
bundles/finance/
  metrics/income-statement.md      type: Metric  (narrates, links both)
  computations/revenue.md          type: Attested Computation  (runtime: bigquery)
  computations/profit.md           type: Attested Computation  (runtime: dbt)
  references/skills/run-on-bq.md, run-dbt.md
  references/attesters/sql-equality.py, dbt-binding.py
```

`metrics/income-statement.md`, the readable doc; trust lives on what it
links, not here:

```markdown
---
type: Metric
title: Income statement (fiscal year)
description: Headline income-statement figures for a fiscal year.
tags: [finance, income-statement]
status: stable
generated: { by: reference_agent/gemini-2.5-pro, at: 2026-06-20T22:53:05Z }
verified: { by: human:ahormati, at: 2026-06-25T09:00:00Z }
stale_after: 2026-12-31T00:00:00Z
sources:
  - id: fpa-handbook
    resource: https://wiki.acme/finance/fpa-handbook
    title: FP&A reporting handbook
---

# Definition
The income statement reports [revenue](../computations/revenue.md) and
[gross profit](../computations/profit.md) for a fiscal year, per the FP&A
reporting handbook.[^fpa-handbook] Each figure is produced by a sanctioned,
attestable computation; this concept only narrates them.

[^fpa-handbook]: FP&A reporting handbook
```

`computations/revenue.md`, BigQuery SQL, human-verified, fresh, and
corroborated by a live dashboard source carrying credibility signals:

```markdown
---
type: Attested Computation
title: Revenue for fiscal year
description: Recognized revenue for a fiscal year, per Finance's definition.
tags: [finance, revenue]
status: stable
runtime: bigquery
parameters:
  - { name: year, type: integer, required: true }
executor:
  resource: references/skills/run-on-bq.md
  receipt: [job_id, executed_sql, result]
attester:
  resource: references/attesters/sql-equality.py
generated: { by: reference_agent/gemini-2.5-pro, at: 2026-06-28T14:00:00Z }
verified: { by: human:ahormati, at: 2026-06-25T09:00:00Z }
stale_after: 2026-12-31T00:00:00Z
sources:
  - id: rev-policy
    resource: https://wiki.acme/finance/revenue-recognition
    title: Revenue recognition policy
    author: team:finance-fpa
    last_modified: 2026-04-02T00:00:00Z
  - id: exec-rev-dash
    resource: dashboards/exec-revenue
    title: Executive revenue dashboard
    author: team:finance-fpa
    usage_count: 5000
    last_modified: 2026-06-18T00:00:00Z
usage_window: { from: 2026-06-01T00:00:00Z, to: 2026-06-30T00:00:00Z }
---

# Computation

    SELECT SUM(amount) AS revenue
    FROM finance.recognized_revenue
    WHERE fiscal_year = @year

Recognized revenue per the recognition policy,[^rev-policy] corroborated by
the executive revenue dashboard.[^exec-rev-dash]

[^rev-policy]: Revenue recognition policy
[^exec-rev-dash]: Executive revenue dashboard
```

`computations/profit.md`, a dbt model, process-verified, and past its
`stale_after`:

```markdown
---
type: Attested Computation
title: Gross profit for fiscal year
description: Gross profit by segment for a fiscal year, per the cost-allocation standard.
tags: [finance, profit]
status: stable
runtime: dbt
parameters:
  - { name: year, type: integer, required: true }
  - { name: segment, type: string, required: true }
executor:
  resource: references/skills/run-dbt.md
  receipt: [run_id, compiled_sql, result]
attester:
  resource: references/attesters/dbt-binding.py
generated: { by: reference_agent/gemini-2.5-pro, at: 2026-06-14T14:00:00Z }
verified: { by: process:finance-nightly, at: 2026-06-12T08:00:00Z }
stale_after: 2026-06-15T00:00:00Z
sources:
  - id: cost-alloc
    resource: https://wiki.acme/finance/cost-allocation
    title: Cost allocation standard
---

# Computation

    SELECT gross_profit
    FROM {{ ref('fct_income_statement') }}
    WHERE fiscal_year = {{ var('year') }}
      AND segment = {{ var('segment') }}

Gross profit by segment per the cost-allocation standard.[^cost-alloc]

[^cost-alloc]: Cost allocation standard
```
`````
