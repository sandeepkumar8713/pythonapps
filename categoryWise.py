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
                                '02_string/12_longest_substring_with_k_unique_char',
                                '07_hashing/13_find_smallest_window'}

questionMap['heap'] = {'01_array/16_find_kth_largest_in_stream',
                       '05_heap/08_compute_mean_of_window',
                       '05_heap/09_kth_smallest_ele_in_marix'}

questionMap['kRemainder'] = {'01_array/29_chocolate_distribution_consecutive',
                             '07_hashing/01_find_largest_sub_array_with_sum_0',
                             '07_hashing/04_array_pair_sum_divisibility',
                             '07_hashing/09_find_all_subarray_with_sum_zero'}

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

questionMap['bfs'] = {'03_linkedList/13_rotten_orange',
                      '08_graph/12_snake_and_ladder',
                      '08_graph/13_knight_problem_min_step'}

questionMap['dfs'] = {'08_graph/03_detect_cycle',
                      '08_graph/11_alien_dictionary',
                      '08_graph/17_overall_array'}

questionMap['pathInMatrix'] = {'06_recursion/02_possible_path_in_matrix',
                               '08_graph/07_find_path_exist',
                               '08_graph/08_min_cost_path_in_matrix'}

questionMap['shortestDist'] = {'08_graph/04_dijkstra',
                               '08_graph/10_ford_warshall'}

questionMap['ssc'] = {'08_graph/06_strongly_connect_component',
                      '08_graph/09_circle_of_string'}

questionMap['verticalDist'] = {'04_tree/02_diagonal_traversal',}

questionMap['HorizontalDist'] = {'04_tree/03_bottom_view_binary_tree',
                                 '04_tree/04_vertical_view_binary_tree',
                                 '04_tree/19_top_view_of_binary_tree'}

questionMap['lca'] = {'04_tree/08_LCA',
                      '04_tree/20_distance_btw_2_nodes'}

questionMap['maxPath'] = {'04_tree/11_max_path_sum_in_binary_tree',
                          '04_tree/12_diameter_of_binary_tree',
                          '04_tree/35_longest_path_of_same_value'}

questionMap['leftCount'] = {'04_tree_bst/03_kth_smallest_element_in_bst',
                            '04_tree_bst/14_rank_of_player'}

questionMap['binarySearch'] = {'04_tree_bst/08_sorted_array_to_bst',
                               '06_recursion/07_magic_index'}

questionMap['nxtInorderNode'] = {'04_tree_bst/09_inorder_next_data_in_bst',
                                 '04_tree_bst/10_delete_node_in_BST'}

questionMap['heap'] = {'05_heap/01_median_in_stream',
                       '05_heap/04_non_adjacent_character',
                       '05_heap/05_same_char_d_dist_apart'}




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
