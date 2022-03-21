import subtitle_matcher as sm

def test_match():
	s = sm.SubtitleMatcher("mp4", "./")
	src = "video1.helloworld.mp4"
	expected = "video1.helloworld.srt"
	assert s._rename(src, "srt") == expected

def test_sort():
	src = ["hello_2people.mp4", "hello_11people.mp4", "hello_1people.mp4"]
	expected = ["hello_1people.mp4", "hello_2people.mp4", "hello_11people.mp4"]

	assert sorted(src) != expected
	assert sorted(src, key=sm.NumericalSorter.fn) == expected

def test_rename():
	s = sm.SubtitleMatcher("mp4", "./", "ko")

	src = "video1.helloworld.mp4"
	expected = "video1.helloworld.ko.srt"
	assert s._rename(src, "srt") == expected
