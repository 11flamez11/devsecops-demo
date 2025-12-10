def test_security():
    """Проверка что нет debug режима"""
    import app
    assert not app.DEBUG