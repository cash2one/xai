

#calss header
class _POISED():
	def __init__(self,): 
		self.name = "POISED"
		self.definitions = [u'If an object or a part of your body is poised, it is completely still but ready to move at any moment: ', u'ready to do a particular thing at any moment: ', u'showing very calm and controlled behaviour']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
