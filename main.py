from api import APIHelper, ASTRAL_OBJECT_SELECTOR
from utils import MatrixUtils
import time


def get_coordinates():
    return [[2, 2], [3, 3], [4, 4], [5, 5], [6, 4], [7, 3], [8, 2],
            [2, 8], [3, 7], [4, 6], [6, 6], [7, 7], [8, 8]]


def get_input_matrix():
    matrix = APIHelper.generate_get_request()
    return matrix['goal']


def create_x():
    coordinates = get_coordinates()
    for coordinate in coordinates:
        print("Updating coordinate: " + str(coordinate))
        APIHelper.PolyanetGenerator.generate_astral_object(row=coordinate[0], column=coordinate[1])
        time.sleep(3)


def create_crossmint_logo():
    matrix = get_input_matrix()
    row_len = len(matrix)
    col_len = len(matrix[0])
    for row in range(0, row_len):
        for col in range(0, col_len):
            attribute_astral_object = MatrixUtils.get_attribute_astral_object(matrix[row][col])
            if not attribute_astral_object:
                continue
            print("Updating coordinate: [" + str(row) + ", " + str(col) + "]")
            astral_object_selector_class = ASTRAL_OBJECT_SELECTOR.get(attribute_astral_object[1])
            input_data = {"row": row, "column": col}
            if astral_object_selector_class["attribute"] is not None:
                input_data[astral_object_selector_class["attribute"]] = attribute_astral_object[0]
            astral_object_selector_class["generator_class"].generate_astral_object(
                **input_data
            )
            time.sleep(3)


def main():
    # create_x()
    create_crossmint_logo()


if __name__ == "__main__":
    main()