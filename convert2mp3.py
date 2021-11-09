import os
from pydub import AudioSegment

for directory in os.listdir("."):

	if not os.path.isfile(directory): 	# if f is a directory

		print(f"\nIn directory [{directory}]\n-------------------------")

		for f in os.listdir(directory):

			audio_format = str(f).split(".")[-1]

			# exclude processing of mp3 files
			if (audio_format != "mp3") and (audio_format != "py"):
				try:
					m4a_audio = AudioSegment.from_file("{}/{}".format(directory, str(f)), str(audio_format))
					print(f"Converting [{f}]")
					m4a_audio.export("{}/{}".format(directory, str(f).split(str(audio_format))[0]+".mp3"), format="mp3")
					# delete previous format
					os.remove("{}/{}".format(directory, f))
				except:
					print("Error. Check if file format is supported.")

			# exclude processing of the script file
			elif audio_format == "py":
				pass

			else:
				print("File format is already mp3.")

	elif os.path.isfile(directory):

		audio_format = str(directory).split(".")[-1]

		if (audio_format != "mp3") and (audio_format != "py"):
			try:
				m4a_audio = AudioSegment.from_file("{}".format(str(directory)), str(audio_format))
				print(f"Converting [{directory}]")
				m4a_audio.export("{}".format(str(directory).split(str(audio_format))[0]+".mp3"), format="mp3")
				# delete previous format
				os.remove(directory)
			except:
				print("Error. Check if file format is supported.")

		# exclude processing of the script file
		elif audio_format == "py":
			pass

		else:
			print("File format is already mp3.")
	else:
		pass
