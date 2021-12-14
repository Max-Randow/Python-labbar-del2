# Write your code for lab 8d here.

from test_driver import store_test_case, run_free_spans_tests


# Create additional test cases, and add to them to create_tests_for_free_span().

def create_tests_for_free_span() -> dict:
    """Create and return a number of test cases for the free_spans function"""
    test_cases = dict()

    store_test_case(
        test_cases,
        1,
        start_str="08:00",  # Search interval starts
        end_str="21:00",  # Search interval ends
        booking_data=["07:00-09:00", "13:00-18:00"],  # This day's appointments
        exp_result=["09:00-13:00", "18:00-21:00"],
    )  # Expected free time

    # -------- YOUR TEST CASES GO HERE -----------------------
    # For each case, add a brief description of what you want to test.
    store_test_case(
            # Nothing is booked for the entire day
            test_cases,
            1,
            start_str="00:00",
            end_str="23:59",
            booking_data=[],
            exp_result=["00:00-23:59"]
    
    )

    store_test_case(
            # Nothing is booked for the entire day
            test_cases,
            1,
            start_str="00:00",
            end_str="23:59",
            booking_data=[],
            exp_result=["00:00-23:59"]
    
    )

    store_test_case(
            # Just random times, and a 1 minute booking
            test_cases,
            1,
            start_str="10:00",
            end_str="18:35",
            booking_data=["06:00-10:00", "10:00-12:30", "18:34-18:35"],
            exp_result=["12:30-18:34"]
    
    )

    store_test_case(
            # One minute bookings
            test_cases,
            1,
            start_str="03:00",
            end_str="03:01",
            booking_data=["03:01-03:02","02:59-03:01"],
            exp_result=["03:00-03:01"]
    
    )
    store_test_case(
            # Bookings over start and end.
            test_cases,
            1,
            start_str="15:00",
            end_str="18:00",
            booking_data=["15:00-16:00","16:30-17:20","17:30-18:30"],
            exp_result=["16:00-16:30","17:20-17:30"]
    
    )

    store_test_case(
            # Bookings over start and end.
            test_cases,
            1,
            start_str="15:00",
            end_str="19:00",
            booking_data=["12:00-19:00"],
            exp_result=[]
    
    )
    
    print("Test cases generated.")

    return test_cases


if __name__ == '__main__':
    # Actually run the tests, using the test driver functions
    tests = create_tests_for_free_span()
    run_free_spans_tests(tests)
