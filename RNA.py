rna_encoding = {
    "A":"U",
    "C":"G",
    "G":"C",
    "T":"A"
}
rna_decoding = {
    "U":"A",
    "G":"C",
    "C":"G",
    "A":"T"
}
selection = ["U","A","T","G","C"]
rna = ""
dna = ""
while 1:
    print("(1)Encode RNA")
    print("(2)Decode RNA")
    print("(3)Amino acid encoder")
    z = input(":")
    if z == "1":
        z = input(":")
        for char in z:
            if char in selection:
                rna += rna_encoding[char]
            else:
                rna += char
        print("\n",rna)
    elif z == "2":
        z = input(":")
        for char in z:
            if char in selection:
                dna += rna_decoding[char]
            else:
                dna += char
        print("\n",dna)
    elif z == "3":
        print("(1)Use lastest encoded rna")
        print("(2)Enter in rna")
        z = input("\n\n:")

        amino_encoding = {
            "U":{"U":{"U":{"Phe"},
                    "C":{"Phe"},
                    "A":{"Leu"},
                    "G":{"Leu"}
                    },
                "C":{
                    "U":{"Ser"},
                    "C":{"Ser"},
                    "A":{"Ser"},
                    "G":{"Ser"} 
                },
                "A":{
                    "U":{"Tyr"},
                    "C":{"Tyr"},
                    "A":{"Stop"},
                    "G":{"Stop"}
                },
                "G":{
                    "U":{"Cys"},
                    "C":{"Cys"},
                    "A":{"Stop"},
                    "G":{"Trp"}
                }
                },
            "C":{"U":{
                    "U":{"Leu"},
                    "C":{"Leu"},
                    "A":{"Leu"},
                    "G":{"Leu"}
                    },
                "C":{
                    "U":{"Pro"},
                    "C":{"Pro"},
                    "A":{"Pro"},
                    "G":{"Pro"}
                    },
                "A":{
                    "U":{"His"},
                    "C":{"His"},
                    "A":{"Gln"},
                    "G":{"Gln"}
                    },
                "G":{
                    "U":{"Arg"},
                    "C":{"Arg"},
                    "A":{"Arg"},
                    "G":{"Arg"}
                    }
                },
            "A":{"U":{
                    "U":{"lle"},
                    "C":{"lle"},
                    "A":{"lle"},
                    "G":{"Met"}
                    },
                "C":{
                    "U":{"Thr"},
                    "C":{"Thr"},
                    "A":{"Thr"},
                    "G":{"Thr"}
                    },
                "A":{
                    "U":{"Asn"},
                    "C":{"Asn"},
                    "A":{"Lys"},
                    "G":{"Lys"}
                    },
                "G":{
                    "U":{"Ser"},
                    "C":{"Ser"},
                    "A":{"Arg"},
                    "G":{"Arg"}
                    }
                },
            "G":{"U":{
                    "U":{"Val"},
                    "C":{"Val"},
                    "A":{"Val"},
                    "G":{"Val"}
                    },
                "C":{
                    "U":{"Ala"},
                    "C":{"Ala"},
                    "A":{"Ala"},
                    "G":{"Ala"}
                    },
                "A":{
                    "U":{"Asp"},
                    "C":{"Asp"},
                    "A":{"Glu"},
                    "G":{"Glu"}
                    },
                "G":{
                    "U":{"Gly"},
                    "C":{"Gly"},
                    "A":{"Gly"},
                    "G":{"Gly"}
                    }
                }
            }
        if z == "1":
            if rna == "":
                print("Encoded rna not found")
            else:
                counter = 0
                eye = ""
                all_aminods_found = []
                for char in rna:
                    if char in selection:
                        counter += 1
                        eye += char
                        if counter == 3:
                            all_aminods_found.append(amino_encoding[eye[0]][eye[1]][eye[2]])
                    else:
                        eye = ""
                        counter = 0
                print(all_aminods_found)
        else:
            rna = input("\n\n:")
            counter = 0
            eye = ""
            all_aminods_found = []
            for char in rna:
                if char in selection:
                    counter += 1
                    eye += char
                    if counter == 3:
                        all_aminods_found.append(amino_encoding[eye[0]][eye[1]][eye[2]])
                else:
                    eye = ""
                    counter = 0
            print(all_aminods_found)
    input(".")
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")