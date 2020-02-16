import { ArgumentParser } from "argparse";
import { SubtitleMatcher } from "./SubtitleMatcher";


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
