import os

from PySide2 import QtWidgets

from mapclientplugins.multiplefilechooserstep.loaddirectoryfiles import LoadDirectoryFilesDialog
from mapclientplugins.multiplefilechooserstep.ui_configuredialog import Ui_ConfigureDialog

INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''


class ConfigureDialog(QtWidgets.QDialog):
    """
    Configure dialog to present the user with the options to configure this step.
    """

    def __init__(self, parent=None):
        """
        Constructor
        """
        QtWidgets.QDialog.__init__(self, parent)

        self._ui = Ui_ConfigureDialog()
        self._ui.setupUi(self)
        self._ui.pushButtonRemove.setEnabled(False)

        # Keep track of the previous identifier so that we can track changes
        # and know how many occurrences of the current identifier there should
        # be.
        self._previousIdentifier = ''
        # Set a place holder for a callable that will get set from the step.
        # We will use this method to decide whether the identifier is unique.
        self.identifierOccursCount = None

        self._previousLocation = ''
        self._workflow_location = ''
        self._files = []

        self._make_connections()

    def _make_connections(self):
        self._ui.lineEditIdentifier.textChanged.connect(self.validate)
        self._ui.pushButtonAdd.clicked.connect(self._add_clicked)
        self._ui.pushButtonRemove.clicked.connect(self._remove_clicked)
        self._ui.pushButtonRemoveAll.clicked.connect(self._remove_all_clicked)
        self._ui.listWidgetFiles.itemSelectionChanged.connect(self._file_selection_changed)

    def _file_selection_changed(self):
        self._ui.pushButtonRemove.setEnabled(len(self._ui.listWidgetFiles.selectedIndexes()))

    def _remove_all_clicked(self):
        self._ui.listWidgetFiles.clear()

    def _remove_clicked(self):
        for i in reversed(range(self._ui.listWidgetFiles.count())):
            item = self._ui.listWidgetFiles.item(i)
            if self._ui.listWidgetFiles.isItemSelected(item):
                self._ui.listWidgetFiles.takeItem(i)

    def _add_clicked(self):
        dlg = LoadDirectoryFilesDialog(self)
        dlg.set_previous_location(self._previousLocation)

        if dlg.exec_() == QtWidgets.QDialog.Accepted:
            files = dlg.get_files()
            rel_files = []
            for file in files:
                rel_files.append(os.path.relpath(file, self._workflow_location))

            self._previousLocation = dlg.get_previous_location()
            self._ui.listWidgetFiles.addItems(rel_files)

    def set_workflow_location(self, workflow_location):
        self._workflow_location = workflow_location

    def accept(self):
        """
        Override the accept method so that we can confirm saving an
        invalid configuration.
        """
        result = QtWidgets.QMessageBox.Yes
        if not self.validate():
            result = QtWidgets.QMessageBox.warning(
                self, 'Invalid Configuration',
                'This configuration is invalid.  Unpredictable behaviour may result if you choose \'Yes\', are you sure you want to save this configuration?)',
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if result == QtWidgets.QMessageBox.Yes:
            QtWidgets.QDialog.accept(self)

    def validate(self):
        """
        Validate the configuration dialog fields.  For any field that is not valid
        set the style sheet to the INVALID_STYLE_SHEET.  Return the outcome of the
        overall validity of the configuration.
        """
        # Determine if the current identifier is unique throughout the workflow
        # The identifierOccursCount method is part of the interface to the workflow framework.
        value = self.identifierOccursCount(self._ui.lineEditIdentifier.text())
        valid = (value == 0) or (value == 1 and self._previousIdentifier == self._ui.lineEditIdentifier.text())
        if valid:
            self._ui.lineEditIdentifier.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.lineEditIdentifier.setStyleSheet(INVALID_STYLE_SHEET)

        valid_files = True
        for i in range(self._ui.listWidgetFiles.count()):
            file = self._ui.listWidgetFiles.item(i).text()
            if not os.path.isfile(os.path.join(self._workflow_location, file)):
                valid_files = False

        return valid and valid_files

    def getConfig(self):
        """
        Get the current value of the configuration from the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        """
        self._previousIdentifier = self._ui.lineEditIdentifier.text()
        config = {'identifier': self._ui.lineEditIdentifier.text()}
        files = []
        for i in range(self._ui.listWidgetFiles.count()):
            files.append(self._ui.listWidgetFiles.item(i).text())
        config['files'] = files

        return config

    def setConfig(self, config):
        """
        Set the current value of the configuration for the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        """
        self._previousIdentifier = config['identifier']
        self._ui.lineEditIdentifier.setText(config['identifier'])
        self._ui.listWidgetFiles.addItems(config['files'])
