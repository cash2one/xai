

#calss header
class _LINED():
	def __init__(self,): 
		self.name = "LINED"
		self.definitions = [u'(of paper) having lines printed across it : ', u'(of the skin on the face) having lines because of age: ', u'If a piece of clothing is lined, it has an extra layer of thin material sewn inside it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
