def main():
    import sys

    def parse_all(lines, case_num, index, results):
        if case_num == 0:
            return results
        if index + 1 >= len(lines):
            results.append("-1")
            return results
        try:
            x_line = lines[index].strip()
            values_line = lines[index + 1].strip()
            x = int(x_line)
            str_vals = values_line.split()
            if len(str_vals) != x:
                results.append("-1")
            else:
                def to_ints(strs, acc):
                    if not strs:
                        return acc
                    return to_ints(strs[1:], acc + [int(strs[0])])

                nums = to_ints(str_vals, [])

                def sum_power4(vals):
                    if not vals:
                        return 0
                    head, *tail = vals
                    if head <= 0:
                        return head**4 + sum_power4(tail)
                    return sum_power4(tail)

                results.append(str(sum_power4(nums)))
        except:
            results.append("-1")
        return parse_all(lines, case_num - 1, index + 2, results)

    try:
        input_lines = sys.stdin.read().splitlines()
        if not input_lines:
            return
        total_cases = int(input_lines[0])
        output = parse_all(input_lines[1:], total_cases, 0, [])
        print("\n".join(output))
    except:
        print("-1")

if __name__ == "__main__":
    main()
