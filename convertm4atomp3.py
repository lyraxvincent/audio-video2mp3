import os
from pydub import AudioSegment

for directory in os.listdir("."):
	if not os.path.isfile(directory): 	# if f is a directory
		print(f"\nIn directory [{directory}]\n-------------------------")
		for f in os.listdir(directory):
			try: 	# if format is m4a
				m4a_audio = AudioSegment.from_file("{}/{}".format(directory, str(f)), "m4a")
				print(f"Converting [{f}]")
				m4a_audio.export("{}/{}".format(directory, str(f).split(".m4a")[0]+".mp3"), format="mp3")
				# delete m4a format
				os.remove("{}/{}".format(directory, f))
			except:
				print("File format not m4a.")
	elif os.path.isfile(directory):
		try: 	# if format is m4a
			m4a_audio = AudioSegment.from_file("{}".format(str(directory)), "m4a")
			print(f"Converting [{f}]")
			m4a_audio.export("{}".format(str(directory).split(".m4a")[0]+".mp3"), format="mp3")
			# delete m4a format
			os.remove(directory)
		except:
			print("File format not m4a.")
	else:
		pass
