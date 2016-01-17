import sqlalchemy


class Enum(sqlalchemy.types.TypeDecorator):
    impl = sqlalchemy.types.SmallInteger

    def __init__(self, enum_class, **kwargs):
        super().__init__(**kwargs)
        self._enum_class = enum_class

    def process_bind_param(self, value, dialect):
        return value.value

    def process_result_value(self, value, dialect):
        return self._enum_class(value)

    @property
    def python_type(self):
        return self._enum_class
