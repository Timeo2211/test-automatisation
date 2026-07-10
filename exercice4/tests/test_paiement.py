import pytest
import responses

from app.inscription import inscrire_cours_payant

PAYMENT_API = "https://paiement.codeunmax.test/api/charge"
BASE_URL = "http://localhost:8000"
COURS_ID = "python-avance"

APPRENANT = {"email": "apprenant.mock@codeunmax.fr"}


@pytest.mark.unit
@responses.activate
def test_paiement_accepte_confirme_l_inscription():
    responses.add(responses.POST, PAYMENT_API, json={"transaction": "ok"}, status=200)
    resultat = inscrire_cours_payant(BASE_URL, PAYMENT_API, APPRENANT, COURS_ID)
    assert resultat["ok"] is True, f"Inscription attendue OK, obtenu : {resultat}"
    assert "confirmee" in resultat["message"].lower()
    assert len(responses.calls) == 1, "Le service de paiement doit etre appele une seule fois"


@pytest.mark.unit
@responses.activate
def test_paiement_refuse_affiche_un_message_d_erreur():
    responses.add(responses.POST, PAYMENT_API, json={"erreur": "carte"}, status=402)
    resultat = inscrire_cours_payant(BASE_URL, PAYMENT_API, APPRENANT, COURS_ID)
    assert resultat["ok"] is False, f"Refus de paiement attendu, obtenu : {resultat}"
    assert "refuse" in resultat["message"].lower(), (
        f"Message d'erreur inattendu : {resultat['message']!r}"
    )
