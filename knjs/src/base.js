function Kn(){};
var kn = new Kn();

Kn.prototype._uni_halant = "ccd";
Kn.prototype._uni_prev_value_chars = [
	"cbe", "cbf", "cc0", "cc1",
    "cc2", "cc3", "cc4", "cc6",
	"cc7", "cc8", "cca", "ccb",
	"ccc", "ccd", "c82", "c83", "200d"
];

Kn.prototype.letters = function(txt) {
	function hexval(i) {
		return txt[i].charCodeAt(0).toString(16);
	}

	function prev_hexval(i) {
		if (txt[i-1]){
			return txt[i-1].charCodeAt(0).toString(16);
		}
		return "";
	};

	function iskn(i) {
		var re = new RegExp(/^[\u0C80-\u0CFF\u200D]+$/);
		return txt[i].match(re) ? true : false;
	};
	
    var l = txt.length;
    var out = [];
	
    for (var i=0; i<l; i++) {
        var cond = (this._uni_prev_value_chars.indexOf(hexval(i)) != -1 ||
                    prev_hexval(i) === this._uni_halant);
		
        if (out.length > 0 && iskn(i) && cond) {
            out[out.length-1] += txt[i];
        }
        else {
            out.push(txt[i]);
        }
    }
    return out;
};

Kn.prototype.length = function(txt){
    return this.letters(txt).length;
};


Kn.prototype._rearrange_and_replace = function(inp){
    // If inp is vowel, then no need to change
	var that = this;

    // If input letter is only vowel, then directly convert it
    if (this._vowels.indexOf(inp) !== -1){
        return this._u2a_map[inp];
    }

    // Detect kaagunitha and convert to ASCII using Map
    inp = inp.replace(this._REGEX_UNI_CONSONANT_PLUS_VOWEL, function(match, g1, g2, g3){
        return that._substitute_ascii(g1, [g2, g3], []);
    });

    // Arkavattu vs Ra vattu
    // If ZWJ is not used then use Arkavattu, First vattakshara after Ra
    // is treated as new Base, and add arkavattu in the end
    inp = inp.replace(this._REGEX_UNI_REPH_WITHOUT_ZWJ,
                      function(match, g1, g2, g3, g4, g5, g6){
                          // First vattakshara will become base
                          var base = g2.replace(that._halant, "");
                          var append_chars = [that._ascii_arkavattu];
                          return that._substitute_ascii(base, [g5, g6], [g3, g4], append_chars);
                      });
    
    // Detect Vattakshara(with ZWJ or Without), Ignore ZWJ in match
    inp = inp.replace(this._REGEX_UNI_VATTAKSHARA,
                      function(match, g1, g2, g3, g4, g5, g6){
                          return that._substitute_ascii(g1, [g5, g6], [g2, g3, g4]);
                      });
    return inp;
}


Kn.prototype._substitute_ascii = function(base, dep_vowel, vattaksharagalu, append_chars){
    var op = "";
    if (dep_vowel[0] === undefined){
        // Dependent vowel is not present, that means only consonant
        // convert it directly using Map
        op += this._u2a_map[base];
    }
    else{
        if (this._anusvara_visarga.indexOf(dep_vowel[0]) === -1){
            // If first dependent vowel is not Anuswara and visarga then
            // join base and dep vowel since in ASCII vattakshara is added in
            // the end after dep vowel(In Unicode it is dep vowel + vattakshara)
            op += this._u2a_map[base + dep_vowel[0]];
        }
        else{
            // Only base now, anuswara visarga will be added later
            op += this._u2a_map[base];
        }
    }

    // If Vattaksharagalu exists, replace with ASCII vattakshara and add
    for (var i=0; i<vattaksharagalu.length; i++){
        if (vattaksharagalu[i] !== undefined){
            op += this._u2a_map[vattaksharagalu[i]];
        }
    }

    // Previously not added anuswara visarga, add it now since vattakshara
    // already added.
    if (this._anusvara_visarga.indexOf(dep_vowel[0]) !== -1){
        op += this._u2a_map[dep_vowel[0]];
    }

    // If contains second dep vowel add it to the converted
    if (dep_vowel[1] !== undefined){
        op += this._u2a_map[dep_vowel[1]];
    }

    if (append_chars !== undefined) {
        op += append_chars.join("");
    }
    return op;
}

Kn.prototype.ascii_to_unicode = function (txt, english_numbers){
    that = this;

    // Insert ZWNJ if required before converting anything else
    txt = txt.replace(this._REGEX_ASCII_ZWNJ,
                      function(match, g1, g2) {
                          return g1 + that._uni_zwnj + g2;
                      });

    // Replace all which can be replaced using Maps
	txt = this._replace_from_map(txt);
   
    // Identify dependent vowel followed by 3 level vattaksharas
    // Replace vattaksharas with equivalant unicode combination and
    // reorg and move dep vowel to end
	txt = txt.replace(this._REGEX_ASCII_VATTAKSHARA_3,
                      function(match, g1, g2, g3, g4){
                          return g2 + g3 + g4 + g1;
                      });

    // Identify dependent vowel followed by 2 level vattaksharas
    // Replace vattaksharas with equivalant unicode combination and
    // reorg and move dep vowel to end
	txt = txt.replace(this._REGEX_ASCII_VATTAKSHARA_2,
                      function(match, g1, g2, g3){
                          return g2 + g3 + g1;
                      });

    // Identify dependent vowel followed by 1 level vattaksharas
    // Replace vattaksharas with equivalant unicode combination and
    // reorg and move dep vowel to end
	txt = txt.replace(this._REGEX_ASCII_VATTAKSHARA_1,
                      function(match, g1, g2){
                          return g2 + g1;
                      });

    // If any more vattakshara pending, without dependent vowel
    // For example ಮ್ಮ
	txt = this._replace_vattakshara(txt);

    // Handle Numbers
    if (english_numbers === undefined || !english_numbers) {
        txt = this._to_unicode_numbers(txt);
    }

    // Now it is converted to Unicode except few left out chars

    // Handle Reph when ZWJ is used
    txt = txt.replace(this._REGEX_UNI_REPH_BEFORE_CONVERT,
                      function(match, g1, g2, g3, g4, g5, g6){
                          // Add ZWJ after Ra and retain others as is
                          var op = g1 + that._uni_zwj + g2;
                          if (g3 !== undefined){
                              op += g3;
                          }
                          if (g4 !== undefined){
                              op += g4;
                          }
                          if (g5 !== undefined){
                              op += g5;
                          }
                          if (g6 !== undefined){
                              op += g6;
                          }
                          return op;
                      });

    // Handle Reph when no ZWJ is used. If ascii arkavattu present in
    // the end, remove it and add Ra to the beginning and make first
    // char in Match as vattakshara
    txt = txt.replace(this._REGEX_UNI_ASCII_ARKAVATTU,
                      function(match, g1, g2, g3, g4, g5){
                          var op = that._uni_ra + that._halant + g1;
                          if (g2 !== undefined){
                              op += g2;
                          }
                          if (g3 !== undefined){
                              op += g3;
                          }
                          if (g4 !== undefined){
                              op += g4;
                          }
                          if (g5 !== undefined){
                              op += g5;
                          }

                          return op;
                      });
    
    return txt;
}

Kn.prototype.unicode_to_ascii = function(txt, english_numbers){
	var converted = [];
	var that = this;
    // Split into Kn letters and convert each letter to ASCII
	this.letters(txt).map(function(letter){
		converted.push(that._rearrange_and_replace(letter));
	});

    // Replace Anuswara and Visarga with ASCII chars
	txt = this._unicode_anusvara_visarga(converted.join(""));

    // Handle Numbers
    // No special handling required, Font will change the look and feel
    // of number in ASCII
    txt = this._to_ascii_numbers(txt)

    // ZWNJ
    // Since ZWNJ is not available in Map, it is not replaced
    // rest of the letters already replaced. We can remove this
    // char from output since in ASCII chars will not mix
    txt = txt.replace(/\u200c/g, "");
    
    // Handle Reph

    // Handle ZWJ and ZWNJ
    return txt;
}

