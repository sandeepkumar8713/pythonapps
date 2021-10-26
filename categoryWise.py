# Question : List all category wise question

questionMap = dict()

questionMap['arrayCreation'] = {'01_array/26_min_operation_to_make_same',
                                '01_array/27_min_operation_to_make_equal',
                                '26_sixthFolder/48_min_inc_to_reach_target', }

questionMap['hashing'] = {'26_sixthFolder/46_good_split_count', }

questionMap['leftRightSum'] = {'01_array/03_find_equilibrium',
                               '01_array/10_rainwater_trapping',
                               '01_array/14_find_pivot_element', }

questionMap['LIS'] = {'01_array/04_longest_increasing_subsequnce', }

questionMap['minPlatform'] = {'01_array/06_minimum_platform', }

questionMap['quickSort'] = {'01_array/09_find_kth_small_element', }

questionMap['slidingWindow'] = {'01_array/12_chocolate_distribution',
                                '01_array/20_flip_ele_to_1',
                                '02_string/12_longest_substring_with_k_unique_char', }

questionMap['heap'] = {'01_array/16_find_kth_largest_in_stream', }

questionMap['kRemainder'] = {'01_array/29_chocolate_distribution_consecutive', }

questionMap['palindrome'] = {'02_string/03_longest_palindrome_substring',
                             '02_string/08_form_palindrome_with_min_insertion',
                             '02_string/09_form_palindrome_with_min_append',
                             '02_string/20_chunked_palindrome',
                             '02_string/25_palindrome_permutation',
                             '02_string/31_palindrome_from_2_strings',
                             '03_linkedList/29_is_plaindrome',}

questionMap['dpDfs'] = {'02_string/07_longest_common_substring', }

questionMap['bitVector'] = {'02_string/23_unique_char_without_map', }

questionMap['compressStr'] = {'02_string/26_compressed_string',
                              '02_string/33_decompress_string'}

questionMap['linkedList'] = {'03_linkedList/02_detect_and_remove_loop',
                             '03_linkedList/03_merge_two_list',
                             '03_linkedList/14_clone_double_linked',}

questionMap['reachInArray'] = {'03_linkedList/10_circular_tour', }

questionMap['bfs'] = {'03_linkedList/13_rotten_orange', }



def getSelectedFilename():
    overallSet = []
    for key, value in questionMap.items():
        overallSet.extend(list(value))
    return overallSet


if __name__ == "__main__":
    fileList = getSelectedFilename()
    for item in fileList:
        print(item)
    print(len(fileList))
