import os
import PySimpleGUI as sg
from runWhisper import runWisper

#show list of audio files in the folder
List_column = [
    [
    sg.Text("Select folder with your audio files"),
    sg.In(size=(25,1), enable_events=True, key="-FOLDER-"),
    sg.FolderBrowse()
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40,20),
            key="-FILE LIST-"
        )
    ]
]

#show Transcription of the audio file
file_name_column = [
    [sg.Text("Transcription of audio file: ")],
    [sg.Text(size=(40,1), key="-TOUT-")],
    ]


#-----Layout of app------
layout = [ 
    [
            sg.Column(List_column),
            sg.VSeparator(),
            sg.Column(file_name_column),
    ]
]

window = sg.Window("WhisperTool", layout)

#event loop
while True:
    event, values = window.read()
    #End program if user closes the window or presses 'OK'
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    #-FOLDER- event, make a list of files
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try: 
            #get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        file_names = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
             and f.lower().endswith((".mp3", ".wav")) # only support wave and mp3 for now. I can add more later.
        ]
        window["-FILE LIST-"].update(file_names)

    elif event == "-FILE LIST-": #file was chosen
        try:
            file_path = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(file_path)
            #run whisper on chosen sound file
            text = runWisper(file_path)

            window["-TOUT-"].update(text)

        except:
            pass

#close application window
window.close()