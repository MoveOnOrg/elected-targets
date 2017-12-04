# Elected Targets

This Django app provides models, a router, and admin interface for elected petition targets, e.g. members of Congress.

## How to Use

In `settings.py`, add `elected_targets` to `INSTALLED_APPS` and `ElectedTargetsRouter()` to `DATABASE_ROUTERS`. Then import and use any models in `models.py` as needed.
