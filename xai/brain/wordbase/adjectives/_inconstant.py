

#calss header
class _INCONSTANT():
	def __init__(self,): 
		self.name = "INCONSTANT"
		self.definitions = [u'not staying the same, especially in emotion, behaviour, or choice of sexual partner: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
