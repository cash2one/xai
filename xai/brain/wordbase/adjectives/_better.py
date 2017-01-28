

#calss header
class _BETTER():
	def __init__(self,): 
		self.name = "BETTER"
		self.definitions = [u'comparative of  good : of a higher standard, or more suitable, pleasing, or effective than other things or people: ', u'If you are or get better after an illness or injury, you are healthy again: ', u'to improve: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
