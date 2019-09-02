import sandboxify as sb
import numpy as np
import cv2
import time

class Sandbox:
    def __init__(self, config, kinect, renderer):
        self.zeros = np.zeros((640, 480))
        self.config = config
        self.kinect = kinect
        self.renderer = renderer
        
    def execute(self):
        print('starting explorer box')
        current_depth = self.kinect.get_depth_image_mm()
        previous_depth_reset = np.copy(current_depth)
        previous_depth = np.copy(current_depth)
        
        while True:			
			original_depth = self.kinect.get_depth_image_mm()
			current_depth = np.copy(original_depth)
			diff_coords = self.kinect.get_depth_image_diff_mm(previous_depth, current_depth, self.config.depth_mm_threshold_diff)
			current_depth[diff_coords] = previous_depth[diff_coords]
			
			coords_qty = len(np.where(original_depth < [self.config.depth_mm_min])[0])
			if coords_qty < self.config.depth_px_qty_ignore:
				print('take current depth image', coords_qty)
				current_depth = original_depth
				previous_depth_reset = np.copy(current_depth)
			else:
				print('take previous depth image', coords_qty)
				c = np.where(current_depth < [self.config.depth_mm_min])
				current_depth[c] = previous_depth_reset[c]
			
			previous_depth = np.copy(current_depth)
			cv2.imshow('sandbox', self.renderer.execute(current_depth))
			key = cv2.waitKey(1)
			if key == 27:
				break
				
			time.sleep(self.config.depth_frame_rate) 
