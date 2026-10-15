# mindandhealth-publish-plugin

[![Version sur main](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fnovanoticia%2Fmindandhealth-publish-plugin%2Fmain%2Fplugins%2Fmindandhealth-publish%2Fplugin.json&query=%24.version&prefix=v&label=Version%20sur%20main&color=blue)](https://github.com/novanoticia/mindandhealth-publish-plugin/blob/main/plugins/mindandhealth-publish/plugin.json)
[![Dernière version publiée](https://img.shields.io/github/v/release/novanoticia/mindandhealth-publish-plugin?display_name=tag&label=Derni%C3%A8re%20version%20publi%C3%A9e&color=green)](https://github.com/novanoticia/mindandhealth-publish-plugin/releases/latest)

[English](README.md) · [Français](README.fr.md) · [简体中文](README.zh-CN.md)

Plugin Claude Code d’**accompagnement éditorial conversationnel** pour les publications de [mindandhealth.org](https://mindandhealth.org) sur Obsidian Publish.

Compatible avec [Agent Plugins 1.0.0](https://agent-plugins.org/specification) et le format [Agent Skills](https://agentskills.io/specification). Une variante pour les interfaces de chat est également disponible.

L’assistant commence par une conversation, puis propose un brouillon lorsque l’idée se précise. Il peut ensuite préparer une newsletter LinkedIn, une publication courte et un prompt d’image. **Tout reste dans le chat ; le coffre Obsidian n’est jamais modifié.**

## Langues

**L’espagnol reste la langue de sortie par défaut**, même si vous lisez cette documentation en français. Demandez explicitement le français, l’anglais, le chinois simplifié ou une version bilingue. L’assistant conserve ce choix jusqu’à votre prochaine demande de changement.

Exemples :

- « Continuons en français et préparons la newsletter. »
- « Aide-moi à affiner ce brouillon en français. »
- « Prépare une version bilingue en français et en chinois simplifié, d’abord en français. »
- « Volvamos al español. »

Les instructions internes restent en anglais. Les citations, les URL, les noms de fichiers et les clés YAML sont conservés. Une source étrangère ne change pas automatiquement la langue de sortie. Voir le [guide des langues](plugins/mindandhealth-publish/skills/mindandhealth-publish/references/languages.md).

## Ressources i18n

Le skill charge les textes fixes depuis son [dossier i18n](plugins/mindandhealth-publish/skills/mindandhealth-publish/i18n/README.md) : `es.json` est la référence espagnole ; `en.json`, `fr.json` et `zh-CN.json` contiennent les mêmes clés et paramètres nommés. Les questions, titres d’interface et rappels utilisent ces ressources. La prose des articles et les notes éthiques sont rédigées à chaque fois.

Le [glossaire](plugins/mindandhealth-publish/skills/mindandhealth-publish/i18n/GLOSSARY.md) et l’[état des traductions](plugins/mindandhealth-publish/skills/mindandhealth-publish/i18n/STATUS.md) précisent les choix et les limites. Ces traductions sont des brouillons produits avec l’IA, sans révision linguistique humaine enregistrée. Les tests vérifient la structure, les empreintes des sources et le contenu du ZIP ; ils ne prouvent pas le comportement du modèle en situation réelle.

```bash
python3 scripts/build_distribution.py --sync-i18n --check
python3 scripts/validate_i18n.py
python3 -m unittest discover -s tests -v
```

## Méthode de travail

1. **Conversation exploratoire.** Pablo apporte un thème, une intuition, une question ou une lecture. L’assistant croise les perspectives, nuance et apporte des contre-arguments.
2. **Cristallisation.** Pablo demande un canevas, ou l’assistant le propose une seule fois lorsque la matière est suffisante.
3. **Canevas.** Un bloc Markdown dans le chat rassemble le brouillon issu de la conversation.
4. **Itération.** Le canevas change uniquement à la suite d’une demande explicite ou d’une suggestion approuvée.
5. **Finalisation.** Pablo copie manuellement le texte dans Obsidian et peut demander des contenus dérivés.

Le canevas n’est pas un fichier sur disque. Beaucoup de conversations restent exploratoires et n’aboutissent pas à un article.

## Fonctionnalités et limites

Le plugin accompagne la réflexion, crée un canevas compatible avec Obsidian, propose un frontmatter minimal et ajoute une note éthique. Sur demande, il produit une newsletter LinkedIn, une publication pour le fil et un prompt d’image au format 1570:880.

La variante Claude Code peut lire le coffre pour vérifier des articles et proposer des liens internes. La variante chat utilise uniquement les titres et textes fournis par Pablo.

Le plugin n’écrit aucun fichier, ne publie rien et ne génère pas d’images. Pablo ajoute lui-même le bloc YAML de coautorat à l’aide de son Tagger GPT, les étiquettes finales à l’aide de son modèle Obsidian, et les éventuelles images.

## Deux variantes

| Variante | Emplacement | Nom du skill | Usage |
|---|---|---|---|
| Plugin | `plugins/mindandhealth-publish/skills/mindandhealth-publish/` | `mindandhealth-publish` | Claude Code / onglet Code de Claude Desktop ; lecture du coffre et commande `/publish`. |
| Chat | `claude-ai/mindandhealth-publish/` | `mindandhealth-publish-chat` | Clients compatibles avec les skills : Claude.ai, Perplexity, Mistral et ChatGPT. Pas d’accès au coffre local. |

N’installez pas les deux variantes dans le même environnement : leurs déclencheurs risquent de se chevaucher.

## Installation

### Claude Code et Claude Desktop Code

```text
/plugin marketplace add novanoticia/mindandhealth-publish-plugin
/plugin install mindandhealth-publish@mindandhealth-publish-plugin
```

L’installation fournit `/publish` et les déclencheurs en langage naturel.

### Claude.ai

1. Téléchargez [mindandhealth-publish-claude-ai.zip depuis Releases](https://github.com/novanoticia/mindandhealth-publish-plugin/releases/latest/download/mindandhealth-publish-claude-ai.zip).
2. Ouvrez **Settings → Capabilities → Skills → Upload skill**.
3. Importez le ZIP et activez le skill.

L’accès aux skills personnalisés dépend de l’offre et des capacités activées dans votre compte.

### Perplexity

Téléchargez le même ZIP, ouvrez la gestion des **Skills**, puis choisissez l’importation d’un skill et activez-le.

### Mistral AI

Décompressez le ZIP. Dans l’espace **Work**, ouvrez **Skills** et sélectionnez le dossier `mindandhealth-publish-chat/` contenant `SKILL.md`.

### ChatGPT

Dans un environnement où **Work** et **Plugins** sont disponibles, ajoutez le plugin par son nom ou l’URL du dépôt. La disponibilité dépend du compte et des fonctionnalités activées.

La description de la variante chat reste sous les limites de compatibilité documentées : 500 caractères pour Mistral et 1 024 octets UTF-8 pour Perplexity.

## Utilisation

```text
/publish [contexte facultatif]
```

- **Sans argument :** démarrer une conversation exploratoire.
- **Thème ou question :** explorer avant de structurer.
- **Brouillon fourni :** commencer par un diagnostic et choisir une révision légère, moyenne ou approfondie.
- **URL, citation ou sources :** inventorier les sources avant de les transformer.
- **Demande explicite :** passer au mode ou au contenu dérivé correspondant.

## Protocole d’itération

| Intention | Exemple | Réponse |
|---|---|---|
| Question | « Que penses-tu de la section 2 ? » | Répondre dans le chat sans réécrire le canevas. |
| Suggestion | « Et si nous commencions par cette citation ? » | Évaluer, puis appliquer après accord. |
| Demande | « Réécris l’introduction. » | Renvoyer le canevas complet avec un bref relevé des changements. |
| Exploration | « Propose trois introductions. » | Présenter les variantes sans modifier le canevas. |
| Conversation parallèle | « À propos… » | Explorer la digression et conserver le canevas. |
| Validation | « Gardons cette version. » | Fixer l’état et proposer la prochaine étape. |
| Pause | « Laisse-moi réfléchir. » | Indiquer l’état actuel et s’arrêter. |

Changer de langue ne réécrit pas automatiquement un canevas déjà approuvé.

## Principes éditoriaux

- Croiser technique et sciences humaines.
- Préserver l’honnêteté épistémique, le doute et le caractère provisoire des choix.
- Introduire un désaccord constructif et des nuances.
- Utiliser une métaphore concrète et sensorielle lorsque le sujet s’y prête.
- Terminer par une question ouverte ou un geste modeste.
- Rédiger une note éthique originale pour chaque article : assistance de l’IA déclarée, responsabilité éditoriale humaine et clauses adaptées au sujet.
- Conserver tout le travail éditorial dans le chat.

## Organisation du dépôt

```text
.claude-plugin/marketplace.json           Catalogue du marketplace
plugins/mindandhealth-publish/
  plugin.json                            Source des métadonnées communes
  .claude-plugin/plugin.json              Manifeste compatible avec Claude
  commands/publish.md                    Commande installée
  skills/mindandhealth-publish/           Instructions, modes et références
claude-ai/mindandhealth-publish/          Variante pour le chat
scripts/build_distribution.py            Validation et création du ZIP
.github/workflows/distribution.yml       Vérification et publication des versions
README.fr.md                             Documentation française
README.zh-CN.md                          Documentation en chinois simplifié
```

Le dossier `.claude-plugin/` à la racine décrit le marketplace, pas un second plugin. Dans le plugin, les deux formats de manifeste sont nécessaires pour les clients portables et Claude. Les métadonnées communes proviennent de `plugins/mindandhealth-publish/plugin.json` et sont synchronisées par le script.

## Construction et distribution

Le ZIP se télécharge depuis [Releases](https://github.com/novanoticia/mindandhealth-publish-plugin/releases) ; il n’est plus versionné sur `main`. Pour le construire avec Python 3.10 ou une version ultérieure :

```bash
python3 scripts/build_distribution.py
```

Résultat : `dist/mindandhealth-publish-claude-ai.zip`. Le dossier `dist/` est ignoré par Git. À sources identiques, le ZIP est identique.

Après une modification des métadonnées :

```bash
python3 scripts/build_distribution.py --sync-manifests --check
python3 -m unittest discover -s tests -v
```

Alignez la version du skill avec celle du manifeste portable. Ajoutez les notes dans `docs/releases/<version>.md`, puis publiez un tag `v<version>`. GitHub Actions vérifie le paquet et joint le ZIP à la release. Les versions précédentes du ZIP restent récupérables dans l’historique Git.

## Accès au coffre

La variante Claude Code peut lire les fichiers Markdown du coffre. Chemin par défaut :

```text
~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Pablo's Vault/website/
```

Adaptez la configuration locale dans les instructions du plugin. Aucun contenu n’est écrit dans le coffre.

## Auteur et licence

**Pablo Rodríguez López** — [mindandhealth.org](https://mindandhealth.org). Licence : Apache-2.0.
