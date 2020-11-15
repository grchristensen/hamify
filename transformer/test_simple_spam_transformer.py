from simple_spam_transformer import SimpleSpamTransformer


def test_transform_should_not_return_empty_string():
    transformer = SimpleSpamTransformer()

    transformed_spam = transformer.transform("FREE AVOCADOS")

    assert isinstance(transformed_spam, str)
    assert transformed_spam != ""
