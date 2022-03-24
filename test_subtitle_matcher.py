from pathlib import Path
from typing import List

import pytest

from pytest_mock import MockerFixture
from subtitle_matcher import SubtitleMatcher, NumericalSorter


PATH_ROOT="workspace_root/"
SUFFIX="ko"
VIDEO_EXT="mp4"

@pytest.fixture(autouse=True)
def s():
	return SubtitleMatcher(VIDEO_EXT, PATH_ROOT, SUFFIX)

@pytest.fixture
def video_src_list():
	#return [f"{PATH_ROOT}{name}.{VIDEO_EXT}" for name in ("hello_2people", "hello_11people", "hello_1people")]
	return ["hello_2people.mp4", "hello_11people.mp4", "hello_1people.mp4"]


def rename_mocked(src: str, dst: str):
	assert Path(src).stem == Path(dst).stem
	assert src.endswith("mp4")
	assert dst.endswith("ko.smi") or dst.endswith("ko.srt")

def test_sort():
	src = ["hello_2people", "hello_11people", "hello_1people"]
	expected =  ["hello_1people", "hello_2people", "hello_11people"]

	assert sorted(src) != expected
	assert sorted(src, key=NumericalSorter()) == expected

def test_rename_with_suffix(s: SubtitleMatcher):
	basename = "video1.helloworld"
	src = f"{basename}.{VIDEO_EXT}"
	expected = f"{basename}.{SUFFIX}.srt"
	assert s._get_new_name(src, "srt") == expected

def test_get_file_list(s: SubtitleMatcher, mocker: MockerFixture, video_src_list: List[str]):
	subtitle_src_list = ["chapter3.smi", "chapter2.smi", "chapter1.srt"]

	mocked_rename = mocker.patch("os.rename")
	mocked_rename.side_effect = rename_mocked

	mocked_listdir = mocker.patch("os.listdir")
	mocked_listdir.return_value = video_src_list + subtitle_src_list
	vids, subs = s._get_file_list()

	assert set(vids) == set(f"{PATH_ROOT}{it}" for it in video_src_list)
	assert set(subs) == set(f"{PATH_ROOT}{it}" for it in subtitle_src_list)

def test_match(s: SubtitleMatcher, mocker: MockerFixture, video_src_list: List[str]):
	#assert mocked_rename.call_count == len(video_src_list)
	#assert mocked_listdir.assert_called_once_with("./")
	pass



