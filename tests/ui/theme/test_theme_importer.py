import pytest
from contextlib import nullcontext as does_not_raise
from ui.theme.theme_importer import ThemeImporter, _rgba_to_hex, _normalize_color, _lighten, _inverse_bw



def test_rgba_to_hex_valid():
    result = _rgba_to_hex("rgba(40,42,54,0.95)")
    assert result == "#282A36"


def test_rgba_to_hex_no_valid():
    result = _rgba_to_hex("rgba(40,42)")
    assert result == "#000000"


def test_normalize_color_returns_none():
    result = _normalize_color("tu_040x42")
    assert result is None

def test_normalize_color_returns_hex():
    result = _normalize_color("#282A36")
    assert result == "#282A36"

def test_normalize_color_returns_again():
    result = _normalize_color("rgba(40,42,54,0.95)")
    assert result == "#282A36"

def test_lighten_no_valid():
    result = _lighten("000000")
    assert result == "000000"


def test_lighten_valid():
    result = _lighten("#353535")
    assert result == "#535353"


def test_inverse_bw_no_valid():
    result = _inverse_bw("000000")
    assert result == "#000000"

def test_invers_bw_if_light():
    result = _inverse_bw("#FFF5D6")
    assert result == "#000000"


def test_invers_bw_if_dark():
    result = _inverse_bw("#5E0000")
    assert result == "#FFFFFF"


@pytest.fixture
def importer():
    return ThemeImporter()


def test_load_json_valid(importer, tmp_path):
    theme_file = tmp_path / "theme.json"
    theme_file.write_text('{"colors": {}}', encoding="utf8")

    result = importer._load_json(str(theme_file))

    assert result == {"colors": {}}


def test_load_json_broken(importer, tmp_path):
    theme_file = tmp_path / "theme.json"
    theme_file.write_text("это не json", encoding="utf8")
    with pytest.raises(Exception):
        importer._load_json(str(theme_file))


def test_load_json_empty(importer):
    with pytest.raises(Exception):
        importer._load_json("несуществующий/путь/theme.json")


def test_extract_comfy_base_keys(importer):
    result = importer._extract_comfy_base({"colors": {"comfy_base": {"bg": "#000"}}})
    assert result == {"bg": "#000"}

def test_extract_comfy_base_no_keys(importer):
    result = importer._extract_comfy_base({})
    assert result == {}

def test_map_to_tokens_key_not_fit(importer):
    result = importer._map_to_tokens({"не подходит": "#000000"})
    assert result["bg_header"] is None

def test_map_to_tokens_key_fit_value_valid(importer):
    result = importer._map_to_tokens({"bg-color": "#010101"})
    assert result["bg_header"] == "#010101"

def test_map_to_tokens_key_fit_value_no_valid(importer):
    result = importer._map_to_tokens({"bg-color": "rgba(1,1,1,1)"})
    assert result["bg_header"] == "#010101"



