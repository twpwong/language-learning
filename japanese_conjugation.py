# Japanese verb conjugation utility

HIRAGANA_VOWEL_MAP = {
    'あ': 'a','か':'a','さ':'a','た':'a','な':'a','は':'a','ま':'a','ら':'a','が':'a','ざ':'a','だ':'a','ば':'a','ぱ':'a',
    'い': 'i','き':'i','し':'i','ち':'i','に':'i','ひ':'i','み':'i','り':'i','ぎ':'i','じ':'i','ぢ':'i','び':'i','ぴ':'i',
    'う': 'u','く':'u','す':'u','つ':'u','ぬ':'u','ふ':'u','む':'u','ゆ':'u','る':'u','ぐ':'u','ず':'u','づ':'u','ぶ':'u','ぷ':'u',
    'え': 'e','け':'e','せ':'e','て':'e','ね':'e','へ':'e','め':'e','れ':'e','げ':'e','ぜ':'e','で':'e','べ':'e','ぺ':'e',
    'お': 'o','こ':'o','そ':'o','と':'o','の':'o','ほ':'o','も':'o','よ':'o','ろ':'o','を':'o','ご':'o','ぞ':'o','ど':'o','ぼ':'o','ぽ':'o'
}

def classify_verb(verb: str) -> str:
    """Classify a verb into godan, ichidan, suru, or kuru."""
    if verb.endswith('する'):
        return 'suru'
    if verb.endswith('くる') or verb.endswith('来る'):
        return 'kuru'

    if verb.endswith('る'):
        if len(verb) >= 2:
            prev = verb[-2]
            vowel = HIRAGANA_VOWEL_MAP.get(prev)
            if vowel in ('i', 'e'):
                return 'ichidan'
    return 'godan'

def conjugate_godan(root: str, ending: str, form: str) -> str:
    masu_map = {'う':'い','く':'き','ぐ':'ぎ','す':'し','ず':'じ','つ':'ち','ぬ':'に','ぶ':'び','む':'み','る':'り'}
    nai_map = {'う':'わ','く':'か','ぐ':'が','す':'さ','ず':'ざ','つ':'た','ぬ':'な','ぶ':'ば','む':'ま','る':'ら'}
    ta_map = {
        'う':'った','つ':'った','る':'った',
        'く':'いた','ぐ':'いだ','す':'した',
        'ぬ':'んだ','ぶ':'んだ','む':'んだ','ず':'した'
    }
    te_map = {
        'う':'って','つ':'って','る':'って',
        'く':'いて','ぐ':'いで','す':'して',
        'ぬ':'んで','ぶ':'んで','む':'んで','ず':'して'
    }
    if form == 'masu':
        return root + masu_map.get(ending, '') + 'ます'
    if form == 'nai':
        return root + nai_map.get(ending, '') + 'ない'
    if form == 'ta':
        return root + ta_map.get(ending, '')
    if form == 'te':
        return root + te_map.get(ending, '')
    raise ValueError(f"Unsupported form: {form}")

def conjugate_ichidan(root: str, form: str) -> str:
    if form == 'masu':
        return root + 'ます'
    if form == 'nai':
        return root + 'ない'
    if form == 'ta':
        return root + 'た'
    if form == 'te':
        return root + 'て'
    raise ValueError(f"Unsupported form: {form}")

def conjugate_irregular(verb: str, form: str) -> str:
    if verb.endswith('する'):
        base = 'し'
        if form == 'masu':
            return base + 'ます'
        if form == 'nai':
            return base + 'ない'
        if form == 'ta':
            return base + 'た'
        if form == 'te':
            return base + 'て'
    if verb.endswith('くる') or verb.endswith('来る'):
        if form == 'masu':
            return 'きます'
        if form == 'nai':
            return 'こない'
        if form == 'ta':
            return 'きた'
        if form == 'te':
            return 'きて'
    raise ValueError(f"Unsupported irregular verb/form combination: {verb}, {form}")

def conjugate(verb: str, form: str) -> str:
    """Conjugate a verb into the specified form."""
    kind = classify_verb(verb)
    if kind in ('suru', 'kuru'):
        return conjugate_irregular(verb, form)
    if kind == 'ichidan':
        root = verb[:-1]
        return conjugate_ichidan(root, form)
    # godan
    root, ending = verb[:-1], verb[-1]
    return conjugate_godan(root, ending, form)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Japanese verb conjugation')
    parser.add_argument('verb', help='verb in dictionary form (plain present)')
    parser.add_argument('form', choices=['masu', 'nai', 'ta', 'te'], help='desired form')
    args = parser.parse_args()
    result = conjugate(args.verb, args.form)
    print(result)
