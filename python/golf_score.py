import sys

def get_score_name(regulation_stroke, player_stroke):
    # スコア名 = 規定打数 - 実際の打数
    score_diff = regulation_stroke - player_stroke
    # 特別スコアをdictにまとめる
    special_score = {
        (5, 1): "コンドル",
        (5, 2): "アルバトロス",
        (4, 1): "ホールインワン",
        (3, 1): "ホールインワン",
    }
    # reg, play の組み合わせで spe_score のキーの組み合わせがあったら
    if (regulation_stroke, player_stroke) in special_score:
        # (regu, play)がキーの値を返す
        return special_score[(regulation_stroke, player_stroke)]
    
    # 通常スコア
    # score_diff == 2でイーグルを返す
    if score_diff == 2:
        return "イーグル"
    # score_diff == 1でバーディを返す
    elif score_diff == 1:
        return "バーディ"
    # score_diff == 0でパーを返す
    elif score_diff == 0:
        return "パー"
    # score_diff > 0でボギーを返す
    elif score_diff < 0:
        bogey_count = abs(score_diff)
        return f"{bogey_count}ボギー" if bogey_count > 1 else "ボギー"
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
