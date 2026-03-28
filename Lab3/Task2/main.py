from text_editor import TextEditor
from text_editor_model import TextEditorModel

def main():
    model = TextEditorModel("First Line\nSecond Line\n\nFourth Line\nFifth Line")
    editor = TextEditor(model)
    editor.set_visible(True)

if __name__ == "__main__":
    main()