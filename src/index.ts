import os from "os";
import fs from "fs-extra";
import path from "path";
import util from "util";
import ArgumentParser from "argparse";


let parser = new ArgumentParser.ArgumentParser();
parser.addArgument(["-f", "--folder"], {help: "folder containing movies", defaultValue: "./"});
parser.addArgument(['-v', "--video_ext"], {help: "video extension", choices: ["mkv", "mp4", "avi"], required: true});
parser.addArgument(['-s', "--subtitle_ext"], {help: "subtitle extension", choices: ["smi", "srt"], defaultValue: "smi"});

let argv = parser.parseArgs();

main(argv);


function main(argv: object) {
    console.log(typeof argv, argv);
}

