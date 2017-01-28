

#calss header
class _RADIAL():
	def __init__(self,): 
		self.name = "RADIAL"
		self.definitions = [u'spreading out from a central point: ', u'relating to the area around the central part of the body', u'relating to the radius (= the thicker of the two bones in the lower arm): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
