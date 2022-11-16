from enum import Enum


class Actions(Enum):
    Exit = "exit"
    AddBook = "add"
    RemoveBook = "remove"
    FindBook = "find"
    PrintAt = "print"
    PrintAll = "print all"
    Back = "back"
    Undo = "undo"

    SetAuthor = "author"
    SetYear = "year"
    SetTitle = "title"

    SetId = "id"

    Execute = "execute"

    Return = "Что-нибудь"
