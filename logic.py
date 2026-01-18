def get_github_url(username):
    if not username:
        return
    return f"https://api.github.com/users/{username}"
