class NotesError(Exception):
    """Базовая ошибка приложения заметок."""


class NoteValidationError(NotesError):
    """Пользователь ввёл некорректные данные."""


class NoteNotFoundError(NotesError):
    """Заметка с таким идентификатором не найдена."""


class StorageError(NotesError):
    """Ошибка чтения или записи файла."""