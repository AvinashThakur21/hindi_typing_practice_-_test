def calculate_typing_metrics(original_text, typed_text,start_time ,end_time ):

    from datetime import datetime

    def calculate_cpm(typed_text, time_taken_seconds):
        num_chars = len(typed_text)
        cpm = (num_chars / time_taken_seconds) * 60
        return cpm

    def calculate_accuracy(original_text, typed_text):
        original_chars = list(original_text)
        typed_chars = list(typed_text)
        correct_chars = 0

        for i in range(min(len(original_chars), len(typed_chars))):
            if original_chars[i] == typed_chars[i]:
                correct_chars += 1

        accuracy = (correct_chars / len(original_chars)) * 100
        return accuracy

    # print(end_time,start_time)
    start_time_timestamp = start_time.replace("Z", "+00:00")
    start_time = datetime.fromisoformat(start_time_timestamp)

    end_time_timestamp = end_time.replace("Z", "+00:00")
    end_time = datetime.fromisoformat(end_time_timestamp)

    time_taken_seconds = int( end_time.timestamp() - start_time.timestamp())
    # print(time_taken_seconds)

    cpm = calculate_cpm(typed_text, time_taken_seconds)
    accuracy = calculate_accuracy(original_text, typed_text)

    if accuracy == 0:
        return 0
    else:
        return cpm/accuracy

