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
- demit_func: Produce a TRAK .TIN file with a certain demit value, ready to run simulation. File changes are made based off an original file fed into the function. Returns nothing other than the file it produces. <br /> 
-- Format: demit_func(‘path/original_file_to_change.TLS’, ‘path/file_to_save_as.TLS’, demit value to set to: a float) <br />
- avg_func: Produce a TRAK .TIN file with certain avg value, ready to run simulation. File changes are made based off an original file fed into the function. Returns nothing other than the file it produces. <br /> 
-- Format: avg_func(‘path/original_file_to_change.TLS’, ‘path/file_to_save_as.TLS’, avg value set to: a float)<br />  
- avg_demit_ncycle_func: Produce TRAK .TIN file for each (avg, demit, ncycle) given, ready to run simulation. File changes are made based off an original file fed into the function. Returns: a message saying what file was created. <br /> 
-- Format: avg_demit_ncycle_func(‘path/original_file_to_change.TLS’, ‘path/file_to_save_as.TLS’, avg value set to: a float, demit value set to: a float, ncycle value set to: an integer) <br />
- converg_func: for each file in a list, given a convergence threshold, determine whether the current converges within that threshold. Returns: a list of files with whether they converge or not, as well as final current for those that converge <br />
-- Format: converg_func([‘file1.TLS’, ‘file2.TLS’, ’file3.TLS’, etc…], convergence threshold value: a float) <br />
- mesh_file_electrode_spacing2: produce a mesh file with the focus electrode and anode spacings given, save the file to the specified name. The defining lines of the focus electrode and anode distances as put into the function can be seen in the figure below. Function returns nothing other than the file that is saved. <br />
![fe_positions_descriptions](https://github.com/mkdunc/E-lens/assets/154284388/1c04ccf7-abab-4c29-9efe-ec4663bd5ce5)
--Format: mesh_file_electrode_spacing2(focus electrode x position: a float, focus electrode y position: a float, anode support x position: a float, anode support y position: a float, ‘path/file_to_save_to.MIN’)<br />
Note: all the details for the mesh file are defined within this function and can be manually changed if one wants to change the mesh.  <br />
- estat_file2: write an estat file with given input mesh file,file to save to, emission potential, and potential of the focus electrode, shield, and control electrode. Returns nothing other than the file that is created. <br />
-- Format: estat_file2(‘path/mesh_file’, ‘path/estat_file_to_save.EIN’, emission potential: a string of the value, focus electrode potential: a string of the value) <br />
- mesh_permag_file2: write a mesh file as the input for permag. Returns nothing other than the file that is created. <br />
-- Format: mesh_permag_file2(‘path/mesh_permag_filename.MIN’) <br />
Note: all the details for the mesh file are defined within this function and can be manually changed if one wants to change the mesh.  <br />
- permag_file2: write the magnetic permag file, given the desired input mesh file. Returns nothing other than the file that is created. <br />
-- Format: permag_file2(‘path/mesh_file_to_use’, ‘path/file_to_save_as.PIN’) <br />
Note: The magnet’s current that produces a field is the Current(2) parameter. It can be changed to change the solenoidal magnetic field.  <br />
- TRAK_file2: write the trak .tin file with the given input estat and permag files. Returns nothing other than the file that is created. <br />
-- Format: TRAK_file2(‘path/estat_file_name.EOU’, ‘path/permag_file_name.POU’, ‘path/TRAK_file_to_save_to.TIN’)  <br />
Note: The other specific TRAK parameters are pre-set in this function, so it would be the first one to run and then change that one for desired changes in avg, demit, and ncycle. <br />
- run_parallel: call the run parallel script (run_trak_cmd.py) with the given file list, number of simulations to run in parallel, and command. The command can be TRAK, MESH, ESTAT, or PERMAG. Returns nothing other than running the script. <br />
Format: run_parallel([‘file1’, ‘file2’, file3’, etc…], number of files t run in parallel: a string, command to run: a string. Can be either TRAK, MESH, ESTAT, or PERMAG)  <br />



<ins> Upper Level TRAK Tools (SimpleSource_TRAK_tools.ipynb):  </ins> <br />








