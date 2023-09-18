import streamlit as st
import pandas as pd
import os
import io
import glob

st.set_page_config(page_title="Stats Dashboard", page_icon=":dolphin:", layout="centered", initial_sidebar_state="auto", menu_items=None)

# this bit of code is to protect this page
def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():



    # Specify the folder path
    folder_path = "/home/sovnav/projects/nav-stats/StreamlitApp/input/"

    # Use os.listdir() to get a list of all files in the folder
    files = os.listdir(folder_path)

    # Define a custom sorting key to extract characters 13 to 15 from the file names
    def custom_sort_key(file_name):
        if len(file_name) >= 15:
            return file_name[12:15]
        else:
            return file_name  # Handle shorter file names gracefully

    # Sort the files based on the custom sorting key
    sorted_files = sorted(files, key=custom_sort_key,reverse=True)
    # print the latest file in the folder
    st.markdown("""
    #
    #
    #
        The latest file found in the database:
        """)

    st.write(sorted_files[0])

    if st.button(label="add new file"):

        # define path of orca generated stats file
        input_path = "/home/sovnav/projects/nav-stats/StreamlitApp/input/"  

        # define path of brokedown tables
        output_path = "/home/sovnav/projects/nav-stats/StreamlitApp/output"

        # loop over all files in the input folder
        for file_name in os.listdir(input_path):
            # make sure the file is a text file
            if not file_name.endswith('.sts'):
                continue
            
            # construct the full path to the file
            file_path = os.path.join(input_path, file_name)
            
            # read the file into a string variable            
            with open(file_path, 'r', encoding='iso-8859-1') as f:
                file_contents = f.read()

            # split the file into separate tables
            tables = file_contents.split('\n\n')

            # save the names of the tables
            table_names = tables[1::2]

            # create an empty list to store the dataframes
            dataframes = []

            # loop through the tables and convert each one to a dataframe
            for table in tables:
                # skip any tables that don't have a header that starts with "Name"
                if not table.startswith('Name'):
                    continue

                # read the table into a dataframe
                df = pd.read_csv(io.StringIO(table), sep='\t')

                # select the "Mean" column and transpose the resulting dataframe
                df = df.loc[:, ['Name', 'Mean']].set_index('Name').T

                # add the dataframe to the list
                dataframes.append(df)

            # create the output directory if it doesn't exist
            os.makedirs(output_path, exist_ok=True)

            # loop through the dataframes and save each one as a CSV file
            for i, data in enumerate(dataframes):
                df = pd.DataFrame(data)
                df_name = f'{os.path.splitext(file_name)[0]}-{table_names[i]}.csv'  # use table_names to name the output files
                df.to_csv(os.path.join(output_path, df_name), index=False)


        # Specify the input folder path
        input_folder = "/home/sovnav/projects/nav-stats/StreamlitApp/output/"

        # List all files in the input folder
        input_files = os.listdir(input_folder)

        # Create a dictionary to store DataFrames with the same observation name
        observation_to_dataframe = {}

        # Iterate through the input files
        for input_file in input_files:
            if len(input_file) >= 26 and input_file.endswith(".csv"):
                file_name = input_file[26:-4]  # Characters 21 to -4 (excluding ".csv")
                sequence_number = input_file[12:15]  # Characters 13:15
                file_path = os.path.join(input_folder, input_file)
                
                # Read the CSV file
                df = pd.read_csv(file_path)
                
                # Add the sequence number as a new column
                df['Seq'] = sequence_number
                
                # Check if a DataFrame with the same observation name already exists
                if file_name in observation_to_dataframe:
                    # Append data from the current file to the existing DataFrame
                    existing_df = observation_to_dataframe[file_name]
                    observation_to_dataframe[file_name] = pd.concat([existing_df, df], ignore_index=True)
                else:
                    # Create a new DataFrame for the observation name and add it to the dictionary
                    observation_to_dataframe[file_name] = df

        # Save each concatenated and sorted DataFrame with the observation name
        for observation_name, df in observation_to_dataframe.items():
            # Sort the DataFrame by the 'Seq' column
            df = df.sort_values(by='Seq')
            
            output_file_path = f"/home/sovnav/projects/nav-stats/StreamlitApp/final/{observation_name}.csv"
            df.to_csv(output_file_path, index=False)
            #st.write(f"Saved concatenated and sorted DataFrame to '{output_file_path}'")
        st.write(" ")
        st.write("Concatenation, sorting, DataFrames saved, and Sequence Numbers added.")
        st.write(" ")

        # delete all files from temporary folder

        # Use glob to get a list of all .csv files in the folder
        csv_files = glob.glob(os.path.join(input_folder, "*.csv"))

        # Loop through the list of .csv files and delete each one
        for file_path in csv_files:
            try:
                os.remove(file_path)
                #st.write(f"Deleted file: {file_path}")
            except OSError as e:
                st.write(f"Error deleting file {file_path}: {e}")