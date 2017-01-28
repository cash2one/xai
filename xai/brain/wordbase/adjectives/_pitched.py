

#calss header
class _PITCHED():
	def __init__(self,): 
		self.name = "PITCHED"
		self.definitions = [u'sloping and not flat: ', u'used to refer to percussion instruments that produce musical notes of one or more definite pitches']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
