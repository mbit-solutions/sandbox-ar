import cv2

class Config:
	def __init__(self):
		self.window_width = 1600
		self.window_height = 1200
		self.depth_mm_min = 1010
		self.depth_mm_max = 1330
		self.depth_mm_threshold_diff = 40
		self.depth_px_qty_ignore = 11000	
		self.depth_frame_rate = 0.3
		self.depth_posterize_qty = 15	
