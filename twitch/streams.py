from twitch_types import Pagination, Stream


class Streams:
    def __init__(self, twitch):
        self.__twitch = twitch

    def get_streams(
        self,
        after=None,
        before=None,
        limit=None,
        game_id=None,
        language=None,
        user_id=None,
        user_login=None,
    ):
        routes = "streams"
        params = {}

        if after is not None:
            params["after"] = after
        if before is not None:
            params["before"] = before
        if limit is not None:
            params["limit"] = limit
        if game_id is not None:
            params["game_id"] = game_id
        if language is not None:
            params["language"] = language
        if user_id is not None:
            params["user_id"] = user_id
        if user_login is not None:
            params["user_login"] = user_login

        res = self.__twitch.get(routes, params)

        streams = []
        if "data" in res:
            for stream in res["data"]:
                streams.append(Stream(**stream))

        pagination = None
        if "pagination" in res:
            pagination = Pagination(**res["pagination"])

        return streams, pagination
