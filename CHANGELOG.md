# Changelog

Todos los cambios relevantes del plugin/skill `mindandhealth-publish` se documentan aquí. Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/); versionado [SemVer](https://semver.org/lang/es/) (mayor = ruptura, menor = ampliación, parche = correcciones).

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
