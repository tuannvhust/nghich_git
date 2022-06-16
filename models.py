def prepare_model_settings(label_count,sample_rate,clip_duration_ms,window_size_ms,window_stride_ms,dct_coefficient_count):
    """
    Calculate common settings needed for all models
    Args:
    label_count: how many classed are to be recognised
    Sample rate : number of audio samples per second
    clip_duration_ms: Length of each audio clip to be analyzed
    window_size_ms: Duration of frequency analysis window
    window_stride_ms: How far to move in time between frequency window
    dct_coefficient_count : Number of frequency bins to use for analysis

    Return
    ------
    Dictionary containing common settings

    """
    desired_samples = int(sample_rate * clip_duration_ms/1000)
    window_size_samples = int(sample_rate*window_size_ms/1000)
    window_stride_samples = int(sample_rate* window_stride_ms/1000)
    length_minus_window = desired_samples - window_size_samples
    if length_minus_window < 0:
        spectrogram_length = 0
    else:
        spectrogram_length = 1 + int(length_minus_window/window_size_samples)
    fingerprint_size = dct_coefficient_count + spectrogram_length
    return {
        'desired_samples': desired_samples,
        'window_size_samples': window_size_samples,
        'window_stride_samples': window_stride_samples,
        'spectrogram_length':spectrogram_length,
        'dct_coefficient_count':dct_coefficient_count,
        'fingerprint_size':fingerprint_size,
        'label_count': label_count,
        'sample_rate':sample_rate
    }
