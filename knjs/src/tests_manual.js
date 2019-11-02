var data = [
	["¸ÁévÀAvÀæ", "ಸ್ವಾತಂತ್ರ"],
    ["AiÀÄdÕ", "ಯಜ್ಞ"],
    ["PÁåA¥ÉÇÌÃ", "ಕ್ಯಾಂಪ್ಕೋ"],
    ["¥ÉÇæ", "ಪ್ರೊ"],
    ["DAiÉÄÌ", "ಆಯ್ಕೆ"],
    ["®PÀëå", "ಲಕ್ಷ್ಯ"],
    ["J®ègÉÆ¼ÀUÉÆAzÁUÀÄ ªÀÄAPÀÄwªÀÄä", "ಎಲ್ಲರೊಳಗೊಂದಾಗು ಮಂಕುತಿಮ್ಮ"],
    ["PÀ£ÀßqÀ ªÀÄvÀÄÛ ¸ÀA¸ÀÌøw E¯ÁSÉ", "ಕನ್ನಡ ಮತ್ತು ಸಂಸ್ಕೃತಿ ಇಲಾಖೆ"],
    ["Pïgï", "ಕ್‌ರ್"],
    ["gÁåAPï", "ರ‍್ಯಾಂಕ್"],
    ["AiÀiÁAðPï", "ರ್ಯಾಂಕ್"],
    ["¸ÀÆAiÀÄð", "ಸೂರ್ಯ"],
    ["¸ÀÆAiÀiÁð", "ಸೂರ್ಯಾ"],
    ["PÁåPï", "ಕ್ಯಾಕ್"],
    ["UÉÆæPï", "ಗ್ರೊಕ್"],
    ["¥ÀæweÉÕ", "ಪ್ರತಿಜ್ಞೆ"],
    ["¦æÃw", "ಪ್ರೀತಿ"],
    ["CAiÉÆåÃ", "ಅಯ್ಯೋ"],
    ["UÁæªÀiÁ¥sÉÇÃ£ÀÄ", "ಗ್ರಾಮಾಫೋನು"],
    ["¨ÉÃrPÉÆ¼ÀÄîwÛzÉÝÃ£É", "ಬೇಡಿಕೊಳ್ಳುತ್ತಿದ್ದೇನೆ"],
    ["UÉÆÃ¾õÀÎgÉ", "ಗೋಱ್ಗರೆ"],
    ["ªÀÄÆgÀÄ ¥ÉÇæmÁ£ïUÀ¼ÀÄ", "ಮೂರು ಪ್ರೊಟಾನ್‌ಗಳು"],
    ["¨sÁμÉ¬ÄAzÀ", "ಭಾಷೆಯಿಂದ"],
    ["¥ÉÇÃZÀÄðVÃ¸ï", "ಪೋರ್ಚುಗೀಸ್"],
    ["ªÀiÁqÀÄvÀÛÉA§ÄzÀgÀ°è", "ಮಾಡುತ್ತೆಂಬುದರಲ್ಲಿ", true],
    ["ªÀiÁqÀÄvÉÛA§ÄzÀgÀ°è",  "ಮಾಡುತ್ತೆಂಬುದರಲ್ಲಿ"],
    ["CªÀ¢üAiÀÄ°èAiÉÄÃ", "ಅವಧಿಯಲ್ಲಿಯೇ"],
    ["CªÀ¢ü0iÀÄ°è0iÉÄÃ", "ಅವಧಿಯಲ್ಲಿಯೇ", true]
]

data.forEach(function(item){
    QUnit.test( "a2u " + item[0] + " => " + item[1], function( assert ) {
	assert.strictEqual(kn.ascii_to_unicode(item[0]), item[1]);
    });
    if (item[2] === undefined) {
	QUnit.test( "u2a " + item[1] + " => " + item[0], function( assert ) {
	    assert.strictEqual(kn.unicode_to_ascii(item[1]), item[0]);
	});
    }
});

QUnit.test( "u2a ೦ ೧ ೨ ೩ ೪ ೫ ೬ ೭ ೮ ೯ => 0 1 2 3 4 5 6 7 8 9", function( assert ) {
	assert.strictEqual(kn.unicode_to_ascii("೦ ೧ ೨ ೩ ೪ ೫ ೬ ೭ ೮ ೯"), "0 1 2 3 4 5 6 7 8 9");
});

QUnit.test( "u2a 0 1 2 3 4 5 6 7 8 9 => 0 1 2 3 4 5 6 7 8 9", function( assert ) {
	assert.strictEqual(kn.unicode_to_ascii("0 1 2 3 4 5 6 7 8 9"), "0 1 2 3 4 5 6 7 8 9");
});

QUnit.test( "a2u 0 1 2 3 4 5 6 7 8 9 => ೦ ೧ ೨ ೩ ೪ ೫ ೬ ೭ ೮ ೯", function( assert ) {
	assert.strictEqual(kn.ascii_to_unicode("0 1 2 3 4 5 6 7 8 9"), "೦ ೧ ೨ ೩ ೪ ೫ ೬ ೭ ೮ ೯");
});

QUnit.test( "a2u 0 1 2 3 4 5 6 7 8 9 => 0 1 2 3 4 5 6 7 8 9", function( assert ) {
	assert.strictEqual(kn.ascii_to_unicode("0 1 2 3 4 5 6 7 8 9", true), "0 1 2 3 4 5 6 7 8 9");
});
