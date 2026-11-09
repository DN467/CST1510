"""
RECORD CHECK  -  my version
===========================

Name  :  Daniel Negassi
Lane  :  IT
Date  :  08/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

def parse_line(raw_line):
    """Clean and parse one messy record."""

    parts = raw_line.split(":", 1)

    lane = parts[0].strip().upper()
    data = parts[1].strip()

    return {
         "lane": lane, 
         "data": data,
}


# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

raw_records = [
    "IT : srv-01 , used=87 , total=100",
    "IT : Srv-02 , used=  45 , total=  100",
    "IT : srv-03 , used=  120 , total=  100",
    "IT : Srv-04 , used=  90 , total=  100",
    "IT : srv-05 , used=  30 , total=  100"
]


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

for raw_record in raw_records:
    result = parse_line(raw_record)
    print(result)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
