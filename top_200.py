questionMap = dict()

questionMap['Asked'] = {'01_array/16_find_kth_largest_in_stream',
                        '01_array/19_next_greater',
                        '01_array/24_most_frequent_k',
                        '02_string/06_chk_anagram',
                        '02_string/23_unique_char_without_map',
                        '02_string/35_check_if_subsequence',
                        '03_linkedList/03_merge_two_list',
                        '03_linkedList/14_clone_double_linked',
                        '03_linkedList/16_reverse_list_in_group',
                        '03_linkedList/17_point_arbitrary_to_next_higher',
                        '03_linkedList/19_merge_second_half',
                        '04_tree/01_left_view_of_tree',
                        '04_tree/08_LCA',
                        '04_tree/36_find_duplicate_subtree',
                        '04_tree_bst/02_kth_largest_element_in_bst',
                        '07_hashing/03_count_distinct_element_in_window',
                        '08_graph/03_detect_cycle',
                        '08_graph/07_find_path_exist',
                        '08_graph/13_knight_problem_min_step',
                        '10_dynamic_programming/15_count_possible_decoding',
                        '10_dynamic_programming/30_check_2_strings_are_interleaved',
                        '12_backtracking/03_count_possible_path',
                        '12_backtracking/04_print_all_possible_path',
                        '14_trie/03_print_all_anagram_together',
                        '14_trie/09_left_right_of_prefix',
                        '14_trie/11_match_all_wild_card',
                        '21_firstFolder/04_max_submatrix',
                        '21_firstFolder/06_count_island_in_matrix',
                        '21_firstFolder/50_subsequence_sum_divisible_by_n',
                        '22_secondFolder/08_find_next_bigger_number',
                        '22_secondFolder/09_celebrity_problem',
                        '22_secondFolder/25_make_most_coin_equal',
                        '23_thirdFolder/04_sorted_matrix_search',
                        '24_fourthFolder/20_text_justification',
                        '24_fourthFolder/30_first_missing_positive',
                        '25_fifthFolder/13_asteroid_collision',
                        '25_fifthFolder/33_drop_off_center',
                        '25_fifthFolder/41_farthest_node_in_set',
                        '26_sixthFolder/17_common_trigram_count',
                        '27_seventhFolder/21_multiply_num_in_str',
                        '27_seventhFolder/24_sort_colors',
                        '27_seventhFolder/26_ls_output',
                        '27_seventhFolder/31_process_scheduler',
                        '27_seventhFolder/46_coupon_hierarchy',
                        '28_eighthFolder/02_task_scheduling',
                        '28_eighthFolder/06_closest_subarray_sum',
                        '28_eighthFolder/34_delete_duplicate_freq',
                        '28_eighthFolder/35_cache_with_time_limit',
                        '28_eighthFolder/43_perfect_substring',
                        '29_ninthFolder/07_sliding_window_max',
                        '29_ninthFolder/08_suggestion_word',
                        }

questionMap['Standard'] = {'01_array/04_longest_increasing_subsequnce',
                           '01_array/29_chocolate_distribution_consecutive',
                           '02_string/04_print_all_permutation',
                           '02_string/03_longest_palindrome_substring',
                           '02_string/07_longest_common_substring',
                           '02_string/08_form_palindrome_with_min_insertion',
                           '02_string/15_kmp_algorithm',
                           '02_string/17_bucket_sort',
                           '02_string/22_represent_string_by_substring',
                           '03_linkedList/05_sum_of_two_linked_list',
                           '03_linkedList/11_merge_k_sorted_list',
                           '03_linkedList/12_first_non_repeat_char_in_stream',
                           '03_linkedList/13_rotten_orange',
                           '04_tree/03_bottom_view_binary_tree',
                           '04_tree_bst/06_largest_bst_subtree',
                           '04_tree_bst/09_inorder_next_data_in_bst',
                           '04_tree_bst/10_delete_node_in_BST',
                           '04_tree_bst/14_rank_of_player',
                           '05_heap/05_same_char_d_dist_apart',
                           '05_heap/07_connect_n_ropes',
                           '05_heap/09_kth_smallest_ele_in_matrix',
                           '07_hashing/05_longest_consecutive_subsequence',
                           '07_hashing/21_implement_version_control',
                           '08_graph/04_dijkstra',
                           '08_graph/10_ford_warshall',
                           '08_graph/11_alien_dictionary',
                           '09_greedy/09_minimum_spanning_tree',
                           '10_dynamic_programming/04_edit_distance',
                           '10_dynamic_programming/25_box_stacking',
                           '11_divide_and_conquer/07_quick_sort',
                           '14_trie/05_auto_complete',
                           '14_trie/12_word_search_2',
                           '23_thirdFolder/21_word_transform',
                           '21_firstFolder/19_find_intersection_in_linked_list',
                           '21_firstFolder/31_binary_searchable',
                           '24_fourthFolder/19_hit_counter',
                           '24_fourthFolder/48_split_array_largest_sum',
                           '25_fifthFolder/18_rearrange_pos_neg',
                           '25_fifthFolder/12_bipartite_graph',
                           '26_sixthFolder/04_guess_num_pick',
                           '27_seventhFolder/17_max_prod_array',
                           '27_seventhFolder/19_max_sub_array',
                           '27_seventhFolder/23_find_all_triplet',
                           '27_seventhFolder/34_single_number',
                           '27_seventhFolder/37_weight_job_scheduling',
                           '27_seventhFolder/38_longest_valid_parentheses',
                           '27_seventhFolder/40_square_root',
                           '27_seventhFolder/50_max_contiguous_sub_array',
                           '28_eighthFolder/14_wiggle_subsequence',
                           '29_ninthFolder/05_football_training',
                           '29_ninthFolder/11_max_len_concat',
                           '29_ninthFolder/32_rehabilitation_session'
                           }

questionMap['Important'] = {'01_array/01_find_missing_number',
                            '01_array/02_find_subarray_for_sum',
                            '01_array/06_minimum_platform',
                            '01_array/09_find_kth_small_element',
                            '01_array/10_rainwater_trapping',
                            '01_array/18_print_matrix_in_spiral',
                            '01_array/22_merge_to_make_palindrome',
                            '01_array/32_zero_matrix',
                            '02_string/11_longest_common_prefix',
                            '02_string/12_longest_substring_with_k_unique_char',
                            '02_string/33_decompress_string',
                            '03_linkedList/02_detect_and_remove_loop',
                            '04_tree/05_level_order_in_spiral_form',
                            '04_tree/11_max_path_sum_in_binary_tree',
                            '04_tree/12_diameter_of_binary_tree',
                            '04_tree/15_serialize_deserialze_a_binary_tree',
                            '04_tree/17_print_node_at_dist_k_from_a_node',
                            '04_tree/22_tree_equal_to_subtree',
                            '04_tree/28_isomorphic_tree',
                            '04_tree/29_convert_postorder_inorder_to_tree',
                            '04_tree_bst/01_check_BST',
                            '04_tree_bst/03_kth_smallest_element_in_bst',
                            '05_heap/01_median_in_stream',
                            '07_hashing/04_array_pair_sum_divisibility',
                            '08_graph/08_min_cost_path_in_matrix',
                            '08_graph/09_circle_of_string',
                            '09_greedy/02_make_change_with_min_coin',
                            '09_greedy/04_page_fault_in_LRU',
                            '09_greedy/08_max_len_chain',
                            '10_dynamic_programming/02_knapsack',
                            '10_dynamic_programming/03_minimum_jump',
                            '10_dynamic_programming/05_all_possible_coin_change',
                            '10_dynamic_programming/09_minimum_sum_partition',
                            '10_dynamic_programming/10_count_ways_to_cover_distance',
                            '10_dynamic_programming/17_gold_mine',
                            '10_dynamic_programming/33_longest_consecutive_path_in_matrix',
                            '10_dynamic_programming/34_assembly_line',
                            '11_divide_and_conquer/04_median_of_two_sorted_array',
                            '12_backtracking/05_generate_valid_ip',
                            '21_firstFolder/15_rotate_matrix_by_90',
                            '21_firstFolder/21_max_steal_house',
                            '21_firstFolder/23_find_x_in_sorted_rotated_array',
                            '21_firstFolder/25_next_bigger_palindrome',
                            '21_firstFolder/29_couple_holding_hands',
                            '21_firstFolder/30_redundant_connection',
                            '21_firstFolder/44_find_safe_states',
                            '21_firstFolder/47_shortest_alternalte_path',
                            '22_secondFolder/35_word_break',
                            '22_secondFolder/43_buy_sell_stock_2_at_max',
                            '23_thirdFolder/15_baby_names',
                            '23_thirdFolder/26_confusing_number',
                            '23_thirdFolder/28_longest_arithmetic_progression',
                            '23_thirdFolder/47_my_calendar_3',
                            '24_fourthFolder/06_sensor_in_room',
                            '24_fourthFolder/07_max_distance_on_bench',
                            '24_fourthFolder/11_merge_overlapping_intervals',
                            '24_fourthFolder/14_find_min_in_rotated',
                            '24_fourthFolder/28_candy_distribution',
                            '24_fourthFolder/32_minimum_refueling',
                            '25_fifthFolder/39_clone_graph',
                            '25_fifthFolder/46_burst_ballons',
                            '26_sixthFolder/10_pacific_water_flow',
                            '26_sixthFolder/13_sliding_window_median',
                            '26_sixthFolder/32_bus_routes',
                            '26_sixthFolder/40_koko_banana',
                            '26_sixthFolder/41_longest_string_chain',
                            '26_sixthFolder/49_combination_sum',
                            '27_seventhFolder/02_swim_in_rising_water',
                            '27_seventhFolder/25_partition_equal_sum',
                            '27_seventhFolder/32_max_bomb_detonate',
                            '27_seventhFolder/35_maximum_path_sum',
                            '27_seventhFolder/36_province_count',
                            '27_seventhFolder/42_check_rotated_matrix',
                            '28_eighthFolder/19_match_stick_to_square',
                            '28_eighthFolder/22_longest_palindromic_subsequence',
                            }

questionMap['Noted'] = {'01_array/20_flip_ele_to_1',
                        '02_string/05_remove_adjacent_char',
                        '02_string/10_longest_non_repeating_substring',
                        '03_linkedList/04_flatting_a_linked_list',
                        '06_recursion/04_special_keyboard',
                        '07_hashing/18_find_recurring_fraction',
                        '10_dynamic_programming/21_wildcard_pattern_matching',
                        '21_firstFolder/05_find_dist_in_matrix',
                        '21_firstFolder/22_array_wave_form',
                        '21_firstFolder/43_knight_dialer',
                        '22_secondFolder/13_insert_in_constant',
                        '23_thirdFolder/34_articulation_point',
                        '24_fourthFolder/13_simplify_debts',
                        '24_fourthFolder/29_k_inverse_pairs_array',
                        '24_fourthFolder/49_shortest_path_break_wall',
                        '24_fourthFolder/50_escape_large_maze',
                        '25_fifthFolder/21_optimal_pair_sum',
                        '25_fifthFolder/40_word_break_2',
                        '26_sixthFolder/11_one_and_zero_subset',
                        '26_sixthFolder/19_beautiful_arrangement',
                        '26_sixthFolder/21_reconstruct_itinerary',
                        '26_sixthFolder/22_shopping_offers',
                        '26_sixthFolder/28_max_chunks_to_make_sorted',
                        '26_sixthFolder/34_push_dominoes',
                        '26_sixthFolder/45_stone_game_3',
                        '27_seventhFolder/07_shortest_path_visiting_node',
                        '27_seventhFolder/09_min_subsequence_in_big_str',
                        '28_eighthFolder/07_scramble_string',
                        '28_eighthFolder/08_unique_bst',
                        '28_eighthFolder/11_flip_game',
                        '28_eighthFolder/16_arithmetic_slice_2',
                        '28_eighthFolder/18_concatenated_string',
                        '28_eighthFolder/46_water_flower',
                        '28_eighthFolder/49_median_of_top_k',
                        }

questionMap['outerCheck1'] = {'01_array/26_min_operation_to_make_same',
                              '01_array/27_min_operation_to_make_equal',
                              '02_string/27_substring_rotation',
                              '02_string/30_find_extra_character',
                              '03_linkedList/09_find_min_element_from_stack',
                              '03_linkedList/24_find_sum_pair',
                              '03_linkedList/28_partition_into_three',
                              '03_linkedList/29_is_palindrome',
                              '04_tree/02_diagonal_traversal',
                              '04_tree/23_max_level_sum',
                              '04_tree/25_boundary_traversal',
                              '04_tree/32_print_kth_sum_path',
                              '04_tree_bst/07_find_sum_pair_in_bst',
                              '04_tree_bst/11_correct_swapped_bst',
                              '04_tree_bst/13_rank_from_stream',
                              '05_heap/04_non_adjacent_character',
                              '05_heap/06_find_smallest_range',
                              '06_recursion/03_combination_sum',
                              '06_recursion/07_magic_index',
                              '06_recursion/09_parentheses_combination',
                              '07_hashing/02_pair_to_swap_from_2_array',
                              '07_hashing/07_find_all_pair_for_sum',
                              '07_hashing/17_sort_linked_list_as_array',
                              '07_hashing/20_cellphone_numpad',
                              '07_hashing/22_find_4_eles_for_given_sum',
                              '08_graph/05_min_swap',
                              '08_graph/15_stepping_numbers',
                              '08_graph/17_overall_array',
                              '09_greedy/05_largest_number_possible',
                              '09_greedy/06_min_diff_in_height',
                              '10_dynamic_programming/12_optimal_game_strategy',
                              '12_backtracking/02_solve_sudoku',
                              '21_firstFolder/16_print_all_root_to_leaf',
                              }

if __name__ == "__main__":
    question_count = 0
    for qType, set_items in questionMap.items():
        # for item in (sorted(set_items)):
        #     print("'" + item + "',")

        print(qType, len(set_items))
        question_count += len(set_items)
    print('Total', question_count)
