from typing import Literal

GetEmailPreferencesByTokenResponse200Category = Literal["checkins", "recap", "updates"]

GET_EMAIL_PREFERENCES_BY_TOKEN_RESPONSE_200_CATEGORY_VALUES: set[
    GetEmailPreferencesByTokenResponse200Category
] = {
    "checkins",
    "recap",
    "updates",
}


def check_get_email_preferences_by_token_response_200_category(
    value: str,
) -> GetEmailPreferencesByTokenResponse200Category:
    if value in GET_EMAIL_PREFERENCES_BY_TOKEN_RESPONSE_200_CATEGORY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_EMAIL_PREFERENCES_BY_TOKEN_RESPONSE_200_CATEGORY_VALUES!r}"
    )
