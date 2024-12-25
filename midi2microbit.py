import mido
import argparse

def midi_to_note_array(file_path):
    midi_file = mido.MidiFile(file_path)

    note_mapping = {
        0: 'C', 1: 'C#', 2: 'D', 3: 'D#', 4: 'E', 5: 'F', 6: 'F#',
        7: 'G', 8: 'G#', 9: 'A', 10: 'A#', 11: 'B'
    }

    result = []

    for track in midi_file.tracks:
        time_accumulated = 0 

        for msg in track:
            if msg.type == 'note_on' or msg.type == 'note_off':
                time_accumulated += msg.time

                if msg.type == 'note_on' and msg.velocity > 0:
                    note = note_mapping[msg.note % 12]
                    octave = msg.note // 12
                    note_name = f"{note}{octave}"

                    relative_length = round(time_accumulated / midi_file.ticks_per_beat)
                    if relative_length > 1:
                        result.append(f"{note_name}:{relative_length}")
                    else:
                        result.append(note_name)

                    time_accumulated = 0

    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='midi2microbit',
                    description='This script converts midi files, to strings playable with the micro:bit board.',
                    epilog='Use music.play(), to play the string. The --start and --end arguments might be useful, due to the limited memory of most micro:bit models.')
    parser.add_argument("file", type=str, help="The path to the midi file you want to convert.")
    parser.add_argument("-s", "--start", type=int, default=0, help="Starting note to extract from.")
    parser.add_argument("-e", "--end", type=int, default=None, help="Last note to extract to.")
    args = parser.parse_args()
    file_path = args.file
    note_array = midi_to_note_array(file_path)
    if args.end is not None:
        note_array = note_array[args.start:args.end]
    else:
        note_array = note_array[args.start:]
    print(note_array)