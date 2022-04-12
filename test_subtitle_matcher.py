from unittest.mock import MagicMock

import pytest
from pytest_mock import MockerFixture

from subtitle_matcher import NumericalSorter, SubtitleMatcher

PATH_ROOT = "workspace_root/"
LANG_SUFFIX = "ko"
VIDEO_EXT = "mp4"


@pytest.fixture
def sm():
    return SubtitleMatcher(VIDEO_EXT, PATH_ROOT, LANG_SUFFIX)


@pytest.fixture
def mocked_listdir(mocker: MockerFixture):
    video_src_list = [
        "hello_2people.mp4",
        "hello_11people.mp4",
        "hello_1people.mp4",
    ]
    subtitle_src_list = ["chapter3.smi", "chapter2.smi", "chapter1.srt"]

    mocked_listdir = mocker.patch("os.listdir")
    mocked_listdir.return_value = video_src_list + subtitle_src_list

    return mocked_listdir


@pytest.fixture
def mocked_rename(mocker: MockerFixture):
    mocked_rename = mocker.patch("os.rename")
    return mocked_rename


def test_sort():
    src = ["hello_2people", "hello_11people", "hello_1people"]
    expected = ["hello_1people", "hello_2people", "hello_11people"]

    assert sorted(src) != expected
    assert sorted(src, key=NumericalSorter()) == expected
    return


@pytest.mark.parametrize(
    "sm",
    [
        SubtitleMatcher(VIDEO_EXT, PATH_ROOT, None),
        SubtitleMatcher(VIDEO_EXT, PATH_ROOT, LANG_SUFFIX),
    ],
)
def test_get_new_name(sm: SubtitleMatcher):
    basename = "video1.helloworld"
    subtitle_ext = "srt"

    src = f"{basename}.{VIDEO_EXT}"
    if sm.suffix:
        expected = f"{basename}.{LANG_SUFFIX}.{subtitle_ext}"
    else:
        expected = f"{basename}.{subtitle_ext}"

    assert sm._get_new_name(src, subtitle_ext) == expected
    return


def test_get_sorted_file_list(sm: SubtitleMatcher, mocked_listdir: MagicMock):
    actual_vids, actual_subs = sm._get_sorted_file_list()

    assert actual_vids == list(
        f"{PATH_ROOT}{it}"
        for it in [
            "hello_1people.mp4",
            "hello_2people.mp4",
            "hello_11people.mp4",
        ]
    )
    assert actual_subs == list(
        f"{PATH_ROOT}{it}"
        for it in ["chapter1.srt", "chapter2.smi", "chapter3.smi"]
    )

    mocked_listdir.assert_called_once_with(PATH_ROOT)
    return


def test_match(
    sm: SubtitleMatcher, mocked_rename: MagicMock, mocked_listdir: MagicMock
):
    sm.match()

    assert mocked_rename.call_count == len(mocked_listdir.return_value) // 2
    mocked_listdir.assert_called_once_with(PATH_ROOT)
    return


def test_match_with_insufficient_subtitles(
    sm: SubtitleMatcher, mocked_rename: MagicMock, mocked_listdir: MagicMock
):
    mocked_listdir.return_value = [
        it for it in mocked_listdir.return_value if not it.endswith("srt")
    ]

    with pytest.raises(RuntimeError):
        sm.match()
    mocked_rename.assert_not_called()
