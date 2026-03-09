# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By

# Open Chrome browser
driver = webdriver.Chrome()

# Generate a simple login page in browser (no external website needed)
login_page = """
<html>
  <body>
    <h1>Bank Login Page</h1>
    <input type="text" id="username" placeholder="Username">
    <input type="password" id="password" placeholder="Password">
    <button id="login-btn" onclick="login()">Login</button>
    <div id="error-msg" style="color:red; display:none;">Incorrect Password</div>
    <script>
      function login() {
        let user = document.getElementById('username').value;
        let pass = document.getElementById('password').value;
        if (user === 'user123' && pass === 'pass123') {
          document.body.innerHTML = '<h1>Login Successful!</h1>';
        } else {
          document.getElementById('error-msg').style.display = 'block';
        }
      }
    </script>
  </body>
</html>
"""

# Load the local login page
driver.get("data:text/html," + login_page)

# ========== TC-001: Valid Login ==========
print("Test 1: Valid Login - Expected Pass")
driver.find_element(By.ID, "username").send_keys("user123")
driver.find_element(By.ID, "password").send_keys("pass123")
driver.find_element(By.ID, "login-btn").click()
# Verify login success
if "Login Successful!" in driver.page_source:
    print("Test 1 Result: Pass")
else:
    print("Test 1 Result: Fail")

# ========== TC-002: Invalid Password ==========
print("\nTest 2: Invalid Password - Expected Fail (No error message)")
driver.get("data:text/html," + login_page)  # Back to login page
driver.find_element(By.ID, "username").send_keys("user123")
driver.find_element(By.ID, "password").send_keys("wrong123")  # Wrong password
driver.find_element(By.ID, "login-btn").click()
# Verify error message (simulate bug for Jira)
try:
    error_msg = driver.find_element(By.ID, "error-msg").text
    if "Incorrect Password" in error_msg:
        print("Test 2 Result: Pass (Error message shown)")
    else:
        print("Test 2 Result: Fail (No error message, Jira Bug TC-002)")
except:
    print("Test 2 Result: Fail (No error message, Jira Bug TC-002)")

# Close browser
driver.quit()
print("\nAll Tests Completed!")