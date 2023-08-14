from typing import Any, Dict

from ..get_versions import get_pydantic_version

pydantic_version = get_pydantic_version()


if pydantic_version.value == 1:

    class core_schema:  # noqa
        def CoreSchema(self):
            ...

        def general_after_validator_function(self):
            ...

        def str_schema(self):
            ...

        def ValidationInfo(self):
            ...


if pydantic_version.value == 2:
    from pydantic_core import core_schema  # noqa


JsonSchemaValue = Dict[str, Any]


class BasePydanticV2:
    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        source,
    ) -> core_schema.CoreSchema:
        return core_schema.general_after_validator_function(
            cls._validate, core_schema.str_schema()
        )

    @classmethod
    def __get_pydantic_json_schema__(
        cls, core_schema: core_schema.CoreSchema, handler
    ) -> JsonSchemaValue:
        field_schema = handler(core_schema)
        field_schema.update(type="string", format=cls.format)
        return field_schema

    @classmethod
    def _validate(cls, __input_value: str, _: core_schema.ValidationInfo) -> str:
        cls.validate_type(__input_value)
        return cls.validate(__input_value)


class BaseMaskV2(BasePydanticV2):
    @classmethod
    def _validate(cls, __input_value: str, _: core_schema.ValidationInfo) -> str:
        cls.validate_type(__input_value)
        cls.validate_mask(__input_value)
        return cls.validate(__input_value)


class BaseDigitsV2(BasePydanticV2):
    @classmethod
    def _validate(cls, __input_value: str, _: core_schema.ValidationInfo) -> str:
        cls.validate_type(__input_value)
        cls.validate_numbers(__input_value)
        return cls.validate(__input_value)
