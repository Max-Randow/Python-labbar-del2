# =========================================================================
# Type definition
# =========================================================================
# Define the type somehow...  The initial "" is simply here as a placeholder.
from typing import NamedTuple,List
import copy
from cal_abstraction import *

TimeSpanSeq = NamedTuple("TimeSpanSeq", [("sequences",List[TimeSpan])])

# =========================================================================
#  Function implementations
# =========================================================================

# Implement these functions!  Also determine if you need *additional* functions.

def new_time_span_seq(sequences : List[TimeSpan] = None) -> TimeSpanSeq:
    """Creates a new TimeSpanSeq"""
    if sequences is None:
        sequences = []
    else:
        ensure_type(sequences,List[TimeSpan])

    return TimeSpanSeq(sequences)
    

def tss_is_empty(time_span_seq : TimeSpanSeq) -> bool:
    """Returns true or false depending on if the TimeSpanSeq is empty or not"""
    ensure_type(time_span_seq,TimeSpanSeq)

    return not time_span_seq.sequences
     


def tss_plus_span(time_span_seq : TimeSpanSeq, time_span : TimeSpan):
    """Adds a TimeSpan to a TimeSpanSequence, returns a new TimeSpanSequence"""
    tss =  copy.deepcopy(time_span_seq)
    ensure_type(time_span_seq,TimeSpanSeq) and ensure_type(time_span,TimeSpan)
    tss.sequences.append(time_span)

    def ts_sort_key(ts):
        #Convert to minutes
        return hour_number(time_hour(ts_start(ts))) * 60 + \
                           minute_number(time_minute(ts_start(ts)))

    tss = new_time_span_seq(sorted(tss.sequences, key=ts_sort_key))

    return tss


def tss_iter_spans(time_span_seq):
    ensure_type(time_span_seq,TimeSpanSeq)

    for span in time_span_seq.sequences:
        yield span


def show_time_spans(time_span_seq):
    """Outputs all the TimeSpans in TimeSpanSeq"""
    generator = tss_iter_spans(time_span_seq)

    for span in generator:
        print(span)


# Keep only time spans that satisfy pred.
# You do not need to modify this function.
def tss_keep_spans(tss, pred):
    result = new_time_span_seq()
    for span in tss_iter_spans(tss):
        if pred(span):
            result = tss_plus_span(result, span)

    return result


