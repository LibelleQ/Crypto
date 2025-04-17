# Cours - MAC, Hash, Chiffrement Authentifié

# Un .MD existe avec les questions types qui peuvent arriver au contrôle + partiel
[Questions type](https://github.com/LibelleQ/Crypto/blob/main/controle_question.MD)


## Probabilisme / Déterminisme

- `KeyGen` est **probabiliste** (génère une clé aléatoire).
- `Encrypt` est **probabiliste** (utilise souvent un IV ou du padding aléatoire).
- `Decrypt` est **déterministe** (résultat unique si les entrées sont valides).

---

## MAC - Intégrité des Données

- Un **MAC** (Message Authentication Code) assure **l'intégrité** et **l'authenticité** d’un message.

### Modèles d'attaquant

- Une **contrefaçon** consiste à produire un couple (M', T') valide, sans connaître la clé.
- Objectif : forger le bon tag T' pour un message M'.

### Types d’attaques

- **Existentielles** : réussir à forger un couple valide (M', T') quelconque.
- **Universelles** : attaquant capable de forger n’importe quel message/tag valide.

> ATTENTION Si (M, T) est un couple déjà vu, ce n’est **pas** une contrefaçon.

### Scénarios d'attaque

- **Messages connus** : l'attaquant a accès à plusieurs couples (M, T).
- **Messages choisis** : l'attaquant choisit les messages et observe les tags générés.

---

## Sécurité d’un MAC

- **Brute force sur la clé** : essayer toutes les clés possibles.
- **Brute force sur le tag** : tester toutes les valeurs de tag possibles.

ATTENTION Le tag doit être suffisamment long : typiquement **2⁹⁶** bits.

> Pourquoi pas plus long ?  
> Pour limiter les temps de réponse en ligne et éviter les risques de **bannissement** ou **détection d’attaque**.

---

## Propriétés de l’opérateur XOR

- A ⊕ B = B ⊕ A (commutatif)
- Exemple :
  - m1, m2, m3 et T
  - m1′, m2′, m3′ et T′

---

## Structure d’un MAC

- Un **tag** est le **résultat d’un calcul** utilisant une clé secrète.
- Exemples de MAC robustes :
  - **AES-128-EMAC**
  - **AES-256-CBC-MAC**

### CBC-MAC

- Pas d’IV
- Taille de bloc fixe
- Utilisé dans IPSec, GlobalPlatform, etc.
- Robuste, mais attention : nécessite des messages de **taille fixe** ou des mécanismes d'encapsulation.

### EMAC

- Ajoute une **couche de chiffrement** supplémentaire
- Dépend de la taille de bloc, de la clé

---

## HMAC et Fonctions de Hachage

### Sécurité d’un hash

- **Préimage** : difficile de trouver un message M tel que H(M) = T
- **Résistance aux collisions** : difficile de trouver deux messages M ≠ M′ tels que H(M) = H(M′)
- Espace requis : ≈ (2^h / 2) * h bits (attaque de type "birthday")

### Fonction de hachage seule

- **Ne garantit pas l'intégrité** : sans clé, on peut forger => **attaque universelle**

### Fonction éponge (Sponge Function)

- Utilisée dans SHA-3
- Paramètres :
  - r : taux (rate)
  - c : capacité (capacity)
- Plus la capacité est grande, plus la sécurité est élevée
- MAC via éponge : injecter la **clé dans la capacité**

---

## Fonction de Hachage

- Domaine : {0,1}* → {0,1}ⁿ (de taille variable à taille fixe)
- Pas **symétrique** ni **asymétrique** dans le sens classique : ce sont des **fonctions unidirectionnelles**

---

## Modes de Chiffrement

- **ECB** (Electronic Codebook)
- **CBC** (Cipher Block Chaining)

---

## Chiffrement Authentifié

### Trois constructions classiques

1. **Encrypt and MAC**
   - C = Encrypt(K1, M)
   - T = MAC(K2, M)

2. **MAC then Encrypt**
   - T = MAC(K1, M)
   - C = Encrypt(K1, M || T)

3. **Encrypt then MAC** Recommandé
   - C = Encrypt(K1, M)
   - T = MAC(K2, C)

Exemple : AES-128-CBC + HMAC-SHA2-256

---

## Construction de Fonction de Hachage

- Problème : **pseudo-collisions**
- Fonction f interne doit être résistante aux collisions

Exemple : (m1, m2, m3), (m1′, m2, m3) ⇒ même H’ : vulnérabilité
