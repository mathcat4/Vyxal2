codepage  = "λƛ¬∧⟑∨⟇÷«\n»°•‘†€"
codepage += "½∆ø↔¢⌐æʀʁɾɽÞƈ∞¨ "
codepage += "!\"#$%&'()*+,-./01"
codepage += "23456789:;<=>?@A"
codepage += "BCDEFGHIJKLMNOPQ"
codepage += "RSTUVWXYZ[\\]`^_abc"
codepage += "defghijklmnopqrs"
codepage += "tuvwxyz{|}ß↑↓∴∵›"
codepage += "‹∷¤ð→←βτȧḃċḋėḟġḣ"
codepage += "ḭŀṁṅȯṗṙṡṫẇẋẏż√⟨⟩"
codepage += "‛₀₁₂₃₄₅₆₇₈¶⁋§ε¡"
codepage += "∑¦≈µȦḂĊḊĖḞĠḢİĿṀṄ"
codepage += "ȮṖṘṠṪẆẊẎŻ₌₍⁰¹²∇⌈"
codepage += "⌊¯±₴…□↳↲⋏⋎꘍ꜝ℅≤≥"
codepage += "≠⁼ƒɖ∪∩⊍£¥⇧⇩ǍǎǏǐǑ"
codepage += "ǒǓǔ⁽‡≬×⁺↵⅛¼¾Π„‟"

assert len(codepage) == 256

command_dict = {
    "¬": ("stack.append(int(not pop(stack)))", 1),
    "∧": ("rhs, lhs = pop(stack, 2); stack.append(lhs and rhs)", 2),
    "⟑": ("rhs, lhs = pop(stack, 2); stack.append(rhs and lhs)", 2),
    "∨": ("rhs, lhs = pop(stack, 2); stack.append(lhs or rhs)", 2),
    "⟇": ("rhs, lhs = pop(stack, 2); stack.append(rhs or lhs)", 2),
    "÷": ("for item in iterable(pop(stack)): stack.append(item)", 1),
    "•": ("rhs, lhs = pop(stack, 2); stack.append(log(lhs, rhs))", 2),
    "†": ("fn = pop(stack); stack += function_call(fn, stack)", 1),
    "€": ("rhs, lhs = pop(stack, 2); stack.append(split(lhs, rhs))", 2),
    "½": ("stack.append(divide(pop(stack), 2))", 1),
    "↔": ("rhs, lhs = pop(stack, 2); stack.append(combinations_replace_generate(lhs, rhs))", 2),
    "⌐": ("stack.append(complement(pop(stack)))", 1),
    "æ": ("stack.append(is_prime(pop(stack)))", 1),
    "ʀ": ("stack.append(orderless_range(0, int(add(pop(stack), 1))))", 1),
    "ʁ": ("stack.append(orderless_range(0, int(pop(stack))))", 1),
    "ɾ": ("stack.append(orderless_range(1, int(add(pop(stack), 1))))", 1),
    "ɽ": ("stack.append(orderless_range(1, int(pop(stack))))", 1),
    "ƈ": ("rhs, lhs = pop(stack, 2); stack.append(ncr(lhs, rhs))", 2),
    "∞": ("stack.append(Generator(lambda x: x))", 0),
    "!": ("stack.append(len(stack))", 0),
    '"': ("rhs, lhs = pop(stack, 2); stack.append([lhs, rhs])", 2),
    "$": ("top = pop(stack); over = pop(stack); stack += [top, over]", 2),
    "%": ("rhs, lhs = pop(stack, 2); stack.append(modulo(lhs, rhs))", 2),
    "*": ("rhs, lhs = pop(stack, 2); stack.append(multiply(lhs, rhs))", 2),
    "+": ("rhs, lhs = pop(stack, 2); stack.append(add(lhs, rhs))", 2),
    ",": ("VY_print(pop(stack)); printed = True", 1),
    "-": ("rhs, lhs = pop(stack, 2); stack.append(subtract(lhs, rhs))", 2),
    "/": ("rhs, lhs = pop(stack, 2); stack.append(divide(lhs, rhs))", 2),
    ":": ("temp = deref(pop(stack)); stack += [temp]*2", 1),
    "^": ("stack = stack[::-1]", 0),
    "_": ("pop(stack)", 1),
    "<": ("rhs, lhs = pop(stack, 2); stack.append(compare(lhs, rhs, Comparitors.LESS_THAN))", 2),
    ">": ("rhs, lhs = pop(stack, 2); stack.append(compare(lhs, rhs, Comparitors.GREATER_THAN))", 2),
    "=": ("rhs, lhs = pop(stack, 2); stack.append(compare(lhs, rhs, Comparitors.EQUALS))", 2),
    "?": ("stack.append(get_input(0))", 0),
    "A": ("stack.append(int(all(iterable(pop(stack)))))", 1),
    "B": ("stack.append(VY_int(pop(stack), 2))", 1),
    "C": ("stack.append(chrord(pop(stack)))", 1),
    "D": ("temp = deref(pop(stack)); stack += [temp]*3", 1),
    "E": ("stack.append(VY_eval(pop(stack)))", 1),
    "F": ("fn, vector = pop(stack, 2); stack.append(VY_filter(fn, vector))", 2),
    "G": ("stack.append(VY_max(iterable(pop(stack))))", 1),
    "H": ("stack.append(VY_int(pop(stack), 16))", 1),
    "I": ("stack.append(VY_int(pop(stack)))", 1),
    "J": ("rhs, lhs = pop(stack, 2); stack.append(join(lhs, rhs))", 2),
    "K": ("stack.append(divisors_of(pop(stack)))", 1),
    "L": ("stack.append(len(iterable(pop(stack))))", 1),
    "M": ("fn, vector = pop(stack, 2); stack.append(VY_map(fn, vector))", 2),
    "N": ("stack.append(negate(pop(stack)))", 1),
    "O": ("needle, haystack = pop(stack, 2); stack.append(iterable(haystack).count(needle))", 2),
    "P": ("rhs, lhs = pop(stack, 2); stack.append(VY_str(lhs).strip(VY_str(rhs)))", 2),
    "Q": ("exit()", 0),
    "R": ("fn, vector = pop(stack, 2); stack += VY_reduce(fn, vector)", 2),
    "S": ("stack.append(VY_str(pop(stack)))", 1),
    "T": ("stack.append([n for n in iterable(pop(stack)) if bool(n)])", 1),
    "U": ("stack.append(uniquify(pop(stack)))", 1),
    "V": ("replacement, needle, haystack = pop(stack, 3); stack.append(replace(haystack, needle, replacement))", 3),
    "W": ("stack = [deref(stack)]", 0),
    "X": ("context_level += 1", 0),
    "Y": ("rhs, lhs = pop(stack, 2); stack.append(interleave(lhs, rhs))", 2),
    "Z": ("rhs, lhs = pop(stack, 2); stack.append(Generator(VY_zip(iterable(lhs), iterable(rhs))))", 2),
    "a": ("stack.append(int(any(iterable(pop(stack)))))", 1),
    "b": ("stack.append(VY_bin(pop(stack)))", 1),
    "c": ("needle, haystack = pop(stack, 2); haystack = iterable(haystack, str)\nif type(haystack) is str: needle = VY_str(needle)\nstack.append(int(needle in iterable(haystack, str)))", 2),
    "d": ("stack.append(multiply(pop(stack), 2))", 1),
    "e": ("rhs, lhs = pop(stack, 2); stack.append(exponate(lhs, rhs))", 2),
    "f": ("stack.append(flatten(iterable(pop(stack))))", 1),
    "g": ("stack.append(VY_min(iterable(pop(stack))))", 1),
    "h": ("stack.append(iterable(pop(stack))[0])", 1),
    "i": ("rhs, lhs = pop(stack, 2)\nstack.append(index(lhs, rhs))", 2),
    "j": ("rhs, lhs = pop(stack, 2); stack.append(str(rhs).join([str(x) for x in iterable(lhs)]))", 2),
    "l": ("rhs, lhs = pop(stack, 2); stack.append(nwise_pair(lhs, rhs))", 2),
    "m": ("item = pop(stack); stack.append(add(item, reverse(item)))", 1),
    "n": ("stack.append(context_values[context_level % len(context_values)])", 0),
    "o": ("needle, haystack = pop(stack, 2); stack.append(remove(haystack, needle))", 2),
    "p": ("rhs, lhs = pop(stack, 2); stack.append(int(str(lhs).startswith(str(rhs))))", 2),
    "q": ("stack.append('`' + VY_str(pop(stack)) + '`')", 1),
    "r": ("rhs, lhs = pop(stack, 2); stack.append(orderless_range(lhs, rhs))", 2),
    "s": ("stack.append(VY_sorted(pop(stack)))", 1),
    "t": ("stack.append(iterable(pop(stack))[-1])", 1),
    "u": ("stack.append(-1)", 0),
    "w": ("stack.append([pop(stack)])", 1),
    "x": ("context_level -= 1", 0),
    "y": ("stack += uninterleave(pop(stack))", 1),
    "z": ("fn, vector = pop(stack, 2); stack += VY_zipmap(fn, vector)", 2),
    "↑": ("stack.append(max(pop(stack), key=lambda x: x[-1]))", 1),
    "↓": ("stack.append(min(pop(stack), key=lambda x: x[-1]))", 1),
    "∴": ("rhs, lhs = pop(stack, 2); stack.append(VY_max(lhs, rhs))", 2),
    "∵": ("rhs, lhs = pop(stack, 2); stack.append(VY_min(lhs, rhs))", 2),
    "β": ("alphabet, number = pop(stack, 2); stack.append(utilities.from_ten(number, alphabet))", 2),
    "τ": ("alphabet, number = pop(stack, 2); stack.append(utilities.to_ten(number, alphabet))", 2),
    "›": ("stack.append(add(pop(stack), 1))", 1),
    "‹": ("stack.append(subtract(pop(stack), 1))", 1),
    "∷": ("stack.append(modulo(pop(stack), 2))", 1),
    "¤": ("stack.append('')", 0),
    "ð": ("stack.append(' ')", 0),
    "ȧ": ("stack.append(VY_abs(pop(stack)))", 1),
    "ḃ": ("stack.append(int(not compare(pop(stack), 0, Comparitors.EQUALS)))", 1),
    "ċ": ("stack.append(compare(pop(stack), 1, Comparitors.NOT_EQUALS))", 1),
    "ḋ": ("rhs, lhs = pop(stack, 2); stack.append(VY_divmod(lhs, rhs))", 2), # Dereference because generators could accidentally get exhausted.
    "ė": ("stack.append(Generator(enumerate(iterable(pop(stack)))))", 1),
    "ḟ": ("rhs, lhs = pop(stack, 2); stack.append(find(lhs, rhs))", 2),
    "ġ": ("rhs = pop(stack)\nif VY_type(rhs) in [list, Generator]: stack.append(gcd(rhs))\nelse: stack.append(gcd(pop(stack), rhs))", 1),
    "ḣ": ("top = iterable(pop(stack)); stack.append(top[0]); stack.append(top[1:])", 1),
    "ḭ": ("rhs, lhs = pop(stack, 2); stack.append(integer_divide(lhs, rhs))", 2),
    "ŀ": ("start, needle, hastack = pop(stack, 3); stack.append(find(haystack, needle, start))", 3),
    "ṁ": ("top = iterable(pop(stack)); stack.append(divide(summate(top), len(top)))", 1),
    "ṅ": ("stack.append(first_n(pop(stack)))", 1),
    "ȯ": ("n, fn = pop(stack, 2); stack.append(first_n(fn, n))", 2),
    "ṗ": ("stack.append(powerset(iterable(pop(stack))))", 1),
    "ṙ": ("stack.append(VY_round(pop(stack)))", 1),
    "ṡ": ("fn , vector = pop(stack, 2); stack.append(VY_sorted(vector, fn))", 2),
    "ṫ": ("vector = iterable(pop(stack)); stack.append(vector[:-1]); stack.append(vector[-1])", 1),
    "ẇ": ("rhs, lhs = pop(stack, 2); stack.append(wrap(lhs, rhs))", 2),
    "ẋ": ("rhs, lhs = pop(stack, 2); main = None;\nif VY_type(lhs) is Function: main = pop(stack)\nstack.append(repeat(lhs, rhs, main))", 2),
    "ẏ": ("obj = iterable(pop(stack)); stack.append(Generator(range(0, len(obj))))", 1),
    "ż": ("obj = iterable(pop(stack)); stack.append(Generator(range(1, len(obj) + 1)))", 1),
    "√": ("stack.append(exponate(pop(stack), 0.5))", 1),
    "₀": ("stack.append(10)", 0),
    "₁": ("stack.append(100)", 0),
    "₂": ("stack.append(const_divisibility(pop(stack), 2, lambda item: len(item) % 2 == 0))", 1),
    "₃": ("stack.append(const_divisibility(pop(stack), 3, lambda item: len(item) == 1))", 1),
    "₄": ("stack.append(26)", 0),
    "₅": ("top = pop(stack); res = const_divisibility(top, 5, lambda item: (top, len(item)))\nif type(res) is tuple: stack += list(res)\nelse: stack.append(res)", 1),
    "₆": ("stack.append(64)", 0),
    "₇": ("stack.append(128)", 0),
    "₈": ("stack.append(256)", 0),
    "¶": ("stack.append('\\n')", 0),
    "⁋": ("stack.append('\\n'.join([VY_str(x) for x in iterable(pop(stack))]))", 1),
    "§": ("stack.append(vertical_join(pop(stack)))", 1),
    "ε": ("padding, vector = pop(stack, 2); stack.append(vertical_join(vector, padding))", 2),
    "¡": ("stack.append(factorial(pop(stack)))", 1),
    "∑": ("stack.append(summate(pop(stack)))", 0),
    "¦": ("stack.append(cumulative_sum(iterable(pop(stack))))", 1),
    "≈": ("stack.append(int(len(set(iterable(pop(stack)))) == 1))", 1),
    "Ȧ": ("value, index, vector = pop(stack, 3); stack.append(assigned(iterable(vector), index, value))", 3),
    "Ḃ": ("stack += bifuricate(pop(stack))", 1),
    "Ċ": ("stack.append(counts(pop(stack)))", 1),
    "Ḋ": ("rhs, lhs = pop(stack, 2); stack.append(compare(modulo(lhs, rhs), 0, Comparitors.EQUALS))", 2),
    "Ė": ("code = VY_exec(pop(stack)); stack.append(code)", 1),
    "Ḟ": ("""top = pop(stack)
if VY_type(top) is Number:
    limit = int(top); vector = pop(stack)
else:
    limit = -1; vector = top
fn = pop(stack)
stack.append(Generator(fn, limit=limit, initial=iterable(vector)))
""", 2),
    "Ġ": ("stack.append(group_consecutive(iterable(pop(stack))))", 1),
    "Ḣ": ("stack.append(iterable(pop(stack))[1:])", 1),
    "İ": ("indexes, vector = pop(stack, 2); stack.append(indexed_into(iterable(vector), iterable(indexes)))", 2),
    "Ŀ": ("new, original, string = pop(stack, 3)\nif Function in map(type, (new, original, string)): stack.append(repeat_no_collect(original, new, string))\nelse: stack.append(transilterate(iterable(original, str), iterable(new, str), iterable(string, str)))", 3),
    "Ṁ": ("item, index, vector = pop(stack, 3);\nif Function in map(type, (item, index, vector)): stack.append(map_every_n(vector, item, index))\nelse: stack.append(inserted(vector, item, index))", 3),
    "Ṅ": ("top = pop(stack);\nif VY_type(top) == Number:stack.append(Generator(partition(top)))\nelse: stack.append(' '.join([VY_str(x) for x in top]))", 1), #---------------------------
    "Ȯ": ("if len(stack) >= 2: stack.append(stack[-2])\nelse: stack.append(get_input(0))", 0),
    "Ṗ": ("stack.append(Generator(permutations(iterable(pop(stack)))))", 1),
    "Ṙ": ("stack.append(reverse(pop(stack)))", 1),
    "Ṡ": ("stack = [summate(stack)]", 0),
    "Ṫ": ("stack.append(iterable(pop(stack), str)[:-1])", 1),
    "Ẇ": ("rhs, lhs = pop(stack, 2); stack.append(split(lhs, rhs, True))", 2),
    "Ẋ": ("rhs, lhs = pop(stack, 2); stack.append(cartesian_product(lhs, rhs))", 2),
    "Ẏ": ("index, vector = pop(stack, 2); stack.append(iterable(vector)[0:index])", 2),
    "Ż": ("index, vector = pop(stack, 2); stack.append(iterable(vector)[1:index])", 2),
    "⁰": ("stack.append(input_values[0][0][-1])", 0),
    "¹": ("stack.append(input_values[0][0][-2])", 0),
    "²": ("x = pop(stack); stack.append(multiply(deref(x), deref(x)))", 1),
    "∇": ("c, b, a = pop(stack, 3); stack.append(c); stack.append(a); stack.append(b)", 3),
    "⌈": ("stack.append(ceiling(pop(stack)))", 1),
    "⌊": ("stack.append(floor(pop(stack)))", 1),
    "¯": ("stack.append(deltas(pop(stack)))", 1),
    "±": ("stack.append(sign_of(pop(stack)))", 1),
    "₴": ("VY_print(pop(stack), end=''); printed = True", 1),
    "…": ("top = pop(stack); stack.append(top); VY_print(top); printed = True", 0),
    "□": ("if inputs: stack.append([inputs])\nelse:\n    s, x = [], input()\n    while x:\n        s.append(Vy_eval(x)); x = input()", 0),
    "↳": ("rhs, lhs = pop(stack, 2); stack.append(rshift(lhs, rhs))", 2),
    "↲": ("rhs, lhs = pop(stack, 2); stack.append(lshift(lhs, rhs))", 2),
    "⋏": ("rhs, lhs = pop(stack, 2); stack.append(bit_and(lhs, rhs))", 2),
    "⋎": ("rhs, lhs = pop(stack, 2); stack.append(bit_or(lhs, rhs))", 2),
    "꘍": ("rhs, lhs = pop(stack, 2); stack.append(bit_xor(lhs, rhs))", 2),
    "ꜝ": ("stack.append(bit_not(pop(stack)))", 1),
    "℅": ("stack.append(random.choice(iterable(pop(stack))))", 1),
    "≤": ("rhs, lhs = pop(stack, 2); stack.append(compare(lhs, rhs, Comparitors.LESS_THAN_EQUALS))", 2),
    "≥": ("rhs, lhs = pop(stack, 2); stack.append(compare(lhs, rhs, Comparitors.GREATER_THAN_EQUALS))", 2),
    "≠": ("rhs, lhs = pop(stack, 2); stack.append(compare(lhs, rhs, Comparitors.NOT_EQUALS))", 2),
    "⁼": ("rhs, lhs = pop(stack, 2); stack.append(int(lhs == rhs))", 2),
    "ƒ": ("stack.append(fractionify(pop(stack)))", 1),
    "ɖ": ("stack.append(decimalify(pop(stack)))", 1),
    "×": ("stack.append('*')", 0),
    "∪": ("rhs, lhs = pop(stack, 2); stack.append(set_union(lhs, rhs))", 2),
    "∩": ("rhs, lhs = pop(stack, 2); stack.append(set_intersection(lhs, rhs))", 2),
    "⊍": ("rhs, lhs = pop(stack, 2); stack.append(set_caret(lhs, rhs))", 2),
    "£": ("register = pop(stack)", 1),
    "¥": ("stack.append(register)", 0),
    "⇧": ("stack.append(graded(pop(stack)))", 1),
    "⇩": ("stack.append(graded_down(pop(stack)))", 1),
    "Ǎ": ("stack.append(two_power(pop(stack)))", 1),
    "ǎ": ("stack.append(nth_prime(pop(stack)))", 1),
    "Ǐ": ("stack.append(prime_factors(pop(stack)))", 1),
    "ǐ": ("stack.append(all_prime_factors(pop(stack)))", 1),
    "Ǒ": ("rhs, lhs = pop(stack, 2); stack.append(order(lhs, rhs))", 2),
    "Ǔ": ("rhs, lhs = pop(stack, 2); stack += overloaded_iterable_shift(lhs, rhs, ShiftDirections.LEFT)", 2),
    "ǔ": ("rhs, lhs = pop(stack, 2); stack += overloaded_iterable_shift(lhs, rhs, ShiftDirections.RIGHT)", 2),
    "¢": ("replacement, needle, haystack = pop(stack, 3); stack.append(infinite_replace(haystack, needle, replacement)", 3),
    "↵": ("stack.append(split_newlines_or_pow_10(pop(stack))", 1),
    "⅛": ("global_stack.append(pop(stack))", 1),
    "¼": ("stack.append(pop(global_stack))", 0),
    "¾": ("stack.append(deref(global_stack))", 0),
    "Π": ("stack.append(product(iterable(pop(stack))))", 1),
    "„": ("stack = iterable_shift(stack, ShiftDirections.LEFT)", 0),
    '‟': ("stack = iterable_shift(stack, ShiftDirections.RIGHT)", 0)
}

math_command_dict = {
    "S": ("arg = pop(stack); stack.append(vectorise(math.asin, arg))", 1),
    "C": ("arg = pop(stack); stack.append(vectorise(math.acos, arg))", 1),
    "T": ("arg = pop(stack); stack.append(vectorise(math.atan, arg))", 1),
    "q": ("coeff_a, coeff_b = pop(stack, 2); stack.append(polynomial([coeff_a, coeff_b, 0]))", 2),
    "Q": ("coeff_b, coeff_c = pop(stack, 2); stack.append(polynomial([1, coeff_b, coeff_c]))", 2),
    "P": ("coeff = iterable(pop(stack)); stack.append(polynomial(coeff));", 1),
    "s": ("arg = pop(stack); stack.append(vectorise(math.sin, arg))", 1),
    "c": ("arg = pop(stack); stack.append(vectorise(math.cos, arg))", 1),
    "t": ("arg = pop(stack); stack.append(vectorise(math.tan, arg))", 1),
    "ƈ": ("rhs, lhs = pop(stack, 2); stack.append(divide(factorial(lhs), factorial(subtract(lhs, rhs))))", 2),
    "±": ("rhs, lhs = pop(stack, 2); stack.append(vectorise(math.copysign, lhs, rhs))", 2),
    "K": ("arg = pop(stack); stack.append(summate(join(0, divisors_of(arg)[:-1])))", 1),
    "²": ("arg = pop(stack); stack.append(compare(exponate(exponate(arg, 0.5), 2), arg, Comparitors.EQUALS))", 1),
    "e": ("arg = pop(stack); stack.append(vectorise(math.exp, arg))", 1),
    "E": ("arg = pop(stack); stack.append(vectorise(math.expm1, arg))", 1),
    "L": ("arg = pop(stack); stack.append(vectorise(math.log, arg))", 1),
    "l": ("arg = pop(stack); stack.append(vectorise(math.log2, arg))", 1),
    "τ": ("arg = pop(stack); stack.append(vectorise(math.log10, arg))", 1),
    "d": ("rhs, lhs = pop(stack, 2); stack.append(distance_between(lhs, rhs))", 2),
    "D": ("arg = pop(stack); stack.append(vectorise(math.degrees, arg))", 1),
    "R": ("arg = pop(stack); stack.append(vectorise(math.radians, arg))", 1),
    "≤": ("arg = pop(stack); stack.append(compare(VY_abs(arg), 1, Comparitors.LESS_THAN_EQUALS))", 1)
}

string_command_dict = {
    "o": ("needle, haystack = pop(stack, 2); stack.append(infinite_replace(haystack, needle, ''))", 2),
    "V": ("replacement, needle, haystack = pop(stack, 3); stack.append(infinite_replace(haystack, needle, replacement)", 3),
    "c": ("string = pop(stack); stack.append('«' + utilities.from_ten(utilities.to_ten(string, utilities.base27alphabet), encoding.codepage_string_compress) + '«')", 1),
    "C": ("number = pop(stack); stack.append('»' + utilities.from_ten(number, encoding.codepage_number_compress) + '»')", 1),
    "l": ("stack.append(str(pop(stack)).lower())", 1),
    "U": ("stack.append(str(pop(stack)).upper())", 1),
    "t": ("stack.append(str(pop(stack)).title())", 1),
    "$": ("stack.append(str(pop(stack)).swapcase())", 1),
    "Ċ": ("stack.append(centre(iterable(pop(stack))))", 1),
    "m": ("stack.append(palindromise(iterable(pop(stack))))", 1),
    "e": ("stack.append(run_length_encode(iterable(pop(stack), str)))", 1), 
    "d": ("stack.append(run_length_decode(pop(stack)))", 1)
}

list_command_dict = {
    "…": ("value, vector = pop(stack, 2); stack.append(distribute(vector, value))", 2),
    "↓": ("fn, vector = pop(stack, 2); stack.append(min(VY_zipmap(fn, vector), key=lambda x: x[-1]))", 2),
    "↑": ("fn, vector = pop(stack, 2); stack.append(max(VY_zipmap(fn, vector), key=lambda x: x[-1]))", 2),
    "ḋ": ("vector = pop(stack); stack.append(all_combinations(vector));", 1),
    "F": ("stack.append(Generator(fibonacci(), is_numeric_sequence=True))", 0),
    "!": ("stack.append(Generator(factorials(), is_numeric_sequence=True))", 0)
}

misc_command_dict = {
    "U": ("if not online_version: stack.append(urllib.request.urlopen(pop(stack)).read().decode())", 1)
}
