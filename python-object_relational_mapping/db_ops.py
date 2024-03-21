from model_state import State


def list_states(session):
    """
    Function to list all State objects from the database.
    """
    # Query the database
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
