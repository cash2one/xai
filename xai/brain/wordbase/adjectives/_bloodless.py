

#calss header
class _BLOODLESS():
	def __init__(self,): 
		self.name = "BLOODLESS"
		self.definitions = [u'A bloodless military operation involves no deaths: ', u'used to describe a face or skin that is extremely pale: ', u'without emotion']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
