"""Reflex custom component Monaco."""

# For wrapping react guide, visit https://reflex.dev/docs/wrapping-react/overview/

import reflex as rx


class MonacoComponent(rx.Component):
    """Base Monaco component."""

    library = "@monaco-editor/react@4.7.0"

    # The language to use for the editor.
    language: rx.Var[str]

    # The theme to use for the editor.
    theme: rx.Var[str] = rx.color_mode_cond("light", "vs-dark")

    # The options, refer to Monaco interface IStandaloneEditorConstructionOptions at
    # https://microsoft.github.io/monaco-editor/docs.html#interfaces/editor.IStandaloneEditorConstructionOptions.html
    options: rx.Var[dict]
    
    # The line to jump to in the editor.
    line: rx.Var[int] = rx.Var.create(1)

    # The height of the editor.
    width: rx.Var[str]

    # The height of the editor.
    height: rx.Var[str]


class MonacoEditor(MonacoComponent):
    """The Monaco Editor component."""

    tag = "MonacoEditor"

    is_default = True

    # The default value to display in the editor.
    default_value: rx.Var[str]

    # The default language to use for the editor.
    default_language: rx.Var[str]

    # The path to the default file to load in the editor.
    default_path: rx.Var[str]

    # The value to display in the editor.
    value: rx.Var[str]

    # Triggered when the editor value changes.
    on_change: rx.EventHandler[rx.event.passthrough_event_spec(str)]

    # Triggered when the content is validated. (limited to some languages)
    on_validate: rx.EventHandler[rx.event.passthrough_event_spec(str)]


class DiffMonacoEditor(MonacoComponent):
    """The Monaco Diff Editor component."""

    tag = "DiffEditor"

    # The original value to display in the editor.
    original: rx.Var[str]

    # The modified value to display in the editor.
    modified: rx.Var[str]

    # The language to use for the original editor. (left pane)
    original_language: rx.Var[str]

    # The language to use for the modified editor. (right pane)
    modified_language: rx.Var[str]

    # The path to the original file to load in the editor.
    original_model_path: rx.Var[str]

    # The path to the modified file to load in the editor.
    modified_model_path: rx.Var[str]

    # Whether to keep the original model.
    keep_current_original_model: rx.Var[bool]

    # Whether to keep the modified model.
    keep_current_modified_model: rx.Var[bool]


monaco = MonacoEditor.create
monaco_diff = DiffMonacoEditor.create
