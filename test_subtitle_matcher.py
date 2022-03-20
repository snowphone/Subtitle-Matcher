import subtitle_matcher as sm

def test_match():
	s = sm.SubtitleMatcher("mp4", "srt", "./")
	src = "video1.helloworld.mp4"
	expected = "video1.helloworld.srt"
	assert s._rename(src) == expected

def test_sort():
	src = ["hello_2people.mp4", "hello_11people.mp4", "hello_1people.mp4"]
	expected = ["hello_1people.mp4", "hello_2people.mp4", "hello_11people.mp4"]

	assert sorted(src, key=sm.NumericalSorter.fn) == expected

def test_rename():
	s = sm.SubtitleMatcher("mp4", "srt", "./", "ko")

	src = "video1.helloworld.mp4"
	expected = "video1.helloworld.ko.srt"
	assert s._rename(src) == expected


