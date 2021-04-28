from app.simple_spam_transformer import SimpleSpamTransformer, SpamFilter


def test_transform_should_not_return_empty_string():
    transformer = SimpleSpamTransformer()

    transformed_spam, _ = transformer.transform("FREE AVOCADOS")

    assert isinstance(transformed_spam, str)
    assert transformed_spam != ""


def test_filter_should_not_flag_ham():
    spam_filter = SpamFilter()

    assert spam_filter.filter("Important message from general studies")[0] == "ham"
