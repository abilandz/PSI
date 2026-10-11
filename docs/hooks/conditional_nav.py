def on_config(config):
    """
    Conditionally change the navigation depending on the theme.
    Remark: Each time I change something here, I have to restart: mkdocs serve (it won't update automatically)
    """
    theme_name = config.theme.name

    if theme_name == "material": # Navigation for "Material"
        config.nav = [
            {"Introduction": "index.md"}, # this file "index.md" must be in docs/
            {"Semester": [
                {"WS 2026/27": "src/WS_2026_2027.md"},
                {"SS 2026": "src/SS_2026.md"},
                {"WS 2025/26": "src/WS_2025_2026.md"},
            ]},
            {"Organizers": "src/organizers.md"},
        ]

    elif theme_name == "mkdocs": # Navigation for theme "bootstrap" theme (the default theme, but I have to use "mkdocs", not "bootstrap" as the name here)
        config.nav = [
            {"Introduction": "index.md"}, # this file "index.md" must be in docs/
        ]

    elif theme_name == "readthedocs": # Different structure for "ReadTheDocs" theme
        config.nav = [
            {"Introduction": "index.md"}, # this file "index.md" must be in docs/
        ]

    else: # Optional: fallback for unknown themes
        config.nav = [
            {"Home": "index.md"},
        ]

    return config
