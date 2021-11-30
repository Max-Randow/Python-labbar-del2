# =========================================================================
# Type definition
# =========================================================================
# Define the type somehow...  The initial "" is simply here as a placeholder.
from typing import NamedTuple,List
import copy
from cal_abstraction import CalendarDay, Time, TimeSpan, ensure_type, new_time_span,Hour,Minute

TimeSpanSeq = NamedTuple("TimeSpanSeq", [("sequences",List[TimeSpan])])

# =========================================================================
#  Function implementations
# =========================================================================

# Implement these functions!  Also determine if you need *additional* functions.

def new_time_span_seq(sequences : List[TimeSpan] = None) -> TimeSpanSeq:
    """Create a new TimeSpanSeq"""
    if sequences is None:
        sequences = []
    else:
        ensure_type(sequences,List[TimeSpan])

    return TimeSpanSeq(sequences)
    

def tss_is_empty(time_span_seq : TimeSpanSeq) -> bool:
    """Returns true or false depending on if the TimeSpanSeq is empty or not"""
    ensure_type(time_span_seq,TimeSpanSeq)

    return not time_span_seq.sequences
     


def tss_plus_span(time_span_seq, time_span):
    """Adds a TimeSpan to a TimeSpanSequence, returns a new TimeSpanSequence"""
    tss =  copy.deepcopy(time_span_seq)
    ensure_type(time_span_seq,TimeSpanSeq) and ensure_type(time_span,TimeSpan)

    tss.sequences.append(time_span)

    return tss


def tss_iter_spans(time_span_seq):
    ensure_type(time_span_seq,TimeSpanSeq)

    for span in time_span_seq.sequences:
        yield span


def show_time_spans(time_span_seq):
    #Is it okay to iterate here?
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


#Test code
tss = new_time_span_seq([new_time_span(Time(Hour(14),Minute(00)),Time(Hour(16),Minute(00)))])
print(tss_is_empty(tss))
tss = tss_plus_span(tss,new_time_span(Time(Hour(15),Minute(00)),Time(Hour(17),Minute(00))))

show_time_spans(tss)
