from PySide6 import QtWidgets, QtCore

from mapclientplugins.multiplefilechooserstep.ui_loaddirectoryfiles import Ui_LoadDirectoryFilesDialog


class LoadDirectoryFilesDialog(QtWidgets.QDialog):
    """
    Configure dialog to present the user with the options to configure this step.
    """

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)

        self._ui = Ui_LoadDirectoryFilesDialog()
        self._ui.setupUi(self)

        self._fileSystemModel = QtWidgets.QFileSystemModel()
        self._ui.treeView.setModel(self._fileSystemModel)
        self._previous_location = None

        self._make_connections()

    def _make_connections(self):
        self._ui.lineEditFilterList.textEdited.connect(self._filter_list_edited)

    def _filter_list_edited(self):
        filters = self._ui.lineEditFilterList.text().split(',')
        filters = [f.rstrip().strip() for f in filters]
        self._fileSystemModel.setNameFilters(filters)

    def showEvent(self, event):
        self._ui.lineEditFilterList.setFocus()

    def exec_(self) -> int:
        location = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Directory Location', self._previous_location)

        if location:
            self._previous_location = location
            self._fileSystemModel.setRootPath(location)
            self._ui.treeView.setRootIndex(self._fileSystemModel.index(location))
        else:
            return QtWidgets.QDialog.DialogCode.Rejected

        return QtWidgets.QDialog.exec_(self)

    def set_previous_location(self, previous_location):
        self._previous_location = previous_location

    def get_previous_location(self):
        return self._previous_location

    def _get_files_in_path(self, root_path):
        root_dir = QtCore.QDir(root_path)
        root_dir.setNameFilters(self._fileSystemModel.nameFilters())
        root_dir.setFilter(self._fileSystemModel.filter())
        entries = root_dir.entryInfoList()
        files = []
        for entry in entries:
            if entry.isDir():
                files.extend(self._get_files_in_path(entry.filePath()))
            else:
                files.append(entry.filePath())

        return files

    def get_files(self):
        root_path = self._fileSystemModel.rootPath()
        return self._get_files_in_path(root_path)
