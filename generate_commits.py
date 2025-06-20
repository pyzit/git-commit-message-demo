import os
import subprocess
import random
import time

# Professional commit titles
PROFESSIONAL_COMMITS = [
    "feat(auth): implement JWT-based authentication",
    "feat(api): add pagination to user endpoint",
    "fix(auth): handle expired access tokens properly",
    "fix(db): resolve deadlock in user creation flow",
    "docs(readme): add setup instructions for local dev",
    "docs(changelog): update for v1.2.0 release",
    "chore(deps): bump Flask to 2.3.2",
    "chore(env): rename .env.example for clarity",
    "refactor(router): separate public and private routes",
    "refactor(auth): simplify token validation logic",
    "test(api): add integration tests for /login",
    "test(auth): mock external OAuth provider",
    "perf(cache): add Redis caching to dashboard API",
    "perf(db): optimize query performance for reports",
    "style: apply consistent formatting with Black",
    "build(ci): configure GitHub Actions for test suite",
    "feat(profile): allow users to upload profile pictures",
    "feat(settings): add user preferences for notifications",
    "fix(validation): sanitize email inputs",
    "fix(ui): align modal content on mobile",
    "docs(contributing): add pull request template",
    "chore: remove unused dependencies from requirements.txt",
    "refactor(forms): split login and signup forms",
    "test(forms): add tests for edge-case inputs",
    "feat(notifications): integrate email alerts for new logins",
    "feat(api): support batch user import via CSV",
    "fix(logger): prevent sensitive data from being logged",
    "docs(env): document required secrets in README",
    "style(css): remove redundant styles from layout.css",
    "chore(cleanup): delete old migration files",
    "build(deploy): add Dockerfile for staging environment",
    "feat(stats): add analytics dashboard for admins",
    "fix(timezone): normalize user activity logs to UTC",
    "refactor(settings): extract config into settings module",
    "perf(images): compress avatar uploads before saving",
    "test(payments): stub Stripe API for CI runs",
    "chore(db): create user_sessions table migration",
    "fix(api): return correct status codes for auth errors",
    "docs(openapi): regenerate docs with latest schemas",
    "feat(admin): allow deactivating user accounts",
    "test(admin): ensure role permissions are enforced",
    "style(html): clean up indentation in base template",
    "build(ci): add caching to reduce build times",
    "fix(ui): improve responsiveness of sidebar nav",
    "refactor(api): decouple auth logic from views",
    "feat(invitations): send email invites with expiration",
    "chore(config): use dotenv for config loading",
    "docs(security): add policy for handling credentials",
    "fix(passwords): enforce minimum length validation",
    "feat(auth): add Google login via OAuth2"
]

# Optional commit bodies
BODIES = [
    "This change introduces necessary logic for validating JWT tokens, including handling for expired and invalid tokens.",
    "Ensures paginated data improves frontend performance and UX when browsing through large datasets.",
    "Refactors form logic to better support extensibility and future improvements.",
    "Adds tests that simulate real user login sessions, covering both success and failure paths.",
    "Updates documentation to help new contributors understand the config setup and workflow.",
    "Fixes a critical bug where users were not redirected correctly after login under certain network conditions.",
    "Splits business logic into smaller functions and adds inline comments for clarity.",
    "Ensures the test environment mimics production as closely as possible with stubbed external APIs.",
    "Adds better error messages and logs for debugging invalid form inputs.",
    "Initial setup for integrating third-party analytics, with stubbed values for local testing."
]

# Issue footers
FOOTERS = [
    "Closes #12",
    "Fixes #45",
    "Relates to #32",
    "Part of #28",
    ""
]

def generate_commit(i):
    title = PROFESSIONAL_COMMITS[i % len(PROFESSIONAL_COMMITS)]

    body = ""
    if random.random() < 0.4:  # 40% chance to add body
        body = "\n\n" + random.choice(BODIES)

    footer = ""
    if random.random() < 0.3:  # 30% chance to add footer
        footer = "\n\n" + random.choice(FOOTERS)

    return title + body + footer

def create_commits(branch_name, count, filename):
    subprocess.run(["git", "checkout", branch_name], check=True)

    for i in range(count):
        with open(filename, "a") as f:
            f.write(f"{branch_name} - change {i+1}\n")

        message = generate_commit(i)
        subprocess.run(["git", "add", filename])
        subprocess.run(["git", "commit", "-m", message])
        print(f"\n[{branch_name}] ✅ Commit {i+1}:\n{message}\n{'-'*60}")
        time.sleep(0.05)

    subprocess.run(["git", "push", "origin", branch_name], check=True)
    print(f"\n🎉 Pushed {count} high-quality commits to `{branch_name}`.")

if __name__ == "__main__":
    print("🚧 Generating high-quality commits for `good-commits`...")
    create_commits("good-commits", 50, "good-commits.txt")
    print("✅ Done.")
