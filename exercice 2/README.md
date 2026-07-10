# TEST-5 — Suite E2E en Page Object Model (Code un max)

Suite E2E structurée en Page Object Model couvrant les 5 parcours clés de la
plateforme : login valide, login refusé, navigation catalogue, inscription à un
cours, déconnexion.

## Arborescence

```
pages/                 Page Objects (locators + méthodes métier)
  base_page.py         interactions Selenium bas niveau (attentes explicites)
  login_page.py        LoginPage
  catalogue_page.py    CataloguePage
  inscription_page.py  InscriptionPage
  dashboard_page.py    DashboardPage
tests/                 les 5 scénarios (8–10 tests)
conftest.py            fixtures driver + session_connectee (login mutualisé)
pytest.ini             testpaths, markers, convention de nommage
app/                   plateforme de démo (Flask)
```

## Lancer la suite

1. Créer/activer le venv et installer les dépendances :

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Démarrer la plateforme dans un terminal à part :

   ```bash
   PORT=8000 python -m app.server      # écoute sur http://localhost:8000
   ```

3. Lancer les tests dans un autre terminal :

   ```bash
   pytest                              # 9 tests E2E
   ```

## Variables d'environnement

| Variable   | Défaut                  | Rôle                                      |
|------------|-------------------------|-------------------------------------------|
| `BASE_URL` | `http://localhost:8000` | URL de la plateforme utilisée par les tests |
| `HEADLESS` | `1`                     | `HEADLESS=0` pour voir le navigateur (debug) |

> Si le port 8000 est occupé, lancer par ex. `PORT=8010 python -m app.server`
> puis `BASE_URL=http://localhost:8010 pytest`.

## Ordre aléatoire

`pytest-randomly` mélange l'ordre à chaque run (seed affichée en en-tête). Pour
retrouver un ordre fixe pendant le débogage : `pytest -p no:randomly`.
