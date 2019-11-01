#!/usr/bin/python3
import json
import collections

a2u_datadict = {}
a2u_vattakshara_dict = {}
u2a_datadict = {}
ascii_consonants_start_chars = set()


def makemap_vattakshara(uni, asci):
    u_items = uni.split(" ")
    a_items = asci.split(" ")
    for idx, item in enumerate(a_items):
        a2u_vattakshara_dict[item] = u_items[idx]
        u2a_datadict[u_items[idx]] = a_items[idx]


def makemap(uni, asci, a2u_only=False, u2a_only=False):
    global ascii_consonants_start_chars

    u_items = uni.split(" ")
    a_items = asci.split(" ")
    for idx, item in enumerate(a_items):
        if not u2a_only:
            a2u_datadict[item] = u_items[idx]

        if not a2u_only:
            u2a_datadict[u_items[idx]] = a_items[idx]

        if not u2a_only:
            ascii_consonants_start_chars.add(item[0])


makemap("ಂ ಃ ಅಂ ಅಃ", "A B CA CB", u2a_only=True)
makemap("ಅ ಆ ಇ ಈ ಉ ಊ ಋ ೠ ಎ ಏ ಐ ಒ ಓ ಔ",
        "C D E F G H IÄ IÆ2 J K L M N O")
makemap("ಕ್ ಕ ಕಾ ಕಿ ಕೀ ಕು ಕೂ ಕೃ ಕೆ ಕೇ ಕೈ ಕೊ ಕೋ ಕೌ",
        "Pï PÀ PÁ Q QÃ PÀÄ PÀÆ PÀÈ PÉ PÉÃ PÉÊ PÉÆ PÉÆÃ PË")
makemap("ಖ್ ಖ ಖಾ ಖಿ ಖೀ ಖು ಖೂ ಖೃ ಖೆ ಖೇ ಖೈ ಖೊ ಖೋ ಖೌ",
        "Sï R SÁ T TÃ RÄ RÆ RÈ SÉ SÉÃ SÉÊ SÉÆ SÉÆÃ SË")
makemap("ಗ್ ಗ ಗಾ ಗಿ ಗೀ ಗು ಗೂ ಗೃ ಗೆ ಗೇ ಗೈ ಗೊ ಗೋ ಗೌ",
        "Uï UÀ UÁ V VÃ UÀÄ UÀÆ UÀÈ UÉ UÉÃ UÉÊ UÉÆ UÉÆÃ UË")
makemap("ಘ್ ಘ ಘಾ ಘಿ ಘೀ ಘು ಘೂ ಘೃ ಘೆ ಘೇ ಘೈ ಘೊ ಘೋ ಘೌ",
        "Wï WÀ WÁ X XÃ WÀÄ WÀÆ WÀÈ WÉ WÉÃ WÉÊ WÉÆ WÉÆÃ WË")
makemap("ಙ್ ಙ", "Yï Y")
makemap("ಚ್ ಚ ಚಾ ಚಿ ಚೀ ಚು ಚೂ ಚೃ ಚೆ ಚೇ ಚೈ ಚೊ ಚೋ ಚೌ",
        "Zï ZÀ ZÁ a aÃ ZÀÄ ZÀÆ ZÀÈ ZÉ ZÉÃ ZÉÊ ZÉÆ ZÉÆÃ ZË")
makemap("ಛ್ ಛ ಛಾ ಛಿ ಛೀ ಛು ಛೂ ಛೃ ಛೆ ಛೇ ಛೈ ಛೊ ಛೋ ಛೌ",
        "bï bÀ bÁ c cÃ bÀÄ bÀÆ bÀÈ bÉ bÉÃ bÉÊ bÉÆ bÉÆÃ bË")
makemap("ಜ್ ಜ ಜಾ ಜಿ ಜೀ ಜು ಜೂ ಜೃ ಜೆ ಜೇ ಜೈ ಜೊ ಜೋ ಜೌ",
        "eï d eÁ f fÃ dÄ dÆ dÈ eÉ eÉÃ eÉÊ eÉÆ eÉÆÃ eË")
makemap("ಝ್ ಝ ಝಾ ಝಿ ಝೀ ಝು ಝೂ ಝೃ ಝೆ ಝೇ ಝೈ ಝೊ ಝೋ ಝೌ",
        "gÀhiï gÀhÄ gÀhiÁ jhÄ jhÄÃ gÀhÄÄ gÀhÄÆ gÀhÄÈ gÉhÄ gÉhÄÃ "
        "gÉhÄÊ gÉhÆ gÉhÆÃ gÀhiË")
makemap("ಞ್ ಞ", "kï k")
makemap("ಟ್ ಟ ಟಾ ಟಿ ಟೀ ಟು ಟೂ ಟೃ ಟೆ ಟೇ ಟೈ ಟೊ ಟೋ ಟೌ",
        "mï l mÁ n nÃ lÄ lÆ lÈ mÉ mÉÃ mÉÊ mÉÆ mÉÆÃ mË")
makemap("ಠ್ ಠ ಠಾ ಠಿ ಠೀ ಠು ಠೂ ಠೃ ಠೆ ಠೇ ಠೈ ಠೊ ಠೋ ಠೌ",
        "oï oÀ oÁ p pÃ oÀÄ oÀÆ oÀÈ oÉ oÉÃ oÉÊ oÉÆ oÉÆÃ oË")
makemap("ಡ್ ಡ ಡಾ ಡಿ ಡೀ ಡು ಡೂ ಡೃ ಡೆ ಡೇ ಡೈ ಡೊ ಡೋ ಡೌ",
        "qï qÀ qÁ r rÃ qÀÄ qÀÆ qÀÈ qÉ qÉÃ qÉÊ qÉÆ qÉÆÃ qË")
makemap("ಢ್ ಢ ಢಾ ಢಿ ಢೀ ಢು ಢೂ ಢೃ ಢೆ ಢೇ ಢೈ ಢೊ ಢೋ ಢೌ",
        "qsï qsÀ qsÁ rü rüÃ qsÀÄ qsÀÆ qsÀÈ qsÉ qsÉÃ qsÉÊ qsÉÆ qsÉÆÃ qsË")
makemap("ಣ್ ಣ ಣಾ ಣಿ ಣೀ ಣು ಣೂ ಣೃ ಣೆ ಣೇ ಣೈ ಣೊ ಣೋ ಣೌ",
        "uï t uÁ tÂ tÂÃ tÄ tÆ tÈ uÉ uÉÃ uÉÊ uÉÆ uÉÆÃ uË")
makemap("ತ್ ತ ತಾ ತಿ ತೀ ತು ತೂ ತೃ ತೆ ತೇ ತೈ ತೊ ತೋ ತೌ",
        "vï vÀ vÁ w wÃ vÀÄ vÀÆ vÀÈ vÉ vÉÃ vÉÊ vÉÆ vÉÆÃ vË")
makemap("ಥ್ ಥ ಥಾ ಥಿ ಥೀ ಥು ಥೂ ಥೃ ಥೆ ಥೇ ಥೈ ಥೊ ಥೋ ಥೌ",
        "xï xÀ xÁ y yÃ xÀÄ xÀÆ xÀÈ xÉ xÉÃ xÉÊ xÉÆ xÉÆÃ xË")
makemap("ದ್ ದ ದಾ ದಿ ದೀ ದು ದೂ ದೃ ದೆ ದೇ ದೈ ದೊ ದೋ ದೌ",
        "zï zÀ zÁ ¢ ¢Ã zÀÄ zÀÆ zÀÈ zÉ zÉÃ zÉÊ zÉÆ zÉÆÃ zË")
makemap("ಧ್ ಧ ಧಾ ಧಿ ಧೀ ಧು ಧೂ ಧೃ ಧೆ ಧೇ ಧೈ ಧೊ ಧೋ ಧೌ",
        "zsï zsÀ zsÁ ¢ü ¢üÃ zsÀÄ zsÀÆ zsÀÈ zsÉ zsÉÃ zsÉÊ zsÉÆ zsÉÆÃ zsË")
makemap("ನ್ ನ ನಾ ನಿ ನೀ ನು ನೂ ನೃ ನೆ ನೇ ನೈ ನೊ ನೋ ನೌ",
        "£ï £À £Á ¤ ¤Ã £ÀÄ £ÀÆ £ÀÈ £É £ÉÃ £ÉÊ £ÉÆ £ÉÆÃ £Ë")
makemap("ಪ್ ಪ ಪಾ ಪಿ ಪೀ ಪು ಪೂ ಪೃ ಪೆ ಪೇ ಪೈ ಪೊ ಪೋ ಪೌ",
        "¥ï ¥À ¥Á ¦ ¦Ã ¥ÀÅ ¥ÀÇ ¥ÀÈ ¥É ¥ÉÃ ¥ÉÊ ¥ÉÇ ¥ÉÇÃ ¥Ë")
makemap("ಫ್ ಫ ಫಾ ಫಿ ಫೀ ಫು ಫೂ ಫೃ ಫೆ ಫೇ ಫೈ ಫೊ ಫೋ ಫೌ",
        "¥sï ¥sÀ ¥sÁ ¦ü ¦üÃ ¥sÀÅ ¥sÀÇ ¥sÀÈ ¥sÉ ¥sÉÃ ¥sÉÊ ¥sÉÇ ¥sÉÇÃ ¥sË")
makemap("ಪು ಪೂ ಪೊ ಪೋ", "¥ÀÄ ¥ÀÆ ¥ÉÆ ¥ÉÆÃ", a2u_only=True)
makemap("ಫು ಫೂ ಫೊ ಫೋ", "¥sÀÄ ¥sÀÆ ¥sÉÆ ¥sÉÆÃ", a2u_only=True)
makemap("ಬ್ ಬ ಬಾ ಬಿ ಬೀ ಬು ಬೂ ಬೃ ಬೆ ಬೇ ಬೈ ಬೊ ಬೋ ಬೌ",
        "¨ï § ¨Á © ©Ã §Ä §Æ §È ¨É ¨ÉÃ ¨ÉÊ ¨ÉÆ ¨ÉÆÃ ¨Ë")
makemap("ಭ್ ಭ ಭಾ ಭಿ ಭೀ ಭು ಭೂ ಭೃ ಭೆ ಭೇ ಭೈ ಭೊ ಭೋ ಭೌ",
        "¨sï ¨sÀ ¨sÁ ©ü ©üÃ ¨sÀÄ ¨sÀÆ ¨sÀÈ ¨sÉ ¨sÉÃ ¨sÉÊ ¨sÉÆ ¨sÉÆÃ ¨sË")
makemap("ಮ್ ಮ ಮಾ ಮಿ ಮೀ ಮು ಮೂ ಮೃ ಮೆ ಮೇ ಮೈ ಮೊ ಮೋ ಮೌ",
        "ªÀiï ªÀÄ ªÀiÁ «Ä «ÄÃ ªÀÄÄ ªÀÄÆ ªÀÄÈ ªÉÄ ªÉÄÃ ªÉÄÊ ªÉÆ ªÉÆÃ ªÀiË")
makemap("ಯ್ ಯ ಯಾ ಯಿ ಯೀ ಯು ಯೂ ಯೃ ಯೆ ಯೇ ಯೈ ಯೊ ಯೋ ಯೌ",
        "AiÀiï AiÀÄ AiÀiÁ ¬Ä ¬ÄÃ AiÀÄÄ AiÀÄÆ AiÀÄÈ AiÉÄ AiÉÄÃ AiÉÄÊ "
        "AiÉÆ AiÉÆÃ AiÀiË")
makemap("ಯ್ ಯ ಯಾ ಯಿ ಯೀ ಯು ಯೂ ಯೃ ಯೆ ಯೇ ಯೈ ಯೊ ಯೋ ಯೌ",
        "0iÀiï 0iÀÄ 0iÀiÁ ¬Ä ¬ÄÃ 0iÀÄÄ 0iÀÄÆ 0iÀÄÈ 0iÉÄ 0iÉÄÃ 0iÉÄÊ "
        "0iÉÆ 0iÉÆÃ 0iÀiË", a2u_only=True)
makemap("ರ್ ರ ರಾ ರಿ ರೀ ರು ರೂ ರೃ ರೆ ರೇ ರೈ ರೊ ರೋ ರೌ",
        "gï gÀ gÁ j jÃ gÀÄ gÀÆ gÀÈ gÉ gÉÃ gÉÊ gÉÆ gÉÆÃ gË")
makemap("ಲ್ ಲ ಲಾ ಲಿ ಲೀ ಲು ಲೂ ಲೃ ಲೆ ಲೇ ಲೈ ಲೊ ಲೋ ಲೌ",
        "¯ï ® ¯Á ° °Ã ®Ä ®Æ ®È ¯É ¯ÉÃ ¯ÉÊ ¯ÉÆ ¯ÉÆÃ ¯Ë")
makemap("ವ್ ವ ವಾ ವಿ ವೀ ವು ವೂ ವೃ ವೆ ವೇ ವೈ ವೊ ವೋ ವೌ",
        "ªï ªÀ ªÁ « «Ã ªÀÅ ªÀÇ ªÀÈ ªÉ ªÉÃ ªÉÊ ªÉÇ ªÉÇÃ ªË")
makemap("ಶ್ ಶ ಶಾ ಶಿ ಶೀ ಶು ಶೂ ಶೃ ಶೆ ಶೇ ಶೈ ಶೊ ಶೋ ಶೌ",
        "±ï ±À ±Á ² ²Ã ±ÀÄ ±ÀÆ ±ÀÈ ±É ±ÉÃ ±ÉÊ ±ÉÆ ±ÉÆÃ ±Ë")
makemap("ಷ್ ಷ ಷಾ ಷಿ ಷೀ ಷು ಷೂ ಷೃ ಷೆ ಷೇ ಷೈ ಷೊ ಷೋ ಷೌ",
        "μï μÀ μÁ ¶ ¶Ã μÀÄ μÀÆ μÀÈ μÉ μÉÃ μÉÊ μÉÆ μÉÆÃ μË")
makemap("ಸ್ ಸ ಸಾ ಸಿ ಸೀ ಸು ಸೂ ಸೃ ಸೆ ಸೇ ಸೈ ಸೊ ಸೋ ಸೌ",
        "¸ï ¸À ¸Á ¹ ¹Ã ¸ÀÄ ¸ÀÆ ¸ÀÈ ¸É ¸ÉÃ ¸ÉÊ ¸ÉÆ ¸ÉÆÃ ¸Ë")
makemap("ಹ್ ಹ ಹಾ ಹಿ ಹೀ ಹು ಹೂ ಹೃ ಹೆ ಹೇ ಹೈ ಹೊ ಹೋ ಹೌ",
        "ºï ºÀ ºÁ » »Ã ºÀÄ ºÀÆ ºÀÈ ºÉ ºÉÃ ºÉÊ ºÉÆ ºÉÆÃ ºË")
makemap("ಳ್ ಳ ಳಾ ಳಿ ಳೀ ಳು ಳೂ ಳೃ ಳೆ ಳೇ ಳೈ ಳೊ ಳೋ ಳೌ",
        "¼ï ¼À ¼Á ½ ½Ã ¼ÀÄ ¼ÀÆ ¼ÀÈ ¼É ¼ÉÃ ¼ÉÊ ¼ÉÆ ¼ÉÆÃ ¼Ë")

makemap("ಱ್‌ ಱ ಱಾ ಱಿ ಱು ಱೂ ಱೃ ಱೆ ಱೇ ಱೈ ಱೊ ಱೋ ಱೌ",
        "¾õï ¾õÀ ¾õÁ ¾Â ¾Ä ¾Æ ¾È ¾õÉ ¾õÉÃ ¾õÉÊ ¾õÉÆ ¾õÉÆÃ ¾õË")

makemap("ೞ್‌ ೞ ೞಾ ೞಿ ೞು ೞೂ ೞೃ ೞೆ ೞೇ ೞೈ ೞೊ ೞೋ ೞೌ",
        "¿õï ¿õÀ ¿õÁ ¿Â ¿Ä ¿Æ ¿È ¿õÉ ¿õÉÃ ¿õÉÊ ¿õÉÆ ¿õÉÆÃ ¿õË")

exports_data = {
    "anusvara_visarga": ["ಂ", "ಃ"],
    "vowels": "ಅ ಆ ಇ ಈ ಉ ಊ ಋ ೠ ಎ ಏ ಐ ಒ ಓ ಔ ಅಂ ಅಃ".split(" "),
    "halant": "ಕ್"[1],
    "consonants": "ಕ ಖ ಗ ಘ ಙ ಚ ಛ ಜ ಝ ಞ ಟ ಠ ಡ ಢ ಣ ತ ಥ ದ ಧ ನ ಪ ಫ ಬ ಭ ಮ ಯ ರ ಲ ವ ಶ ಷ ಸ ಹ ಳ ಱ ೞ".split(" "),
    "dep_vowels": "್ ಾ ಿ ೀ ು ೂ ೃ ೆ ೇ ೈ ೊ ೋ ೌ ಂ ಃ".split(" "),
    "u2a_map": u2a_datadict,
    "kn_numbers": "೦ ೧ ೨ ೩ ೪ ೫ ೬ ೭ ೮ ೯".split(" "),
    "en_numbers": "0 1 2 3 4 5 6 7 8 9".split(" "),
    "ascii_halant": "ï",
    "ascii_consonants_start_chars": list(ascii_consonants_start_chars),
    "uni_zwnj": "\u200c",
    "uni_zwj": "\u200d",
    "ascii_arkavattu": "ð",
    "uni_ra": "ರ"
}

print("Kn.prototype._replace_a2u_anuswara_visarga = function(txt) {"
      "    return txt.replace('A', 'ಂ').replace('B', 'ಃ');"
      "}")

print("Kn.prototype._replace_from_map = function(txt){")
od = collections.OrderedDict(sorted(a2u_datadict.items(), reverse=True))

print("    return txt", end="")

for k, v in od.items():
    print(".replace(/{0}/g, \"{1}\")".format(k, v), end="")

print(";")
print("}")

vattaksharagalu = ""
halant = "ಕ್"[1]
for ele in "ಕಖಗಘಙಚಛಜಝಞಟಠಡಢಣತಥದಧನಪಫಬಭಮಯರಲವಶಷಸಹಳಱೞ":
    vattaksharagalu += halant + ele + " "

ascii_vattaksharagalu = "Ì Í Î Ï Ð Ñ Ò Ó Ô Õ Ö × Ø Ù Ú Û Ü Ý Þ ß à á â ã ä å æ è é ê ë ì í î ù ú"
makemap_vattakshara(vattaksharagalu.strip(), ascii_vattaksharagalu)
dep_vowels = "್ ಾ ಿ ೀ ು ೂ ೃ ೆ ೇ ೈ ೊ ೋ ೌ ಂ ಃ"

other_maps = {
    "ø": "ೃ",
    "ñ": "ೄ",
    "„": "ಽ",
    "ó": "಼"
}

# ASCII Halant + Consonant => Add ZWNJ between
print("Kn.prototype._REGEX_ASCII_ZWNJ = "
      "new RegExp('({0})([{1}])', 'g');".format(
          exports_data["ascii_halant"],
          "".join(exports_data["ascii_consonants_start_chars"])
      ))

print("Kn.prototype._REGEX_ASCII_VATTAKSHARA_3 = "
      "new RegExp('([{0}])([{1}])([{2}])([{3}])', 'g');".format(
          dep_vowels.replace(" ", ""),
          ascii_vattaksharagalu.replace(" ", ""),
          ascii_vattaksharagalu.replace(" ", ""),
          ascii_vattaksharagalu.replace(" ", "")
      ))

print("Kn.prototype._REGEX_ASCII_VATTAKSHARA_2 = "
      "new RegExp('([{0}])([{1}])([{2}])', 'g');".format(
          dep_vowels.replace(" ", ""),
          ascii_vattaksharagalu.replace(" ", ""),
          ascii_vattaksharagalu.replace(" ", "")
      ))

print("Kn.prototype._REGEX_ASCII_VATTAKSHARA_1 = "
      "new RegExp('([{0}])([{1}])', 'g');".format(
          dep_vowels.replace(" ", ""),
          ascii_vattaksharagalu.replace(" ", "")
      ))

ascii_deerga = "Ã"
print("Kn.prototype._u2a_deerga_handle = function(txt) {")
print("    txt = txt.replace("
      "         /({0})([{1}])([{2}])([{3}])/g, "
      "         function(match, g1, g2, g3, g4) {{"
      "             return g2 + g3 + g4 + g1;"
      "         }}"
      "    );".format(
          ascii_deerga,
          ascii_vattaksharagalu.replace(" ", ""),
          ascii_vattaksharagalu.replace(" ", ""),
          ascii_vattaksharagalu.replace(" ", "")
      ))

print("    txt = txt.replace("
      "         /({0})([{1}])([{2}])/g, "
      "         function(match, g1, g2, g3) {{"
      "             return g2 + g3 + g1;"
      "         }}"
      "    );".format(
          ascii_deerga,
          ascii_vattaksharagalu.replace(" ", ""),
          ascii_vattaksharagalu.replace(" ", "")
      ))

print("    txt = txt.replace("
      "         /({0})([{1}])/g, "
      "         function(match, g1, g2) {{"
      "             return g2 + g1;"
      "         }}"
      "    );".format(
          ascii_deerga,
          ascii_vattaksharagalu.replace(" ", "")
      ))

print("    return txt;"
      "}");

print("Kn.prototype._replace_vattakshara =function(txt){")
print("    return txt", end="")

for k, v in a2u_vattakshara_dict.items():
    print(".replace(/{0}/g, \"{1}\")".format(k, v), end="")

for k, v in other_maps.items():
    print(".replace(/{0}/g, \"{1}\")".format(k, v), end="")

print(";")
print("}")

print("Kn.prototype._a2u_deerga_handle = function(txt) {{"
      "    return txt.replace("
      "        /([{uni_dep_vowel_i}{uni_dep_vowel_e}{uni_dep_vowel_o}])({ascii_deerga})/g, "
      "        function(match, g1, g2) {{"
      "            if (g1 == '{uni_dep_vowel_i}') {{ return '{uni_dep_vowel_I}'; }}"
      "            if (g1 == '{uni_dep_vowel_e}') {{ return '{uni_dep_vowel_E}'; }}"
      "            if (g1 == '{uni_dep_vowel_o}') {{ return '{uni_dep_vowel_O}'; }}"
      "        }});"
      "}}".format(
          uni_dep_vowel_i="ಕಿ"[1],
          uni_dep_vowel_e="ಕೆ"[1],
          uni_dep_vowel_o="ಕೊ"[1],
          uni_dep_vowel_I="ಕೀ"[1],
          uni_dep_vowel_E="ಕೇ"[1],
          uni_dep_vowel_O="ಕೋ"[1],
          ascii_deerga="Ã"
      ))


def print_data(data_dict):
    for key, value in data_dict.items():
        print("Kn.prototype._{0} = {1};".format(key, json.dumps(value)))


print("Kn.prototype._REGEX_UNI_ASCII_ARKAVATTU = new RegExp('"
      "([{consonants}])"
      "({halant}[{consonants}])?"
      "({halant}[{consonants}])?"
      "([{dep_vowels}])?"
      "([{dep_vowels}])?"
      "{ascii_arkavattu}', 'g');".format(
          consonants="".join(exports_data["consonants"]),
          uni_zwj=exports_data["uni_zwj"],
          halant=exports_data["halant"],
          ascii_arkavattu=exports_data["ascii_arkavattu"],
          dep_vowels="".join(exports_data["dep_vowels"])))

print("Kn.prototype._REGEX_UNI_REPH_BEFORE_CONVERT = new RegExp('"
      "[^{halant}]?([{uni_ra}])"
      "({halant}[{consonants}])"
      "({halant}[{consonants}])?"
      "({halant}[{consonants}])?"
      "([{dep_vowels}])?"
      "([{dep_vowels}])?', 'g');".format(
          uni_ra=exports_data["uni_ra"],
          consonants="".join(exports_data["consonants"]),
          halant=exports_data["halant"],
          dep_vowels="".join(exports_data["dep_vowels"])))

print("Kn.prototype._REGEX_UNI_REPH_WITHOUT_ZWJ = new RegExp('"
      "^([{uni_ra}])"
      "({halant}[{consonants}])"
      "({halant}[{consonants}])?"
      "({halant}[{consonants}])?"
      "([{dep_vowels}])?"
      "([{dep_vowels}])?$', 'g');".format(
          uni_ra=exports_data["uni_ra"],
          consonants="".join(exports_data["consonants"]),
          halant=exports_data["halant"],
          dep_vowels="".join(exports_data["dep_vowels"])))

print("Kn.prototype._REGEX_UNI_VATTAKSHARA = new RegExp('"
      "^([{consonants}])"
      "{uni_zwj}?"
      "({halant}[{consonants}])"
      "({halant}[{consonants}])?"
      "({halant}[{consonants}])?"
      "([{dep_vowels}])?"
      "([{dep_vowels}])?$', 'g');".format(
          consonants="".join(exports_data["consonants"]),
          uni_zwj=exports_data["uni_zwj"],
          halant=exports_data["halant"],
          dep_vowels="".join(exports_data["dep_vowels"])))


print("Kn.prototype._REGEX_UNI_VOWEL_PLUS_ANUSVARA_VISARGA = new RegExp('"
      "^([{vowels}])([{anusvara_visarga}])$', 'g');".format(
          vowels="".join(exports_data["vowels"]),
          anusvara_visarga="".join(exports_data["anusvara_visarga"])))

print("Kn.prototype._REGEX_UNI_CONSONANT_PLUS_VOWEL = new RegExp('"
      "^([{consonants}])([{dep_vowels}])?([{dep_vowels}])?$', 'g');".format(
          consonants="".join(exports_data["consonants"]),
          dep_vowels="".join(exports_data["dep_vowels"])))

print_data(exports_data)


print("Kn.prototype._unicode_anusvara_visarga = function(txt){return txt", end="")
for av in exports_data["anusvara_visarga"]:
    print('.replace(/{0}/g,"{1}")'.format(av, exports_data["u2a_map"][av]),
          end="")

print(";}")


print("Kn.prototype._to_ascii_numbers = function(txt){return txt", end="")
for idx, n in enumerate(exports_data["kn_numbers"]):
    print('.replace(/{0}/g,"{1}")'.format(n, exports_data["en_numbers"][idx]), end="")
print(";}")

print("Kn.prototype._to_unicode_numbers = function(txt){return txt", end="")
for idx, n in enumerate(exports_data["en_numbers"]):
    print('.replace(/{0}/g,"{1}")'.format(n, exports_data["kn_numbers"][idx]), end="")
print(";}")
