# E-lens
Electron lens source design 



![TRAK_sim_flow](https://github.com/mkdunc/E-lens/assets/154284388/801785be-4bca-47f0-ba30-7e3bc379b553)


## File Hierarchy
Run Simulations in Parallel Script (run_trak_cmd.py): <br />
    - input list of simulation files to run, how many to run in parallel at a time, and the command to run with. Can run mesh,         estat, permag, and trak (though only one type at a time) Will run all of the files when called, and return confirmation         that the simulations ran. NOTE: The filenames, the number of files to run in parallel, and the TRAK command should all           be strings. <br />
    - Example command from an external file to run this file: subprocess.run(['python', 'run_trak_cmd.py', ‘file_list_to_run’,’ number of files to run in parallel’, ‘TRAK’], stdout = subprocess.PIPE) <br /> 
    <br />


Lower level trak tools (Strong_Source_TRAK_tools.ipynb)
