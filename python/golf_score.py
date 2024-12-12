import sys

def get_score_name(regulation_stroke, player_stroke):
    # スコア名 = 規定打数 - 実際の打数
    score_diff = regulation_stroke - player_stroke
    # 特別スコアをdictにまとめる
    score_dict = {
        (5, 1): "コンドル",
        (5, 2): "アルバトロス",
        (4, 1): "ホールインワン",
        (3, 1): "ホールインワン",
        2: "イーグル",
        1: "バーディ",
        0: "パー",
        "bogey": "{}ボギー",
    }
    # reg, play の組み合わせで score_dict のキーの組み合わせがあったら return で返す
    # 要は特別スコアとなるコンドル~ホールインワンまでを優先して判定
    if (regulation_stroke, player_stroke) in score_dict:
        # (regu, play)がキーの値を返す
        return score_dict["bogey"].format(bogey_count if bogey_count > 1 else "")
    
    # score_diff >= 0でイーグルを返す
    if score_diff in score_dict:
        return score_dict[score_diff]
    # score_diff < 0でボギーを返す
    elif score_diff < 0:
        bogey_count = abs(score_diff)
        return f"{bogey_count if bogey_count > 1 else ''}ボギー"
    return "スコア不明"


def player_score():
    # 標準入力から全ての行を読み込み、改行で分割
    lines = sys.stdin.read().strip().split('\n')
    # 1行目: 規定打数、2行目: 実際の打数　それぞれの行は','で区切る
    regulations_strokes = list(map(int, lines[0].split(',')))
    player_strokes = list(map(int, lines[1].split(',')))
    """
    リスト内包表記を使用
    for文で(規定打数, 実際の打数)をループさせる
    """
    scores = [
        get_score_name(regulation, player)
        for regulation, player in zip(regulations_strokes, player_strokes)
    ]
    print(",".join(scores))

player_score()
