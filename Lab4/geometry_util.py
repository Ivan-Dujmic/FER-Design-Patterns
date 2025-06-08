from __future__ import annotations
from point import Point

class GeometryUtil():
    @staticmethod
    def distance_from_point(point1: Point, point2: Point) -> float:
        dx = point1.get_x() - point2.get_x()
        dy = point1.get_y() - point2.get_y()
        return (dx ** 2 + dy ** 2) ** 0.5
    
    @staticmethod
    def distance_from_line_segment(line_point1: Point, line_point2: Point, point: Point) -> float:
        # Vector AB
        ABx = line_point2.get_x() - line_point1.get_x()
        ABy = line_point2.get_y() - line_point1.get_y()
        
        # Vector AP
        APx = point.get_x() - line_point1.get_x()
        APy = point.get_y() - line_point1.get_y()
        
        # Dot product of AB and AP
        dot_product = ABx * APx + ABy * APy
        
        # Length of AB squared
        length_squared = ABx ** 2 + ABy ** 2
        
        if length_squared == 0:
            # Line segment is a point
            return GeometryUtil.distance_from_point(line_point1, point)
        
        # Projection factor of AP onto AB
        projection = dot_product / length_squared
        
        if projection < 0:
            # Closest to point A
            return GeometryUtil.distance_from_point(line_point1, point)
        elif projection > 1:
            # Closest to point B
            return GeometryUtil.distance_from_point(line_point2, point)
        
        # Closest point on the segment
        closest_x = line_point1.get_x() + projection * ABx
        closest_y = line_point1.get_y() + projection * ABy
        
        closest_point = Point(closest_x, closest_y)
        
        return GeometryUtil.distance_from_point(closest_point, point)