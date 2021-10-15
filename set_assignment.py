# #Q1. Suppose that we have performed B Cell epitopes prediction from two websites

# bcell_iedb={"ANPYFSQRMTPYVPKQKKVTKKLRTTTSKPSNKKPDSVRAIDSNATN",
#             "S","PSIPI","NEKVTKGAP","KVTKAAGAP","KVTKGAP","LSISDYFIPLEKSTLVPKK","GAPNLET",
#             "WMDPQKLAALRELVPEIPKIWADL","LSISDYFIPLEKSTLVPKK","LRTTTSKPSN"
#             }

# bcell_bepipred={"ANPYFSQRMTPYVPKQKKVTKKKKPDSVRAIDSNATN",
#             "S","PSIPI","NEKVTKGAP","KVTKGAP","LSISDYFIPLEKSTLVPKK","GAPNLET",
#             "WMDPQKLAALRELVPEIPKIWADL","LSISDYFIPLEKSTLVPKK","LRTTTSKPSN"
#             }
# #Task1
# """
# 1. Count the no of epitopes that are common in iedb and bepipred prediction.
#Answer
bcell_iedb={"ANPYFSQRMTPYVPKQKKVTKKLRTTTSKPSNKKPDSVRAIDSNATN",
            "S","PSIPI","NEKVTKGAP","KVTKAAGAP","KVTKGAP","LSISDYFIPLEKSTLVPKK","GAPNLET",
            "WMDPQKLAALRELVPEIPKIWADL","LSISDYFIPLEKSTLVPKK","LRTTTSKPSN"
            }
bcell_bepipred={"ANPYFSQRMTPYVPKQKKVTKKKKPDSVRAIDSNATN",
            "S","PSIPI","NEKVTKGAP","KVTKGAP","LSISDYFIPLEKSTLVPKK","GAPNLET",
            "WMDPQKLAALRELVPEIPKIWADL","LSISDYFIPLEKSTLVPKK","LRTTTSKPSN"
            }
common_epitope=bcell_iedb&bcell_bepipred
print("The list of common epitopes present in both sets are", common_epitope)

# 2. Count the no of epiotopes that are present in only iedb b cell prediction.
#Answer
bcell_iedb={"ANPYFSQRMTPYVPKQKKVTKKLRTTTSKPSNKKPDSVRAIDSNATN",
            "S","PSIPI","NEKVTKGAP","KVTKAAGAP","KVTKGAP","LSISDYFIPLEKSTLVPKK","GAPNLET",
            "WMDPQKLAALRELVPEIPKIWADL","LSISDYFIPLEKSTLVPKK","LRTTTSKPSN"
            }
bcell_bepipred={"ANPYFSQRMTPYVPKQKKVTKKKKPDSVRAIDSNATN",
            "S","PSIPI","NEKVTKGAP","KVTKGAP","LSISDYFIPLEKSTLVPKK","GAPNLET",
            "WMDPQKLAALRELVPEIPKIWADL","LSISDYFIPLEKSTLVPKK","LRTTTSKPSN"
            }
iedb_epitope=bcell_iedb-bcell_bepipred
print("The epitopes present only in IEDB are",iedb_epitope)

# 3. Count the no of epiotopes that are present in any of the epitopes but not in both.
#Answer
bcell_iedb={"ANPYFSQRMTPYVPKQKKVTKKLRTTTSKPSNKKPDSVRAIDSNATN",
            "S","PSIPI","NEKVTKGAP","KVTKAAGAP","KVTKGAP","LSISDYFIPLEKSTLVPKK","GAPNLET",
            "WMDPQKLAALRELVPEIPKIWADL","LSISDYFIPLEKSTLVPKK","LRTTTSKPSN"
            }
bcell_bepipred={"ANPYFSQRMTPYVPKQKKVTKKKKPDSVRAIDSNATN",
            "S","PSIPI","NEKVTKGAP","KVTKGAP","LSISDYFIPLEKSTLVPKK","GAPNLET",
            "WMDPQKLAALRELVPEIPKIWADL","LSISDYFIPLEKSTLVPKK","LRTTTSKPSN"
            }
unique_epitope_in_grp=bcell_iedb^bcell_bepipred
print("The set of epitopes present either in IEDB or bepipred is",unique_epitope_in_grp)

# 4. Find the total no of uniques epitopes.
bcell_iedb={"ANPYFSQRMTPYVPKQKKVTKKLRTTTSKPSNKKPDSVRAIDSNATN",
            "S","PSIPI","NEKVTKGAP","KVTKAAGAP","KVTKGAP","LSISDYFIPLEKSTLVPKK","GAPNLET",
            "WMDPQKLAALRELVPEIPKIWADL","LSISDYFIPLEKSTLVPKK","LRTTTSKPSN"
            }
bcell_bepipred={"ANPYFSQRMTPYVPKQKKVTKKKKPDSVRAIDSNATN",
            "S","PSIPI","NEKVTKGAP","KVTKGAP","LSISDYFIPLEKSTLVPKK","GAPNLET",
            "WMDPQKLAALRELVPEIPKIWADL","LSISDYFIPLEKSTLVPKK","LRTTTSKPSN"
            }
unique_epitope=bcell_iedb|bcell_bepipred
print("The set of unique epitopes is", unique_epitope)