def remove_redundant_pairs(snip, candidate_pairs, *,
                           start_line_offset=0,
                           start_column_offset=0,
                           end_line_offset=0,
                           end_column_offset=0):
    all_pairs = {
        '>': '<',
        ')': '(',
        '}': '{',
        ']': '['
    }
    candidate_pairs = { k: v for k, v in all_pairs.items()
                       if v in candidate_pairs or k in candidate_pairs }
    pair_counts = { v: 0 for v in candidate_pairs.values() }

    start_line_no = snip.snippet_start[0] + start_line_offset
    start_column_no = snip.snippet_start[1] + start_column_offset
    end_line_no = snip.snippet_end[0] + end_line_offset
    end_column_no = snip.snippet_end[1] + end_column_offset
    for line_no in range(start_line_no, end_line_no + 1):
        line = snip.buffer[line_no]
        start_pos = 0
        end_pos = -1
        line_prefix = ''
        line_suffix = ''
        if line_no == start_line_no:
            line_prefix = line[:start_column_no]
            start_pos = start_column_no
        if line_no == end_line_no and len(line) > end_column_no:
            line_suffix = line[end_column_no:]
            end_pos = end_column_no
        line = line[start_pos:end_pos]

        new_line_chars = []
        for char in line:
            if char in candidate_pairs:
                if pair_counts[candidate_pairs[char]] == 0:
                    continue
                else:
                    pair_counts[candidate_pairs[char]] -= 1
            if char in candidate_pairs.values():
                pair_counts[char] += 1
            new_line_chars.append(char)
        snip.buffer[line_no] = line_prefix + ''.join(new_line_chars) + line_suffix

    snip.cursor.preserve()
