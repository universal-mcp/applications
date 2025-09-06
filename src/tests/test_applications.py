from universal_mcp.applications.zenquotes import ZenquotesApp

def test_zenquotes():
    app = ZenquotesApp()
    quote = app.get_quote()
    assert quote is not None
    assert quote != ""