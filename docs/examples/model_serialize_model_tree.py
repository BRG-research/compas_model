from compas.geometry import Point
from compas_model.elements import Element
from compas_model.model import ElementTree
from compas_model.model import Model


def serialize_model_tree():
    """Serialize a model_tree and nodes and the elements inside."""
    # --------------------------------------------------------------------------
    # create model
    # --------------------------------------------------------------------------
    model = Model()

    # --------------------------------------------------------------------------
    # add group nodes - a typical tree node with a name and geometry
    # --------------------------------------------------------------------------
    car = model.add_group(name="car", geometry=None)
    wheel = car.add_group(name="wheel", geometry=Point(0, 0, 0))

    # --------------------------------------------------------------------------
    # add element nodes - a "special" tree node with a name and element
    # --------------------------------------------------------------------------
    wheel.add_element(name="spoke1", element=Element.from_frame(1, 10, 1))
    wheel.add_element(name="spoke2", element=Element.from_frame(5, 10, 1))
    wheel.add_element(name="spoke3", element=Element.from_frame(10, 10, 1))

    # --------------------------------------------------------------------------
    # Serialize the model_tree.
    # --------------------------------------------------------------------------
    model.hierarchy.to_json("data/my_model_tree.json", pretty=True)

    # --------------------------------------------------------------------------
    # Deserialize the model_tree.
    # --------------------------------------------------------------------------
    model_tree_deserialized = ElementTree.from_json("data/my_model_tree.json")

    # --------------------------------------------------------------------------
    # Print the contents of the deserialized model_tree.
    # --------------------------------------------------------------------------
    model.hierarchy.print()

    print()
    model_tree_deserialized.print()


serialize_model_tree()
