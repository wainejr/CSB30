# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from xml2dict import xml2dict


def generateLikesTuples():
    like_related_tuples = {"likes_band": [], "likes_movie": []}

    band_dict = xml2dict("music")
    movie_dict = xml2dict("movie")

    for key in band_dict.keys():
        for item in band_dict[key]:
            like_related_tuples["likes_band"].append(
                {"values": [item[0], item[1], item[2]]}
            )
            # print(like_related_tuples["likes_band"][-1])

    for key in movie_dict.keys():
        for item in movie_dict[key]:
            like_related_tuples["likes_movie"].append(
                {"values": [item[0], item[1], item[2]]}
            )
            # print(like_related_tuples["likes_movie"][-1])

    return like_related_tuples
