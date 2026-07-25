import runpy
import sys
import types
from pathlib import Path


class Session(dict):
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError as exc:
            raise AttributeError(name) from exc

    def __setattr__(self, name, value):
        self[name] = value


class Dummy:
    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def __call__(self, *args, **kwargs):
        return self

    def __getattr__(self, name):
        return self


class FakeStreamlit(types.ModuleType):
    def __init__(self):
        super().__init__("streamlit")
        self.session_state = Session(experience_mode="Beginner", saved_prompts=[])
        self.sidebar = Dummy()

    def columns(self, spec, *args, **kwargs):
        count = spec if isinstance(spec, int) else len(spec)
        return [Dummy() for _ in range(count)]

    def tabs(self, labels):
        return [Dummy() for _ in labels]

    def form(self, *args, **kwargs):
        return Dummy()

    def expander(self, *args, **kwargs):
        return Dummy()

    def container(self, *args, **kwargs):
        return Dummy()

    def selectbox(self, label, options, *args, **kwargs):
        return list(options)[0] if options else None

    def multiselect(self, label, options, default=None, *args, **kwargs):
        return default or []

    def radio(self, label, options, index=0, *args, **kwargs):
        if index is None:
            return None
        return list(options)[index]

    def checkbox(self, label, value=False, *args, **kwargs):
        return value

    def text_input(self, *args, value="", **kwargs):
        return value

    def text_area(self, *args, value="", **kwargs):
        return value

    def select_slider(self, label, options, value=None, *args, **kwargs):
        return value if value is not None else list(options)[0]

    def number_input(self, label, *args, value=None, **kwargs):
        return value if value is not None else (args[0] if args else 0)

    def button(self, *args, **kwargs):
        return False

    def form_submit_button(self, *args, **kwargs):
        return False

    def download_button(self, *args, **kwargs):
        return False

    def Page(self, *args, **kwargs):
        return Dummy()

    def navigation(self, *args, **kwargs):
        return Dummy()

    def __getattr__(self, name):
        return lambda *args, **kwargs: Dummy()


def test_all_pages_execute_with_streamlit_stub(monkeypatch):
    fake = FakeStreamlit()
    components = types.ModuleType("streamlit.components")
    components_v1 = types.ModuleType("streamlit.components.v1")
    components_v1.html = lambda *args, **kwargs: None
    components.v1 = components_v1
    fake.components = components
    monkeypatch.setitem(sys.modules, "streamlit", fake)
    monkeypatch.setitem(sys.modules, "streamlit.components", components)
    monkeypatch.setitem(sys.modules, "streamlit.components.v1", components_v1)

    root = Path(__file__).resolve().parents[1]
    for page in sorted((root / "pages").glob("[0-9][0-9]_*.py")):
        runpy.run_path(str(page), run_name=f"smoke_{page.stem}")
