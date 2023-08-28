# single responsibility principle
 
'''you are given a list of shapes
 calculate the sum of their areas and print it'''
 
import math
 
# from shapes import Rect, Circle
 
# class ShapesController:
#     # ! violation of SRP
#     # 1 calc of area 
#     # 2 printing the sum
#      def printing_areas_sum(self, shapes):
#          area_sum = 0
#          for shape in shapes:
#              if isinstance(shape, Rect):
#                  area_sum += shape.width * shape.height
#              elif isinstance(shape, Circle):
#                  area_sum += shape.radius * shape.radius * math.pi
                 
#          print(f"Area sum of shapes is: {area_sum: .2f}")
         


# shapes = [Circle(10), Rect(4, 5)]

# ShapesController().printing_areas_sum(shapes)