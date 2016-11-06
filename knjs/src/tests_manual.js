var data = [
	["¸ÁévÀAvÀæ", "ಸ್ವಾತಂತ್ರ"],
    ["AiÀÄdûÕ", "ಯಜ್ಞ"],
    ["PÁåA¥ÉÇÌÃ", "ಕ್ಯಾಂಪ್ಕೋ"],
    ["¥ÉÇæ", "ಪ್ರೊ"],
    ["D0iÉÄÌ", "ಆಯ್ಕೆ"],
    ["®PÀëöå", "ಲಕ್ಷ್ಯ"],
    ["J®ègÉÆ¼ÀUÉÆAzÁUÀÄ ªÀÄAPÀÄwªÀÄä", "ಎಲ್ಲರೊಳಗೊಂದಾಗು ಮಂಕುತಿಮ್ಮ"],
    ["PÀ£ÀßqÀ ªÀÄvÀÄÛ ¸ÀA¸ÀÌøw E¯ÁSÉ", "ಕನ್ನಡ ಮತ್ತು ಸಂಸ್ಕೃತಿ ಇಲಾಖೆ"],
    ["Pïgï", "ಕ್‌ರ್"],
    ["gÁåAPï", "ರ‍್ಯಾಂಕ್"],
    ["AiÀiÁAðPï", "ರ್ಯಾಂಕ್"],
    ["¸ÀÆAiÀÄð", "ಸೂರ್ಯ"],
    ["¸ÀÆAiÀiÁð", "ಸೂರ್ಯಾ"],
    ["PÁåPï", "ಕ್ಯಾಕ್"],
    ["UÉÆæPï", "ಗ್ರೊಕ್"]
]

data.forEach(function(item){
	QUnit.test( "a2u " + item[1], function( assert ) {
		assert.strictEqual(kn.ascii_to_unicode(item[0]), item[1]);
	});
	QUnit.test( "u2a " + item[1], function( assert ) {
		assert.strictEqual(kn.unicode_to_ascii(item[1]), item[0]);
	});
});

QUnit.test( "u2a ೦ ೧ ೨ ೩ ೪ ೫ ೬ ೭ ೮ ೯", function( assert ) {
	assert.strictEqual(kn.unicode_to_ascii("೦ ೧ ೨ ೩ ೪ ೫ ೬ ೭ ೮ ೯"), "0 1 2 3 4 5 6 7 8 9");
});

QUnit.test( "u2a 0 1 2 3 4 5 6 7 8 9", function( assert ) {
	assert.strictEqual(kn.unicode_to_ascii("0 1 2 3 4 5 6 7 8 9"), "0 1 2 3 4 5 6 7 8 9");
});

QUnit.test( "a2u 0 1 2 3 4 5 6 7 8 9", function( assert ) {
	assert.strictEqual(kn.ascii_to_unicode("0 1 2 3 4 5 6 7 8 9"), "೦ ೧ ೨ ೩ ೪ ೫ ೬ ೭ ೮ ೯");
});

QUnit.test( "a2u 0 1 2 3 4 5 6 7 8 9", function( assert ) {
	assert.strictEqual(kn.ascii_to_unicode("0 1 2 3 4 5 6 7 8 9", true), "0 1 2 3 4 5 6 7 8 9");
});
