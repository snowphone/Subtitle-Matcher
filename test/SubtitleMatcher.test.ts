import { SubtitleMatcher } from "../src/SubtitleMatcher"

describe("SubtitleMatcher class test", () => {
	it("checks for rename method", () => {
		let matcher = new SubtitleMatcher("mp4", "srt", "./");
		let src = "video1.helloworld.mp4",
			expected = "video1.helloworld.srt";
		expect(matcher["rename"](src)).toBe(expected);
	})
})