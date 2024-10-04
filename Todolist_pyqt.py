import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton,
                             QListWidget, QListWidgetItem, QCheckBox, QMessageBox, QFileDialog)

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.load_tasks()

    def init_ui(self):
        # Set window title and dimensions
        self.setWindowTitle('To Do List')
        self.setGeometry(400, 400, 600, 600)

        # Create layout
        self.layout = QVBoxLayout()

        # Create input field for tasks
        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText('Enter a new task')
        self.layout.addWidget(self.task_input)

        # Create button to add task
        self.add_task_btn = QPushButton('Add Task', self)
        self.add_task_btn.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_task_btn)

        # Create a list to show tasks
        self.task_list = QListWidget(self)
        self.layout.addWidget(self.task_list)

        # Create button to delete task
        self.delete_task_btn = QPushButton('Delete Task', self)
        self.delete_task_btn.clicked.connect(self.delete_task)
        self.layout.addWidget(self.delete_task_btn)

        # Create buttons to save and load tasks
        self.save_task_btn = QPushButton('Save Tasks', self)
        self.save_task_btn.clicked.connect(self.save_tasks)
        self.layout.addWidget(self.save_task_btn)

        # Set layout to the window
        self.setLayout(self.layout)

    def add_task(self):
        task_text = self.task_input.text()

        if task_text:
            # Create a QListWidgetItem with a checkbox
            item = QListWidgetItem()
            checkbox = QCheckBox(task_text)
            checkbox.stateChanged.connect(lambda: self.toggle_task_status(item))
            self.task_list.addItem(item)
            self.task_list.setItemWidget(item, checkbox)
            self.renumber_tasks()  # Update numbering
            self.task_input.clear()
        else:
            QMessageBox.warning(self, 'Error', 'Task cannot be empty!')

    def toggle_task_status(self, item):
        checkbox = self.task_list.itemWidget(item)
        # Add "(Completed)" to the task if checked
        if checkbox.isChecked():
            checkbox.setText(checkbox.text().split(' (')[0] + " (Completed)")
        else:
            checkbox.setText(checkbox.text().split(' (')[0])

    def delete_task(self):
        selected_task = self.task_list.currentRow()
        if selected_task >= 0:
            self.task_list.takeItem(selected_task)
            self.renumber_tasks()  # Update numbering
        else:
            QMessageBox.warning(self, 'Error', 'No task selected to delete!')

    def renumber_tasks(self):
        # Renumber the tasks in the list after adding or deleting
        for index in range(self.task_list.count()):
            item = self.task_list.item(index)
            checkbox = self.task_list.itemWidget(item)
            task_text = checkbox.text().split(' (')[0].split('. ', 1)[-1]  # Remove number
            checkbox.setText(f"{index + 1}. {task_text}")  # Add updated number

    def save_tasks(self):
        filename, _ = QFileDialog.getSaveFileName(self, 'Save Tasks', os.getenv('HOME'), 'Task Files (*.task)')
        if filename:
            try:
                with open(filename, 'w') as file:
                    for index in range(self.task_list.count()):
                        item = self.task_list.item(index)
                        checkbox = self.task_list.itemWidget(item)
                        completed = checkbox.isChecked()
                        file.write(f'{checkbox.text()}|{completed}\n')
                QMessageBox.information(self, 'Success', 'Tasks saved successfully!')
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Failed to save tasks: {str(e)}')

    def load_tasks(self):
        filename = 'saved_tasks.task'
        if os.path.exists(filename):
            try:
                with open(filename, 'r') as file:
                    for line in file.readlines():
                        task_text, completed = line.strip().split('|')
                        item = QListWidgetItem()
                        checkbox = QCheckBox(task_text)
                        checkbox.setChecked(completed == 'True')
                        checkbox.stateChanged.connect(lambda: self.toggle_task_status(item))
                        self.task_list.addItem(item)
                        self.task_list.setItemWidget(item, checkbox)

            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Failed to load tasks: {str(e)}')

        # After loading, renumber the tasks
        self.renumber_tasks()

    def closeEvent(self, event):
        # Save tasks when the window is closed
        self.save_tasks()
        event.accept()

def main():
    # Create application instance
    app = QApplication(sys.argv)
    # Create instance of the ToDoApp
    window = ToDoApp()
    # Show the application window
    window.show()
    # Execute the app event loop
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
