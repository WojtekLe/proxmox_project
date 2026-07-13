### kontrakt

1. Co dostaje na wejściu?
requests/environment.yaml

2. Co zwraca na wyjściu?
sukces lub listę błędów.

3. Z czego korzysta?
catalog/ (sizes.yaml, templates.yaml, software.yaml, policies.yaml).

4. Nie wolno mu robić?
nie może uruchamiać Terraforma,
nie może łączyć się z Proxmoxem,
nie może modyfikować plików requestu.

### manifest

1. Fail Fast

Błędy wykrywamy jak najwcześniej.

2. Never Guess

Platforma nie zgaduje intencji użytkownika.

3. Single Responsibility

Validator tylko waliduje.

4. Read Only

Validator niczego nie zmienia.

5. Deterministic

Ten sam request zawsze daje ten sam wynik.