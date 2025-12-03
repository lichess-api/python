def test_imports():
    import lichess

    assert lichess

    from lichess import client, models, LichessClient

    assert client
    assert models
    assert LichessClient
