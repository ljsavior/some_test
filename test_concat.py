def concat(strs):
    n = len(strs)

    concat_info = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for common_length in range(min(len(strs[i]), len(strs[j])), 0, -1):
                if strs[i].endswith(strs[j][:common_length]):
                    concat_info[i][j] = common_length
                    break

    segments = []
    segments_idx_dict = dict()
    for i in range(n):
        if i in segments_idx_dict:
            continue
        head_segment_idx = -1
        tail_segment_idx = -1
        for j in range(n):
            if i == j:
                continue
            if j not in segments_idx_dict:
                continue
            segment = segments[segments_idx_dict[j]]
            if concat_info[i][j] > 0 and j == segment[0]:
                head_segment_idx = segments_idx_dict[j]
            if concat_info[j][i] > 0 and j == segment[-1]:
                tail_segment_idx = segments_idx_dict[j]
        if head_segment_idx == -1 and tail_segment_idx == -1:
            segments_idx_dict[i] = len(segments)
            segments.append([i])
        elif head_segment_idx == -1:
            segments[tail_segment_idx].append(i)
            segments_idx_dict[i] = tail_segment_idx
        elif tail_segment_idx == -1:
            segments[head_segment_idx].insert(0, i)
            segments_idx_dict[i] = head_segment_idx
        else:
            segments[tail_segment_idx].append(i)
            segments_idx_dict[i] = tail_segment_idx
    segments.sort(key=lambda seg: seg[0])

    final_strs = []
    pre_idx = -1
    for segment in segments:
        if len(final_strs) > 0:
            final_strs.append('\n')
        for idx in segment:
            start_idx = 0
            if pre_idx >= 0 and concat_info[pre_idx][idx] > 0:
                start_idx = concat_info[pre_idx][idx]
            s = strs[idx][start_idx:]
            final_strs.append(s)
            pre_idx = idx
    return ''.join(final_strs)


def test():
    assert 'abcde\nfghij\nklmno' == concat([
        'abcde',
        'fghij',
        'klmno'
    ])

    assert 'abcdefg\nkkkkk' == concat([
        'abcde',
        'cdefg',
        'kkkkk'
    ])

    assert 'abcde\nfghijkl' == concat([
        'abcde',
        'fghij',
        'hijkl'
    ])

    assert 'abcdefghi' == concat([
        'abcde',
        'cdefg',
        'efghi'
    ])

    assert '123abcdefg' == concat([
        'abcde',
        'cdefg',
        '123ab'
    ])

    assert 'abcdefgab' == concat([
        'abcde',
        'abcde',
        'cdefgab'
    ])

    assert 'abcdefghab' == concat([
        'abcde',
        'cdefg',
        'efghab'
    ])


if __name__ == '__main__':
    test()
