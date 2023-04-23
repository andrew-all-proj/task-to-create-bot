from aiogram.dispatcher.filters.state import State, StatesGroup

class State_bot(StatesGroup):
    """Class for FSM"""
    st_main = State()
    st_get_weather = State()
    st_currency_convertor = State()
    st_select_currency = State()
    st_random_picture = State()

