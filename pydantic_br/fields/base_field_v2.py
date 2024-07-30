from __future__ import annotations

from typing import Any, Dict, Mapping

from ..get_versions import get_pydantic_version

pydantic_version = get_pydantic_version()


if pydantic_version.value == 2:
    try:
        from pydantic_core import core_schema  # type: ignore
    except ModuleNotFoundError:
        raise ModuleNotFoundError("Are you sure you installed pydantic_core")

CoreSchema: Any = Mapping[str, Any]
JsonSchemaValue = Dict[str, Any]


class BasePydanticV2:
    format = "generic"

    @classmethod
    def validate_type(cls, value: Any):
        ...

    @classmethod
    def validate(cls, value: str):
        ...

    @classmethod
    def validate_mask(cls, value: str):
        ...

    @classmethod
    def validate_numbers(cls, value: str):
        ...

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        source,
        *args,
        **kwargs,
    ) -> CoreSchema:
        try:
            schema = core_schema.with_info_after_validator_function(
                cls._validate, core_schema.str_schema()
            )
        except Exception:
            schema = core_schema.general_after_validator_function(
                cls._validate, core_schema.str_schema()
            )
        return schema

    @classmethod
    def __get_pydantic_json_schema__(
        cls,
        core_schema: CoreSchema,
        handler,
        *args,
        **kwargs,
    ) -> JsonSchemaValue:
        field_schema = handler(core_schema)
        field_schema.update(type="string", format=cls.format)
        return field_schema

    @classmethod
    def _validate(cls, __input_value: str, *args, **kwargs) -> str:
        cls.validate_type(__input_value)
        return cls.validate(__input_value)


class BaseMaskV2(BasePydanticV2):
    @classmethod
    def _validate(cls, __input_value: str, *args, **kwargs) -> str:
        cls.validate_type(__input_value)
        cls.validate_mask(__input_value)
        return cls.validate(__input_value)


class BaseDigitsV2(BasePydanticV2):
    @classmethod
    def _validate(cls, __input_value: str, *args, **kwargs) -> str:
        cls.validate_type(__input_value)
        cls.validate_numbers(__input_value)
        return cls.validate(__input_value)
