# TEST-6 à TEST-8 — Données dynamiques, mocking & CI (Code un max)

Suite de tests rendue indépendante des données (Faker) et des services externes
(mock du paiement), avec gestion des environnements local/CI et un pipeline
GitHub Actions publiant un rapport en artifact.

## Arborescence

```
pages/                   Page Objects (POM)
tests/
  test_login.py          login valide + login refusé (paramétré)
  test_catalogue.py      navigation catalogue
  test_inscription.py    inscription E2E avec apprenant généré par Faker
  test_deconnexion.py    déconnexion
  test_paiement.py       paiement mocké (accepté 200 / refusé 402) — marker unit
conftest.py              fixtures : config, driver, session_connectee, apprenant (Faker)
pytest.ini               markers unit / e2e
ruff.toml                config du lint
.env.example             variables attendues (copier en .env en local)
.github/workflows/ci.yml pipeline 3 jobs : lint / unit_tests / e2e_tests
app/                     plateforme de démo (Flask)
```

## Configuration (local)

```bash
cp .env.example .env      # puis adapter si besoin
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

Variables (`.env` en local, variables du workflow en CI) :

| Variable          | Défaut                    | Rôle                                  |
|-------------------|---------------------------|---------------------------------------|
| `BASE_URL`        | `http://localhost:8000`   | URL de la plateforme                  |
| `SERVICE_EMAIL`   | `eleve.test@codeunmax.fr` | Compte de service (login mutualisé)   |
| `SERVICE_PASSWORD`| `Test1234!`               | Mot de passe du compte de service     |
| `FAKER_SEED`      | `12345`                   | Seed Faker (données reproductibles)   |
| `HEADLESS`        | `1`                       | `0` pour voir le navigateur (debug)   |

## Lancer les tests

```bash
# Serveur dans un terminal (si port 8000 occupé : PORT=8010 + BASE_URL=...)
python -m app.server

# Tests dans un autre terminal
pytest                 # toute la suite (11 tests)
pytest -m unit         # tests rapides mockés, sans serveur ni navigateur
pytest -m e2e          # tests end-to-end (serveur requis)
```

Rapport HTML : `pytest --html=rapport-tests.html --self-contained-html`.

## Pipeline CI

`.github/workflows/ci.yml` s'exécute sur `push` et `pull_request` avec 3 jobs :

- **lint** : `ruff check .`
- **unit_tests** : `pytest -m unit` (rapide, sans navigateur)
- **e2e_tests** : `pytest -m e2e` (installe Chrome, démarre le serveur) — dépend de
  `unit_tests` via `needs:`

Chaque job de tests génère un rapport HTML publié en artifact
(`actions/upload-artifact`, `if: always()` pour le récupérer même en cas d'échec).
