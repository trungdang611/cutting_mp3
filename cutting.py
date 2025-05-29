from pydub import AudioSegment

def time_to_ms(minutes, seconds):
    return (minutes * 60 + seconds) * 1000

def cut_mp3(input_file, start_ms, end_ms, output_file):
    audio = AudioSegment.from_mp3(input_file)
    cut_audio = audio[start_ms:end_ms]
    cut_audio.export(output_file, format="mp3")
    print(f"Đã cắt từ {start_ms}ms đến {end_ms}ms sang file {output_file}")

start_ms = time_to_ms(38, 44)
end_ms = time_to_ms(43, 31)

cut_mp3("./input.mp3", start_ms, end_ms, "./output_cut.mp3")
