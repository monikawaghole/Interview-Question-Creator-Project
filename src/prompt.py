
prompt_template = """
    You are an expert at creating questions based on uploaded pdf file.
    Your goal is to generate interview questions based on uploaded pdf.
    You do this by asking questions about the text below:

    ------------
    {text}
    ------------

    Create questions that will prepare the coders or programmers for their tests.
    Make sure not to lose any important information.

    QUESTIONS:
    """


refine_template = ("""
    You are an expert at creating practice questions based on uploaded pdf file.
    Your goal is to  generate answer for an interview questions.
    We have received some practice questions to a certain extent: {existing_answer}.
    We have the option to refine the existing questions or add new ones.
    (only if necessary) with some more context below.
    ------------
    {text}
    ------------

    Given the new context, refine the original questions in English.
    If the context is not helpful, please provide the original questions.
    QUESTIONS:
    """
    )