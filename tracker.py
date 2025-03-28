class EuclideanDistTracker:    
    def __init__(self):        
        self.center_points = {}        
        self.id_count = 0

    #Calculate and identify the center of the rectangle   
    def update(self, objects_rect):
        objects_bbs_ids = []    
        for rect in objects_rect:        
            x, y, w, h = rect        
            cx = (x + x + w) // 2        
            cy = (y + y + h) // 2        
            print(cx, cy)