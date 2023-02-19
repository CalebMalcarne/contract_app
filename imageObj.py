'''
Created By: Caleb Malcarne
Program: Invoice Filler 


'''

from PIL import Image
from globals import *

class image():
    def __init__(self, name, dir, length, width, description, autoResize, customSize):
        self.img = Image.open(dir)
        
        self.name = name
        self.dir = dir
        self.length = self.img.size[0]
        self.width = self.img.size[1]
        self.user_len = int(length)
        self.user_width = int(width)
        self.description = description
        self.autoResize = autoResize
        self.customSize = customSize
        
        if(self.autoResize):
            self.resize_Auto(self.width, self.length, self.dir)
        elif(self.customSize):
            self.resize_custom(self.user_width, self.user_len, self.dir)
        
    def resize_Auto(self, width, height, dir):
        
        size_lim = image_threshold
        
        img = Image.open(dir)
        
        if(width > size_lim or height > size_lim):
            scaler = 0
            if width > height:
                scaler = width
            else:
                scaler = height
                
            scaler = size_lim/scaler
            
            width = int(width * scaler)
            height = int(height * scaler)
            
            size = (height, width)
            resized = img.resize(size)
            
            new_dir = f"temp/{self.name}.png"
            self.dir = new_dir
            print(new_dir)
            
            resized.save(new_dir)
 
    def resize_custom(self, width, height, dir):
        img = Image.open(dir)
        size = (height, width)
        resized = img.resize(size)
        print(height, " ", width)
        
        new_dir = f"temp/{self.name}_r.png"
        self.dir = new_dir
        print(new_dir)
    
        resized.save(new_dir)
    
    def getName(self):
        return self.name
    
    def getDir(self):
        return self.dir
    
    def getDescription(self):
        return self.description