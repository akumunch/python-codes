Implementation of a precise 6-month flight price search using per-date Amadeus queries

Searches flights from tomorrow up to 6 months ahead by iterating over departure dates
and selecting the true lowest priced offer with exact airline and departure time.
Highly accurate and deterministic, but slower due to multiple API calls per route.

