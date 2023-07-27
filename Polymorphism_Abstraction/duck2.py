class Guitar:
    def sounds(self):
        print("rock sound")
        
        
class Drums:
    def sounds(self):
        print("bang bang")
        
    
instruments = [Guitar(), Drums()]    
    
for any_type in instruments:
   any_type.sounds()