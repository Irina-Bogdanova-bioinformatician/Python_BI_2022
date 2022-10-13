# fastq_filtrator.py

Filtering of reads in fastq by GC composition, quality, length, saving results to files.

**main()**
Carrying out reads filtering in fastq file, saving passed reads to {prefix}_passed.fastq and filtered to
{prefix}_filtered.fastq (only if the save_filtered argument is true).
Input:
- input_fastq: fastq file (not compressed);
- output_file_prefix: the prefix of the path to the file to which the result will be written;
- gc_bounds: the gc interval (in percent) for filtering (by default is (0, 100), including bounds;
- length_bounds: the length interval for filtering, by default (0, 2^32), including bounds. If one value is indicating - this is the upper bound;
- quality_threshold: the threshold value of the average read quality (phred33 scale), 0 by default;
- save_filtered: whether to save the filtered rows, false by default.

**length_filter()**
 Answering the question whether the sequence (str) passes the length filter.
 Input:
- seq: a string;
- length_bounds: the length interval for filtering, by default (0, 2^32), including bounds. If one value is indicating - this is the upper bound

Output:
- boolean value indicating if the filter is passed (False/True)

**quality_filter()**
 Answering the question whether nucleotide sequence passes the quality filter. The filter is not passed if average quality for all nucleotides is below the threshold.
 Input:
- quality_str: quality line from fastq file;
- quality_threshold: the threshold value of the average read quality (phred33 scale), 0 by default.

Output:
- boolean value indicating if the filter is passed (False/True)
 
**gc_filter()**
 Answering the question whether nucleotide sequence passes the GC content filter.
 Input:
 - seq: nucleotide sequence;
 - gc_bounds: the GC interval (in percent) for filtering (by default is (0, 100), including bounds.

Output:
 - boolean value indicating if the filter is passed

**Requirements**:
python>=3.6
