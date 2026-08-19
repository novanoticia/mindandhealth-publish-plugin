# Changelog

Todos los cambios relevantes del plugin/skill `mindandhealth-publish` se documentan aquí. Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/); versionado [SemVer](https://semver.org/lang/es/) (mayor = ruptura, menor = ampliación, parche = correcciones).

## [1.2.0] — 2026-08-19

### Cambiado
- **La variante de chat pasa a llamarse `mindandhealth-publish-chat`** (`claude-ai/mindandhealth-publish/SKILL.md`). Antes las dos variantes del repositorio declaraban `name: mindandhealth-publish`, lo que hace que cualquier herramienta que recorra el repositorio completo (conversores, empaquetadores, validadores) aborte por conflicto de nombre: dos skills no pueden reclamar el mismo nombre publicado. La variante de plugin conserva `mindandhealth-publish`, de modo que el marketplace, el slash command `/publish` y las instalaciones existentes de Claude Code no se ven afectados.
- Bundle `mindandhealth-publish-claude-ai.zip` regenerado: la carpeta interna pasa de `mindandhealth-publish/` a `mindandhealth-publish-chat/`.
- README: nueva tabla «Las dos variantes», árbol de arquitectura anotado con el `name` de cada una y ruta de Mistral actualizada.

### Migración
- **Claude.ai / Perplexity / Mistral:** desinstala el skill anterior y vuelve a subir el bundle. Aparecerá como `mindandhealth-publish-chat`. Los gatillos en lenguaje natural no cambian.
- **Claude Code:** nada que hacer.

### Notas
- Sin cambios de comportamiento del skill en ninguna de las dos variantes.
- Las dos copias siguen manteniéndose a mano y han divergido en cuatro archivos (`SKILL.md`, `modes/generate.md`, `modes/transform.md`, `references/mapa-tematico.md`). Parte de esa divergencia es deliberada (acceso al vault) y parte es deriva. Pendiente: generar la variante de chat desde la de plugin con un script de build.

## [1.1.0] — 2026-06-10

### Añadido
- Compatibilidad de instalación del skill con **Mistral AI** (espacio *Work*): descomprimir el bundle y seleccionar la carpeta `mindandhealth-publish/`. Documentada en el README.

### Cambiado
- **`claude-ai/mindandhealth-publish/SKILL.md` — `description` reducida a 453 caracteres / 458 bytes** (antes 708) para cumplir el límite de 500 caracteres que aplica Mistral, conservando los gatillos de activación en lenguaje natural; pasa a bloque escalar YAML (`>-`). Bundle `mindandhealth-publish-claude-ai.zip` regenerado.
- README: nota técnica actualizada con los límites por plataforma (Perplexity 1024 bytes, Mistral 500 caracteres).

### Notas
- Sin cambios de comportamiento del skill; el salto refleja la ampliación de plataformas soportadas.

## [1.0.0] — versión inicial

### Añadido
- Skill de acompañamiento editorial conversacional para mindandhealth.org (Obsidian Publish): modos, derivados (newsletter LinkedIn, post de feed, prompt de imagen) y pie ético de variación controlada. Disponible como plugin de Claude Code y como bundle subible a Claude.ai y Perplexity.
