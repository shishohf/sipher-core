import re

rules = {
    "Password": re.compile(r"\s*pass(word|phrase|wd|code)*\s*(:|=|is|was)\s*[a-z0-9\-_\!]+"),
    "AWS_Credentials": re.compile(r"(access_key_id|secret_access_key)"),
    "Combos": re.compile(r"^[a-z0-9\-\._]+@[a-z0-9\-\.]+\.[a-z]{2,4}[ \t;,:\|]+\S+"),
    "Proxies": re.compile(r"^[0-9]\d{1,3}(\.\d{1,3}){3}:\d{1,5}"),
    "DB_Dumps": re.compile(r"^[- ]{3}(php[mM]y[aA]dmin [sS][qQ][lL] [d,D]ump)"),
    "IPTV": re.compile(r"^#EXT[M,I]"),
    "HelloWorld": re.compile(r"^word+"),
    "MySQL_Connect": re.compile(r"mysql_[p]*connect\([\"']{0,1}[a-z0-9\-\.\$]+[\"']{0,1}\s*,"),
    "Hidden_Shells": re.compile(r"\\x[0-9a-f]{2}\\x[0-9a-f]{2}\\x[0-9a-f]{2}\\x["
                                r"0-9a-f]{2}\\x[0-9a-f]{2}\\x[0-9a-f]{2}\\x[0-9a-f]{"
                                r"2}\\x[0-9a-f]{2}\\x[0-9a-f]{2}\\x[0-9a-f]{2}"),
}

def process_rules(data):
    for rule, logic in rules.items():
        if logic.search(data):
            return rule
    return False