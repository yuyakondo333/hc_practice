import sys
import datetime

class Calendar:
    def __init__(self, month, year):
        # 本日の日付を dt_now 変数に格納
        self.year = year
        self.month = month

    # 西暦と月を出力
    def header_month_year(self):
        # month, year を取得して出力
        return print(f"      {self.month}月 {self.year}")

    # ヘッダーの曜日を出力
    def header_weekday(self):
        # ヘッダーとなる曜日を yobi 変数に格納
        yobi = ['月', '火', '水', '木', '金', '土', '日']
        # 1つスペースを開けて月~日までを yobi_str に格納
        yobi_str = ' '.join(yobi)
        # yobi_strを出力すると月~日までが出力される
        return print(yobi_str)
    
    # 月の最終日を取得
    def month_lastday(self):
        """
        引数または今月の月の1日から31日プラスする->翌月になる
        翌月の1日にして1日分戻す->引数または今月の月の最終日を取得
        結果を変数に格納
        """
        firstday_next_month = datetime.date(self.year, self.month, 1) + datetime.timedelta(days=31)
        # 翌月の1日から1日前に戻す->今月の最終日を取得できる
        return (firstday_next_month.replace(day=1) - datetime.timedelta(days=1)).day

    # 1日の曜日を取得
    def firstday_weekday(self):
        return datetime.date(self.year, self.month, 1).weekday()
    
    # 日付を表示
    def display_date(self):
        # 1日の曜日を取得
        first_weekday = self.firstday_weekday()
        # 文字スペース2マス + 文字と文字の間のスペース1マス = 3マスのスペース
        print(("   " * first_weekday), end="")
        # 月の最終日を取得
        last_day = self.month_lastday()

        # 1日から最終日まで出力
        for day in range(1, last_day+1):
            # day:2とすることで1桁でも2マス使用する
            print(f"{day:2}", end=" ")
            # 日曜日で改行
            # first_weekday->0~6
            # day->0~lastday
            if (first_weekday + day) % 7 == 0:
                # 改行
                print()
        # 最後の改行
        print()  


if __name__ == '__main__':
    # コマンドライン引数を取得
    args = sys.argv

    try:
        # 引数が1つ->ファイル名だけで実行した場合
        if len(sys.argv) == 1:
            # 現在の時刻の月をmonthに格納
            month = datetime.date.today().month
        # args[2]をmonthに格納
        else:
            month = int(args[2])
        # monthが　1~12 ではなかった場合
        if not (1 <= month <= 12):
            # ValueErrorを発生
            raise ValueError
    except ValueError:
        # エラーメッセージを発生
        sys.exit(f"{args[2]} is neither a month number (1..12) nor a name")

    # 現在の年を取得
    year = datetime.date.today().year

    # カレンダーを生成して表示
    calendar = Calendar(month, year)
    calendar.header_month_year()
    calendar.header_weekday()
    calendar.display_date()