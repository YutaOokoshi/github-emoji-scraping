from github import Github
from config import CONFIG


def main():
    g = Github(CONFIG['GITHUB']['user'],CONFIG['GITHUB']['pw'])

    cnt=0

    # 問題１：1000件取得でkリうようにしてください

    # 例１）
    # starrが1つ以上あるリポジトリ一覧をスター数の降順で取得し1つづつ処理を回す （最大1000件出力する）
    for repo in g.search_repositories(query="stars:>1", order="desc", sort="stars"):
        print(repo.name)

        # 100件出力したらforを抜ける
        cnt += 1
        if cnt >= 100:
            print(f"{cnt}件出力しました。")
            break


    # 問題２：１つ１つのリポジトリのREADME.mdファイルを取得してください。
    # for xxxxxx



if __name__ == '__main__':
    main()
