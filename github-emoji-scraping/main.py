from github import Github
from config import CONFIG


def main():
    g = Github(CONFIG['GITHUB']['access_token'])

    for repo in g.get_user().get_repos():
        print(repo.name)

if __name__ == '__main__':
    main()
