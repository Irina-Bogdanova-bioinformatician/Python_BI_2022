def length_filter(seq: str, length_bounds: list or int) -> bool:
    """Answering the question if the sequence (str) passes the length filter.
    :param seq: a string
    :param length_bounds: the length interval for filtering, by default (0, 2**32), including bounds.
    If one value is indicating - this is the upper bound.
    :return: boolean value indicating if the filter is passed
    """
    seq_length = len(seq)
    if len(length_bounds) == 1:
        if seq_length <= int(length_bounds):
            return True
        else:
            return False
    elif len(length_bounds) == 2:
        if int(length_bounds[0]) <= seq_length <= int(length_bounds[1]):
            return True
        else:
            return False


def quality_filter(quality_str: str, quality_threshold: int) -> bool:
    """ Answering the question if nucleotide sequence passes the quality filter. The filter is not passed if
    average quality for all nucleotides is below the threshold.
    :param quality_str: quality line from fastq file
    :param quality_threshold: the threshold value of the average read quality (phred33 scale), 0 by default
    :return: boolean value indicating if the filter is passed
    """
    mean_quality = sum([ord(el) - 33 for el in quality_str]) / len(quality_str)
    if mean_quality >= quality_threshold:
        return True
    else:
        return False


def gc_filter(seq: str, gc_bounds: list or int) -> bool:
    """ Answering to the Ultimate Question of Life, the Universe, and Everything...
    Just joking:) I'm not the Deep Thought, but only a small function that answers the question if nucleotide sequence
    passes the GC content filter.
    :param seq: nucleotide sequence
    :param gc_bounds: the GC interval (in percent) for filtering (by default is (0, 100), including bounds
    :return: boolean value indicating if the filter is passed
    """
    gc_content = (seq.upper().count("G") + seq.upper().count("C")) * 100 / len(seq)
    if len(gc_bounds) == 1:
        if gc_content <= int(gc_bounds):
            return True
        else:
            return False
    elif len(gc_bounds) == 2:
        if int(gc_bounds[0]) <= gc_content <= int(gc_bounds[1]):
            return True
        else:
            return False


def main(input_fastq: str, output_file_prefix: str, gc_bounds=(0, 100), length_bounds=(0, 2**32), quality_threshold=0,
         save_filtered=False):
    """ Carrying out reads filtering in fastq file, saving passed reads to "{prefix}+_passed.fastq" and filtered to
        "{prefix}+_filtered.fastq" (only if the save_filtered argument is True).

    :param input_fastq: fastq file (not compressed)
    :param output_file_prefix: the prefix of the path to the file to which the result will be written.
    :param gc_bounds: the GC interval (in percent) for filtering (by default is (0, 100), including bounds
    :param length_bounds: the length interval for filtering, by default (0, 2**32), including bounds.
    If one value is indicating - this is the upper bound.
    :param quality_threshold: the threshold value of the average read quality (phred33 scale), 0 by default
    :param save_filtered: whether to save the filtered rows, False by default
    """

    out_file_passed = output_file_prefix + "_passed.fastq"
    functions_lst = [gc_filter, quality_filter, length_filter]
    thresholds_lst = [gc_bounds, quality_threshold, length_bounds]

    filtered_reads = []

    with open(input_fastq) as input_file, open(out_file_passed, "w") as out_passed:
        line_number = 0

        for line in input_file:
            if line:
                if line_number % 4 == 0:
                    read_id = line.strip()
                    line_number += 1
                    continue
                elif (line_number - 1) % 4 == 0:
                    seq = line.strip()
                    line_number += 1
                    continue
                elif (line_number - 2) % 4 == 0:
                    separator = line.strip()
                    line_number += 1
                    continue
                elif (line_number - 3) % 4 == 0:
                    quality_line = line.strip()
                    line_number += 1

                    lines_for_func = [seq, quality_line, seq]

                    for func, input_line, threshold in zip(functions_lst, lines_for_func, thresholds_lst):
                        passed = func(input_line, threshold)  # False/True
                        if not passed:
                            if save_filtered:
                                filtered_reads.append([read_id, seq, separator, quality_line])
                            break
                    if passed:
                        out_passed.write(read_id + "\n")
                        out_passed.write(seq + "\n")
                        out_passed.write(separator + "\n")
                        out_passed.write(quality_line + "\n")

        if filtered_reads and save_filtered:
            out_file_filtered = output_file_prefix + "_filtered.fastq"
            with open(out_file_filtered, "w") as out_filtered:
                for read_info in filtered_reads:
                    for line in read_info:
                        out_filtered.write(line + "\n")
