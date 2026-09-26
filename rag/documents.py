from pathlib import Path


def load_documents():

    documents = [
        """
        California Housing Dataset contains information about
        housing districts in California.

        The dataset includes features such as longitude,
        latitude, housing median age, total rooms,
        total bedrooms, population, households,
        median income, and ocean proximity.

        The target variable is median house value.
        """,

        """
        Median income represents the median income of households
        in a housing district.

        Higher median income is generally associated with
        higher house values in the California Housing dataset.
        """,

        """
        Ocean proximity describes the location of a housing district
        relative to the ocean.

        Categories include:
        NEAR BAY,
        <1H OCEAN,
        INLAND,
        NEAR OCEAN,
        and ISLAND.
        """,

        """
        House price prediction is a regression problem because
        the target variable, median house value, is a continuous
        numerical value.

        Machine learning models such as Linear Regression,
        Random Forest Regressor, and Gradient Boosting Regressor
        can be used for this task.
        """
    ]

    return documents


if __name__ == "__main__":

    documents = load_documents()

    print("Documents loaded successfully!")

    print("Number of documents:", len(documents))

    for i, document in enumerate(documents, start=1):

        print(f"\nDocument {i}:")
        print(document)