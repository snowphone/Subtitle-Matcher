#!/usr/bin/env python3
from argparse import ArgumentParser
import os
from re import compile, split
from typing import Literal, Optional

import tabulate


class SubtitleMatcher:
	def __init__(self, video_ext: str, folder: str, suffix: Optional[str] = None) -> None:
		self.video_ext = video_ext
		self.folder = folder
		self.regexp = compile(f"{self.video_ext}$")

		self.suffix = suffix

	def match(self):
		items = os.listdir(self.folder)
		items = [ os.path.join(self.folder, it) for it in items ]

		videos = [it for it in items if it.endswith(self.video_ext)]
		subtitles = [it for it in items if it.endswith("smi") or it.endswith("srt")]

		videos.sort(key=NumericalSorter.fn)
		subtitles.sort(key=NumericalSorter.fn)

		if(len(videos) != len(subtitles)):
			raise RuntimeError("len(videos) != len(subtitles)")

		line_list = []
		for v, s in zip(videos, subtitles):
			subtitle_ext = s.split('.')[-1]
			new_name = self._rename(v, subtitle_ext)
			os.rename(s, new_name)

			line_list.append( (os.path.basename(s) , os.path.basename(new_name)))
		print(tabulate.tabulate(line_list, headers=["From", "To"], tablefmt="fancy_grid"))
	
	def _rename(self, src: str, subtitle_ext: Literal["smi", "srt"]) -> str:
		if self.suffix:
			return self.regexp.sub(f"{self.suffix}.{subtitle_ext}", src)
		return self.regexp.sub(subtitle_ext, src)


class NumericalSorter:
	@staticmethod
	def fn(s: str):
		return [NumericalSorter._try_int(i) for i in split(r"(\d+)", s)]
	
	@staticmethod
	def _try_int(n: str):
		if n.isdecimal():
			return int(n)
		return n




def main(args):
	s = SubtitleMatcher(args.video_ext, args.folder, args.suffix)
	s.match()


if __name__ == "__main__":
	parser = ArgumentParser()
	parser.add_argument("-f", "--folder", help="folder containing movies", default="./")
	parser.add_argument("-v", "--video_ext", help="video extension", choices=["mkv", "mp4", "avi"], required=True)
	parser.add_argument("--suffix", help="optional suffix", default=None)

	main(parser.parse_args())


