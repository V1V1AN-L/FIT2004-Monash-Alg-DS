import unittest
from assignment2 import CatsTrie

__author__ = "Compiled by Junru (William) Wei, last updated 21/05/2023"


class CatGPTTest(unittest.TestCase):

    def test_default(self):
        sentences = ["abc", "abazacy", "dbcef", "xzz", "gdbc", "abazacy", "xyz", "abazacy", "dbcef", "xyz", "xxx",
                     "xzz"]
        trie = CatsTrie(sentences)
        self.assertTrue(trie.autoComplete("ab") == "abazacy")
        self.assertTrue(trie.autoComplete("a") == "abazacy")
        self.assertTrue(trie.autoComplete("dbcef") == "dbcef")
        self.assertTrue(trie.autoComplete("dbcefz") == None)
        self.assertTrue(trie.autoComplete("ba") == None)
        self.assertTrue(trie.autoComplete("x") == "xyz")
        self.assertTrue(trie.autoComplete("") == "abazacy")

    def test_default_2(self):
        sentences = ["abc", "abczacy", "dbcef", "xzz", "gdbc", "abczacy", "xyz", "abczacy", "dbcef", "xyz", "xxx",
                     "xzz"]
        trie = CatsTrie(sentences)
        self.assertTrue(trie.autoComplete("abc") == "abczacy")

    def test_01(self):
        sentences = ["ab", "a"]
        trie = CatsTrie(sentences)
        self.assertTrue(trie.autoComplete("") == "a")
        self.assertTrue(trie.autoComplete("a") == "a")
        self.assertTrue(trie.autoComplete("ab") == "ab")
        self.assertTrue(trie.autoComplete("abc") == None)
        self.assertTrue(trie.autoComplete("b") == None)
        self.assertTrue(trie.autoComplete("fittwozerozerofour") == None)

    def test_02(self):
        sentences = ["a", "ab"]
        trie = CatsTrie(sentences)
        self.assertTrue(trie.autoComplete("") == "a")
        self.assertTrue(trie.autoComplete("a") == "a")
        self.assertTrue(trie.autoComplete("ab") == "ab")
        self.assertTrue(trie.autoComplete("abc") == None)
        self.assertTrue(trie.autoComplete("b") == None)
        self.assertTrue(trie.autoComplete("fittwozerozerofour") == None)


    def test_05(self):
        sentences = ["a", "a", "aa", "aa"]
        trie = CatsTrie(sentences)
        self.assertTrue(trie.autoComplete("") == "a")
        self.assertTrue(trie.autoComplete("a") == "a")
        self.assertTrue(trie.autoComplete("aa") == "aa")
        self.assertTrue(trie.autoComplete("b") == None)


    """
        def test_06(self):
            sentences = []
            trie = CatsTrie(sentences)
            self.assertTrue(trie.autoComplete("") == None)
            self.assertTrue(trie.autoComplete("a") == None)
            self.assertTrue(trie.autoComplete("bruh") == None)
    """


    def test_07(self):
        # Extract of The Oxford 3000 word list
        # Source: https://www.oxfordlearnersdictionaries.com/wordlist/american_english/oxford3000/
        sentences = ["fit", "fix", "fixed", "flag", "flame", "flash", "flat", "flavor", "flesh", "flight", "float", "flood",
                     "floor", "flour", "flow", "flower", "flu", "fly", "flying", "focus", "fold", "folding", "folk",
                     "follow", "following", "food", "foot", "football", "for", "force", "forecast", "foreign", "forest",
                     "forever", "forget", "forgive", "fork", "form", "formal", "former", "formerly", "formula", "fortune",
                     "forward", "found", "foundation"]
        trie = CatsTrie(sentences)
        self.assertTrue(trie.autoComplete("") == "fit")
        self.assertTrue(trie.autoComplete("f") == "fit")
        self.assertTrue(trie.autoComplete("fi") == "fit")
        self.assertTrue(trie.autoComplete("fify") == None)
        self.assertTrue(trie.autoComplete("fit") == "fit")
        self.assertTrue(trie.autoComplete("fiu") == None)
        self.assertTrue(trie.autoComplete("fiv") == None)
        self.assertTrue(trie.autoComplete("fiw") == None)
        self.assertTrue(trie.autoComplete("fix") == "fix")
        self.assertTrue(trie.autoComplete("fixe") == "fixed")
        self.assertTrue(trie.autoComplete("fiy") == None)
        self.assertTrue(trie.autoComplete("fj") == None)
        self.assertTrue(trie.autoComplete("fk") == None)
        self.assertTrue(trie.autoComplete("fl") == "flag")
        self.assertTrue(trie.autoComplete("fla") == "flag")
        self.assertTrue(trie.autoComplete("flat") == "flat")
        self.assertTrue(trie.autoComplete("flo") == "float")
        self.assertTrue(trie.autoComplete("flu") == "flu")
        self.assertTrue(trie.autoComplete("fo") == "focus")
        self.assertTrue(trie.autoComplete("foo") == "food")
        self.assertTrue(trie.autoComplete("for") == "for")
        self.assertTrue(trie.autoComplete("forb") == None)
        self.assertTrue(trie.autoComplete("forc") == "force")
        self.assertTrue(trie.autoComplete("ford") == None)
        self.assertTrue(trie.autoComplete("monash") == None)


    def test_08(self):
        # Extract of the Constitution of the United States, Article I
        # Source: https://www.archives.gov/founding-docs/constitution-transcript
        sentences = [

            "we", "the", "people", "of", "the", "united", "states", "in", "order", "to", "form", "a", "more", "perfect",
            "union", "establish", "justice", "insure", "domestic", "tranquility", "provide", "for", "the", "common",
            "defence", "promote", "the", "general", "welfare", "and", "secure", "the", "blessings", "of", "liberty", "to",
            "ourselves", "and", "our", "posterity", "do", "ordain", "and", "establish", "this", "constitution", "for",
            "the", "united", "states", "of", "america",

            "article", "one",

            "section", "one",

            "all", "legislative", "powers", "herein", "granted", "shall", "be", "vested", "in", "a", "congress", "of",
            "the", "united", "states", "which", "shall", "consist", "of", "a", "senate", "and", "house", "of",
            "representatives",

            "section", "two",

            "the", "house", "of", "representatives", "shall", "be", "composed", "of", "members", "chosen", "every",
            "second", "year", "by", "the", "people", "of", "the", "several", "states", "and", "the", "electors", "in",
            "each", "state", "shall", "have", "the", "qualifications", "requisite", "for", "electors", "of", "the", "most",
            "numerous", "branch", "of", "the", "state", "legislature",
            "no", "person", "shall", "be", "a", "representative", "who", "shall", "not", "have", "attained", "to", "the",
            "age", "of", "twenty", "five", "years", "and", "been", "seven", "years", "a", "citizen", "of", "the", "united",
            "states", "and", "who", "shall", "not", "when", "elected", "be", "an", "inhabitant", "of", "that", "state",
            "in", "which", "he", "shall", "be", "chosen",
            "representatives", "and", "direct", "taxes", "shall", "be", "apportioned", "among", "the", "several", "states",
            "which", "may", "be", "included", "within", "this", "union", "according", "to", "their", "respective",
            "numbers", "which", "shall", "be", "determined", "by", "adding", "to", "the", "whole", "number", "of", "free",
            "persons", "including", "those", "bound", "to", "service", "for", "a", "term", "of", "years", "and",
            "excluding", "indians", "not", "taxed", "three", "fifths", "of", "all", "other", "persons", "the", "actual",
            "enumeration", "shall", "be", "made", "within", "three", "years", "after", "the", "first", "meeting", "of",
            "the", "congress", "of", "the", "united", "states", "and", "within", "every", "subsequent", "term", "of", "ten",
            "years", "in", "such", "manner", "as", "they", "shall", "by", "law", "direct", "the", "number", "of",
            "representatives", "shall", "not", "exceed", "one", "for", "every", "thirty", "thousand", "but", "each",
            "state", "shall", "have", "at", "least", "one", "representative", "and", "until", "such", "enumeration",
            "shall", "be", "made", "the", "state", "of", "new", "hampshire", "shall", "be", "entitled", "to", "chuse",
            "three", "massachusetts", "eight", "rhodeisland", "and", "providence", "plantations", "one", "connecticut",
            "five", "newyork", "six", "new", "jersey", "four", "pennsylvania", "eight", "delaware", "one", "maryland",
            "six", "virginia", "ten", "north", "carolina", "five", "south", "carolina", "five", "and", "georgia", "three",
            "when", "vacancies", "happen", "in", "the", "representation", "from", "any", "state", "the", "executive",
            "authority", "thereof", "shall", "issue", "writs", "of", "election", "to", "fill", "such", "vacancies",
            "the", "house", "of", "representatives", "shall", "chuse", "their", "speaker", "and", "other", "officers",
            "and", "shall", "have", "the", "sole", "power", "of", "impeachment",

            "section", "three",

            "the", "senate", "of", "the", "united", "states", "shall", "be", "composed", "of", "two", "senators", "from",
            "each", "state", "chosen", "by", "the", "legislature", "thereof", "for", "six", "years", "and", "each",
            "senator", "shall", "have", "one", "vote",
            "immediately", "after", "they", "shall", "be", "assembled", "in", "consequence", "of", "the", "first",
            "election", "they", "shall", "be", "divided", "as", "equally", "as", "may", "be", "into", "three", "classes",
            "the", "seats", "of", "the", "senators", "of", "the", "first", "class", "shall", "be", "vacated", "at", "the",
            "expiration", "of", "the", "second", "year", "of", "the", "second", "class", "at", "the", "expiration", "of",
            "the", "fourth", "year", "and", "of", "the", "third", "class", "at", "the", "expiration", "of", "the", "sixth",
            "year", "so", "that", "one", "third", "may", "be", "chosen", "every", "second", "year", "and", "if",
            "vacancies", "happen", "by", "resignation", "or", "otherwise", "during", "the", "recess", "of", "the",
            "legislature", "of", "any", "state", "the", "executive", "thereof", "may", "make", "temporary", "appointments",
            "until", "the", "next", "meeting", "of", "the", "legislature", "which", "shall", "then", "fill", "such",
            "vacancies",
            "no", "person", "shall", "be", "a", "senator", "who", "shall", "not", "have", "attained", "to", "the", "age",
            "of", "thirty", "years", "and", "been", "nine", "years", "a", "citizen", "of", "the", "united", "states", "and",
            "who", "shall", "not", "when", "elected", "be", "an", "inhabitant", "of", "that", "state", "for", "which", "he",
            "shall", "be", "chosen",
            "the", "vice", "president", "of", "the", "united", "states", "shall", "be", "president", "of", "the", "senate",
            "but", "shall", "have", "no", "vote", "unless", "they", "be", "equally", "divided",
            "the", "senate", "shall", "chuse", "their", "other", "officers", "and", "also", "a", "president", "pro",
            "tempore", "in", "the", "absence", "of", "the", "vice", "president", "or", "when", "he", "shall", "exercise",
            "the", "office", "of", "president", "of", "the", "united", "states",
            "the", "senate", "shall", "have", "the", "sole", "power", "to", "try", "all", "impeachments", "when", "sitting",
            "for", "that", "purpose", "they", "shall", "be", "on", "oath", "or", "affirmation", "when", "the", "president",
            "of", "the", "united", "states", "is", "tried", "the", "chief", "justice", "shall", "preside", "and", "no",
            "person", "shall", "be", "convicted", "without", "the", "concurrence", "of", "two", "thirds", "of", "the",
            "members", "present",
            "judgment", "in", "cases", "of", "impeachment", "shall", "not", "extend", "further", "than", "to", "removal",
            "from", "office", "and", "disqualification", "to", "hold", "and", "enjoy", "any", "office", "of", "honor",
            "trust", "or", "profit", "under", "the", "united", "states", "but", "the", "party", "convicted", "shall",
            "nevertheless", "be", "liable", "and", "subject", "to", "indictment", "trial", "judgment", "and", "punishment",
            "according", "to", "law",

            "section", "four",

            "the", "times", "places", "and", "manner", "of", "holding", "elections", "for", "senators", "and",
            "representatives", "shall", "be", "prescribed", "in", "each", "state", "by", "the", "legislature", "thereof",
            "but", "the", "congress", "may", "at", "any", "time", "by", "law", "make", "or", "alter", "such", "regulations",
            "except", "as", "to", "the", "places", "of", "chusing", "senators",
            "the", "congress", "shall", "assemble", "at", "least", "once", "in", "every", "year", "and", "such", "meeting",
            "shall", "be", "on", "the", "first", "monday", "in", "december", "unless", "they", "shall", "by", "law",
            "appoint", "a", "different", "day",

            "section", "five",

            "each", "house", "shall", "be", "the", "judge", "of", "the", "elections", "returns", "and", "qualifications",
            "of", "its", "own", "members", "and", "a", "majority", "of", "each", "shall", "constitute", "a", "quorum", "to",
            "do", "business", "but", "a", "smaller", "number", "may", "adjourn", "from", "day", "to", "day", "and", "may",
            "be", "authorized", "to", "compel", "the", "attendance", "of", "absent", "members", "in", "such", "manner",
            "and", "under", "such", "penalties", "as", "each", "house", "may", "provide",
            "each", "house", "may", "determine", "the", "rules", "of", "its", "proceedings", "punish", "its", "members",
            "for", "disorderly", "behaviour", "and", "with", "the", "concurrence", "of", "two", "thirds", "expel", "a",
            "member",
            "each", "house", "shall", "keep", "a", "journal", "of", "its", "proceedings", "and", "from", "time", "to",
            "time", "publish", "the", "same", "excepting", "such", "parts", "as", "may", "in", "their", "judgment",
            "require", "secrecy", "and", "the", "yeas", "and", "nays", "of", "the", "members", "of", "either", "house",
            "on", "any", "question", "shall", "at", "the", "desire", "of", "one", "fifth", "of", "those", "present", "be",
            "entered", "on", "the", "journal",
            "neither", "house", "during", "the", "session", "of", "congress", "shall", "without", "the", "consent", "of",
            "the", "other", "adjourn", "for", "more", "than", "three", "days", "nor", "to", "any", "other", "place", "than",
            "that", "in", "which", "the", "two", "houses", "shall", "be", "sitting",

            "section", "six",

            "the", "senators", "and", "representatives", "shall", "receive", "a", "compensation", "for", "their",
            "services", "to", "be", "ascertained", "by", "law", "and", "paid", "out", "of", "the", "treasury", "of", "the",
            "united", "states", "they", "shall", "in", "all", "cases", "except", "treason", "felony", "and", "breach", "of",
            "the", "peace", "be", "privileged", "from", "arrest", "during", "their", "attendance", "at", "the", "session",
            "of", "their", "respective", "houses", "and", "in", "going", "to", "and", "returning", "from", "the", "same",
            "and", "for", "any", "speech", "or", "debate", "in", "either", "house", "they", "shall", "not", "be",
            "questioned", "in", "any", "other", "place",
            "no", "senator", "or", "representative", "shall", "during", "the", "time", "for", "which", "he", "was",
            "elected", "be", "appointed", "to", "any", "civil", "office", "under", "the", "authority", "of", "the",
            "united", "states", "which", "shall", "have", "been", "created", "or", "the", "emoluments", "whereof", "shall",
            "have", "been", "encreased", "during", "such", "time", "and", "no", "person", "holding", "any", "office",
            "under", "the", "united", "states", "shall", "be", "a", "member", "of", "either", "house", "during", "his",
            "continuance", "in", "office",

            "section", "seven",

            "all", "bills", "for", "raising", "revenue", "shall", "originate", "in", "the", "house", "of",
            "representatives", "but", "the", "senate", "may", "propose", "or", "concur", "with", "amendments", "as", "on",
            "other", "bills",
            "every", "bill", "which", "shall", "have", "passed", "the", "house", "of", "representatives", "and", "the",
            "senate", "shall", "before", "it", "become", "a", "law", "be", "presented", "to", "the", "president", "of",
            "the", "united", "states", "if", "he", "approve", "he", "shall", "sign", "it", "but", "if", "not", "he",
            "shall", "return", "it", "with", "his", "objections", "to", "that", "house", "in", "which", "it", "shall",
            "have", "originated", "who", "shall", "enter", "the", "objections", "at", "large", "on", "their", "journal",
            "and", "proceed", "to", "reconsider", "it", "if", "after", "such", "reconsideration", "two", "thirds", "of",
            "that", "house", "shall", "agree", "to", "pass", "the", "bill", "it", "shall", "be", "sent", "together", "with",
            "the", "objections", "to", "the", "other", "house", "by", "which", "it", "shall", "likewise", "be",
            "reconsidered", "and", "if", "approved", "by", "two", "thirds", "of", "that", "house", "it", "shall", "become",
            "a", "law", "but", "in", "all", "such", "cases", "the", "votes", "of", "both", "houses", "shall", "be",
            "determined", "by", "yeas", "and", "nays", "and", "the", "names", "of", "the", "persons", "voting", "for",
            "and", "against", "the", "bill", "shall", "be", "entered", "on", "the", "journal", "of", "each", "house",
            "respectively", "if", "any", "bill", "shall", "not", "be", "returned", "by", "the", "president", "within",
            "ten", "days", "sundays", "excepted", "after", "it", "shall", "have", "been", "presented", "to", "him", "the",
            "same", "shall", "be", "a", "law", "in", "like", "manner", "as", "if", "he", "had", "signed", "it", "unless",
            "the", "congress", "by", "their", "adjournment", "prevent", "its", "return", "in", "which", "case", "it",
            "shall", "not", "be", "a", "law",
            "every", "order", "resolution", "or", "vote", "to", "which", "the", "concurrence", "of", "the", "senate", "and",
            "house", "of", "representatives", "may", "be", "necessary", "except", "on", "a", "question", "of",
            "adjournment", "shall", "be", "presented", "to", "the", "president", "of", "the", "united", "states", "and",
            "before", "the", "same", "shall", "take", "effect", "shall", "be", "approved", "by", "him", "or", "being",
            "disapproved", "by", "him", "shall", "be", "repassed", "by", "two", "thirds", "of", "the", "senate", "and",
            "house", "of", "representatives", "according", "to", "the", "rules", "and", "limitations", "prescribed", "in",
            "the", "case", "of", "a", "bill",

            "section", "eight",

            "the", "congress", "shall", "have", "power", "to", "lay", "and", "collect", "taxes", "duties", "imposts", "and",
            "excises", "to", "pay", "the", "debts", "and", "provide", "for", "the", "common", "defence", "and", "general",
            "welfare", "of", "the", "united", "states", "but", "all", "duties", "imposts", "and", "excises", "shall", "be",
            "uniform", "throughout", "the", "united", "states",
            "to", "borrow", "money", "on", "the", "credit", "of", "the", "united", "states",
            "to", "regulate", "commerce", "with", "foreign", "nations", "and", "among", "the", "several", "states", "and",
            "with", "the", "indian", "tribes",
            "to", "establish", "an", "uniform", "rule", "of", "naturalization", "and", "uniform", "laws", "on", "the",
            "subject", "of", "bankruptcies", "throughout", "the", "united", "states",
            "to", "coin", "money", "regulate", "the", "value", "thereof", "and", "of", "foreign", "coin", "and", "fix",
            "the", "standard", "of", "weights", "and", "measures",
            "to", "provide", "for", "the", "punishment", "of", "counterfeiting", "the", "securities", "and", "current",
            "coin", "of", "the", "united", "states",
            "to", "establish", "post", "offices", "and", "post", "roads",
            "to", "promote", "the", "progress", "of", "science", "and", "useful", "arts", "by", "securing", "for",
            "limited", "times", "to", "authors", "and", "inventors", "the", "exclusive", "right", "to", "their",
            "respective", "writings", "and", "discoveries",
            "to", "constitute", "tribunals", "inferior", "to", "the", "supreme", "court",
            "to", "define", "and", "punish", "piracies", "and", "felonies", "committed", "on", "the", "high", "seas", "and",
            "offences", "against", "the", "law", "of", "nations",
            "to", "declare", "war", "grant", "letters", "of", "marque", "and", "reprisal", "and", "make", "rules",
            "concerning", "captures", "on", "land", "and", "water",
            "to", "raise", "and", "support", "armies", "but", "no", "appropriation", "of", "money", "to", "that", "use",
            "shall", "be", "for", "a", "longer", "term", "than", "two", "years",
            "to", "provide", "and", "maintain", "a", "navy",
            "to", "make", "rules", "for", "the", "government", "and", "regulation", "of", "the", "land", "and", "naval",
            "forces",
            "to", "provide", "for", "calling", "forth", "the", "militia", "to", "execute", "the", "laws", "of", "the",
            "union", "suppress", "insurrections", "and", "repel", "invasions",
            "to", "provide", "for", "organizing", "arming", "and", "disciplining", "the", "militia", "and", "for",
            "governing", "such", "part", "of", "them", "as", "may", "be", "employed", "in", "the", "service", "of", "the",
            "united", "states", "reserving", "to", "the", "states", "respectively", "the", "appointment", "of", "the",
            "officers", "and", "the", "authority", "of", "training", "the", "militia", "according", "to", "the",
            "discipline", "prescribed", "by", "congress",
            "to", "exercise", "exclusive", "legislation", "in", "all", "cases", "whatsoever", "over", "such", "district",
            "not", "exceeding", "ten", "miles", "square", "as", "may", "by", "cession", "of", "particular", "states", "and",
            "the", "acceptance", "of", "congress", "become", "the", "seat", "of", "the", "government", "of", "the",
            "united", "states", "and", "to", "exercise", "like", "authority", "over", "all", "places", "purchased", "by",
            "the", "consent", "of", "the", "legislature", "of", "the", "state", "in", "which", "the", "same", "shall", "be",
            "for", "the", "erection", "of", "forts", "magazines", "arsenals", "dockyards", "and", "other", "needful",
            "buildingsand",
            "to", "make", "all", "laws", "which", "shall", "be", "necessary", "and", "proper", "for", "carrying", "into",
            "execution", "the", "foregoing", "powers", "and", "all", "other", "powers", "vested", "by", "this",
            "constitution", "in", "the", "government", "of", "the", "united", "states", "or", "in", "any", "department",
            "or", "officer", "thereof",

            "section", "nine",

            "the", "migration", "or", "importation", "of", "such", "persons", "as", "any", "of", "the", "states", "now",
            "existing", "shall", "think", "proper", "to", "admit", "shall", "not", "be", "prohibited", "by", "the",
            "congress", "prior", "to", "the", "year", "one", "thousand", "eight", "hundred", "and", "eight", "but", "a",
            "tax", "or", "duty", "may", "be", "imposed", "on", "such", "importation", "not", "exceeding", "ten", "dollars",
            "for", "each", "person",
            "the", "privilege", "of", "the", "writ", "of", "habeas", "corpus", "shall", "not", "be", "suspended", "unless",
            "when", "in", "cases", "of", "rebellion", "or", "invasion", "the", "public", "safety", "may", "require", "it",
            "no", "bill", "of", "attainder", "or", "ex", "post", "facto", "law", "shall", "be", "passed",
            "no", "capitation", "or", "other", "direct", "tax", "shall", "be", "laid", "unless", "in", "proportion", "to",
            "the", "census", "or", "enumeration", "herein", "before", "directed", "to", "be", "taken",
            "no", "tax", "or", "duty", "shall", "be", "laid", "on", "articles", "exported", "from", "any", "state",
            "no", "preference", "shall", "be", "given", "by", "any", "regulation", "of", "commerce", "or", "revenue", "to",
            "the", "ports", "of", "one", "state", "over", "those", "of", "another", "nor", "shall", "vessels", "bound",
            "to", "or", "from", "one", "state", "be", "obliged", "to", "enter", "clear", "or", "pay", "duties", "in",
            "another",
            "no", "money", "shall", "be", "drawn", "from", "the", "treasury", "but", "in", "consequence", "of",
            "appropriations", "made", "by", "law", "and", "a", "regular", "statement", "and", "account", "of", "the",
            "receipts", "and", "expenditures", "of", "all", "public", "money", "shall", "be", "published", "from", "time",
            "to", "time",
            "no", "title", "of", "nobility", "shall", "be", "granted", "by", "the", "united", "states", "and", "no",
            "person", "holding", "any", "office", "of", "profit", "or", "trust", "under", "them", "shall", "without", "the",
            "consent", "of", "the", "congress", "accept", "of", "any", "present", "emolument", "office", "or", "title",
            "of", "any", "kind", "whatever", "from", "any", "king", "prince", "or", "foreign", "state",

            "section", "ten",

            "no", "state", "shall", "enter", "into", "any", "treaty", "alliance", "or", "confederation", "grant", "letters",
            "of", "marque", "and", "reprisal", "coin", "money", "emit", "bills", "of", "credit", "make", "any", "thing",
            "but", "gold", "and", "silver", "coin", "a", "tender", "in", "payment", "of", "debts", "pass", "any", "bill",
            "of", "attainder", "ex", "post", "facto", "law", "or", "law", "impairing", "the", "obligation", "of",
            "contracts", "or", "grant", "any", "title", "of", "nobility",
            "no", "state", "shall", "without", "the", "consent", "of", "the", "congress", "lay", "any", "imposts", "or",
            "duties", "on", "imports", "or", "exports", "except", "what", "may", "be", "absolutely", "necessary", "for",
            "executing", "its", "inspection", "laws", "and", "the", "net", "produce", "of", "all", "duties", "and",
            "imposts", "laid", "by", "any", "state", "on", "imports", "or", "exports", "shall", "be", "for", "the", "use",
            "of", "the", "treasury", "of", "the", "united", "states", "and", "all", "such", "laws", "shall", "be",
            "subject", "to", "the", "revision", "and", "controul", "of", "the", "congress",
            "no", "state", "shall", "without", "the", "consent", "of", "congress", "lay", "any", "duty", "of", "tonnage",
            "keep", "troops", "or", "ships", "of", "war", "in", "time", "of", "peace", "enter", "into", "any", "agreement",
            "or", "compact", "with", "another", "state", "or", "with", "a", "foreign", "power", "or", "engage", "in", "war",
            "unless", "actually", "invaded", "or", "in", "such", "imminent", "danger", "as", "will", "not", "admit", "of",
            "delay"

        ]
        trie = CatsTrie(sentences)
        self.assertTrue(trie.autoComplete("") == "the")
        self.assertTrue(trie.autoComplete("monash") == None)  # :(
        self.assertTrue(trie.autoComplete("a") == "and")
        self.assertTrue(trie.autoComplete("al") == "all")
        self.assertTrue(trie.autoComplete("any") == "any")
        self.assertTrue(trie.autoComplete("b") == "be")
        self.assertTrue(trie.autoComplete("by") == "by")
        self.assertTrue(trie.autoComplete("c") == "congress")
        self.assertTrue(trie.autoComplete("d") == "during")
        self.assertTrue(trie.autoComplete("e") == "each")
        self.assertTrue(trie.autoComplete("f") == "for")
        self.assertTrue(trie.autoComplete("g") == "government")
        self.assertTrue(trie.autoComplete("h") == "house")
        self.assertTrue(trie.autoComplete("ha") == "have")
        self.assertTrue(trie.autoComplete("i") == "in")
        self.assertTrue(trie.autoComplete("j") == "journal")
        self.assertTrue(trie.autoComplete("k") == "keep")
        self.assertTrue(trie.autoComplete("l") == "law")
        self.assertTrue(trie.autoComplete("m") == "may")
        self.assertTrue(trie.autoComplete("n") == "no")
        self.assertTrue(trie.autoComplete("not") == "not")
        self.assertTrue(trie.autoComplete("o") == "of")
        self.assertTrue(trie.autoComplete("on") == "on")
        self.assertTrue(trie.autoComplete("or") == "or")
        self.assertTrue(trie.autoComplete("p") == "president")
        self.assertTrue(trie.autoComplete("q") == "qualifications")
        self.assertTrue(trie.autoComplete("r") == "representatives")
        self.assertTrue(trie.autoComplete("s") == "shall")
        self.assertTrue(trie.autoComplete("st") == "states")
        self.assertTrue(trie.autoComplete("su") == "such")
        self.assertTrue(trie.autoComplete("t") == "the")
        self.assertTrue(trie.autoComplete("to") == "to")
        self.assertTrue(trie.autoComplete("u") == "united")
        self.assertTrue(trie.autoComplete("v") == "vacancies")
        self.assertTrue(trie.autoComplete("w") == "which")
        self.assertTrue(trie.autoComplete("x") == None)
        self.assertTrue(trie.autoComplete("y") == "years")
        self.assertTrue(trie.autoComplete("z") == None)


    def test_09(self):
        # Extract from the FIT2004 S1 2023 A2 assignment brief, Monash University
        sentences = [

            "fit", "two", "zero", "zero", "four", "s", "one", "twenty", "twenty", "three", "assignment", "two",

            "deadline",

            "friday", "twenty", "sixth", "may", "twenty", "twenty", "three", "sixteen", "thirty", "sharp", "aedt",

            "late", "submission", "penalty",

            "ten", "percent", "penalty", "per", "day", "submissions", "more", "than", "seven", "calendar", "days", "late",
            "will", "receive", "zero", "the", "number", "of", "days", "late", "is", "rounded", "up", "eg", "five",
            "minutes", "late", "means", "one", "day", "late", "twenty", "seven", "hours", "late", "is", "two", "days",
            "late",
            "for", "special", "consideration", "please", "visit", "the", "following", "page", "and", "fill", "out", "the",
            "appropriate", "form",
            "https", "colon", "slash", "slash", "forms", "dot", "monash", "dot", "edu", "slash", "special", "hyphen",
            "consideration", "for", "clayton", "students",
            "https", "colon", "slash", "slash", "sors", "dot", "monash", "dot", "edu", "dot", "my", "slash", "for",
            "malaysian", "students",
            "the", "deadlines", "in", "this", "unit", "are", "strict", "last", "minute", "submissions", "are", "at", "your",
            "own", "risk",

            "programming", "criteria",

            "it", "is", "required", "that", "you", "implement", "this", "exercise", "strictly", "using", "the", "python",
            "programming", "language", "version", "should", "not", "be", "earlier", "than", "three", "point", "five",
            "this", "practical", "work", "will", "be", "marked", "on", "the", "time", "complexity", "space", "complexity",
            "and", "functionality", "of", "your", "program", "and", "your", "documentation",
            "your", "program", "will", "be", "tested", "using", "automated", "test", "scripts", "it", "is", "therefore",
            "critically", "important", "that", "you", "name", "your", "files", "and", "functions", "as", "specified", "in",
            "this", "document", "if", "you", "do", "not", "it", "will", "make", "your", "submission", "difficult", "to",
            "mark", "and", "you", "will", "be", "penalised",

            "submission", "requirement",

            "you", "will", "submit", "a", "single", "python", "file", "assignment", "two", "dot", "py", "moodle", "will",
            "not", "accept", "submissions", "of", "other", "file", "types",

            "plagiarism",

            "the", "assignments", "will", "be", "checked", "for", "plagiarism", "using", "an", "advanced", "plagiarism",
            "detector", "in", "previous", "semesters", "many", "students", "were", "detected", "by", "the", "plagiarism",
            "detector", "and", "almost", "all", "got", "zero", "mark", "for", "the", "assignment", "or", "even", "zero",
            "marks", "for", "the", "unit", "as", "penalty", "and", "as", "a", "result", "the", "large", "majority", "of",
            "those", "students", "failed", "the", "unit", "helping", "others", "to", "solve", "the", "assignment", "is",
            "not", "accepted", "please", "do", "not", "share", "your", "solutions", "partially", "or", "completely", "to",
            "others", "using", "contents", "from", "the", "internet", "books", "etc", "without", "citing", "is",
            "plagiarism", "if", "you", "use", "such", "content", "as", "part", "of", "your", "solution", "and", "properly",
            "cite", "it", "it", "is", "not", "plagiarism", "but", "you", "wouldnt", "be", "getting", "any", "marks", "that",
            "are", "possibly", "assigned", "for", "that", "part", "of", "the", "task", "as", "it", "is", "not", "your",
            "own", "work",

            "the", "use", "of", "generative", "ai", "and", "similar", "tools", "is", "not", "allowed", "in", "this", "unit",

            "end", "of", "page", "one",

            "learning", "outcomes",

            "this", "assignment", "achieves", "the", "learning", "outcomes", "of",
            "one", "analyse", "general", "problem", "solving", "strategies", "and", "algorithmic", "paradigms", "and",
            "apply", "them", "to", "solving", "new", "problems",
            "two", "prove", "correctness", "of", "programs", "analyse", "their", "space", "and", "time", "complexities",
            "three", "compare", "and", "contrast", "various", "abstract", "data", "types", "and", "use", "them",
            "appropriately",
            "four", "develop", "and", "implement", "algorithms", "to", "solve", "computational", "problems",

            "in", "addition", "you", "will", "develop", "the", "following", "employability", "skills",
            "text", "comprehension",
            "designing", "test", "cases",
            "ability", "to", "follow", "specifications", "precisely",

            "assignment", "timeline",

            "in", "order", "to", "be", "successful", "in", "this", "assessment", "the", "following", "steps", "are",
            "provided", "as", "a", "suggestion", "this", "is", "an", "approach", "which", "will", "be", "useful", "to",
            "you", "both", "in", "future", "units", "and", "in", "industry",

            "planning",

            "one", "read", "the", "assignment", "specification", "as", "soon", "as", "possible", "and", "write", "out", "a",
            "list", "of", "questions", "you", "have", "about", "it",
            "two", "try", "to", "resolve", "these", "questions", "by", "viewing", "the", "faq", "on", "ed", "or", "by",
            "thinking", "through", "the", "problems", "over", "time",
            "three", "as", "soon", "as", "possible", "start", "thinking", "about", "the", "problems", "in", "the",
            "assignment",
            "it", "is", "strongly", "recommended", "that", "you", "do", "not", "write", "code", "until", "you", "have", "a",
            "solid", "feeling", "for", "how", "the", "problem", "works", "and", "how", "you", "will", "solve", "it",
            "four", "writing", "down", "small", "examples", "and", "solving", "them", "by", "hand", "is", "an", "excellent",
            "tool", "for", "coming", "to", "a", "better", "understanding", "of", "the", "problem",
            "as", "you", "are", "doing", "this", "you", "will", "also", "get", "a", "feel", "for", "the", "kinds", "of",
            "edge", "cases", "your", "code", "will", "have", "to", "deal", "with",
            "five", "write", "down", "a", "highlevel", "description", "of", "the", "algorithm", "you", "will", "use",
            "six", "determine", "the", "complexity", "of", "your", "algorithm", "idea", "ensuring", "it", "meets", "the",
            "requirements",

            "end", "of", "page", "two",

            "implementing",

            "one", "think", "of", "test", "cases", "that", "you", "can", "use", "to", "check", "if", "your", "algorithm",
            "works",
            "use", "the", "edge", "cases", "you", "found", "during", "the", "previous", "phase", "to", "inspire", "your",
            "test", "cases",
            "it", "is", "also", "a", "good", "idea", "to", "generate", "large", "random", "test", "cases",
            "sharing", "test", "cases", "is", "allowed", "as", "it", "is", "not", "helping", "solve", "the", "assignment",
            "two", "code", "up", "your", "algorithm", "remember", "decomposition", "and", "comments", "and", "test", "it",
            "on", "the", "tests", "you", "have", "thought", "of",
            "three", "try", "to", "break", "your", "code", "think", "of", "what", "kinds", "of", "inputs", "you", "could",
            "be", "presented", "with", "which", "your", "code", "might", "not", "be", "able", "to", "handle",
            "large", "inputs",
            "small", "inputs",
            "inputs", "with", "strange", "properties",
            "what", "if", "everything", "is", "the", "same",
            "what", "if", "everything", "is", "different",
            "etc",

            "before", "submission",

            "make", "sure", "that", "the", "inputoutput", "format", "of", "your", "code", "matches", "the", "specification",
            "make", "sure", "your", "filenames", "match", "the", "specification",
            "make", "sure", "your", "functions", "are", "named", "correctly", "and", "take", "the", "correct", "inputs",
            "remove", "print", "statements", "and", "test", "code", "from", "the", "file", "you", "are", "going", "to",
            "submit",

            "end", "of", "page", "three",

            "documentation",

            "for", "this", "assignment", "and", "all", "assignments", "in", "this", "unit", "you", "are", "required", "to",
            "document", "and", "comment", "your", "code", "appropriately", "whilst", "part", "of", "the", "marks", "of",
            "each", "question", "are", "for", "documentation", "there", "is", "a", "baseline", "level", "of",
            "documentation", "you", "must", "have", "in", "order", "for", "your", "code", "to", "receive", "marks",
            "in", "other", "words",
            "insufficient", "documentation", "might", "result", "in", "you", "getting", "zero", "for", "the", "entire",
            "question", "for", "which", "it", "is", "insufficient",
            "this", "documentationcommenting", "must", "consist", "of", "but", "is", "not", "limited", "to",
            "for", "each", "function", "highlevel", "description", "of", "that", "function", "this", "should", "be", "a",
            "two", "or", "three", "sentence", "explanation", "of", "what", "this", "function", "does",
            "your", "main", "function", "in", "the", "assignment", "should", "contain", "a", "generalised", "description",
            "of", "the", "approach", "your", "solution", "uses", "to", "solve", "the", "assignment", "task",
            "for", "each", "function", "specify", "what", "the", "input", "to", "the", "function", "is", "and", "what",
            "output", "the", "function", "produces", "or", "returns", "if", "appropriate",
            "for", "each", "function", "the", "appropriate", "big", "oh", "or", "big", "theta", "time", "and", "space",
            "complexity", "of", "that", "function", "in", "terms", "of", "the", "input", "size", "make", "sure", "you",
            "specify", "what", "the", "variables", "involved", "in", "your", "complexity", "refer", "to", "remember",
            "that", "the", "complexity", "of", "a", "function", "includes", "the", "complexity", "of", "any", "function",
            "calls", "it", "makes",
            "within", "functions", "comments", "where", "appropriate", "generally", "speaking", "you", "would", "comment",
            "complicated", "lines", "of", "code", "which", "you", "should", "try", "to", "minimise", "or", "a", "large",
            "block", "of", "code", "which", "performs", "a", "clear", "and", "distinct", "task", "often", "blocks", "like",
            "this", "are", "good", "candidates", "to", "be",
            "their", "own", "functions",

            "a", "suggested", "function", "documentation", "layout", "would", "be", "as", "follows",

            "def", "my", "underscore", "function", "left", "bracket", "argv", "one", "comma", "argv", "two", "right",
            "bracket", "colon",
            "start", "of", "comment", "block",
            "function", "description",
            "approach", "description", "if", "main", "function",
            "input",
            "argv", "one",
            "argv", "two",
            "output", "return", "or", "postcondition",
            "time", "complexity",
            "aux", "space", "complexity",
            "end", "of", "comment", "block",
            "then", "write", "your", "codes", "here",

            "there", "is", "a", "documentation", "guide", "available", "on", "moodle", "in", "the", "assignment", "section",
            "which", "contains", "a", "demonstration", "of", "how", "to", "document", "code", "to", "the", "level",
            "required", "in", "the", "unit",

            "end", "of", "page", "four"

        ]
        trie = CatsTrie(sentences)
        self.assertTrue(trie.autoComplete("") == "the")
        self.assertTrue(trie.autoComplete("a") == "and")
        self.assertTrue(trie.autoComplete("b") == "be")
        self.assertTrue(trie.autoComplete("c") == "code")
        self.assertTrue(trie.autoComplete("d") == "documentation")
        self.assertTrue(trie.autoComplete("e") == "end")
        self.assertTrue(trie.autoComplete("f") == "for")
        self.assertTrue(trie.autoComplete("g") == "getting")
        self.assertTrue(trie.autoComplete("h") == "have")
        self.assertTrue(trie.autoComplete("i") == "is")
        self.assertTrue(trie.autoComplete("j") == None)
        self.assertTrue(trie.autoComplete("k") == "kinds")
        self.assertTrue(trie.autoComplete("l") == "late")
        self.assertTrue(trie.autoComplete("m") == "make")
        self.assertTrue(trie.autoComplete("n") == "not")
        self.assertTrue(trie.autoComplete("o") == "of")
        self.assertTrue(trie.autoComplete("p") == "plagiarism")
        self.assertTrue(trie.autoComplete("q") == "question")
        self.assertTrue(trie.autoComplete("r") == "required")
        self.assertTrue(trie.autoComplete("s") == "slash")
        self.assertTrue(trie.autoComplete("t") == "the")
        self.assertTrue(trie.autoComplete("u") == "unit")
        self.assertTrue(trie.autoComplete("v") == "variables")
        self.assertTrue(trie.autoComplete("w") == "will")
        self.assertTrue(trie.autoComplete("x") == None)
        self.assertTrue(trie.autoComplete("y") == "you")
        self.assertTrue(trie.autoComplete("z") == "zero")
        self.assertTrue(trie.autoComplete("ab") == "about")
        self.assertTrue(trie.autoComplete("ac") == "accept")
        self.assertTrue(trie.autoComplete("ad") == "addition")
        self.assertTrue(trie.autoComplete("ae") == "aedt")
        self.assertTrue(trie.autoComplete("ai") == "ai")
        self.assertTrue(trie.autoComplete("al") == "algorithm")
        self.assertTrue(trie.autoComplete("an") == "and")
        self.assertTrue(trie.autoComplete("ap") == "appropriate")
        self.assertTrue(trie.autoComplete("ar") == "are")
        self.assertTrue(trie.autoComplete("as") == "as")
        self.assertTrue(trie.autoComplete("at") == "at")
        self.assertTrue(trie.autoComplete("au") == "automated")
        self.assertTrue(trie.autoComplete("av") == "available")
        self.assertTrue(trie.autoComplete("ba") == "baseline")
        self.assertTrue(trie.autoComplete("be") == "be")
        self.assertTrue(trie.autoComplete("bi") == "big")
        self.assertTrue(trie.autoComplete("bl") == "block")
        self.assertTrue(trie.autoComplete("bo") == "books")
        self.assertTrue(trie.autoComplete("br") == "bracket")
        self.assertTrue(trie.autoComplete("bu") == "but")
        self.assertTrue(trie.autoComplete("by") == "by")
        self.assertTrue(trie.autoComplete("ca") == "cases")
        self.assertTrue(trie.autoComplete("ch") == "check")
        self.assertTrue(trie.autoComplete("ci") == "cite")
        self.assertTrue(trie.autoComplete("cl") == "clayton")
        self.assertTrue(trie.autoComplete("co") == "code")
        self.assertTrue(trie.autoComplete("cr") == "criteria")
        self.assertTrue(trie.autoComplete("da") == "days")
        self.assertTrue(trie.autoComplete("de") == "description")
        self.assertTrue(trie.autoComplete("di") == "different")
        self.assertTrue(trie.autoComplete("do") == "documentation")
        self.assertTrue(trie.autoComplete("du") == "during")
        self.assertTrue(trie.autoComplete("ea") == "each")
        self.assertTrue(trie.autoComplete("ed") == "edge")
        self.assertTrue(trie.autoComplete("eg") == "eg")
        self.assertTrue(trie.autoComplete("em") == "employability")
        self.assertTrue(trie.autoComplete("en") == "end")
        self.assertTrue(trie.autoComplete("et") == "etc")
        self.assertTrue(trie.autoComplete("ev") == "everything")
        self.assertTrue(trie.autoComplete("ex") == "examples")
        self.assertTrue(trie.autoComplete("fa") == "failed")
        self.assertTrue(trie.autoComplete("fe") == "feel")
        self.assertTrue(trie.autoComplete("fi") == "file")
        self.assertTrue(trie.autoComplete("fo") == "for")
        self.assertTrue(trie.autoComplete("fr") == "from")
        self.assertTrue(trie.autoComplete("fu") == "function")
        self.assertTrue(trie.autoComplete("ge") == "getting")
        self.assertTrue(trie.autoComplete("go") == "good")
        self.assertTrue(trie.autoComplete("gu") == "guide")
        self.assertTrue(trie.autoComplete("ha") == "have")
        self.assertTrue(trie.autoComplete("he") == "helping")
        self.assertTrue(trie.autoComplete("hi") == "highlevel")
        self.assertTrue(trie.autoComplete("ho") == "how")
        self.assertTrue(trie.autoComplete("ht") == "https")
        self.assertTrue(trie.autoComplete("hy") == "hyphen")
        self.assertTrue(trie.autoComplete("id") == "idea")
        self.assertTrue(trie.autoComplete("if") == "if")
        self.assertTrue(trie.autoComplete("im") == "implement")
        self.assertTrue(trie.autoComplete("in") == "in")
        self.assertTrue(trie.autoComplete("is") == "is")
        self.assertTrue(trie.autoComplete("it") == "it")


    def test_edgerunners_case_3(self):
        # Lyrics from I Really Want to Stay at Your House
        # Source: https://open.spotify.com/track/7mykoq6R3BArsSpNDjFQTm?si=ad96c59a91464936
        sentences = [
            'i', 'couldnt', 'wait', 'for', 'you', 'to', 'come', 'clear', 'the', 'cupboards',
            'but', 'now', 'youre', 'going', 'to', 'leave', 'with', 'nothing', 'but', 'a', 'sign',
            'another', 'evening', 'ill', 'be', 'sitting', 'reading', 'in', 'between', 'your', 'lines',
            'because', 'i', 'miss', 'you', 'all', 'the', 'time',

            'so', 'get', 'away',
            'another', 'way', 'to', 'feel', 'what', 'you', 'didnt', 'want', 'yourself', 'to', 'know',
            'and', 'let', 'yourself', 'go', 'you', 'know', 'you', 'didnt', 'lose', 'your', 'selfcontrol',
            'lets', 'start', 'at', 'the', 'rainbow',
            'turn', 'away',
            'another', 'way', 'to', 'be', 'where', 'you', 'didnt', 'want', 'yourself', 'to', 'go',
            'and', 'let', 'yourself', 'go',
            'is', 'that', 'a', 'compromise',

            'so', 'what', 'do', 'you', 'wanna', 'do', 'whats', 'your', 'pointofview',
            'theres', 'a', 'party', 'soon', 'do', 'you', 'wanna', 'go',
            'a', 'handshake', 'with', 'you', 'whats', 'your', 'pointofview',
            'im', 'on', 'top', 'of', 'you', 'i', 'dont', 'wanna', 'go',
            'cause', 'i', 'really', 'wanna', 'stay', 'at', 'your', 'house',
            'and', 'i', 'hope', 'this', 'works', 'out',
            'but', 'you', 'know', 'how', 'much', 'you', 'broke', 'me', 'apart',
            'im', 'done', 'with', 'you', 'im', 'ignoring', 'you',
            'i', 'dont', 'wanna', 'know',

            'and', 'im', 'aware', 'that', 'you', 'were', 'lying', 'in', 'the', 'gutter',
            'cause', 'i', 'did', 'everything', 'to', 'be', 'there', 'by', 'your', 'sideide',
            'so', 'when', 'you', 'tell', 'me', 'im', 'the', 'reason', 'i', 'just', 'cant', 'believe', 'the', 'lies',
            'and', 'why', 'do', 'i', 'so', 'want', 'to', 'call', 'you', 'call', 'you', 'call', 'you', 'call', 'you',

            'so', 'what', 'do', 'you', 'wanna', 'do', 'whats', 'your', 'pointofview',
            'theres', 'a', 'party', 'soon', 'do', 'you', 'wanna', 'go',
            'a', 'handshake', 'with', 'you', 'whats', 'your', 'pointofview',
            'im', 'on', 'top', 'of', 'you', 'i', 'dont', 'wanna', 'go',
            'cause', 'i', 'really', 'wanna', 'stay', 'at', 'your', 'house',
            'and', 'i', 'hope', 'this', 'works', 'out',
            'but', 'you', 'know', 'how', 'much', 'you', 'broke', 'me', 'apart',
            'im', 'done', 'with', 'you', 'im', 'ignoring', 'you',
            'i', 'dont', 'wanna', 'know',

            'oh',
            'ohoh', 'ohohoh',
            'i', 'dont', 'know', 'why', 'im', 'no', 'one',

            'so', 'get', 'away',
            'another', 'way', 'to', 'feel', 'what', 'you', 'didnt', 'want', 'yourself', 'to', 'know',
            'and', 'let', 'yourself', 'go',
            'you', 'know', 'you', 'didnt', 'lose', 'your', 'selfcontrol',
            'lets', 'start', 'at', 'the', 'rainbow',
            'turn', 'away',
            'another', 'way', 'to', 'be', 'where', 'you', 'didnt', 'want', 'yourself', 'to', 'go',
            'let', 'yourself', 'go',
            'is', 'that', 'a', 'compromise',

            'so', 'what', 'do', 'you', 'wanna', 'do', 'whats', 'your', 'pointofview',
            'theres', 'a', 'party', 'soon', 'do', 'you', 'wanna', 'go',
            'a', 'handshake', 'with', 'you', 'whats', 'your', 'pointofview',
            'im', 'on', 'top', 'of', 'you', 'i', 'dont', 'wanna', 'go',
            'cause', 'i', 'really', 'wanna', 'stay', 'at', 'your', 'house',
            'and', 'i', 'hope', 'this', 'works', 'out',
            'but', 'you', 'know', 'how', 'much', 'you', 'broke', 'me', 'apart',
            'im', 'done', 'with', 'you', 'im', 'ignoring', 'you',
            'i', 'dont', 'wanna', 'know'
        ]
        mycattrie = CatsTrie(sentences)
        self.assertEqual(mycattrie.autoComplete(""), "you")
        self.assertEqual(mycattrie.autoComplete("a"), "a")
        self.assertEqual(mycattrie.autoComplete("b"), "but")
        self.assertEqual(mycattrie.autoComplete("c"), "call")
        self.assertEqual(mycattrie.autoComplete("d"), "do")
        self.assertEqual(mycattrie.autoComplete("e"), "evening")
        self.assertEqual(mycattrie.autoComplete("f"), "feel")
        self.assertEqual(mycattrie.autoComplete("g"), "go")
        self.assertEqual(mycattrie.autoComplete("h"), "handshake")
        self.assertEqual(mycattrie.autoComplete("i"), "i")
        self.assertEqual(mycattrie.autoComplete("j"), "just")
        self.assertEqual(mycattrie.autoComplete("k"), "know")
        self.assertEqual(mycattrie.autoComplete("l"), "let")
        self.assertEqual(mycattrie.autoComplete("m"), "me")
        self.assertEqual(mycattrie.autoComplete("n"), "no")
        self.assertEqual(mycattrie.autoComplete("o"), "of")
        self.assertEqual(mycattrie.autoComplete("p"), "pointofview")
        self.assertEqual(mycattrie.autoComplete("q"), None)
        self.assertEqual(mycattrie.autoComplete("r"), "really")
        self.assertEqual(mycattrie.autoComplete("s"), "so")
        self.assertEqual(mycattrie.autoComplete("t"), "to")
        self.assertEqual(mycattrie.autoComplete("u"), None)
        self.assertEqual(mycattrie.autoComplete("v"), None)
        self.assertEqual(mycattrie.autoComplete("w"), "wanna")
        self.assertEqual(mycattrie.autoComplete("x"), None)
        self.assertEqual(mycattrie.autoComplete("y"), "you")
        self.assertEqual(mycattrie.autoComplete("z"), None)
        self.assertEqual(mycattrie.autoComplete("you"), "you")
        self.assertEqual(mycattrie.autoComplete("your"), "your")
        self.assertEqual(mycattrie.autoComplete("youre"), "youre")
        self.assertEqual(mycattrie.autoComplete("control"), None)
        self.assertEqual(mycattrie.autoComplete("view"), None)
        self.assertEqual(mycattrie.autoComplete("do"), "do")
        self.assertEqual(mycattrie.autoComplete("don"), "dont")
        self.assertEqual(mycattrie.autoComplete("ing"), None)
        self.assertEqual(mycattrie.autoComplete("on"), "on")
        self.assertEqual(mycattrie.autoComplete("one"), "one")
        self.assertEqual(mycattrie.autoComplete("oh"), "oh")
    def test_edge_case_1(self):
        sentences = [
            "fg", "fg", "fg", "fg", "fg", "fg", "abc", "abc", "abc", "abc", "abc",
            "abdc", "abdc", "abdc", "abdz", "abdz", "abdz", "abdz", "ac", "ac", "ac", "ac", "ac"
        ]
        mycattrie = CatsTrie(sentences)
        self.assertEqual(mycattrie.autoComplete(""), "fg")
        self.assertEqual(mycattrie.autoComplete("z"), None)
        self.assertEqual(mycattrie.autoComplete("a"), "abc")
        self.assertEqual(mycattrie.autoComplete("ab"), "abc")
        self.assertEqual(mycattrie.autoComplete("abd"), "abdz")
        self.assertEqual(mycattrie.autoComplete("abdd"), None)
        self.assertEqual(mycattrie.autoComplete("bdz"), None)
        self.assertEqual(mycattrie.autoComplete("dz"), None)
        self.assertEqual(mycattrie.autoComplete("bc"), None)

    def test_edge_case_2(self):
        sentences = [
            "f", "f", "f", "f", "f", "f", "abca", "abca", "abca", "abca",
            "abc", "abc", "abc", "abc", "ad", "ad", "ad", "ad", "ad"
        ]
        mycattrie = CatsTrie(sentences)
        self.assertEqual(mycattrie.autoComplete(""), "f")
        self.assertEqual(mycattrie.autoComplete("a"), "ad")
        self.assertEqual(mycattrie.autoComplete("abc"), "abc")
        self.assertEqual(mycattrie.autoComplete("abcd"), None)

    def test_definitely_random(self):
        sentences = ['according', 'to', 'all', 'known', 'laws', 'of', 'aviation', 'there', 'is', 'no', 'way', 'a',
                     'bee', 'should', 'be', 'able', 'to', 'fly', 'its', 'wings', 'are', 'too', 'small', 'to', 'get',
                     'its', 'fat', 'little', 'body', 'off', 'the', 'ground', 'the', 'bee', 'of', 'course', 'flies',
                     'anyway', 'because', 'bees', 'dont', 'care', 'what', 'humans', 'think', 'is', 'impossible',
                     'yellow', 'black', 'yellow', 'black', 'yellow', 'black', 'yellow', 'black', 'ooh', 'black', 'and',
                     'yellow', 'lets', 'shake', 'it', 'up', 'a', 'little', 'barry', 'breakfast', 'is', 'ready',
                     'coming', 'hang', 'on', 'a', 'second', 'hello', 'barry', 'adam', 'can', 'you', 'believe', 'this',
                     'is', 'happening', 'i', 'cant', 'ill', 'pick', 'you', 'up', 'looking', 'sharp', 'use', 'the',
                     'stairs', 'your', 'father', 'paid', 'good', 'money', 'for', 'those', 'sorry', 'im', 'excited',
                     'heres', 'the', 'graduate', 'were', 'very', 'proud', 'of', 'you', 'son', 'a', 'perfect', 'report',
                     'card', 'all', 'bs', 'very', 'proud', 'ma', 'i', 'got', 'a', 'thing', 'going', 'here', 'you',
                     'got', 'lint', 'on', 'your', 'fuzz', 'ow', 'thats', 'me', 'wave', 'to', 'us', 'well', 'be', 'in',
                     'row', 'bye', 'barry', 'i', 'told', 'you', 'stop', 'flying', 'in', 'the', 'house', 'hey', 'adam',
                     'hey', 'barry', 'is', 'that', 'fuzz', 'gel', 'a', 'little', 'special', 'day', 'graduation',
                     'never', 'thought', 'id', 'make', 'it', 'three', 'days', 'grade', 'school', 'three', 'days',
                     'high', 'school', 'those', 'were', 'awkward', 'three', 'days', 'college', 'im', 'glad', 'i',
                     'took', 'a', 'day', 'and', 'hitchhiked', 'around', 'the', 'hive', 'you', 'did', 'come', 'back',
                     'different', 'hi', 'barry', 'artie', 'growing', 'a', 'mustache', 'looks', 'good', 'hear', 'about',
                     'frankie', 'yeah', 'you', 'going', 'to', 'the', 'funeral', 'no', 'im', 'not', 'going', 'everybody',
                     'knows', 'sting', 'someone', 'you', 'die', 'dont', 'waste', 'it', 'on', 'a', 'squirrel', 'such',
                     'a', 'hothead', 'i', 'guess', 'he', 'could', 'have', 'just', 'gotten', 'out', 'of', 'the', 'way',
                     'i', 'love', 'this', 'incorporating', 'an', 'amusement', 'park', 'into', 'our', 'day', 'thats',
                     'why', 'we', 'dont', 'need', 'vacations', 'boy', 'quite', 'a', 'bit', 'of', 'pomp', 'under', 'the',
                     'circumstances', 'well', 'adam', 'today', 'we', 'are', 'men', 'we', 'are', 'bee', 'men', 'amen',
                     'hallelujah', 'students', 'faculty', 'distinguished', 'bees', 'please', 'welcome', 'dean',
                     'buzzwell', 'welcome', 'new', 'hive', 'city', 'graduating', 'class', 'of', 'that', 'concludes',
                     'our', 'ceremonies', 'and', 'begins', 'your', 'career', 'at', 'honex', 'industries', 'will', 'we',
                     'pick', 'our', 'job', 'today', 'i', 'heard', 'its', 'just', 'orientation', 'heads', 'up', 'here',
                     'we', 'go', 'keep', 'your', 'hands', 'and', 'antennas', 'inside', 'the', 'tram', 'at', 'all',
                     'times', 'wonder', 'what', 'itll', 'be', 'like', 'a', 'little', 'scary', 'welcome', 'to', 'honex',
                     'a', 'division', 'of', 'honesco', 'and', 'a', 'part', 'of', 'the', 'hexagon', 'group', 'this',
                     'is', 'it', 'wow', 'wow', 'we', 'know', 'that', 'you', 'as', 'a', 'bee', 'have', 'worked', 'your',
                     'whole', 'life', 'to', 'get', 'to', 'the', 'point', 'where', 'you', 'can', 'work', 'for', 'your',
                     'whole', 'life', 'honey', 'begins', 'when', 'our', 'valiant', 'pollen', 'jocks', 'bring', 'the',
                     'nectar', 'to', 'the', 'hive', 'our', 'top', 'secret', 'formula', 'is', 'automatically', 'color',
                     'corrected', 'scent', 'adjusted', 'and', 'bubble', 'contoured', 'into', 'this', 'soothing',
                     'sweet', 'syrup', 'with', 'its', 'distinctive', 'golden', 'glow', 'you', 'know', 'as', 'honey',
                     'that', 'girl', 'was', 'hot', 'shes', 'my', 'cousin', 'she', 'is', 'yes', 'were', 'all', 'cousins',
                     'right', 'youre', 'right', 'at', 'honex', 'we', 'constantly', 'strive', 'to', 'improve', 'every',
                     'aspect', 'of', 'bee', 'existence', 'these', 'bees', 'are', 'stress', 'testing', 'a', 'new',
                     'helmet', 'technology', 'what', 'do', 'you', 'think', 'he', 'makes', 'not', 'enough', 'here', 'we',
                     'have', 'our', 'latest', 'advancement', 'the', 'krelman', 'what', 'does', 'that', 'do', 'catches',
                     'that', 'little', 'strand', 'of', 'honey', 'that', 'hangs', 'after', 'you', 'pour', 'it', 'saves',
                     'us', 'millions', 'can', 'anyone', 'work', 'on', 'the', 'krelman', 'of', 'course', 'most', 'bee',
                     'jobs', 'are', 'small', 'ones', 'but', 'bees', 'know', 'that', 'every', 'small', 'job', 'if',
                     'its', 'done', 'well', 'means', 'a', 'lot', 'but', 'choose', 'carefully', 'because', 'youll',
                     'stay', 'in', 'the', 'job', 'you', 'pick', 'for', 'the', 'rest', 'of', 'your', 'life', 'the',
                     'same', 'job', 'the', 'rest', 'of', 'your', 'life', 'i', 'didnt', 'know', 'that', 'whats', 'the',
                     'difference', 'youll', 'be', 'happy', 'to', 'know', 'that', 'bees', 'as', 'a', 'species', 'havent',
                     'had', 'one', 'day', 'off', 'in', 'million', 'years', 'so', 'youll', 'just', 'work', 'us', 'to',
                     'death', 'well', 'sure', 'try', 'wow', 'that', 'blew', 'my', 'mind', 'whats', 'the', 'difference',
                     'how', 'can', 'you', 'say', 'that', 'one', 'job', 'forever', 'thats', 'an', 'insane', 'choice',
                     'to', 'have', 'to', 'make', 'im', 'relieved', 'now', 'we', 'only', 'have', 'to', 'make', 'one',
                     'decision', 'in', 'life', 'but', 'adam', 'how', 'could', 'they', 'never', 'have', 'told', 'us',
                     'that', 'why', 'would', 'you', 'question', 'anything', 'were', 'bees', 'were', 'the', 'most',
                     'perfectly', 'functioning', 'society', 'on', 'earth', 'you', 'ever', 'think', 'maybe', 'things',
                     'work', 'a', 'little', 'too', 'well', 'here', 'like', 'what', 'give', 'me', 'one', 'example', 'i',
                     'dont', 'know', 'but', 'you', 'know', 'what', 'im', 'talking', 'about', 'please', 'clear', 'the',
                     'gate', 'royal', 'nectar', 'force', 'on', 'approach', 'wait', 'a', 'second', 'check', 'it', 'out',
                     'hey', 'those', 'are', 'pollen', 'jocks', 'wow', 'ive', 'never', 'seen', 'them', 'this', 'close',
                     'they', 'know', 'what', 'its', 'like', 'outside', 'the', 'hive', 'yeah', 'but', 'some', 'dont',
                     'come', 'back', 'hey', 'jocks', 'hi', 'jocks', 'you', 'guys', 'did', 'great', 'youre', 'monsters',
                     'youre', 'sky', 'freaks', 'i', 'love', 'it', 'i', 'love', 'it', 'i', 'wonder', 'where', 'they',
                     'were', 'i', 'dont', 'know', 'their', 'days', 'not', 'planned', 'outside', 'the', 'hive', 'flying',
                     'who', 'knows', 'where', 'doing', 'who', 'knows', 'what', 'you', 'cant', 'just', 'decide', 'to',
                     'be', 'a', 'pollen', 'jock', 'you', 'have', 'to', 'be', 'bred', 'for', 'that', 'right', 'look',
                     'thats', 'more', 'pollen', 'than', 'you', 'and', 'i', 'will', 'see', 'in', 'a', 'lifetime', 'its',
                     'just', 'a', 'status', 'symbol', 'bees', 'make', 'too', 'much', 'of', 'it', 'perhaps', 'unless',
                     'youre', 'wearing', 'it', 'and', 'the', 'ladies', 'see', 'you', 'wearing', 'it', 'those', 'ladies',
                     'arent', 'they', 'our', 'cousins', 'too', 'distant', 'distant', 'look', 'at', 'these', 'two',
                     'couple', 'of', 'hive', 'harrys', 'lets', 'have', 'fun', 'with', 'them', 'it', 'must', 'be',
                     'dangerous', 'being', 'a', 'pollen', 'jock', 'yeah', 'once', 'a', 'bear', 'pinned', 'me',
                     'against', 'a', 'mushroom', 'he', 'had', 'a', 'paw', 'on', 'my', 'throat', 'and', 'with', 'the',
                     'other', 'he', 'was', 'slapping', 'me', 'oh', 'my', 'i', 'never', 'thought', 'id', 'knock', 'him',
                     'out', 'what', 'were', 'you', 'doing', 'during', 'this', 'trying', 'to', 'alert', 'the',
                     'authorities', 'i', 'can', 'autograph', 'that', 'a', 'little', 'gusty', 'out', 'there', 'today',
                     'wasnt', 'it', 'comrades', 'yeah', 'gusty', 'were', 'hitting', 'a', 'sunflower', 'patch', 'six',
                     'miles', 'from', 'here', 'tomorrow', 'six', 'miles', 'huh', 'barry', 'a', 'puddle', 'jump', 'for',
                     'us', 'but', 'maybe', 'youre', 'not', 'up', 'for', 'it', 'maybe', 'i', 'am', 'you', 'are', 'not',
                     'were', 'going', 'at', 'j', 'gate', 'what', 'do', 'you', 'think', 'buzzy', 'boy', 'are', 'you',
                     'bee', 'enough', 'i', 'might', 'be', 'it', 'all', 'depends', 'on', 'what', 'means', 'hey', 'honex',
                     'dad', 'you', 'surprised', 'me', 'you', 'decide', 'what', 'youre', 'interested', 'in', 'well',
                     'theres', 'a', 'lot', 'of', 'choices', 'but', 'you', 'only', 'get', 'one', 'do', 'you', 'ever',
                     'get', 'bored', 'doing', 'the', 'same', 'job', 'every', 'day', 'son', 'let', 'me', 'tell', 'you',
                     'about', 'stirring', 'you', 'grab', 'that', 'stick', 'and', 'you', 'just', 'move', 'it', 'around',
                     'and', 'you', 'stir', 'it', 'around', 'you', 'get', 'yourself', 'into', 'a', 'rhythm', 'its', 'a',
                     'beautiful', 'thing', 'you', 'know', 'dad', 'the', 'more', 'i', 'think', 'about', 'it', 'maybe',
                     'the', 'honey', 'field', 'just', 'isnt', 'right', 'for', 'me', 'you', 'were', 'thinking', 'of',
                     'what', 'making', 'balloon', 'animals', 'thats', 'a', 'bad', 'job', 'for', 'a', 'guy', 'with', 'a',
                     'stinger', 'janet', 'your', 'sons', 'not', 'sure', 'he', 'wants', 'to', 'go', 'into', 'honey',
                     'barry', 'you', 'are', 'so', 'funny', 'sometimes', 'im', 'not', 'trying', 'to', 'be', 'funny',
                     'youre', 'not', 'funny', 'youre', 'going', 'into', 'honey', 'our', 'son', 'the', 'stirrer',
                     'youre', 'gonna', 'be', 'a', 'stirrer', 'no', 'ones', 'listening', 'to', 'me', 'wait', 'till',
                     'you', 'see', 'the', 'sticks', 'i', 'have', 'i', 'could', 'say', 'anything', 'right', 'now', 'im',
                     'gonna', 'get', 'an', 'ant', 'tattoo', 'lets', 'open', 'some', 'honey', 'and', 'celebrate',
                     'maybe', 'ill', 'pierce', 'my', 'thorax', 'shave', 'my', 'antennae', 'shack', 'up', 'with', 'a',
                     'grasshopper', 'get', 'a', 'gold', 'tooth', 'and', 'call', 'everybody', 'dawg', 'im', 'so',
                     'proud', 'were', 'starting', 'work', 'today', 'todays', 'the', 'day', 'come', 'on', 'all', 'the',
                     'good', 'jobs', 'will', 'be', 'gone', 'yeah', 'right', 'pollen', 'counting', 'stunt', 'bee',
                     'pouring', 'stirrer', 'front', 'desk', 'hair', 'removal', 'is', 'it', 'still', 'available', 'hang',
                     'on', 'two', 'left', 'one', 'of', 'thems', 'yours', 'congratulations', 'step', 'to', 'the', 'side',
                     'whatd', 'you', 'get', 'picking', 'crud', 'out', 'stellar', 'wow', 'couple', 'of', 'newbies',
                     'yes', 'sir', 'our', 'first', 'day', 'we', 'are', 'ready', 'make', 'your', 'choice', 'you', 'want',
                     'to', 'go', 'first', 'no', 'you', 'go', 'oh', 'my', 'whats', 'available', 'restroom', 'attendants',
                     'open', 'not', 'for', 'the', 'reason', 'you', 'think', 'any', 'chance', 'of', 'getting', 'the',
                     'krelman', 'sure', 'youre', 'on', 'im', 'sorry', 'the', 'krelman', 'just', 'closed', 'out', 'wax',
                     'monkeys', 'always', 'open', 'the', 'krelman', 'opened', 'up', 'again', 'what', 'happened', 'a',
                     'bee', 'died', 'makes', 'an', 'opening', 'see', 'hes', 'dead', 'another', 'dead', 'one', 'deady',
                     'deadified', 'two', 'more', 'dead', 'dead', 'from', 'the', 'neck', 'up', 'dead', 'from', 'the',
                     'neck', 'down', 'thats', 'life', 'oh', 'this', 'is', 'so', 'hard', 'heating', 'cooling', 'stunt',
                     'bee', 'pourer', 'stirrer', 'humming', 'inspector', 'number', 'seven', 'lint', 'coordinator',
                     'stripe', 'supervisor', 'mite', 'wrangler', 'barry', 'what', 'do', 'you', 'think', 'i', 'should',
                     'barry', 'barry', 'all', 'right', 'weve', 'got', 'the', 'sunflower', 'patch', 'in', 'quadrant',
                     'nine', 'what', 'happened', 'to', 'you', 'where', 'are', 'you', 'im', 'going', 'out', 'out', 'out',
                     'where', 'out', 'there', 'oh', 'no', 'i', 'have', 'to', 'before', 'i', 'go', 'to', 'work', 'for',
                     'the', 'rest', 'of', 'my', 'life', 'youre', 'gonna', 'die', 'youre', 'crazy', 'hello', 'another',
                     'call', 'coming', 'in', 'if', 'anyones', 'feeling', 'brave', 'theres', 'a', 'korean', 'deli', 'on',
                     'rd', 'that', 'gets', 'their', 'roses', 'today', 'hey', 'guys', 'look', 'at', 'that', 'isnt',
                     'that', 'the', 'kid', 'we', 'saw', 'yesterday', 'hold', 'it', 'son', 'flight', 'decks',
                     'restricted', 'its', 'ok', 'lou', 'were', 'gonna', 'take', 'him', 'up', 'really', 'feeling',
                     'lucky', 'are', 'you', 'sign', 'here', 'here', 'just', 'initial', 'that', 'thank', 'you', 'ok',
                     'you', 'got', 'a', 'rain', 'advisory', 'today', 'and', 'as', 'you', 'all', 'know', 'bees',
                     'cannot', 'fly', 'in', 'rain', 'so', 'be', 'careful', 'as', 'always', 'watch', 'your', 'brooms',
                     'hockey', 'sticks', 'dogs', 'birds', 'bears', 'and', 'bats', 'also', 'i', 'got', 'a', 'couple',
                     'of', 'reports', 'of', 'root', 'beer', 'being', 'poured', 'on', 'us', 'murphys', 'in', 'a', 'home',
                     'because', 'of', 'it', 'babbling', 'like', 'a', 'cicada', 'thats', 'awful', 'and', 'a', 'reminder',
                     'for', 'you', 'rookies', 'bee', 'law', 'number', 'one', 'absolutely', 'no', 'talking', 'to',
                     'humans', 'all', 'right', 'launch', 'positions', 'buzz', 'buzz', 'buzz', 'buzz', 'buzz', 'buzz',
                     'buzz', 'buzz', 'buzz', 'buzz', 'buzz', 'buzz', 'black', 'and', 'yellow', 'hello', 'you', 'ready',
                     'for', 'this', 'hot', 'shot', 'yeah', 'yeah', 'bring', 'it', 'on', 'wind', 'check', 'antennae',
                     'check', 'nectar', 'pack', 'check', 'wings', 'check', 'stinger', 'check', 'scared', 'out', 'of',
                     'my', 'shorts', 'check', 'ok', 'ladies', 'lets', 'move', 'it', 'out', 'pound', 'those', 'petunias',
                     'you', 'striped', 'stem', 'suckers', 'all', 'of', 'you', 'drain', 'those', 'flowers', 'wow', 'im',
                     'out', 'i', 'cant', 'believe', 'im', 'out', 'so', 'blue', 'i', 'feel', 'so', 'fast', 'and', 'free',
                     'box', 'kite', 'wow', 'flowers', 'this', 'is', 'blue', 'leader', 'we', 'have', 'roses', 'visual',
                     'bring', 'it', 'around', 'degrees', 'and', 'hold', 'roses', 'degrees', 'roger', 'bringing', 'it',
                     'around', 'stand', 'to', 'the', 'side', 'kid', 'its', 'got', 'a', 'bit', 'of', 'a', 'kick', 'that',
                     'is', 'one', 'nectar', 'collector', 'ever', 'see', 'pollination', 'up', 'close', 'no', 'sir', 'i',
                     'pick', 'up', 'some', 'pollen', 'here', 'sprinkle', 'it', 'over', 'here', 'maybe', 'a', 'dash',
                     'over', 'there', 'a', 'pinch', 'on', 'that', 'one', 'see', 'that', 'its', 'a', 'little', 'bit',
                     'of', 'magic', 'thats', 'amazing', 'why', 'do', 'we', 'do', 'that', 'thats', 'pollen', 'power',
                     'more', 'pollen', 'more', 'flowers', 'more', 'nectar', 'more', 'honey', 'for', 'us', 'cool', 'im',
                     'picking', 'up', 'a', 'lot', 'of', 'bright', 'yellow', 'could', 'be', 'daisies', 'dont', 'we',
                     'need', 'those', 'copy', 'that', 'visual', 'wait', 'one', 'of', 'these', 'flowers', 'seems', 'to',
                     'be', 'on', 'the', 'move', 'say', 'again', 'youre', 'reporting', 'a', 'moving', 'flower',
                     'affirmative', 'that', 'was', 'on', 'the', 'line', 'this', 'is', 'the', 'coolest', 'what', 'is',
                     'it', 'i', 'dont', 'know', 'but', 'im', 'loving', 'this', 'color', 'it', 'smells', 'good', 'not',
                     'like', 'a', 'flower', 'but', 'i', 'like', 'it', 'yeah', 'fuzzy', 'chemical', 'y', 'careful',
                     'guys', 'its', 'a', 'little', 'grabby', 'my', 'sweet', 'lord', 'of', 'bees', 'candy', 'brain',
                     'get', 'off', 'there', 'problem', 'guys', 'this', 'could', 'be', 'bad', 'affirmative', 'very',
                     'close', 'gonna', 'hurt', 'mamas', 'little', 'boy', 'you', 'are', 'way', 'out', 'of', 'position',
                     'rookie', 'coming', 'in', 'at', 'you', 'like', 'a', 'missile', 'help', 'me', 'i', 'dont', 'think',
                     'these', 'are', 'flowers', 'should', 'we', 'tell', 'him', 'i', 'think', 'he', 'knows', 'what',
                     'is', 'this', 'match', 'point', 'you', 'can', 'start', 'packing', 'up', 'honey', 'because',
                     'youre', 'about', 'to', 'eat', 'it', 'yowser', 'gross', 'theres', 'a', 'bee', 'in', 'the', 'car',
                     'do', 'something', 'im', 'driving', 'hi', 'bee', 'hes', 'back', 'here', 'hes', 'going', 'to',
                     'sting', 'me', 'nobody', 'move', 'if', 'you', 'dont', 'move', 'he', 'wont', 'sting', 'you',
                     'freeze', 'he', 'blinked', 'spray', 'him', 'granny', 'what', 'are', 'you', 'doing', 'wow', 'the',
                     'tension', 'level', 'out', 'here', 'is', 'unbelievable', 'i', 'gotta', 'get', 'home', 'cant',
                     'fly', 'in', 'rain', 'cant', 'fly', 'in', 'rain', 'cant', 'fly', 'in', 'rain', 'mayday', 'mayday',
                     'bee', 'going', 'down', 'ken', 'could', 'you', 'close', 'the', 'window', 'please', 'ken', 'could',
                     'you', 'close', 'the', 'window', 'please', 'check', 'out', 'my', 'new', 'resume', 'i', 'made',
                     'it', 'into', 'a', 'fold', 'out', 'brochure', 'you', 'see', 'folds', 'out', 'oh', 'no', 'more',
                     'humans', 'i', 'dont', 'need', 'this', 'what', 'was', 'that', 'maybe', 'this', 'time', 'this',
                     'time', 'this', 'time', 'this', 'time', 'this', 'time', 'this', 'drapes', 'that', 'is',
                     'diabolical', 'its', 'fantastic', 'its', 'got', 'all', 'my', 'special', 'skills', 'even', 'my',
                     'top', 'ten', 'favorite', 'movies', 'whats', 'number', 'one', 'star', 'wars', 'nah', 'i', 'dont',
                     'go', 'for', 'that', 'kind', 'of', 'stuff', 'no', 'wonder', 'we', 'shouldnt', 'talk', 'to', 'them',
                     'theyre', 'out', 'of', 'their', 'minds', 'when', 'i', 'leave', 'a', 'job', 'interview', 'theyre',
                     'flabbergasted', 'cant', 'believe', 'what', 'i', 'say', 'theres', 'the', 'sun', 'maybe', 'thats',
                     'a', 'way', 'out', 'i', 'dont', 'remember', 'the', 'sun', 'having', 'a', 'big', 'on', 'it', 'i',
                     'predicted', 'global', 'warming', 'i', 'could', 'feel', 'it', 'getting', 'hotter', 'at', 'first',
                     'i', 'thought', 'it', 'was', 'just', 'me', 'wait', 'stop', 'bee', 'stand', 'back', 'these', 'are',
                     'winter', 'boots', 'wait', 'dont', 'kill', 'him', 'you', 'know', 'im', 'allergic', 'to', 'them',
                     'this', 'thing', 'could', 'kill', 'me', 'why', 'does', 'his', 'life', 'have', 'less', 'value',
                     'than', 'yours', 'why', 'does', 'his', 'life', 'have', 'any', 'less', 'value', 'than', 'mine',
                     'is', 'that', 'your', 'statement', 'im', 'just', 'saying', 'all', 'life', 'has', 'value', 'you',
                     'dont', 'know', 'what', 'hes', 'capable', 'of', 'feeling', 'my', 'brochure', 'there', 'you', 'go',
                     'little', 'guy', 'im', 'not', 'scared', 'of', 'himits', 'an', 'allergic', 'thing', 'put', 'that',
                     'on', 'your', 'resume', 'brochure', 'my', 'whole', 'face', 'could', 'puff', 'up', 'make', 'it',
                     'one', 'of', 'your', 'special', 'skills', 'knocking', 'someone', 'out', 'is', 'also', 'a',
                     'special', 'skill', 'right', 'bye', 'vanessa', 'thanks', 'vanessa', 'next', 'week', 'yogurt',
                     'night', 'sure', 'ken', 'you', 'know', 'whatever', 'you', 'could', 'put', 'carob', 'chips', 'on',
                     'there', 'bye', 'supposed', 'to', 'be', 'less', 'calories', 'bye', 'i', 'gotta', 'say',
                     'something', 'she', 'saved', 'my', 'life', 'i', 'gotta', 'say', 'something', 'all', 'right',
                     'here', 'it', 'goes', 'nah', 'what', 'would', 'i', 'say', 'i', 'could', 'really', 'get', 'in',
                     'trouble', 'its', 'a', 'bee', 'law', 'youre', 'not', 'supposed', 'to', 'talk', 'to', 'a', 'human',
                     'i', 'cant', 'believe', 'im', 'doing', 'this', 'ive', 'got', 'to', 'oh', 'i', 'cant', 'do', 'it',
                     'come', 'on', 'no', 'yes', 'no', 'do', 'it', 'i', 'cant', 'how', 'should', 'i', 'start', 'it',
                     'you', 'like', 'jazz', 'no', 'thats', 'no', 'good', 'here', 'she', 'comes', 'speak', 'you', 'fool',
                     'hi', 'im', 'sorry', 'youre', 'talking', 'yes', 'i', 'know', 'youre', 'talking', 'im', 'so',
                     'sorry', 'no', 'its', 'ok', 'its', 'fine', 'i', 'know', 'im', 'dreaming', 'but', 'i', 'dont',
                     'recall', 'going', 'to', 'bed', 'well', 'im', 'sure', 'this', 'is', 'very', 'disconcerting',
                     'this', 'is', 'a', 'bit', 'of', 'a', 'surprise', 'to', 'me', 'i', 'mean', 'youre', 'a', 'bee', 'i',
                     'am', 'and', 'im', 'not', 'supposed', 'to', 'be', 'doing', 'this', 'but', 'they', 'were', 'all',
                     'trying', 'to', 'kill', 'me', 'and', 'if', 'it', 'wasnt', 'for', 'you', 'i', 'had', 'to', 'thank',
                     'you', 'its', 'just', 'how', 'i', 'was', 'raised', 'that', 'was', 'a', 'little', 'weird', 'im',
                     'talking', 'with', 'a', 'bee', 'yeah', 'im', 'talking', 'to', 'a', 'bee', 'and', 'the', 'bee',
                     'is', 'talking', 'to', 'me', 'i', 'just', 'want', 'to', 'say', 'im', 'grateful', 'ill', 'leave',
                     'now', 'wait', 'how', 'did', 'you', 'learn', 'to', 'do', 'that', 'what', 'the', 'talking', 'thing',
                     'same', 'way', 'you', 'did', 'i', 'guess', 'mama', 'dada', 'honey', 'you', 'pick', 'it', 'up',
                     'thats', 'very', 'funny', 'yeah', 'bees', 'are', 'funny', 'if', 'we', 'didnt', 'laugh', 'wed',
                     'cry', 'with', 'what', 'we', 'have', 'to', 'deal', 'with', 'anyway', 'can', 'i', 'get', 'you',
                     'something', 'like', 'what', 'i', 'dont', 'know', 'i', 'mean', 'i', 'dont', 'know', 'coffee', 'i',
                     'dont', 'want', 'to', 'put', 'you', 'out', 'its', 'no', 'trouble', 'it', 'takes', 'two', 'minutes',
                     'its', 'just', 'coffee', 'i', 'hate', 'to', 'impose', 'dont', 'be', 'ridiculous', 'actually', 'i',
                     'would', 'love', 'a', 'cup', 'hey', 'you', 'want', 'rum', 'cake', 'i', 'shouldnt', 'have', 'some',
                     'no', 'i', 'cant', 'come', 'on', 'im', 'trying', 'to', 'lose', 'a', 'couple', 'micrograms',
                     'where', 'these', 'stripes', 'dont', 'help', 'you', 'look', 'great', 'i', 'dont', 'know', 'if',
                     'you', 'know', 'anything', 'about', 'fashion', 'are', 'you', 'all', 'right', 'no', 'hes', 'making',
                     'the', 'tie', 'in', 'the', 'cab', 'as', 'theyre', 'flying', 'up', 'madison', 'he', 'finally',
                     'gets', 'there', 'he', 'runs', 'up', 'the', 'steps', 'into', 'the', 'church', 'the', 'wedding',
                     'is', 'on', 'and', 'he', 'says', 'watermelon', 'i', 'thought', 'you', 'said', 'guatemalan', 'why',
                     'would', 'i', 'marry', 'a', 'watermelon', 'is', 'that', 'a', 'bee', 'joke', 'thats', 'the', 'kind',
                     'of', 'stuff', 'we', 'do', 'yeah', 'different', 'so', 'what', 'are', 'you', 'gonna', 'do', 'barry',
                     'about', 'work', 'i', 'dont', 'know', 'i', 'want', 'to', 'do', 'my', 'part', 'for', 'the', 'hive',
                     'but', 'i', 'cant', 'do', 'it', 'the', 'way', 'they', 'want', 'i', 'know', 'how', 'you', 'feel',
                     'you', 'do', 'sure', 'my', 'parents', 'wanted', 'me', 'to', 'be', 'a', 'lawyer', 'or', 'a',
                     'doctor', 'but', 'i', 'wanted', 'to', 'be', 'a', 'florist', 'really', 'my', 'only', 'interest',
                     'is', 'flowers', 'our', 'new', 'queen', 'was', 'just', 'elected', 'with', 'that', 'same',
                     'campaign', 'slogan', 'anyway', 'if', 'you', 'look', 'theres', 'my', 'hive', 'right', 'there',
                     'see', 'it', 'youre', 'in', 'sheep', 'meadow', 'yes', 'im', 'right', 'off', 'the', 'turtle',
                     'pond', 'no', 'way', 'i', 'know', 'that', 'area', 'i', 'lost', 'a', 'toe', 'ring', 'there', 'once',
                     'why', 'do', 'girls', 'put', 'rings', 'on', 'their', 'toes', 'why', 'not', 'its', 'like',
                     'putting', 'a', 'hat', 'on', 'your', 'knee', 'maybe', 'ill', 'try', 'that', 'you', 'all', 'right',
                     'maam', 'oh', 'yeah', 'fine', 'just', 'having', 'two', 'cups', 'of', 'coffee', 'anyway', 'this',
                     'has', 'been', 'great', 'thanks', 'for', 'the', 'coffee', 'yeah', 'its', 'no', 'trouble', 'sorry',
                     'i', 'couldnt', 'finish', 'it', 'if', 'i', 'did', 'id', 'be', 'up', 'the', 'rest', 'of', 'my',
                     'life', 'are', 'you', 'can', 'i', 'take', 'a', 'piece', 'of', 'this', 'with', 'me', 'sure', 'here',
                     'have', 'a', 'crumb', 'thanks', 'yeah', 'all', 'right', 'well', 'then', 'i', 'guess', 'ill', 'see',
                     'you', 'around', 'or', 'not', 'ok', 'barry', 'and', 'thank', 'you', 'so', 'much', 'again', 'for',
                     'before', 'oh', 'that', 'that', 'was', 'nothing', 'well', 'not', 'nothing', 'but', 'anyway',
                     'this', 'cant', 'possibly', 'work', 'hes', 'all', 'set', 'to', 'go', 'we', 'may', 'as', 'well',
                     'try', 'it', 'ok', 'dave', 'pull', 'the', 'chute', 'sounds', 'amazing', 'it', 'was', 'amazing',
                     'it', 'was', 'the', 'scariest', 'happiest', 'moment', 'of', 'my', 'life', 'humans', 'i', 'cant',
                     'believe', 'you', 'were', 'with', 'humans', 'giant', 'scary', 'humans', 'what', 'were', 'they',
                     'like', 'huge', 'and', 'crazy', 'they', 'talk', 'crazy', 'they', 'eat', 'crazy', 'giant', 'things',
                     'they', 'drive', 'crazy', 'do', 'they', 'try', 'and', 'kill', 'you', 'like', 'on', 'tv', 'some',
                     'of', 'them', 'but', 'some', 'of', 'them', 'dont', 'howd', 'you', 'get', 'back', 'poodle', 'you',
                     'did', 'it', 'and', 'im', 'glad', 'you', 'saw', 'whatever', 'you', 'wanted', 'to', 'see', 'you',
                     'had', 'your', 'experience', 'now', 'you', 'can', 'pick', 'out', 'yourjob', 'and', 'be', 'normal',
                     'well', 'well', 'well', 'i', 'met', 'someone', 'you', 'did', 'was', 'she', 'bee', 'ish', 'a',
                     'wasp', 'your', 'parents', 'will', 'kill', 'you', 'no', 'no', 'no', 'not', 'a', 'wasp', 'spider',
                     'im', 'not', 'attracted', 'to', 'spiders', 'i', 'know', 'its', 'the', 'hottest', 'thing', 'with',
                     'the', 'eight', 'legs', 'and', 'all', 'i', 'cant', 'get', 'by', 'that', 'face', 'so', 'who', 'is',
                     'she', 'shes', 'human', 'no', 'no', 'thats', 'a', 'bee', 'law', 'you', 'wouldnt', 'break', 'a',
                     'bee', 'law', 'her', 'names', 'vanessa', 'oh', 'boy', 'shes', 'so', 'nice', 'and', 'shes', 'a',
                     'florist', 'oh', 'no', 'youre', 'dating', 'a', 'human', 'florist', 'were', 'not', 'dating',
                     'youre', 'flying', 'outside', 'the', 'hive', 'talking', 'to', 'humans', 'that', 'attack', 'our',
                     'homes', 'with', 'power', 'washers', 'and', 'm', 's', 'one', 'eighth', 'a', 'stick', 'of',
                     'dynamite', 'she', 'saved', 'my', 'life', 'and', 'she', 'understands', 'me', 'this', 'is', 'over',
                     'eat', 'this', 'this', 'is', 'not', 'over', 'what', 'was', 'that', 'they', 'call', 'it', 'a',
                     'crumb', 'it', 'was', 'so', 'stingin', 'stripey', 'and', 'thats', 'not', 'what', 'they', 'eat',
                     'thats', 'what', 'falls', 'off', 'what', 'they', 'eat', 'you', 'know', 'what', 'a', 'cinnabon',
                     'is', 'no', 'its', 'bread', 'and', 'cinnamon', 'and', 'frosting', 'they', 'heat', 'it', 'up',
                     'sit', 'down', 'really', 'hot', 'listen', 'to', 'me', 'we', 'are', 'not', 'them', 'were', 'us',
                     'theres', 'us', 'and', 'theres', 'them', 'yes', 'but', 'who', 'can', 'deny', 'the', 'heart',
                     'that', 'is', 'yearning', 'theres', 'no', 'yearning', 'stop', 'yearning', 'listen', 'to', 'me',
                     'you', 'have', 'got', 'to', 'start', 'thinking', 'bee', 'my', 'friend', 'thinking', 'bee',
                     'thinking', 'bee', 'thinking', 'bee', 'thinking', 'bee', 'thinking', 'bee', 'thinking', 'bee',
                     'thinking', 'bee', 'there', 'he', 'is', 'hes', 'in', 'the', 'pool', 'you', 'know', 'what', 'your',
                     'problem', 'is', 'barry', 'i', 'gotta', 'start', 'thinking', 'bee', 'how', 'much', 'longer',
                     'will', 'this', 'go', 'on', 'its', 'been', 'three', 'days', 'why', 'arent', 'you', 'working',
                     'ive', 'got', 'a', 'lot', 'of', 'big', 'life', 'decisions', 'to', 'think', 'about', 'what', 'life',
                     'you', 'have', 'no', 'life', 'you', 'have', 'no', 'job', 'youre', 'barely', 'a', 'bee', 'would',
                     'it', 'kill', 'you', 'to', 'make', 'a', 'little', 'honey', 'barry', 'come', 'out', 'your',
                     'fathers', 'talking', 'to', 'you', 'martin', 'would', 'you', 'talk', 'to', 'him', 'barry', 'im',
                     'talking', 'to', 'you', 'you', 'coming', 'got', 'everything', 'all', 'set', 'go', 'ahead', 'ill',
                     'catch', 'up', 'dont', 'be', 'too', 'long', 'watch', 'this', 'vanessa', 'were', 'still', 'here',
                     'i', 'told', 'you', 'not', 'to', 'yell', 'at', 'him', 'he', 'doesnt', 'respond', 'to', 'yelling',
                     'then', 'why', 'yell', 'at', 'me', 'because', 'you', 'dont', 'listen', 'im', 'not', 'listening',
                     'to', 'this', 'sorry', 'ive', 'gotta', 'go', 'where', 'are', 'you', 'going', 'im', 'meeting', 'a',
                     'friend', 'a', 'girl', 'is', 'this', 'why', 'you', 'cant', 'decide', 'bye', 'i', 'just', 'hope',
                     'shes', 'bee', 'ish', 'they', 'have', 'a', 'huge', 'parade', 'of', 'flowers', 'every', 'year',
                     'in', 'pasadena', 'to', 'be', 'in', 'the', 'tournament', 'of', 'roses', 'thats', 'every',
                     'florists', 'dream', 'up', 'on', 'a', 'float', 'surrounded', 'by', 'flowers', 'crowds', 'cheering',
                     'a', 'tournament', 'do', 'the', 'roses', 'compete', 'in', 'athletic', 'events', 'no', 'all',
                     'right', 'ive', 'got', 'one', 'how', 'come', 'you', 'dont', 'fly', 'everywhere', 'its',
                     'exhausting', 'why', 'dont', 'you', 'run', 'everywhere', 'its', 'faster', 'yeah', 'ok', 'i', 'see',
                     'i', 'see', 'all', 'right', 'your', 'turn', 'tivo', 'you', 'can', 'just', 'freeze', 'live', 'tv',
                     'thats', 'insane', 'you', 'dont', 'have', 'that', 'we', 'have', 'hivo', 'but', 'its', 'a',
                     'disease', 'its', 'a', 'horrible', 'horrible', 'disease', 'oh', 'my', 'dumb', 'bees']

        cattrie = CatsTrie(sentences)

        self.assertEqual(cattrie.autoComplete(''), 'you')
        self.assertEqual(cattrie.autoComplete('a'), 'a')
        self.assertEqual(cattrie.autoComplete('b'), 'bee')
        self.assertEqual(cattrie.autoComplete('c'), 'cant')
        self.assertEqual(cattrie.autoComplete('d'), 'dont')
        self.assertEqual(cattrie.autoComplete('e'), 'eat')
        self.assertEqual(cattrie.autoComplete('f'), 'for')
        self.assertEqual(cattrie.autoComplete('g'), 'get')
        self.assertEqual(cattrie.autoComplete('h'), 'have')
        self.assertEqual(cattrie.autoComplete('i'), 'i')
        self.assertEqual(cattrie.autoComplete('j'), 'just')
        self.assertEqual(cattrie.autoComplete('k'), 'know')
        self.assertEqual(cattrie.autoComplete('l'), 'life')
        self.assertEqual(cattrie.autoComplete('m'), 'my')
        self.assertEqual(cattrie.autoComplete('n'), 'no')
        self.assertEqual(cattrie.autoComplete('o'), 'of')
        self.assertEqual(cattrie.autoComplete('p'), 'pollen')
        self.assertEqual(cattrie.autoComplete('q'), 'quadrant')
        self.assertEqual(cattrie.autoComplete('r'), 'right')
        self.assertEqual(cattrie.autoComplete('s'), 'so')
        self.assertEqual(cattrie.autoComplete('t'), 'the')
        self.assertEqual(cattrie.autoComplete('u'), 'up')
        self.assertEqual(cattrie.autoComplete('v'), 'very')
        self.assertEqual(cattrie.autoComplete('w'), 'what')
        self.assertEqual(cattrie.autoComplete('x'), None)
        self.assertEqual(cattrie.autoComplete('y'), 'you')
        self.assertEqual(cattrie.autoComplete('z'), None)


if __name__ == "__main__":
    unittest.main()