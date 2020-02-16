import { ArgumentParser } from "argparse";
import { AssertionError } from "assert";
import fs from "fs-extra";
import path from "path";


class SubtitleMatcher {
	constructor(private vid_ext: string, private sub_ext: string, private folder: string) { }

	public match() {
		let items = fs.readdirSync(this.folder)
			.map(basepath => path.join(this.folder, basepath));
		let videos = items.filter(i => i.endsWith(this.vid_ext));
		let subtitles = items.filter(i => i.endsWith(this.sub_ext));

		let sorter = Intl.Collator(undefined, { numeric: true }).compare;
		videos.sort(sorter);
		subtitles.sort(sorter);

		if (videos.length != subtitles.length) {
			throw new AssertionError({
				message: `# of videos(${videos.length}) doesn't match # of subtitles(${subtitles.length})`
			});
		}

		zip(videos, subtitles)
			.forEach(([v, s]) => {
				const regexp = new RegExp(`${this.vid_ext}\$`);
				const new_sub_name = v.replace(regexp, this.sub_ext);
				fs.rename(s, new_sub_name)
					.then(() => console.log(`${path.basename(s)} -> ${path.basename(new_sub_name)}`))
			});
	}

}

function zip<T, R>(lhs: Array<T>, rhs: Array<R>): Array<[T, R]> {
	if (!lhs.length || !rhs.length) {
		return [];
	}
	return [[lhs[0], rhs[0]], ...zip(lhs.slice(1), rhs.slice(1))];
}

let parser = new ArgumentParser();
parser.addArgument(["-f", "--folder"], { help: "folder containing movies", defaultValue: "./" });
parser.addArgument(['-v', "--video_ext"], { help: "video extension", choices: ["mkv", "mp4", "avi"], required: true });
parser.addArgument(['-s', "--subtitle_ext"], { help: "subtitle extension", choices: ["smi", "srt"], defaultValue: "smi" });

let argv = parser.parseArgs();
main(argv);


function main(argv: any) {
	let matcher = new SubtitleMatcher(argv["video_ext"], argv["subtitle_ext"], argv["folder"]);
	matcher.match();
}

