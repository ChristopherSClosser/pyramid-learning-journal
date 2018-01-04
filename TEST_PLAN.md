Test plans for pyramid_learning_journal.

Setup for tests with conftest.py
  - setup app
  - fixtures
    - TestApp
    - fill_my_database
    - fill_my_other_database
    - dummy_request

Tests
  - test_post_entry_status_302
  - test_update_entry_status_302
  - test_home_view_status_200
  - test_list_view_returns_dict
  - test_home_route_contains_heading
  - test_home_route_contains_entries
  - test_new_entry_view_status_200
  - test_new_entry_route_contains_heading
  - test_entry_detail_view_status_200
  - test_entry_detail_view_single_entry
  - test_entry_detail_view_has_proper_entry
  - test_edit_entry_view_status_200
  - test_edit_entry_route_contains_heading
  - test_home_route_get_no_entries_has_no_sections
  - test_home_route_has_sections
  - test_home_route_with_many_entries_has_sections
  - test_create_view_post_empty_is_empty_dict
  - test_home_with_many_entries
  - test_new_entry_view_returns_response_given_request
  - test_filling_fake_db
  - test_detail_view_returns_dict_with_db
  - test_update_view_returns_dict_with_db
  - test_detail_view_with_wrong_id_raises_404
  - test_update_view_with_wrong_id_raises_404
