from playwright.sync_api import sync_playwright

class PlaywrightHelper:
    def __init__(self, headless=True):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        print("🚀 Browser launched")

    def navigate_to(self, url):
        self.page.goto(url)
        print(f"🌍 Navigated to {url}")

    def click(self, selector):
        self.page.click(selector)
        print(f"🖱️ Clicked: {selector}")

    def type(self, selector, text, clear=True):
        if clear:
            self.page.fill(selector, "")
        self.page.type(selector, text)
        print(f"⌨️ Typed '{text}' into {selector}")

    def get_text(self, selector):
        text = self.page.inner_text(selector)
        print(f"📋 Text from {selector}: {text}")
        return text

    def is_visible(self, selector):
        visible = self.page.is_visible(selector)
        print(f"👀 Visible {selector}: {visible}")
        return visible

    def wait_for(self, selector, timeout=5000):
        self.page.wait_for_selector(selector, timeout=timeout)
        print(f"⏳ Waited for {selector}")

    def screenshot(self, path="screenshot.png"):
        self.page.screenshot(path=path)
        print(f"📸 Screenshot saved to {path}")

    def assert_text(self, selector, expected_text):
        actual = self.get_text(selector)
        assert expected_text in actual, f"❌ Expected '{expected_text}' in '{actual}'"
        print(f"✅ Text matched in {selector}")

    def select(self, selector, value):
        self.page.select_option(selector, value=value)
        print(f"🎯 Selected '{value}' from {selector}")

    def get_cookies(self):
        cookies = self.context.cookies()
        print(f"🍪 Cookies: {cookies}")
        return cookies

    def set_cookie(self, cookie_dict):
        self.context.add_cookies([cookie_dict])
        print(f"➕ Cookie added: {cookie_dict}")

    def new_tab(self):
        self.page = self.context.new_page()
        print("🗂️ New tab opened")

    def close(self):
        self.browser.close()
        self.playwright.stop()
        print("🛑 Browser closed")