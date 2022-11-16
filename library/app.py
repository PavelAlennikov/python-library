from repository.library import BookRep
import ui.ui as ui
from model.state import StateManager, States


class App:
    @staticmethod
    def run():
        book_rep = BookRep()

        ui.clear()

        state_manager = StateManager(book_rep)
        state_manager.state_changed.add_listener(ui.draw_ui)
        state_manager.change_state(States.Main)

        while state_manager.is_work:
            state_manager.current_state.handle_input(state_manager)
