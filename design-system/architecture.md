# Design system architecture

How to structure a design system so it stays small, consistent and easy for people and agents to follow. Framework-neutral guidance, based on how I built my own design system and on atomic design (Brad Frost). In a real project, `artefacts/07-design-system-rules.md` records the choices made and takes precedence.

## 1. Build in layers

Each layer may use the layers below it, never the ones above. Dependencies point one way.

| Layer | What it is | Examples |
|---|---|---|
| Tokens | Colour, type, spacing, radius, motion. Defined once, named by role | `color.content.primary`, spacing scale |
| Atoms | The smallest interactive or visual parts | button, input, checkbox, icon |
| Molecules | Atoms combined for one job | form field (label, input, hint, error), date picker, notification |
| Organisms | Sections that make sense on their own | table, card, navigation, form |
| Templates | Page layouts with no real content | form page, dashboard |
| Pages and examples | Templates with real content, used to test the system | an example app shell |

If a component needs something from a higher layer, the layers are wrong. Move the shared part down.

### Naming the layers for developers

Atomic design terms (atoms, molecules, organisms) are familiar to many designers, but developers often expect a plain `components/` folder. So:

- **Keep the root folder `components/`.** Do not rename it, and do not add suffixes such as `atom-components`.
- **Do not put the layer in the folder path.** Organise code by type (section 2). Layers *explain* the system, they do not *locate* files. A component's layer can change: a button gains an icon and a loading state, and is it still an atom? With the layer in the path, a change means renaming imports across the codebase.
- **In documentation, name each layer in plain words, with the atomic term in brackets the first time:** Basic components (atoms), Composite components (molecules), Sections (organisms), Page layouts (templates). After that, use whichever the team prefers.
- **Follow the team's existing convention.** If the codebase already uses `components/ui` for basic components (the default in shadcn/ui), keep it. Write the mapping down in `artefacts/07-design-system-rules.md`.

## 2. Folders: organise code by type, show the layers in the docs

Two ways to organise components. Choose one per project and write it down in `07`.

- **By type** (`buttons/`, `forms/`, `cards/`, `navigation/`, `table/`, `icons/`): easy to find by what a thing *is*. Developers search this way.
- **By layer** (`atoms/`, `molecules/`, `organisms/`): shows the dependency order, but forces arguments about whether something is an atom or a molecule.

**Recommended:** organise the code by type, and group the documentation pages by layer. That is how my own system works. Developers find things by what they are, and the layers still teach how the system is built.

```
tokens/              tokens.json is the source, CSS variables come from it
components/
  buttons/           Button, IconButton
  forms/             Input, Select, Checkbox, Radio, Field, FormSection
  navigation/        Header, Tabs, Breadcrumb
  cards/
  table/
  notifications/
  icons/
docs/                components that exist only to build the documentation site
pages/               documentation, grouped by layer: basic, composite, sections, page layouts
```

Names are examples. Use the project's own component types, plural, and keep them consistent.

## 3. Inside a component

Keep what belongs to one component together: the component, its tests, and its documentation or stories. Every component has its states designed (default, hover, focus, disabled, loading, error where relevant) and meets the accessibility baseline in `rules.md`.

## 4. Keep system components and documentation components apart

Components that exist only to build the documentation site go in their own folder (`docs/`). Do not mix them with system components. A component's API must not include props that only serve the documentation site. If a component only makes sense inside this repository, it is not part of the system.

## 5. One source of truth for tokens

- `tokens.json` is the source. Everything else is derived or checked against it.
- Two layers: **primitives** (raw values) and **semantic** tokens (named by role). Components use only semantic tokens.
- Avoid keeping two hand-edited copies of the same values, for example a token file and a stylesheet. In my own system I maintain both by hand and they can drift apart. Generating one from the other removes that risk.

## 6. Naming

- Name components and tokens by **purpose**, not appearance: `Alert`, not `RedBox`; `color.feedback.error-content`, not `red-700`.
- Folder names are the component type, plural and lowercase.
- One name for one thing across design files, code and documentation.

## 7. Adding a component: reuse before you create

Every addition has to be learned, documented and maintained. Before adding:

1. Can an existing component do the job? If it almost can, improve it.
2. Can it be built by combining existing components? Then compose, do not add.
3. If it is genuinely new: name it by purpose, keep the API small, design every state, apply the accessibility baseline, and write a documentation page.
4. Record the decision in the decision log if it affects other people.

Changing an existing component's API, a token value or the folder structure needs the owner's approval first.

## 8. One documentation page per component

Use one page template for every component so pages stay consistent. Each page covers: what it is for, when not to use it, variants, states, accessibility notes, and the design name beside the code name.

## 9. Keep it small, and keep a record

- Fewer, well-explained parts beat many similar ones. Remove what is unclear or unused.
- Log changes in a version history in plain language, one entry per day, so someone outside the project can follow what changed and why.

## Before you add or move something

- [ ] An existing component cannot do this, and composition does not work
- [ ] It sits in the right layer and the right type folder
- [ ] It uses semantic tokens only, with no raw values
- [ ] All states are designed and the accessibility baseline is met
- [ ] It has a documentation page with "when not to use"
- [ ] The owner approved any API, token or folder structure change
