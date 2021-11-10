import os
from pydub import AudioSegment


# Ask if to delete previous unconverted files
delete_initial = str(input("Do you wish to delete initial file formats?(y/N): ")).upper()

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
					if delete_initial == "Y":
						os.remove("{}/{}".format(directory, f))
					else:
						pass
				except:
					print("Error. Check if file format is supported.")

			# exclude processing of the script file
			elif audio_format == "py":
				pass

			else:
				print("File format is already mp3.")

		# Show we have exited current directory
		print("-------------------------\n")

	elif os.path.isfile(directory):

		audio_format = str(directory).split(".")[-1]

		if (audio_format != "mp3") and (audio_format != "py"):
			try:
				m4a_audio = AudioSegment.from_file("{}".format(str(directory)), str(audio_format))
				print(f"Converting [{directory}]")
				m4a_audio.export("{}".format(str(directory).split(str(audio_format))[0]+".mp3"), format="mp3")
				# delete previous format
				if delete_initial == "Y":
					os.remove(directory)
				else:
					pass
			except:
				print("Error. Check if file format is supported.")

		# exclude processing of the script file
		elif audio_format == "py":
			pass

		else:
			print("File format is already mp3.")
	else:
		pass
