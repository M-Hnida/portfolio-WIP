# 📝 TODO & Matrice de Conformité BTS SIO - Bloc 1

Ce document récapitule les tâches restantes pour finaliser votre portfolio pour l'épreuve E4, ainsi que la matrice de couverture des compétences officielles du Bloc 1.

---

## 🛠️ Actions Restantes (À faire par vous)

- [ ] **Ajouter votre photo de profil**
  * Déposer votre photo nommée `photo.jpg` dans le dossier `static/` pour remplacer le lien brisé sur la page d'accueil.
- [x] **Déposer votre CV en PDF**
  * Placé sous `static/cv/CV_Hnida_Mohammed.pdf`.
- [x] **Carte Heuristique des Métiers**
  * Intégrée sous forme de page interactive dynamique avec Mermaid.js sur [/carte-heuristique](file:///C:/Users/got/Documents/code/portfolio/src/routes/carte-heuristique/+page.svelte).
- [ ] **Remplacer le texte temporaire du Stage de 1ère année**
  * Une fois votre stage effectué ou défini, modifier la `detailedDescription` du projet *Stage de 1ère année* dans `src/lib/components/Projects.svelte` (lignes 25-39) avec vos missions réelles.
- [ ] **Ajouter des auto-formations ou certifications (Conseillé par le CNED)**
  * Si vous avez des certifications (Pix, SecNumAcadémie, certifications de cours en ligne, etc.), ajoutez-les dans le tableau `education` dans `src/lib/components/About.svelte` (lignes 2-20) pour valoriser votre auto-formation.

---

## 📊 Matrice de Couverture des Compétences du Bloc 1

Pour l'épreuve E4, le jury doit vérifier que vous maîtrisez **l'ensemble des compétences** du Bloc 1. Voici comment vos projets couvrent chaque critère officiel du référentiel :

### 1. Gérer le patrimoine informatique (GP)
| Compétence Officielle | Projets Couvrants |
| :--- | :--- |
| **GP 1.1** : Recenser et identifier les ressources numériques | *Stage de 1ère année* (inventaire de parc) |
| **GP 1.2** : Exploiter des référentiels, normes et standards | *C# Agenda* (normes POO), *C# Habilitations* (MVC), *Java Client/Serveur* (sockets, MVC) |
| **GP 1.3** : Mettre en place et vérifier les niveaux d'habilitation | *C# : Gestion des habilitations* (authentification, rôles, permissions - **projet clé**) |
| **GP 1.4** : Vérifier les conditions de la continuité d'un service | *Stage de 1ère année* (tests de redondance, vérification de sauvegardes) |
| **GP 1.5** : Gérer des sauvegardes | *Stage de 1ère année* (scripts de backup, NAS) |
| **GP 1.6** : Vérifier le respect des règles d'utilisation | *WordPress : Site E-commerce* (droits d'auteur, charte informatique) |

### 2. Répondre aux incidents et aux demandes d'assistance (RI)
| Compétence Officielle | Projets Couvrants |
| :--- | :--- |
| **RI 2.1** : Collecter, suivre et orienter des demandes | *Stage de 1ère année* (utilisation d'un outil de ticketing / GLPI) |
| **RI 2.2** : Traiter des demandes concernant les services réseau et système | *Java : Client/Serveur* (résolution d'erreurs de socket et connexion réseau) |
| **RI 2.3** : Traiter des demandes concernant les applications | *C# Agenda* & *Bot Discord* (maintenance corrective et évolutive d'applications) |

### 3. Développer la présence en ligne de l'organisation (PL)
| Compétence Officielle | Projets Couvrants |
| :--- | :--- |
| **PL 3.1** : Participer à la valorisation de l'image de l'organisation | *PHP : Site d'articles* (site responsive professionnel), *WordPress : E-commerce* |
| **PL 3.2** : Référencer les services en ligne et mesurer leur visibilité | *PHP : Site d'articles* (optimisation SEO, balises meta, mesure SEO) |
| **PL 3.3** : Participer à l'évolution d'un site Web exploitant des données | *PHP : Site d'articles* (conformité RGPD), *Site E-commerce Full-stack* (API/PostgreSQL) |

### 4. Travailler en mode projet (MP)
| Compétence Officielle | Projets Couvrants |
| :--- | :--- |
| **MP 4.1** : Analyser les objectifs et les modalités d'organisation | *Stage de 1ère année* (cahier des charges), *Site E-commerce Full-stack* |
| **MP 4.2** : Planifier les activités | *Stage de 1ère année* (Gantt, Trello), *Site E-commerce Full-stack* (plan de sprints) |
| **MP 4.3** : Évaluer les indicateurs de suivi et analyser les écarts | *Stage* / *Site E-commerce Full-stack* (revues de jalons et gestion des retards) |

### 5. Mettre à disposition des utilisateurs un service informatique (MS)
| Compétence Officielle | Projets Couvrants |
| :--- | :--- |
| **MS 5.1** : Réaliser les tests d'intégration et d'acceptation | *Java : Client/Serveur* (cahier de tests client/serveur), *Site E-commerce Full-stack* |
| **MS 5.2** : Déployer un service | *PHP : Site d'articles* (mise en production), *WordPress : E-commerce* (hébergement) |
| **MS 5.3** : Accompagner les utilisateurs dans la mise en place d'un service | *WordPress* (guide utilisateur de la boutique), *Bot Discord* (documentation des commandes) |

### 6. Organiser son développement professionnel (DP)
| Compétence Officielle | Projets Couvrants |
| :--- | :--- |
| **DP 6.1** : Mettre en place son environnement d'apprentissage | *Backtesting Trading* (auto-formation sur NautilusTrader, numpy, pandas) |
| **DP 6.2** : Mettre en œuvre des outils et stratégies de veille | *Page Veille du Portfolio* (veille active sur GitHub, Reddit, Twitter, YouTube) |
| **DP 6.3** : Gérer et développer son identité/projet professionnel | *Portfolio lui-même* (CV, carte heuristique, historique de carrière) |

---

## 🔍 Préparation de la Veille pour l'Oral E4 (Séquence 3)

Pour l'oral du BTS, vous devrez exposer votre méthodologie de veille. Préparez des réponses claires sur ces points :
- [ ] **Définition de vos Objectifs** : Pourquoi veiller sur les frameworks JS/TS et l'OWASP ? (Pour anticiper les outils de futurs projets et protéger les applications contre les failles).
- [ ] **Explication du Filtrage (Anti-Infobésité)** : Expliquer comment vous évitez d'être inondé d'informations (sélection de subreddits comme r/webdev, listes Twitter fermées, requêtes GitHub spécifiques).
- [ ] **Esprit critique (QQOQCCP)** : Savoir citer un exemple où vous avez douté d'une info technique (ex: rumeur sur Reddit) et comment vous l'avez validée via la doc officielle (constructeurs/éditeurs) ou une CVE.
- [ ] **Illustration de Sérendipité** : Avoir en tête un exemple où vous cherchiez quelque chose (ex: un fix de bug) et avez découvert par hasard un outil très utile (ex: un nouveau package, outil de dev).
- [ ] **Démonstration des Outils de Recherche** : Être capable d'expliquer comment vous faites une recherche fine (ex: `site:github.com` ou `filetype:pdf`).
