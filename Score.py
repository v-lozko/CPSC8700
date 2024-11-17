class Score:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Score()
        return cls._instance

    def __init__(self):
        if hasattr(self, "_initialized"):
            return
        self._initialized = True
        self._score = 0
        self._high_score = 0 
        self._prev_score = 0

    def get_score(self):
        return self._score
    
    def get_high_score(self):
        return self._high_score
    
    def get_prev_score(self):
        return self._prev_score

    def set_score(self, points):
        self.set_prev_score(points)
        if(points > self._high_score):
            self.set_high_score(points)
        self._score = points

    def set_high_score(self, points):
        self._high_score = points

    def set_prev_score(self, points):
        self._prev_score = points

    def reset_score(self):
        self._score = 0
