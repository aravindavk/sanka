def testsgen_basic(uni, asci):
    u_items = uni.split(" ")
    a_items = asci.split(" ")
    for idx, item in enumerate(a_items):
        print('QUnit.test("u2a {0} => {1}", function(assert){{'
              'assert.strictEqual('
              'kn.unicode_to_ascii("{0}"), "{1}");}});'.format(
                  u_items[idx],
                  item
              ))

        print('QUnit.test("a2u {1} => {0}", function(assert){{'
              'assert.strictEqual('
              'kn.ascii_to_unicode("{1}"), "{0}");}});'.format(
                  u_items[idx],
                  item
              ))


testsgen_basic("ಂ ಃ", "A B")
testsgen_basic("ಅ ಆ ಇ ಈ ಉ ಊ ಋ ಎ ಏ ಐ ಒ ಓ ಔ ಅಂ ಅಃ",
               "C D E F G H IÄ J K L M N O CA CB")
testsgen_basic("ಅಂ ಆಂ ಇಂ ಈಂ ಉಂ ಊಂ ಋಂ ಎಂ ಏಂ ಐಂ ಒಂ ಓಂ ಔಂ",
               "CA DA EA FA GA HA IÄA JA KA LA MA NA OA")
testsgen_basic("ಅಃ ಆಃ ಇಃ ಈಃ ಉಃ ಊಃ ಋಃ ಎಃ ಏಃ ಐಃ ಒಃ ಓಃ ಔಃ",
               "CB DB EB FB GB HB IÄB JB KB LB MB NB OB")
testsgen_basic("ಕ್ ಕ ಕಾ ಕಿ ಕೀ ಕು ಕೂ ಕೃ ಕೆ ಕೇ ಕೈ ಕೊ ಕೋ ಕೌ",
               "Pï PÀ PÁ Q QÃ PÀÄ PÀÆ PÀÈ PÉ PÉÃ PÉÊ PÉÆ PÉÆÃ PË")
testsgen_basic("ಖ್ ಖ ಖಾ ಖಿ ಖೀ ಖು ಖೂ ಖೃ ಖೆ ಖೇ ಖೈ ಖೊ ಖೋ ಖೌ",
               "Sï R SÁ T TÃ RÄ RÆ RÈ SÉ SÉÃ SÉÊ SÉÆ SÉÆÃ SË")
testsgen_basic("ಗ್ ಗ ಗಾ ಗಿ ಗೀ ಗು ಗೂ ಗೃ ಗೆ ಗೇ ಗೈ ಗೊ ಗೋ ಗೌ",
               "Uï UÀ UÁ V VÃ UÀÄ UÀÆ UÀÈ UÉ UÉÃ UÉÊ UÉÆ UÉÆÃ UË")
testsgen_basic("ಘ್ ಘ ಘಾ ಘಿ ಘೀ ಘು ಘೂ ಘೃ ಘೆ ಘೇ ಘೈ ಘೊ ಘೋ ಘೌ",
               "Wï WÀ WÁ X XÃ WÀÄ WÀÆ WÀÈ WÉ WÉÃ WÉÊ WÉÆ WÉÆÃ WË")
testsgen_basic("ಚ್ ಚ ಚಾ ಚಿ ಚೀ ಚು ಚೂ ಚೃ ಚೆ ಚೇ ಚೈ ಚೊ ಚೋ ಚೌ",
               "Zï ZÀ ZÁ a aÃ ZÀÄ ZÀÆ ZÀÈ ZÉ ZÉÃ ZÉÊ ZÉÆ ZÉÆÃ ZË")
testsgen_basic("ಛ್ ಛ ಛಾ ಛಿ ಛೀ ಛು ಛೂ ಛೃ ಛೆ ಛೇ ಛೈ ಛೊ ಛೋ ಛೌ",
               "bï bÀ bÁ c cÃ bÀÄ bÀÆ bÀÈ bÉ bÉÃ bÉÊ bÉÆ bÉÆÃ bË")
testsgen_basic("ಜ್ ಜ ಜಾ ಜಿ ಜೀ ಜು ಜೂ ಜೃ ಜೆ ಜೇ ಜೈ ಜೊ ಜೋ ಜೌ",
               "eï d eÁ f fÃ dÄ dÆ dÈ eÉ eÉÃ eÉÊ eÉÆ eÉÆÃ eË")
testsgen_basic("ಝ್ ಝ ಝಾ ಝಿ ಝೀ ಝು ಝೂ ಝೃ ಝೆ ಝೇ ಝೈ ಝೊ ಝೋ ಝೌ",
               "gÀhiï gÀhÄ gÀhiÁ jhÄ jhÄÃ gÀhÄÄ gÀhÄÆ gÀhÄÈ gÉhÄ gÉhÄÃ "
               "gÉhÄÊ gÉhÆ gÉhÆÃ gÀhiË")
testsgen_basic("ಟ್ ಟ ಟಾ ಟಿ ಟೀ ಟು ಟೂ ಟೃ ಟೆ ಟೇ ಟೈ ಟೊ ಟೋ ಟೌ",
               "mï l mÁ n nÃ lÄ lÆ lÈ mÉ mÉÃ mÉÊ mÉÆ mÉÆÃ mË")
testsgen_basic("ಠ್ ಠ ಠಾ ಠಿ ಠೀ ಠು ಠೂ ಠೃ ಠೆ ಠೇ ಠೈ ಠೊ ಠೋ ಠೌ",
               "oï oÀ oÁ p pÃ oÀÄ oÀÆ oÀÈ oÉ oÉÃ oÉÊ oÉÆ oÉÆÃ oË")
testsgen_basic("ಡ್ ಡ ಡಾ ಡಿ ಡೀ ಡು ಡೂ ಡೃ ಡೆ ಡೇ ಡೈ ಡೊ ಡೋ ಡೌ",
               "qï qÀ qÁ r rÃ qÀÄ qÀÆ qÀÈ qÉ qÉÃ qÉÊ qÉÆ qÉÆÃ qË")
testsgen_basic("ಢ್ ಢ ಢಾ ಢಿ ಢೀ ಢು ಢೂ ಢೃ ಢೆ ಢೇ ಢೈ ಢೊ ಢೋ ಢೌ",
               "qsï qsÀ qsÁ rü rüÃ qsÀÄ qsÀÆ qsÀÈ qsÉ qsÉÃ qsÉÊ qsÉÆ qsÉÆÃ qsË")
testsgen_basic("ಣ್ ಣ ಣಾ ಣಿ ಣೀ ಣು ಣೂ ಣೃ ಣೆ ಣೇ ಣೈ ಣೊ ಣೋ ಣೌ",
               "uï t uÁ tÂ tÂÃ tÄ tÆ tÈ uÉ uÉÃ uÉÊ uÉÆ uÉÆÃ uË")
testsgen_basic("ತ್ ತ ತಾ ತಿ ತೀ ತು ತೂ ತೃ ತೆ ತೇ ತೈ ತೊ ತೋ ತೌ",
               "vï vÀ vÁ w wÃ vÀÄ vÀÆ vÀÈ vÉ vÉÃ vÉÊ vÉÆ vÉÆÃ vË")
testsgen_basic("ಥ್ ಥ ಥಾ ಥಿ ಥೀ ಥು ಥೂ ಥೃ ಥೆ ಥೇ ಥೈ ಥೊ ಥೋ ಥೌ",
               "xï xÀ xÁ y yÃ xÀÄ xÀÆ xÀÈ xÉ xÉÃ xÉÊ xÉÆ xÉÆÃ xË")
testsgen_basic("ದ್ ದ ದಾ ದಿ ದೀ ದು ದೂ ದೃ ದೆ ದೇ ದೈ ದೊ ದೋ ದೌ",
               "zï zÀ zÁ ¢ ¢Ã zÀÄ zÀÆ zÀÈ zÉ zÉÃ zÉÊ zÉÆ zÉÆÃ zË")
testsgen_basic("ಧ್ ಧ ಧಾ ಧಿ ಧೀ ಧು ಧೂ ಧೃ ಧೆ ಧೇ ಧೈ ಧೊ ಧೋ ಧೌ",
               "zsï zsÀ zsÁ ¢ü ¢üÃ zsÀÄ zsÀÆ zsÀÈ zsÉ zsÉÃ zsÉÊ zsÉÆ zsÉÆÃ zsË")
testsgen_basic("ನ್ ನ ನಾ ನಿ ನೀ ನು ನೂ ನೃ ನೆ ನೇ ನೈ ನೊ ನೋ ನೌ",
               "£ï £À £Á ¤ ¤Ã £ÀÄ £ÀÆ £ÀÈ £É £ÉÃ £ÉÊ £ÉÆ £ÉÆÃ £Ë")
testsgen_basic("ಪ್ ಪ ಪಾ ಪಿ ಪೀ ಪು ಪೂ ಪೃ ಪೆ ಪೇ ಪೈ ಪೊ ಪೋ ಪೌ",
               "¥ï ¥À ¥Á ¦ ¦Ã ¥ÀÄ ¥ÀÆ ¥ÀÈ ¥É ¥ÉÃ ¥ÉÊ ¥ÉÆ ¥ÉÆÃ ¥Ë")
testsgen_basic("ಫ್ ಫ ಫಾ ಫಿ ಫೀ ಫು ಫೂ ಫೃ ಫೆ ಫೇ ಫೈ ಫೊ ಫೋ ಫೌ",
               "¥sï ¥sÀ ¥sÁ ¦ü ¦üÃ ¥sÀÄ ¥sÀÆ ¥sÀÈ ¥sÉ ¥sÉÃ ¥sÉÊ ¥sÉÆ ¥sÉÆÃ ¥sË")
testsgen_basic("ಬ್ ಬ ಬಾ ಬಿ ಬೀ ಬು ಬೂ ಬೃ ಬೆ ಬೇ ಬೈ ಬೊ ಬೋ ಬೌ",
               "¨ï § ¨Á © ©Ã §Ä §Æ §È ¨É ¨ÉÃ ¨ÉÊ ¨ÉÆ ¨ÉÆÃ ¨Ë")
testsgen_basic("ಭ್ ಭ ಭಾ ಭಿ ಭೀ ಭು ಭೂ ಭೃ ಭೆ ಭೇ ಭೈ ಭೊ ಭೋ ಭೌ",
               "¨sï ¨sÀ ¨sÁ ©ü ©üÃ ¨sÀÄ ¨sÀÆ ¨sÀÈ ¨sÉ ¨sÉÃ ¨sÉÊ ¨sÉÆ ¨sÉÆÃ ¨sË")
testsgen_basic("ಮ್ ಮ ಮಾ ಮಿ ಮೀ ಮು ಮೂ ಮೃ ಮೆ ಮೇ ಮೈ ಮೊ ಮೋ ಮೌ",
               "ªÀiï ªÀÄ ªÀiÁ «Ä «ÄÃ ªÀÄÄ ªÀÄÆ ªÀÄÈ ªÉÄ ªÉÄÃ ªÉÄÊ ªÉÆ ªÉÆÃ ªÀiË")
testsgen_basic("ಯ್ ಯ ಯಾ ಯಿ ಯೀ ಯು ಯೂ ಯೃ ಯೆ ಯೇ ಯೈ ಯೊ ಯೋ ಯೌ",
               "AiÀiï AiÀÄ AiÀiÁ ¬Ä ¬ÄÃ AiÀÄÄ AiÀÄÆ AiÀÄÈ AiÉÄ AiÉÄÃ AiÉÄÊ "
               "AiÉÆ AiÉÆÃ AiÀiË")
testsgen_basic("ರ್ ರ ರಾ ರಿ ರೀ ರು ರೂ ರೃ ರೆ ರೇ ರೈ ರೊ ರೋ ರೌ",
               "gï gÀ gÁ j jÃ gÀÄ gÀÆ gÀÈ gÉ gÉÃ gÉÊ gÉÆ gÉÆÃ gË")
testsgen_basic("ಲ್ ಲ ಲಾ ಲಿ ಲೀ ಲು ಲೂ ಲೃ ಲೆ ಲೇ ಲೈ ಲೊ ಲೋ ಲೌ",
               "¯ï ® ¯Á ° °Ã ®Ä ®Æ ®È ¯É ¯ÉÃ ¯ÉÊ ¯ÉÆ ¯ÉÆÃ ¯Ë")
testsgen_basic("ವ್ ವ ವಾ ವಿ ವೀ ವು ವೂ ವೃ ವೆ ವೇ ವೈ ವೊ ವೋ ವೌ",
               "ªï ªÀ ªÁ « «Ã ªÀÅ ªÀÇ ªÀÈ ªÉ ªÉÃ ªÉÊ ªÉÇ ªÉÇÃ ªË")
testsgen_basic("ಶ್ ಶ ಶಾ ಶಿ ಶೀ ಶು ಶೂ ಶೃ ಶೆ ಶೇ ಶೈ ಶೊ ಶೋ ಶೌ",
               "±ï ±À ±Á ² ²Ã ±ÀÄ ±ÀÆ ±ÀÈ ±É ±ÉÃ ±ÉÊ ±ÉÆ ±ÉÆÃ ±Ë")
testsgen_basic("ಷ್ ಷ ಷಾ ಷಿ ಷೀ ಷು ಷೂ ಷೃ ಷೆ ಷೇ ಷೈ ಷೊ ಷೋ ಷೌ",
               "µï µÀ µÁ ¶ ¶Ã µÀÄ µÀÆ µÀÈ µÉ µÉÃ µÉÊ µÉÆ µÉÆÃ µË")
testsgen_basic("ಸ್ ಸ ಸಾ ಸಿ ಸೀ ಸು ಸೂ ಸೃ ಸೆ ಸೇ ಸೈ ಸೊ ಸೋ ಸೌ",
               "¸ï ¸À ¸Á ¹ ¹Ã ¸ÀÄ ¸ÀÆ ¸ÀÈ ¸É ¸ÉÃ ¸ÉÊ ¸ÉÆ ¸ÉÆÃ ¸Ë")
testsgen_basic("ಹ್ ಹ ಹಾ ಹಿ ಹೀ ಹು ಹೂ ಹೃ ಹೆ ಹೇ ಹೈ ಹೊ ಹೋ ಹೌ",
               "ºï ºÀ ºÁ » »Ã ºÀÄ ºÀÆ ºÀÈ ºÉ ºÉÃ ºÉÊ ºÉÆ ºÉÆÃ ºË")
testsgen_basic("ಳ್ ಳ ಳಾ ಳಿ ಳೀ ಳು ಳೂ ಳೃ ಳೆ ಳೇ ಳೈ ಳೊ ಳೋ ಳೌ",
               "¼ï ¼À ¼Á ½ ½Ã ¼ÀÄ ¼ÀÆ ¼ÀÈ ¼É ¼ÉÃ ¼ÉÊ ¼ÉÆ ¼ÉÆÃ ¼Ë")
