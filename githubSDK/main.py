from github import GitHub
from pprint import pprint

username = "arcotbha"
login_or_token = "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"


def main():
    # make the request and return github object
    gh = GitHub(login_or_token=login_or_token)

    # Use the github object to get a user by username
    user = gh.get_user(user=username)
    pprint(user.login)

    # Get GPG keys for the user
    keys_data = user.get_keys()
    pprint(keys_data)

    # Get all the repos for the authenticated user
    repos = user.get_repos()
    pprint(repos)

    # Get all the orgs for the authenticated user
    org_data = user.get_orgs()
    pprint(org_data)

    repo = user.create_repo(
        token=login_or_token,
        name="newRepo",
        description="This is a test repo",
    )

    pprint(repo)


if __name__ == "__main__":
    main()
