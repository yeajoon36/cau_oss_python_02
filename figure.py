"""
길이를 입력받아 한 변의 길이를 입력받은 길이로 하는 정삼각형과 정사각형의 넓이, 그리고 반지름의 길이를 입력받은 길이로 하는 원의 넓이를 구하는 함수입니다.
"""


import math #math 모듈의 PI와 sqrt를 사용하기 위해 모듈 불러오기


class Line:
    def __init__(self, length=1):
        """ 
        클래스 Line은 
        외부에서 접근 불가능한 필드 __length가 있으며,
        기본값은 1이다.
        Args:
            length
        Returns:
            아무 값도 리턴하지 않음
        """
        self.__length = length



    def set_length(self, length):
        """ 
        생성자를 통해 초기 __length의 값을 지정한다.
        Args:
            length: 지정할 값
        Returns: 
            아무 값도 리턴하지 않음
        """
        self.__length = length



    def get_length(self):
        """
        지정한 __length의 값을 반환한다.
        Args:
    
        Returns: __length
            int or float: 지정한 길이를 반환합니다.
        """
        return self.__length
    



def area_square(line):
    """ 
    길이를 입력받아 정사각형의 넓이를 구하는 함수입니다.
    Args:
        line (Line): 정사각형 한 변의 길이입니다.
    Returns: line ** 2
        int or float: 정사각형의 넓이를 반환합니다.
    """
    return line.get_length() ** 2
    
    
    
        
    
def area_circle(line):
    """ 
    길이를 입력받아 원의 넓이를 구하는 함수입니다.
    Args: 
        line (Line): 원의 반지름의 길이입니다.
    Returns: line ** 2 * PI
        int or float: 원의 넓이를 반환합니다.
    """
    return line.get_length() ** 2 * math.pi
    

    

    
def area_regular_triangle(line):
    """ 
    길이를 입력받아 정삼각형의 넓이를 구하는 함수입니다.
    Args:
        line (Line): 삼각형 한 변의 길이입니다.
    Returns: line ** 2 * (sqrt 3) / 4
        int or float: 정삼각형의 넓이를 반환합니다.
    """
    return line.get_length() ** 2 * math.sqrt(3) / 4