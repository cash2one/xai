

#calss header
class _LIMITED():
	def __init__(self,): 
		self.name = "LIMITED"
		self.definitions = [u'small in amount or number: ', u'kept within a particular size, range, time, etc.: ', u'used in the name of a limited company']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
