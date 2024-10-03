import os
from scripts.augment_pitch import batch_pitch_shift
from scripts.augment_speed import batch_change_speed
from scripts.augment_volume import batch_adjust_volume
from scripts.augment_time_shift import batch_time_shift
from scripts.augment_filter import batch_filter_audio
from scripts.augment_echo import batch_add_echo
from scripts.augment_frequency_shift import batch_frequency_shift

def run_augmentations():
    recordings_folder = 'recordings'
    augmented_folder = 'augmented'

    batch_pitch_shift(recordings_folder, os.path.join(augmented_folder, 'pitch_shifted'), 2)
    batch_change_speed(recordings_folder, os.path.join(augmented_folder, 'speed_variation'), 1.5)
    batch_adjust_volume(recordings_folder, os.path.join(augmented_folder, 'volume_adjusted'), 5)
    batch_time_shift(recordings_folder, os.path.join(augmented_folder, 'time_shifted'), 300)
    batch_filter_audio(recordings_folder, os.path.join(augmented_folder, 'filtered'), 5000)
    batch_add_echo(recordings_folder, os.path.join(augmented_folder, 'echoed'), 150)
    batch_frequency_shift(recordings_folder, os.path.join(augmented_folder, 'frequency_shifted'), 1.2)
    
if __name__ == '__main__':
    run_augmentations()
