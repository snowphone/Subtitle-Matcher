import { AssertionError } from "assert";
import fs from "fs-extra";
import path from "path";
import { zip } from "./misc";


export class SubtitleMatcher {
	private readonly regexp: RegExp;

	constructor(private vid_ext: string, private sub_ext: string, private folder: string) { 
		this.regexp = new RegExp(`${this.vid_ext}\$`)
	}

	public match(): void {
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
				const new_sub_name = this.rename(v)
				fs.rename(s, new_sub_name)
					.then(() => console.log(`${path.basename(s)} -> ${path.basename(new_sub_name)}`))
			});
	}

	/**
	 * It transforms its extension to `smi | srt` without changing the basename.
	 * @param src video file name
	 */
	private rename(src: string): string {
		const new_sub_name = src.replace(this.regexp, this.sub_ext);
		return new_sub_name;
	}
}
