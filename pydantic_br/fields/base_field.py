from ..tools.get_versions import get_pydantic_version

pydantic_version = get_pydantic_version()


if pydantic_version.value == 1:
    from .base_field_v1 import BaseDigitsv1 as BaseDigits  # type: ignore # noqa
    from .base_field_v1 import BaseMaskv1 as BaseMask  # type: ignore # noqa
    from .base_field_v1 import Basev1 as Base  # type: ignore # noqa

if pydantic_version.value == 2:
    from .base_field_v2 import BaseDigitsV2 as BaseDigits  # type: ignore # noqa
    from .base_field_v2 import BaseMaskV2 as BaseMask  # type: ignore # noqa
    from .base_field_v2 import BaseV2 as Base  # type: ignore # noqa
