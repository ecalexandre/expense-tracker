# Projet Python no 4 — Gestionnaire de dépenses (Expense Tracker)

**Défi :** créer un programme qui permet de noter ses dépenses et de comprendre où va son argent.

## 1. Mise en situation

Imagine que tu veux suivre tes dépenses de la semaine : un repas, un billet d’autobus, un livre ou une sortie. Au lieu de tout garder en tête, tu décides de créer ton propre petit gestionnaire de dépenses dans le terminal.

Ton programme doit être simple à utiliser. Une personne qui ne connaît pas ton code doit pouvoir lancer l’application, enregistrer ses dépenses et consulter un bilan clair.

**Ton objectif n’est pas d’écrire le programme le plus long ni le plus compliqué.** C’est de construire un outil qui fonctionne, qui est facile à comprendre et que tu pourrais améliorer plus tard.

## 2. Ce que ton programme doit permettre de faire

L’utilisateur doit pouvoir :

1. **Ajouter une dépense** en indiquant sa description, son montant et sa catégorie (par exemple : alimentation, transport, loisirs, école ou autre).
2. **Consulter les dépenses** déjà enregistrées, avec suffisamment d’information pour reconnaître chacune d’elles.
3. **Consulter un bilan** comprenant le montant total dépensé, la dépense moyenne, la dépense la plus élevée et la moins élevée.
4. **Voir les dépenses par catégorie**, avec le total dépensé dans chaque catégorie utilisée.
5. **Quitter le programme** quand il le souhaite.

Le programme doit rester utilisable après chaque opération, jusqu’à ce que l’utilisateur décide de quitter.

## 3. Les situations auxquelles penser

Un utilisateur ne fait pas toujours exactement ce que tu prévois. Ton programme doit réagir clairement, sans planter, notamment lorsque :

- aucune dépense n’a encore été enregistrée ;
- un montant n’est pas un nombre ou n’est pas valide ;
- une description ou une catégorie est laissée vide ;
- une option inconnue est choisie dans le menu.

Réfléchis aussi à la manière de présenter les montants d’argent de façon cohérente et lisible.

## 4. Les notions à réutiliser

Avant de commencer, revisite les notions Python que tu as déjà étudiées. Tu n’as pas besoin de toutes les utiliser artificiellement : choisis celles qui servent réellement ton programme.

- Variables, types de données, nombres, chaînes de caractères et conversion des entrées.
- Conditions, `match/case` si utile, boucles `while` et `for`.
- Listes et dictionnaires pour organiser les informations.
- Fonctions pour éviter de répéter les mêmes opérations et rendre le programme plus lisible.
- Opérations mathématiques pour calculer les bilans.
- Gestion des erreurs avec `try/except` et validation des entrées.
- Modules de la bibliothèque standard, lorsque cela simplifie une tâche.

**Pas de classes ni de programmation orientée objet pour ce projet.** L’objectif est de consolider les bases.

Tu connais déjà certaines notions de fichiers et de JSON. **Tu peux les utiliser si tu juges qu’elles sont utiles**, mais l’enregistrement permanent des dépenses n’est pas obligatoire pour la première version.

## 5. Avant de coder

Prends le temps de réfléchir à ton approche. Tu devrais pouvoir expliquer, avec tes mots :

- quelles informations représentent une dépense ;
- comment tu comptes conserver plusieurs dépenses pendant l’exécution ;
- comment l’utilisateur passera d’une opération à une autre ;
- comment tu calculeras et présenteras le bilan ;
- quelles opérations méritent d’être regroupées dans des fonctions.

Quand tu as une idée de la structure générale, viens m’en parler. Nous pourrons discuter de tes choix avant que tu commences l’implémentation. **Je veux voir ton raisonnement, pas seulement le résultat.**

## 6. Organisation du dépôt GitHub

Le dépôt existe déjà : clone-le sur ton ordinateur et travaille à partir de celui-ci. Ton programme doit démarrer à partir d’un fichier nommé **`main.py`**. Tu peux créer d’autres fichiers ou dossiers si cela aide réellement à organiser ton projet.

À la fin, le dépôt doit contenir au minimum :

```text
expense-tracker/
├── main.py
├── README.md
├── LICENSE
├── .gitignore
└── docs/
    └── PROJET_04_EXPENSE_TRACKER.md
```

Le dossier `docs/` contient cet énoncé. Les autres fichiers ou dossiers dépendent de tes choix. Ne publie pas ton environnement virtuel, tes fichiers temporaires, des données personnelles ou des secrets dans Git.

### README.md — documenter ton programme

Rédige le README **avec tes propres mots**, en Markdown. Une personne qui découvre ton dépôt doit pouvoir comprendre et utiliser ton programme sans avoir à lire tout le code.

Ton README doit expliquer :

- **Description :** à quoi sert le programme ?
- **Fonctionnalités :** que peut faire l’utilisateur ?
- **Prérequis :** de quoi a-t-on besoin pour l’exécuter ?
- **Installation et lancement :** comment préparer et démarrer le projet ?
- **Utilisation :** comment se servir du menu et consulter le bilan ?
- **Exemple :** un court exemple d’utilisation ou de résultat.
- **Structure du projet :** à quoi servent les fichiers et dossiers importants ?

Garde la documentation courte, exacte et à jour. Si tu changes le fonctionnement du programme, vérifie aussi ton README.

### LICENSE — une habitude à prendre

Ajoute un fichier **`LICENSE`** à la racine du dépôt. Pour ce projet public, nous choisirons ensemble une licence simple, par exemple la **licence MIT**. Lis-la avec moi pour comprendre ce qu’elle autorise avant de l’ajouter. N’écris pas une licence de ton invention et n’y mets pas d’informations personnelles inutiles.

### Git et GitHub

Fais des commits au fur et à mesure, avec des messages qui décrivent les changements. Utilise `git diff` pour revoir ton travail avant de le pousser. Le dépôt doit rester propre et compréhensible pour quelqu’un qui le découvre.

## 7. Quand le projet de base fonctionne : idées facultatives

Ces idées sont des **défis supplémentaires**, pas des conditions pour réussir la première version :

- enregistrer les dépenses dans un fichier JSON et les retrouver au prochain lancement ;
- ajouter une date à chaque dépense ;
- chercher ou filtrer les dépenses par catégorie ;
- modifier ou supprimer une dépense ;
- produire un bilan pour une période donnée.

Termine et vérifie d’abord la version de base avant d’ajouter des fonctionnalités.

## 8. Comment ton travail sera évalué

Nous regarderons à la fois **ce que fait le programme** et **la façon dont tu l’as construit** : fonctionnement, notions Python utilisées à bon escient, organisation du code, lisibilité, gestion des erreurs, qualité du README et du dépôt Git. Les fonctionnalités supplémentaires sont appréciées, mais elles ne remplacent pas un programme de base fiable.

Tu devras aussi pouvoir m’expliquer tes choix et me montrer comment fonctionne ton programme. Si tu utilises une vidéo, de la documentation ou un outil d’IA pour apprendre quelque chose, assure-toi de comprendre le code que tu conserves. Tu dois pouvoir l’expliquer et le modifier toi-même.

**Rappel : les devoirs et les cours d’école passent en premier.** Travaille sur ce projet quand ton travail scolaire est terminé et à jour.

Bon défi ! 🚀
