import asyncio
from patchright.async_api import async_playwright
import random
import string
import requests
import re
import argparse
from colorama import init, Fore, Style
import time

# Initialize colorama for colored console output
init(autoreset=True)

# Create session for API requests
session = requests.Session()

# Helper Functions
def generate_realistic_name():
    """Generate a realistic name for Discord."""
    first_names = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones"]
    first = random.choice(first_names)
    last = random.choice(last_names)
    return f"{first}{random.randint(1, 999)}"

def generate_username(global_name):
    """Generate a username from global name."""
    base = global_name.replace(" ", "").lower()
    return f"{base}{random.randint(1000, 9999)}"

def generate_alternative_username(base_username):
    """Generate an alternative username if the original is taken."""
    return f"{base_username}{random.randint(10000, 99999)}"

def generate_strong_password():
    """Generate a strong password."""
    chars = (random.choices(string.ascii_lowercase, k=6) +
             random.choices(string.ascii_uppercase, k=2) +
             random.choices(string.digits, k=2) +
             random.choices("!@#$%^&*", k=1))
    random.shuffle(chars)
    return "".join(chars)

def get_email():
    """Fetch a temporary email from tempmail.lol."""
    try:
        r = session.get('https://api.tempmail.lol/generate').json()
        return r.get("address"), r.get("token")
    except Exception as e:
        print(f"{Fore.RED}Error fetching email: {str(e)}")
        return f"fallback{random.randint(100, 999)}@gmail.com", None

async def get_verification_link(email_token):
    """Retrieve the verification link from email."""
    for _ in range(15):
        try:
            r = session.get(f"https://api.tempmail.lol/v2/inbox?token={email_token}").json()
            emails = r.get("emails", [])
            for email in emails:
                if "Verify Email Address for Discord" in email.get("subject", ""):
                    body = email.get("body", "")
                    links = re.findall(r'https://click\.discord\.com/ls/click\?[^"]+', body)
                    if links:
                        return links[0]
        except Exception as e:
            print(f"{Fore.YELLOW}Error checking email: {str(e)}")
        await asyncio.sleep(4)
    return None

# Main Functions
async def fill_registration_form(page, email, global_name, username, password):
    """Fill the Discord registration form."""
    print(f"{Fore.CYAN}Filling registration form for {username}...")
    await page.goto("https://discord.com/register")
    await page.locator("input[name='email']").fill(email)
    await page.locator("input[name='global_name']").fill(global_name)

    # Handle username conflicts
    for _ in range(5):
        await page.locator("input[name='username']").fill(username)
        await asyncio.sleep(1)
        error = await page.evaluate("""() => document.querySelector('[class*="errorMessage"]')?.textContent""")
        if not error or "Username is unavailable" not in error:
            break
        username = generate_alternative_username(username)
        print(f"{Fore.YELLOW}Username taken, trying new username: {username}")

    await page.locator("input[name='password']").fill(password)

    # Select date of birth (April 1999)
    await page.locator(".month_b0f4cc").click()
    await page.locator("[id*='-option-4']").first.click()
    await page.locator(".day_b0f4cc").click()
    await page.locator("[id*='-option-4']").first.click()
    await page.locator(".year_b0f4cc").click()
    await page.locator("div[class*='option']").filter(has_text="1999").first.click()

    # Click checkbox and submit
    await page.locator("input[type='checkbox']").click()
    await page.locator("button[type='submit']").click()

    # Check for errors after submission
    await asyncio.sleep(2)
    error_message = await page.evaluate("""() => document.querySelector('[class*="errorMessage"]')?.textContent""")
    if error_message:
        print(f"{Fore.RED}Registration error for {username}: {error_message}")
        return False, username
    return True, username

async def handle_verification(context, email_token):
    """Handle email verification."""
    print(f"{Fore.CYAN}Waiting for verification link...")
    verification_link = await get_verification_link(email_token)
    if verification_link:
        verification_page = await context.new_page()
        await verification_page.goto(verification_link)
        await verification_page.wait_for_load_state('networkidle')
        
        # Wait for 5 seconds before closing the verification tab
        await asyncio.sleep(10)
        
        # Close the verification page after waiting
        await verification_page.close()
        print(f"{Fore.GREEN}Verification completed.")
        return True  # Indicate that verification was successful
    return False  # Indicate that verification failed


async def get_discord_token(page):
    """Extract Discord token from localStorage or cookies."""
    try:
        token_script = """
        () => {
            function getToken() {
                try {
                    // Try localStorage first
                    let token = window.localStorage.getItem('token');
                    if (token) return token;

                    // Try sessionStorage
                    token = window.sessionStorage.getItem('token');
                    if (token) return token;

                    // Try cookies
                    const cookies = document.cookie.split(';');
                    for (const cookie of cookies) {
                        const [name, value] = cookie.trim().split('=');
                        if (name === 'token') return value;
                    }

                    // If still not found, try to get from webpack
                    if (window.webpackChunkdiscord_app) {
                        const findTokenInModules = (modules) => {
                            for (const m of Object.values(modules)) {
                                if (!m.exports) continue;
                                if (m.exports.default?.getToken) {
                                    const t = m.exports.default.getToken();
                                    if (t) return t;
                                }
                                if (m.exports?.getToken) {
                                    const t = m.exports.getToken();
                                    if (t) return t;
                                }
                            }
                            return null;
                        };

                        // Try existing chunks
                        const chunk = window.webpackChunkdiscord_app;
                        if (chunk.length > 0) {
                            for (const item of chunk) {
                                if (item[1] && item[1].c) {
                                    const t = findTokenInModules(item[1].c);
                                    if (t) return t;
                                }
                            }
                        }

                        // Try pushing new chunk
                        let webpackToken = null;
                        chunk.push([
                            [Math.random()],
                            {},
                            (req) => {
                                if (req.c) {
                                    const t = findTokenInModules(req.c);
                                    if (t) webpackToken = t;
                                }
                            }
                        ]);
                        if (webpackToken) return webpackToken;
                    }

                    return null;
                } catch (e) {
                    console.error('Error in getToken:', e);
                    return null;
                }
            }

            return getToken();
        }
        """

        # รอให้หน้าเว็บโหลดเสร็จ
        await page.wait_for_load_state('networkidle', timeout=30000)
        await asyncio.sleep(5)  # รอให้ JavaScript โหลดเสร็จ

        # ลองดึง token จาก localStorage ก่อน
        token = await page.evaluate("window.localStorage.getItem('token')")
        if token and len(token) > 50:
            print(f"{Fore.GREEN}Found token in localStorage: {token[:30]}...")
            return token

        # ลองดึงจาก sessionStorage
        token = await page.evaluate("window.sessionStorage.getItem('token')")
        if token and len(token) > 50:
            print(f"{Fore.GREEN}Found token in sessionStorage: {token[:30]}...")
            return token

        # ลองดึงจาก cookies
        cookies = await page.context.cookies()
        for cookie in cookies:
            if cookie.get('name') == 'token' and len(cookie.get('value', '')) > 50:
                print(f"{Fore.GREEN}Found token in cookies: {cookie['value'][:30]}...")
                return cookie['value']

        # ถ้ายังไม่เจอ ลองใช้ script ที่รวมทุกวิธี
        print(f"{Fore.YELLOW}Trying alternative token extraction methods...")
        token = await page.evaluate(token_script)
        
        if token and len(token) > 50:
            print(f"{Fore.GREEN}Found token using alternative method: {token[:30]}...")
            return token

        # ถ้ายังไม่เจอ ลองดูใน network requests
        print(f"{Fore.YELLOW}Checking network requests for token...")
        async def handle_response(response):
            if 'api/v9/auth' in response.url:
                try:
                    json_data = await response.json()
                    if 'token' in json_data:
                        return json_data['token']
                except:
                    pass
            return None

        page.on('response', handle_response)
        await asyncio.sleep(2)  # รอให้มีการส่ง request

        print(f"{Fore.YELLOW}Token not found in any location")
        return None

    except Exception as e:
        print(f"{Fore.RED}Error retrieving token: {str(e)}")
        return None


async def register_discord_account(headless=False):
    """Register a single Discord account."""
    print(f"\n{Fore.GREEN}=== Starting new account registration ===")
    global_name = generate_realistic_name()
    username = generate_username(global_name)
    password = generate_strong_password()
    email, email_token = get_email()

    print(f"{Fore.CYAN}Generated details:")
    print(f"  Global Name: {global_name}")
    print(f"  Username: {username}")
    print(f"  Password: {password}")
    print(f"  Email: {email}")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=headless)
        context = await browser.new_context(viewport={"width": 810, "height": 840})
        page = await context.new_page()

        try:
            # Fill and submit registration form
            success, username = await fill_registration_form(page, email, global_name, username, password)
            if not success:
                return False

            print(f"{Fore.GREEN}Successfully registered {username}!")

            # Handle email verification
            if email_token:
                verification_success = await handle_verification(context, email_token)
                if verification_success:
                    print(f"{Fore.GREEN}Email verified successfully for {username}!")
                    # Now that verification is done, retrieve the token
                    token = await get_discord_token(page)
                    if token:
                        print(f"{Fore.GREEN}Token for {username}: {token}")
                        with open("token-work.txt", "a") as f:
                            f.write(f"{email}:{password}:{token}\n")  # Save email instead of username
                        print(f"{Fore.GREEN}Saved token for {email} to token-work.txt")  # Print email instead of username
                        print(f"{Fore.GREEN}Saved token for {username} to token-work.txt")
                    else:
                        print(f"{Fore.RED}Failed to retrieve token for {username}")
                else:
                    print(f"{Fore.YELLOW}Verification failed for {username}")
            else:
                print(f"{Fore.YELLOW}No email token available for {username}")

            return True
        except Exception as e:
            print(f"{Fore.RED}Error during registration for {username}: {str(e)}")
            return False
        finally:
            await asyncio.sleep(5)
            await browser.close()

async def main(num_accounts, headless, infinite_loop=False):
    """Run the Discord account registration process."""
    print(f"{Fore.MAGENTA}=== Discord Account Registration Bot ===")
    success_count = 0
    attempt_count = 0

    while True:
        if not infinite_loop and attempt_count >= num_accounts:
            break

        attempt_count += 1
        print(f"\n{Fore.BLUE}Attempt #{attempt_count}...")

        success = await register_discord_account(headless)
        if success:
            success_count += 1

        print(f"\n{Fore.MAGENTA}Summary: {success_count}/{attempt_count} accounts created successfully")
        
        # If infinite_loop is True, keep repeating the registration process indefinitely.
        if infinite_loop:
            print(f"{Fore.YELLOW}Waiting 2 minutes before next attempt...")
            await asyncio.sleep(120)  # Wait 5 minutes before next attempt
        else:
            if attempt_count < num_accounts:
                print(f"{Fore.YELLOW}Waiting 2 minutes before next attempt...")
                await asyncio.sleep(120)  # Wait 5 minutes between attempts

    print(f"\n{Fore.GREEN}All tasks completed! Total: {success_count}/{attempt_count} accounts created.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated Discord Account Registration Bot")
    parser.add_argument("--num-accounts", type=int, default=1, help="Number of accounts to register (default: 1)")
    parser.add_argument("--headless", action="store_true", help="Run browser in headless mode")
    parser.add_argument("--infinite", action="store_true", help="Run in infinite loop")
    args = parser.parse_args()

    asyncio.run(main(args.num_accounts, args.headless, args.infinite))
