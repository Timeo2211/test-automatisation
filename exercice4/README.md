# Code un max — Suite de tests automatisés (livrable MSPR)

Suite de tests complète de la plateforme de cours **Code un max** :
tests unitaires (TDD), E2E en Page Object Model **cross-browser** (Chrome/Firefox),
données dynamiques (Faker), mocking du paiement (responses), exécution
**parallèle** (pytest-xdist), **reporting HTML** et **couverture** (pytest-cov),
le tout intégré à un pipeline **GitHub Actions**.

## Prérequis

- Python **3.11+**
- **Google Chrome** et/ou **Mozilla Firefox** installés
- Git

> Les drivers (chromedriver / geckodriver) sont résolus automatiquement par
> **Selenium Manager** (intégré à Selenium 4). Rien à installer à la main.

## Cloner

```bash
git clone https://github.com/Timeo2211/test-automatisation.git
cd test-automatisation/exercice4
```

## Installer

```bash
python -m venv venv
source venv/bin/activate            # Windows : venv\Scripts\activate
pip install -r requirements.txt
```

## Lancer l'application (dans un terminal dédié)

```bash
python -m app.server                # http://localhost:8000
```

> Si le port 8000 est occupé : `PORT=8010 python -m app.server`, puis passer
> `BASE_URL=http://localhost:8010` aux commandes de test ci-dessous.

## Lancer les tests (autre terminal)

```bash
source venv/bin/activate

# Toute la suite, en parallèle, avec rapport HTML + couverture (une commande)
pytest -n auto \
  --cov=app --cov-report=html --cov-report=term-missing \
  --html=report.html --self-contained-html

# Sous-ensembles utiles
pytest -m unit                      # tests rapides (sans navigateur ni réseau)
pytest -m e2e                       # tests end-to-end
pytest -p no:randomly               # ordre fixe (débogage)
```

### Choix des navigateurs

Les tests E2E tournent sur Chrome **et** Firefox par défaut. Pour restreindre :

```bash
BROWSERS=chrome pytest -m e2e       # Chrome uniquement
BROWSERS=firefox pytest -m e2e      # Firefox uniquement
```

Chaque scénario E2E apparaît une fois par navigateur (ex. `...[chrome]`, `...[firefox]`).

## Lire le rapport

- **`report.html`** — rapport pytest auto-contenu (à ouvrir dans un navigateur).
- **`htmlcov/index.html`** — rapport de couverture détaillé, ligne par ligne.

En CI, ces deux rapports sont publiés en **artefacts** téléchargeables
(`report-html`, `couverture-html`) sur chaque exécution de l'onglet **Actions**.

## Configuration (variables d'environnement)

| Variable          | Défaut                    | Rôle                                   |
|-------------------|---------------------------|----------------------------------------|
| `BASE_URL`        | `http://localhost:8000`   | URL de la plateforme testée            |
| `BROWSERS`        | `chrome,firefox`          | Navigateurs E2E (séparés par virgule)  |
| `HEADLESS`        | `1`                       | `0` pour voir le navigateur (debug)    |
| `SERVICE_EMAIL`   | `eleve.test@codeunmax.fr` | Compte de service (login mutualisé)    |
| `SERVICE_PASSWORD`| `Test1234!`               | Mot de passe du compte de service      |
| `FAKER_SEED`      | `12345`                   | Seed Faker (données reproductibles)    |

Copier `.env.example` en `.env` pour fixer ces valeurs en local. En CI, elles
sont fournies par le workflow.

## Choix techniques

- **TDD** : la règle de tarification (remise de 15 % dès le 3ᵉ cours,
  `app/tarification.py`) a été développée en Red → Green → Refactor — voir
  l'historique Git (`test(tarification): RED …` puis `feat(tarification): GREEN …`).
- **Parallélisation** : `pytest -n auto` ; les tests sont isolés (driver neuf par
  test, apprenants Faker uniques via UUID, paiement mocké). La suite passe en
  séquentiel **et** en parallèle.
- **Stabilité** : les attentes sont **explicites** (`WebDriverWait` dans
  `BasePage`), aucune temporisation fixe. `pytest-rerunfailures` n'est activé que
  sur `test_inscription` (parcours multi-pages), comme filet de sécurité documenté
  — la stabilité vient d'abord des attentes explicites.
- **Couverture** : mesurée avec `pytest-cov` (compatible xdist). `app/server.py`
  est exercé de bout en bout par les E2E mais, tournant dans un **process séparé**,
  n'est pas instrumenté par pytest-cov ; la couverture porte donc sur le code
  logique (validation, tarification, inscription), **> 90 %**.

## Pipeline CI

`.github/workflows/ci.yml` (racine du dépôt) — déclenché sur `push`,
`pull_request` et manuellement (**Run workflow**) :

- **lint** : `ruff check .`
- **unit_tests** : tests rapides mockés (sans navigateur)
- **full_suite** : suite complète (unit + E2E **Chrome & Firefox**) en `-n auto`,
  publie `report.html` et la couverture HTML en artefacts.
