#%%
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
import model_modules_2d
import time
from scipy.ndimage import gaussian_filter

start = time.time()
# the basic model
nx, nz = 10000, 3250
initial_vel = 1 # km/s
grid_size  = 0.001 # km
x_min, z_min = 0, -0.25

# automatically calculated
x_max = grid_size * nx + x_min
z_max = grid_size * nz + z_min

if __name__ == '__main__':
    # --------------------------------------------------------- #
    # --------------- Initializing the array ------------------ #
    # --------------------------------------------------------- #
    plane_model = np.ones((nx, nz)) * initial_vel
    plane_model_prime = np.ones((nx, nz)) * initial_vel
    
    # --------------------------------------------------------- #
    # ----------------- Specify the values -------------------- #
    # --------------------------------------------------------- #
    # model_modules_2d.layerd_model_setting('121.375_25.075_1d_layer.dat', plane_model_prime)
    model_modules_2d.layerd_model_setting('well_1D_layer.csv', plane_model)
 
    # plane_model_prime = gaussian_filter(plane_model_prime, mode = 'nearest', sigma=30)
    plane_model = gaussian_filter(plane_model, mode = 'nearest', sigma=30)
    
    # plane_model = model_modules_2d.two_layerd_model_combination(arr1 = plane_model, 
    #                                               arr2 = plane_model_prime,
    #                                               fault_dip = 60,
    #                                               fault_x = 4.7)
    # --------------------------------------------------------- #
    # -------------specify your own structures----------------- #
    # --------------------------------------------------------- #
    plane_model = model_modules_2d.set_up_fault_zone(fault_x   = 2, 
                                                  fault_dip = 40, 
                                                  fault_Vp  = -33,
                                                  app_thick = 1.,
                                                  model_arr = plane_model,
                                                  deepest_z = 999.,
                                                  percentage_flag = True
    )
   
    ### create a rectangle area
    # plane_model = model_modules_2d.set_up_rectangle(
    #     arr       = plane_model, 
    #     x1 = 4.7, z1 = -0.05, x2 = 15., z2 = -0.05, x3 = 15., z3 = 0.1, x4 = 5.1618, z4 = 0.8,  
    #     new_value = -5, percentage_flag = True
    # )
   
    # --------------------------------------------------------- #
    # -----------------------Post-Processing------------------- #
    # --------------------------------------------------------- #
    ## padding 3 columns to the array for OpenSWPC reading
    plane_model = np.pad(plane_model, ((3,3),(3,3)), mode='edge')
    
    # model_modules_2d.plot_2D_figures(stacked_matrix, 5., 0.125, 0)
    # plane_model = gaussian_filter(plane_model, mode = 'nearest', sigma=30)
    print('writing file...')
    # model_modules_2d.output_2d(plane_model)
    model_modules_2d.Visualizing_array(plane_model)

    
    end = time.time()
    print(f'done! total time = {end-start:.1f}s')
    
# %%
