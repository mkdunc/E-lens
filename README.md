# E-lens
Electron lens source design 



![TRAK_sim_flow](https://github.com/mkdunc/E-lens/assets/154284388/801785be-4bca-47f0-ba30-7e3bc379b553)


## File Hierarchy
<ins> Run Simulations in Parallel Script (run_trak_cmd.py):  </ins> <br />
- input list of simulation files to run, how many to run in parallel at a time, and the command to run with. Can run mesh, estat, permag, and trak (though only one type at a time) Will run all of the files when called, and return confirmation that the simulations ran. NOTE: The filenames, the number of files to run in parallel, and the TRAK command should all be strings. <br />
- Example command from an external file to run this file: subprocess.run(['python', 'run_trak_cmd.py', ‘file_list_to_run’,’ number of files to run in parallel’, ‘TRAK’], stdout = subprocess.PIPE) <br /> 
    <br />


<ins> Lower level trak tools (SimpleSource_TRAK_base_tools.ipynb) </ins> <br />
Defines all the base tools that will be used in the simulations: <br /> 
 - Current_conv: saves current convergence plot and returns final current for each simulation <br />
-- Format: current_conv(‘path_to_file/file.TLS’) <br />
- E_field_line: plots the electric field at defined slices, the z-slice value given needs to have been run through trak with ESCAN. Returns: the maximum electric field in that slice, The electric field list in that slice <br /> 
-- Format: E_field_line(‘path_to_file/file.TLS’, e-field z-slice location: a float, plots = True) <br />
- cdensity: Saves current density plot at given z-slice and returns current density data, the z-slice given needs to have been run through trak with CDENS. Returns: radii points the current density was calculated at, the corresponding current density <br />
-- Format: cdensity(‘path_to_file/file.TLS’, z-slice location for the plot: a float) <br />
- dist_flatness: calculates the standard deviation of current density up to defined radius at given Z slice. Note that the Z slice given needs to have been run through trak with CDENS. Returns: the average density, standard deviation of current density up to that radius.  <br /> 
-- Format: dist_flatness(‘path_to_file/file.TLS’,  z-slice location for the plot: a float, radius to analyze up to: a float) <br /> 

  
- demit_func (produce TRAK .TIN file with a certain demit value, ready to run simulation. File changes are made based off an original file fed into the function) <br /> 
Format: demit_func(‘path/original_file_to_change.TLS’, ‘path/file_to_save_as.TLS’, demit value set to: a float )<br /> 


