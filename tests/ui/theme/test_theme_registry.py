import pytest


@pytest.fixture
def registry(tmp_path, monkeypatch):
    monkeypatch.setattr(
        "ui.theme.theme_registry.ThemeRegistry.STORAGE_DIR", str(tmp_path)
    )
    fake_themes = {}
    monkeypatch.setattr("ui.theme.theme_registry.THEMES", fake_themes)

    from ui.theme.theme_registry import ThemeRegistry

    return ThemeRegistry()


def test_theme_exists_returns_name_when_found(registry, monkeypatch):
    fake_themes = {"dark": {"bg": "#000"}}
    monkeypatch.setattr("ui.theme.theme_registry.THEMES", fake_themes)
    result = registry.theme_exists({"bg": "#000"})
    assert result == "dark"


def test_theme_exists_returns_none_when_not_found(registry, monkeypatch):
    fake_themes = {"dark": {"bg": "#000"}}
    monkeypatch.setattr("ui.theme.theme_registry.THEMES", fake_themes)
    result = registry.theme_exists({"bg": "#ffffff"})

    assert result is None


def test_add_custom_returns_name(registry, monkeypatch):
    fake_themes = {}
    monkeypatch.setattr("ui.theme.theme_registry.THEMES", fake_themes)
    result = registry.add_custom("name_string", {})

    assert result == "name_string"


def test_add_custom_returns_name_andone(registry, monkeypatch):
    fake_themes = {"name_string": {"bg": "#000"}}
    monkeypatch.setattr("ui.theme.theme_registry.THEMES", fake_themes)
    result = registry.add_custom("name_string", {})

    assert result == "name_string-1"


def test_load_existing_loads_themes_when_files_exist(registry, tmp_path, monkeypatch):
    theme_file = tmp_path / "my_theme.json"
    theme_file.write_text('{"bg": "#000"}', encoding="utf8")

    fake_themes = {}
    monkeypatch.setattr("ui.theme.theme_registry.THEMES", fake_themes)
    monkeypatch.setattr(
        "ui.theme.theme_registry.ThemeRegistry.STORAGE_DIR", str(tmp_path)
    )

    registry._load_existing()

    assert fake_themes == {"my_theme": {"bg": "#000"}}


def test_load_existing_loads_themes_when_files_no_exist(
    registry, tmp_path, monkeypatch
):
    fake_themes = {}
    monkeypatch.setattr("ui.theme.theme_registry.THEMES", fake_themes)
    monkeypatch.setattr(
        "ui.theme.theme_registry.ThemeRegistry.STORAGE_DIR", str(tmp_path)
    )

    registry._load_existing()

    assert fake_themes == {}


def test_load_existing_loads_themes_when_file_name_matches(
    registry, tmp_path, monkeypatch
):
    theme_file = tmp_path / "my_theme.json"
    theme_file.write_text('{"bg": "#111"}', encoding="utf8")
    fake_themes = {"my_theme": {"bg": "#000"}}
    monkeypatch.setattr("ui.theme.theme_registry.THEMES", fake_themes)

    registry._load_existing()

    assert fake_themes == {"my_theme": {"bg": "#000"}}


def test_load_existing_loads_themes_when_file_no_valid(registry, tmp_path, monkeypatch):
    theme_file = tmp_path / "my_theme.json"
    theme_file.write_text("это не json", encoding="utf8")
    logged = []
    monkeypatch.setattr(
        "ui.theme.theme_registry.log_event", lambda msg: logged.append(msg)
    )

    registry._load_existing()

    assert len(logged) > 0
