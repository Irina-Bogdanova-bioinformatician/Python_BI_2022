def check_sequence(new_seq: str):
    """ The function takes a string with nucleotide sequence, checks if there is at least one unexpected character,
    or the sequence is ambiguous (U and T are both there),
    returns the answer if the sequence is correct (true or false) and problem_source if any (Mistake, Ambiguous) or ""
    if there is no problem.

    :param new_seq: string
    :return: correct (True/False), problem_source("Mistake", "Ambiguous", "")
    """
    correct, problem_source = True, ""

    for nucl in new_seq:
        if nucl not in ["A", "T", "G", "C", "a", "t", "g", "c", "U", "u", "N", "n"]:
            correct, problem_source = False, "Mistake"
            break
    if correct:
        if ("U" in new_seq or "u" in new_seq) and ("T" in new_seq or "t" in new_seq):
            correct, problem_source = False, "Ambiguous"

    return correct, problem_source


def get_sequence(new_command: str, new_seq: str, seq_type: str):
    """ Takes command and DNA or RNA sequence, returns the requested sequence in the same register.
    "transcribe" cannot be used with RNA, "reverse-transcribe" cannot be used with DNA.
    :param new_command: one of ["reverse", "complement", "reverse-complement", "transcribe", "reverse-transcribe"]
    :param new_seq: DNA or RNA sequence as a string
    :param seq_type: "DNA" or "RNA"
    :return: the requested sequence in the same register (str) or "" if incorrect command was used
    """
    complementarity_dict_dna = {"A": "T", "T": "A", "G": "C", "C": "G", "N": "N",
                                "a": "t", "t": "a", "g": "c", "c": "g", "n": "n"}

    complementarity_dict_rna = {"A": "U", "U": "A", "G": "C", "C": "G", "N": "N",
                                "a": "u", "u": "a", "g": "c", "c": "g", "n": "n"}

    transcribe_dict = {"A": "U", "T": "A", "G": "C", "C": "G", "N": "N",
                       "a": "u", "t": "a", "g": "c", "c": "g", "n": "n"}

    reverse_transcribe_dict = {"A": "T", "U": "A", "G": "C", "C": "G", "N": "N",
                               "a": "t", "u": "a", "g": "c", "c": "g", "n": "n"}
    result_seq = ""
    if new_command == "reverse":
        result_seq = new_seq[::-1]
    elif new_command == "complement" and seq_type == "DNA":
        result_seq = "".join([complementarity_dict_dna[nucl] for nucl in new_seq])
    elif new_command == "complement" and seq_type == "RNA":
        result_seq = "".join([complementarity_dict_rna[nucl] for nucl in new_seq])
    elif new_command == "reverse-complement" and seq_type == "DNA":
        result_seq = "".join([complementarity_dict_dna[nucl] for nucl in new_seq[::-1]])
    elif new_command == "reverse-complement" and seq_type == "RNA":
        result_seq = "".join([complementarity_dict_rna[nucl] for nucl in new_seq[::-1]])
    elif new_command == "transcribe" and seq_type == "DNA":
        result_seq = "".join([transcribe_dict[nucl] for nucl in new_seq[::-1]])
    elif new_command == "reverse-transcribe" and seq_type == "RNA":
        result_seq = "".join([reverse_transcribe_dict[nucl] for nucl in new_seq[::-1]])

    return result_seq


def main():
    """ The program reads commands from the user in an infinite loop. After the command, the program asks the user for
    a sequence of nucleic acid and prints the result.
    The program saves the case of characters and works only with sequences of nucleic acids.
    """
    commands = ["help", "reverse", "complement", "reverse-complement", "transcribe", "reverse-transcribe", "exit"]

    while True:
        command = input("Enter the command ('exit' if want to finish, 'help' to see all commands): ").lower()
        if command not in commands:
            print(f"The command {command} is incorrect, please try again. You can enter 'help' to get "
                  f"a complete list of possible commands")
            continue
        elif command == "help":
            print(f"A complete list of possible commands:\n{commands}")
            continue
        elif command == "exit":
            print(f"We have finished there. You are breathtaking!")
            break
        else:
            seq = input("Enter the sequence: ").strip()
            correct_seq, problem = check_sequence(seq)
            if not correct_seq and problem == "Mistake":
                print("The sequence contains unexpected characters. Please check the sequence and try again.")
                continue
            elif not correct_seq and problem == "Ambiguous":
                print("The sequence contains U and T. Please check the sequence and try again.")
                continue
            else:
                s_type = "RNA" if "U" in seq or "u" in seq else "DNA"
                if s_type == "RNA" and command == "transcribe":
                    print("RNA cannot be transcribed. Please, use one of the following commands when input RNA "
                          "sequence. Commands: reverse, complement, reverse-complement, reverse-transcribe")
                    continue
                elif s_type == "DNA" and command == "reverse-transcribe":
                    print("DNA cannot be reverse-transcribed. Please, use one of the following commands when input DNA "
                          "sequence. Commands: reverse, complement, reverse-complement, transcribe")
                    continue
                else:
                    result = get_sequence(command, seq, s_type)
                    print(result)
                    continue


if __name__ == '__main__':
    main()
