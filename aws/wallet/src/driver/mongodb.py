# -*- coding: utf-8 -*-
from logzero import logger
from pymongo import MongoClient
from pymongo.errors import ConfigurationError, ConnectionFailure


class MongoDatabaseDriver(object):

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not MongoDatabaseDriver.__instance:
            MongoDatabaseDriver.__instance = object.__new__(cls)
        return MongoDatabaseDriver.__instance

    def __init__(self, host, database, username, password: str = None, **kwargs):
        self._host = host
        self._database = database
        self._username = username
        self._password = password
        self._auth_source = kwargs.get("auth_source", database)
        self._retry_writes = kwargs.get("retry_writes", False)
        self._auth_mechanism = kwargs.get("auth_mechanism", "SCRAM-SHA-1")
        self._conn = None

    def __enter__(self):
        self._conn = self.__new_connection
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_connection()

    @property
    def __new_connection(self) -> MongoClient:
        try:
            return MongoClient(
                host=self._host,
                username=self._username,
                password=self._password,
                authSource=self._auth_source,
                authMechanism=self._auth_mechanism,
                retryWrites=self._retry_writes,
            )

        except ConnectionFailure as cf:
            logger.exception(f"[MONGODB] Connection is failure check. {cf}")
            raise

        except ConfigurationError as ce:
            logger.exception(
                f"[MONGODB] Parameters informed for connection are invalid check. {ce}"
            )
            raise

        except Exception as e:
            logger.exception(f"[MONGODB] Connection error. {e}")
            raise

    def test_ping(self):
        try:
            x = self._conn[self._database].command("ping")
            return x.get("ok", "")

        except Exception as e:
            logger.exception(f"[MONGODB] Test of connection is failure. {e}")
            raise

    def close_connection(self):
        if self._conn:
            self._conn.close()
