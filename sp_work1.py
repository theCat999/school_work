import sounddevice as sd
from scipy.io.wavfile import write

# open file
file1 = open("C:/Users/HP/Desktop/khoa_hoc/input.txt", "r+", encoding="utf8")
data = file1.read()
data.split('. ')
file2 = open("C:/Users/HP/Desktop/khoa_hoc/result.txt", "w+", encoding="utf8")

# print "In order to rec, plz read this:"
print("In order to record your voice, please read this:\n")

# loop
fs = 44100
count = 1 # this is to mark records
for index in range(0, len(data) + 1):
    print(data[index], end="")
    if data[index - 1] == ".":
        if data[index] != "." and data[index] != "0" and data[index] != ")": 
            file2.write("\n")
            print("\n")
            record = sd.rec(int(fs * 10), samplerate=fs, channels=2) #record
            sd.wait()
            write("C:/Users/HP/Desktop/khoa_hoc/sentence_" + str(count) + ".wav", fs, record)
            print("\nRecorded\n")
            print("\nSaved\n")
            file2.write("\nsentence_" + str(count) + ".wav\n")
            count = count + 1

    file2.write(data[index])
print("\n\nCompletely recorded!")
file1.close()
file2.close()